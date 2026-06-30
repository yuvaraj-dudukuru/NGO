/* ============================================================================
 * Capstone Project — Synthetic dataset generator
 * ----------------------------------------------------------------------------
 * Produces a realistic but entirely SYNTHETIC order-level dataset for the
 * "GreenCart" online-retail capstone. No real, proprietary, or personal data.
 *
 * The data is deliberately shaped to contain a discoverable story:
 *   - Revenue grows steadily across FY2025.
 *   - Profit MARGIN erodes, driven mainly by rising discounts in Apparel.
 *   - The South region lags the other markets.
 *   - The Premium segment is a minority of customers but the majority of value.
 *
 * Outputs:
 *   data/sales_clean.csv        — the cleaned, analysis-ready dataset (deliverable)
 *   assets/data.js              — same rows as window.CAPSTONE_DATA for the dashboard
 *
 * Run:  node data/generate_data.js
 * ==========================================================================*/
const fs = require('fs');
const path = require('path');

// ---- deterministic PRNG so the dataset is reproducible ----
let seed = 20250420;
function rand(){ seed = (seed*1103515245 + 12345) & 0x7fffffff; return seed/0x7fffffff; }
function pick(arr){ return arr[Math.floor(rand()*arr.length)]; }
function gauss(mean,sd){ // Box-Muller
  const u=Math.max(1e-9,rand()), v=rand();
  return mean + sd*Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);
}

const REGIONS  = ['North','South','East','West'];
const CATS     = ['Electronics','Apparel','Home','Grocery','Sports'];
const SEGMENTS = ['Premium','Regular','Basic'];

// base price & cost ratio per category
const PRICE = {Electronics:[180,520],Apparel:[35,140],Home:[40,220],Grocery:[8,60],Sports:[30,180]};
const COST_RATIO = {Electronics:0.74,Apparel:0.55,Home:0.62,Grocery:0.80,Sports:0.60};
// share of orders per segment (Premium is the minority)
const SEG_WEIGHT = {Premium:0.18,Regular:0.42,Basic:0.40};
// Premium buys more units / higher price tier -> disproportionate value
const SEG_UNIT = {Premium:[2,8],Regular:[1,4],Basic:[1,3]};
const SEG_PRICE_MULT = {Premium:1.35,Regular:1.0,Basic:0.92};

function weightedSegment(){
  const r=rand(); let acc=0;
  for(const s of SEGMENTS){ acc+=SEG_WEIGHT[s]; if(r<=acc) return s; }
  return 'Basic';
}

// A pool of synthetic customers so we can measure new vs returning
const CUSTOMERS = [];
for(let i=1;i<=900;i++){
  CUSTOMERS.push({ id:'C'+String(i).padStart(4,'0'), region:pick(REGIONS), segment:weightedSegment() });
}

const rows=[];
let orderNo=1000;
const DAYS_2025 = 365;

for(let day=0; day<DAYS_2025; day++){
  const date = new Date(Date.UTC(2025,0,1));
  date.setUTCDate(date.getUTCDate()+day);
  const month = date.getUTCMonth(); // 0..11

  // order volume grows ~ through the year + weekend uplift + seasonal Q4 bump
  const dow = date.getUTCDay();
  const weekend = (dow===0||dow===6)?1.25:1.0;
  const q4 = (month>=9)?1.18:1.0;
  const baseOrders = 6 + month*0.5;
  const nOrders = Math.max(2, Math.round(gauss(baseOrders,2)*weekend*q4));

  for(let o=0;o<nOrders;o++){
    const cust = CUSTOMERS[Math.floor(rand()*CUSTOMERS.length)];
    const region = cust.region;
    const segment = cust.segment;
    const category = pick(CATS);

    const [pmin,pmax]=PRICE[category];
    let unitPrice = +((pmin + rand()*(pmax-pmin)) * SEG_PRICE_MULT[segment]).toFixed(2);

    const [umin,umax]=SEG_UNIT[segment];
    const units = umin + Math.floor(rand()*(umax-umin+1));

    // ----- the engineered story: discounts erode margin over the year -----
    // A broad discount "creep" rises every month (worst in Apparel and the South
    // region), so total profit margin clearly declines while revenue still grows.
    let discount = 0.04 + rand()*0.06;                 // base 4-10%
    discount += month*0.007;                           // broad creep, ~ +7.7% by Dec
    if(category==='Apparel') discount += 0.03 + month*0.010;   // Apparel discounts hardest
    if(region==='South')     discount += 0.05;                 // South leans on discounts
    if(segment==='Premium')  discount -= 0.05;                 // Premium least discounted
    discount = Math.min(0.55, Math.max(0, discount));
    discount = +discount.toFixed(3);

    const gross = unitPrice*units;
    const revenue = +(gross*(1-discount)).toFixed(2);
    const cost = +(gross*COST_RATIO[category]).toFixed(2);
    const profit = +(revenue - cost).toFixed(2);

    rows.push({
      order_id: 'ORD-'+(orderNo++),
      order_date: date.toISOString().slice(0,10),
      month: month+1,
      region, category, segment,
      customer_id: cust.id,
      units,
      unit_price: unitPrice,
      discount_pct: +(discount*100).toFixed(1),
      revenue,
      cost,
      profit,
      margin_pct: +(profit/revenue*100).toFixed(1)
    });
  }
}

// mark new vs returning by first appearance
const seen=new Set();
for(const r of rows){
  r.is_new_customer = seen.has(r.customer_id) ? 0 : 1;
  seen.add(r.customer_id);
}

// ---- write CSV ----
const cols = ['order_id','order_date','month','region','category','segment','customer_id',
              'units','unit_price','discount_pct','revenue','cost','profit','margin_pct','is_new_customer'];
const csv = [cols.join(',')]
  .concat(rows.map(r=>cols.map(c=>r[c]).join(',')))
  .join('\n');
fs.writeFileSync(path.join(__dirname,'sales_clean.csv'), csv);

// ---- write data.js for the dashboard (no fetch / CORS issues on file://) ----
const assetsDir = path.join(__dirname,'..','assets');
if(!fs.existsSync(assetsDir)) fs.mkdirSync(assetsDir,{recursive:true});
const js = 'window.CAPSTONE_DATA = ' + JSON.stringify(rows) + ';\n';
fs.writeFileSync(path.join(assetsDir,'data.js'), js);

// ---- console summary ----
const totRev = rows.reduce((s,r)=>s+r.revenue,0);
const totProfit = rows.reduce((s,r)=>s+r.profit,0);
console.log('Rows:', rows.length);
console.log('Total revenue: $'+(totRev/1000).toFixed(1)+'K');
console.log('Total profit:  $'+(totProfit/1000).toFixed(1)+'K');
console.log('Overall margin:', (totProfit/totRev*100).toFixed(1)+'%');
console.log('Wrote sales_clean.csv and assets/data.js');
