/* ============================================================================
 * Hands-On Activity — Synthetic HR / Workforce dataset generator
 * ----------------------------------------------------------------------------
 * Produces a realistic but entirely SYNTHETIC employee dataset for the
 * "Northwind People Analytics" hands-on activity. No real or personal data.
 *
 * Engineered story (so the dashboard reveals something real):
 *   - Overall attrition is rising through FY2025.
 *   - It concentrates in ENGINEERING and among EARLY-TENURE employees (<18 mo).
 *   - Engagement scores are lowest in Engineering — the likely root cause.
 *
 * Outputs:
 *   data/employees.csv   — the cleaned employee dataset (deliverable)
 *   assets/data.js       — same rows as window.HR_DATA for the dashboard
 *
 * Run:  node data/generate_data.js
 * ==========================================================================*/
const fs = require('fs');
const path = require('path');

let seed = 73101;
function rand(){ seed = (seed*1103515245 + 12345) & 0x7fffffff; return seed/0x7fffffff; }
function pick(a){ return a[Math.floor(rand()*a.length)]; }
function gauss(m,s){ const u=Math.max(1e-9,rand()),v=rand(); return m+s*Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v); }
function wpick(map){ const r=rand(); let acc=0; for(const k in map){acc+=map[k]; if(r<=acc) return k;} return Object.keys(map)[0]; }

const DEPTS = {Engineering:0.30,Sales:0.18,Operations:0.16,'Customer Support':0.14,Marketing:0.10,Finance:0.07,HR:0.05};
const LOCATIONS = ['HQ','Remote','Regional-North','Regional-South'];
const GENDERS = {Female:0.46,Male:0.50,'Non-binary / Other':0.04};
const LEVELS = {Junior:0.40,Mid:0.34,Senior:0.20,Lead:0.06};
const SALARY = {Junior:[45,70],Mid:[65,95],Senior:[95,140],Lead:[135,190]}; // $K
const EXIT_REASONS = ['Better offer','Compensation','Career growth','Relocation','Manager / culture','Personal'];

const ANALYSIS_END = new Date(Date.UTC(2025,11,31));
function iso(d){ return d.toISOString().slice(0,10); }
function monthsBetween(a,b){ return (b.getUTCFullYear()-a.getUTCFullYear())*12 + (b.getUTCMonth()-a.getUTCMonth()); }
function deptEngagementMean(dept){ return dept==='Engineering'?3.0 : dept==='Customer Support'?3.4 : 3.8; }

let nextId = 1001;
function makeEmployee(hireDate){
  const dept = wpick(DEPTS);
  const level = wpick(LEVELS);
  const [smin,smax]=SALARY[level];
  return {
    employee_id:'E'+(nextId++),
    department:dept,
    location:pick(LOCATIONS),
    gender:wpick(GENDERS),
    role_level:level,
    hire_date:hireDate,
    exit_date:null,
    status:'Active',
    exit_reason:'',
    engagement_score:+Math.min(5,Math.max(1,gauss(deptEngagementMean(dept),0.7))).toFixed(1),
    performance_rating:+Math.min(5,Math.max(1,gauss(3.6,0.7))).toFixed(1),
    salary_k:Math.round(smin + rand()*(smax-smin))
  };
}

// ---- initial roster: hired before 2025, spread across 2017-2024 ----
const employees = [];
const N0 = 560;
for(let i=0;i<N0;i++){
  const y = 2017 + Math.floor(rand()*8);            // 2017..2024
  const mo = Math.floor(rand()*12), day = 1+Math.floor(rand()*27);
  employees.push(makeEmployee(iso(new Date(Date.UTC(y,mo,day)))));
}

// ---- simulate FY2025 month by month: hires + exits ----
for(let m=0;m<12;m++){
  const monthStart = new Date(Date.UTC(2025,m,1));
  const monthEnd = new Date(Date.UTC(2025,m+1,0));

  // new hires this month (steady hiring, slight Engineering tilt already in DEPTS)
  const nHires = 6 + Math.round(gauss(2,1.5));
  for(let h=0; h<Math.max(0,nHires); h++){
    const day = 1+Math.floor(rand()*27);
    employees.push(makeEmployee(iso(new Date(Date.UTC(2025,m,day)))));
  }

  // exits among currently-active employees
  for(const e of employees){
    if(e.status!=='Active') continue;
    const hire = new Date(e.hire_date+'T00:00:00Z');
    if(hire > monthStart) continue;                  // not yet started
    const tenure = monthsBetween(hire, monthStart);

    let hazard = 0.010;                              // base monthly exit prob
    if(e.department==='Engineering') hazard *= 2.3;  // Engineering churns most
    else if(e.department==='Sales')  hazard *= 1.5;
    if(tenure < 18) hazard *= 2.1;                   // early-tenure risk
    else if(tenure < 36) hazard *= 1.2;
    else hazard *= 0.7;
    hazard *= (1 + m*0.06);                          // attrition ramps through the year
    if(e.engagement_score < 3.0) hazard *= 1.5;      // disengaged leave more

    if(rand() < hazard){
      const day = 1+Math.floor(rand()*27);
      e.exit_date = iso(new Date(Date.UTC(2025,m,day)));
      e.status = 'Left';
      e.exit_reason = e.department==='Engineering'
        ? wpick({'Career growth':0.32,'Compensation':0.30,'Better offer':0.20,'Manager / culture':0.12,'Relocation':0.03,'Personal':0.03})
        : pick(EXIT_REASONS);
    }
  }
}

// ---- finalise derived fields ----
for(const e of employees){
  const hire = new Date(e.hire_date+'T00:00:00Z');
  const end = e.exit_date ? new Date(e.exit_date+'T00:00:00Z') : ANALYSIS_END;
  e.tenure_months = Math.max(0, monthsBetween(hire,end));
  e.tenure_band = e.tenure_months<18 ? '0-18 mo'
                : e.tenure_months<36 ? '18-36 mo'
                : e.tenure_months<60 ? '3-5 yrs' : '5+ yrs';
}

// ---- write CSV ----
const cols=['employee_id','department','location','gender','role_level','hire_date','exit_date',
            'status','exit_reason','tenure_months','tenure_band','engagement_score','performance_rating','salary_k'];
const csv=[cols.join(',')].concat(employees.map(e=>cols.map(c=>e[c]===null?'':e[c]).join(','))).join('\n');
fs.writeFileSync(path.join(__dirname,'employees.csv'), csv);

// ---- write data.js ----
const assetsDir=path.join(__dirname,'..','assets');
if(!fs.existsSync(assetsDir)) fs.mkdirSync(assetsDir,{recursive:true});
fs.writeFileSync(path.join(assetsDir,'data.js'),'window.HR_DATA = '+JSON.stringify(employees)+';\n');

// ---- summary ----
const active=employees.filter(e=>e.status==='Active').length;
const left2025=employees.filter(e=>e.exit_date && e.exit_date.startsWith('2025')).length;
console.log('Employees (ever):', employees.length);
console.log('Active at year-end:', active);
console.log('Exits in 2025:', left2025);
console.log('YTD attrition ~', (left2025/((active+left2025))*100).toFixed(1)+'%');
console.log('Wrote employees.csv and assets/data.js');
