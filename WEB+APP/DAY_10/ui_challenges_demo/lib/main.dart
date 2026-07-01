import 'package:flutter/material.dart';

void main() => runApp(UiChallengesApp());

// ---------------------------------------------------------------------------
// ROOT WIDGET — a menu that opens each of the five UI challenges
// ---------------------------------------------------------------------------
class UiChallengesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Day 10 UI Challenges',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.teal),
      home: MenuScreen(),
    );
  }
}

class MenuScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Day 10 — UI Challenges')),
      body: ListView(
        children: [
          _tile(context, '1. Profile Card', ProfileCardChallenge()),
          _tile(context, '2. Login Form', LoginFormChallenge()),
          _tile(context, '3. Settings Screen', SettingsChallenge()),
          _tile(context, '4. Product Grid', ProductGridChallenge()),
          _tile(context, '5. Full Scaffold (AppBar/FAB/Drawer)',
              FullScaffoldChallenge()),
        ],
      ),
    );
  }

  Widget _tile(BuildContext context, String label, Widget screen) {
    return Card(
      margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        title: Text(label),
        trailing: Icon(Icons.arrow_forward_ios, size: 16),
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => screen),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 1: Profile card — Card + Row + Column + Expanded
// ---------------------------------------------------------------------------
class ProfileCardChallenge extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('1. Profile Card')),
      body: Center(
        child: Card(
          margin: EdgeInsets.all(16),
          elevation: 4,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: Padding(
            padding: EdgeInsets.all(16),
            child: Row(
              children: [
                // Avatar (placeholder initials)
                CircleAvatar(
                  radius: 40,
                  backgroundColor: Colors.teal,
                  child: Text('JD',
                      style: TextStyle(fontSize: 28, color: Colors.white)),
                ),
                SizedBox(width: 16),
                // Expanded so the text column fills the rest of the row
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('Jordan Doe',
                          style: TextStyle(
                              fontSize: 22, fontWeight: FontWeight.bold)),
                      SizedBox(height: 4),
                      Text('Flutter Developer',
                          style: TextStyle(color: Colors.grey[700])),
                      SizedBox(height: 8),
                      Row(
                        children: [
                          Icon(Icons.location_on,
                              size: 16, color: Colors.teal),
                          SizedBox(width: 4),
                          Text('Bangalore, IN'),
                        ],
                      ),
                      SizedBox(height: 4),
                      Row(
                        children: [
                          Icon(Icons.email, size: 16, color: Colors.teal),
                          SizedBox(width: 4),
                          Expanded(child: Text('jordan.doe@example.com')),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 2: Login form — two TextFields + a submit button
// ---------------------------------------------------------------------------
class LoginFormChallenge extends StatefulWidget {
  @override
  State<LoginFormChallenge> createState() => _LoginFormChallengeState();
}

class _LoginFormChallengeState extends State<LoginFormChallenge> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _obscure = true;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('2. Login Form')),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.lock_outline, size: 64, color: Colors.teal),
            SizedBox(height: 24),
            TextField(
              controller: _emailController,
              keyboardType: TextInputType.emailAddress,
              decoration: InputDecoration(
                labelText: 'Email',
                hintText: 'you@example.com',
                prefixIcon: Icon(Icons.email),
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16),
            TextField(
              controller: _passwordController,
              obscureText: _obscure,
              decoration: InputDecoration(
                labelText: 'Password',
                prefixIcon: Icon(Icons.lock),
                suffixIcon: IconButton(
                  icon: Icon(
                      _obscure ? Icons.visibility : Icons.visibility_off),
                  onPressed: () => setState(() => _obscure = !_obscure),
                ),
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 24),
            ElevatedButton(
              onPressed: () {
                // Demo only: show what was entered.
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                      content: Text(
                          'Submitted: ${_emailController.text.isEmpty ? "(empty)" : _emailController.text}')),
                );
              },
              style: ElevatedButton.styleFrom(
                  minimumSize: Size(double.infinity, 50)),
              child: Text('Sign In'),
            ),
          ],
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 3: Settings screen — ListView of ListTiles + Dividers
// ---------------------------------------------------------------------------
class SettingsChallenge extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('3. Settings')),
      body: ListView(
        children: [
          ListTile(
            leading: Icon(Icons.person),
            title: Text('Account'),
            subtitle: Text('Profile, password'),
            trailing: Icon(Icons.chevron_right),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.notifications),
            title: Text('Notifications'),
            trailing: Switch(value: true, onChanged: null),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.lock),
            title: Text('Privacy'),
            trailing: Icon(Icons.chevron_right),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.language),
            title: Text('Language'),
            subtitle: Text('English'),
            trailing: Icon(Icons.chevron_right),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.help),
            title: Text('Help & Support'),
            trailing: Icon(Icons.chevron_right),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.info),
            title: Text('About'),
            trailing: Icon(Icons.chevron_right),
          ),
        ],
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 4: Product grid — GridView with image, name, price
// (Uses an icon as a placeholder "image" so it runs offline.)
// ---------------------------------------------------------------------------
class ProductGridChallenge extends StatelessWidget {
  final List<Map<String, dynamic>> products = const [
    {'name': 'Wireless Mouse', 'price': r'$24.99', 'color': Colors.blue},
    {'name': 'Mechanical Keyboard', 'price': r'$79.00', 'color': Colors.red},
    {'name': 'USB-C Hub', 'price': r'$39.50', 'color': Colors.orange},
    {'name': 'Webcam HD', 'price': r'$54.00', 'color': Colors.purple},
    {'name': 'Desk Lamp', 'price': r'$29.99', 'color': Colors.green},
    {'name': 'Headphones', 'price': r'$99.00', 'color': Colors.brown},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('4. Product Grid')),
      body: GridView.builder(
        padding: EdgeInsets.all(12),
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          crossAxisSpacing: 12,
          mainAxisSpacing: 12,
          childAspectRatio: 0.8,
        ),
        itemCount: products.length,
        itemBuilder: (context, index) {
          final product = products[index];
          return Card(
            clipBehavior: Clip.antiAlias,
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Placeholder "image" area
                Expanded(
                  child: Container(
                    color: (product['color'] as Color).withOpacity(0.2),
                    child: Icon(Icons.image,
                        size: 56, color: product['color'] as Color),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.all(8),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(product['name'] as String,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(fontWeight: FontWeight.bold)),
                      SizedBox(height: 4),
                      Text(product['price'] as String,
                          style: TextStyle(color: Colors.teal)),
                    ],
                  ),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 5: Full Scaffold — AppBar with actions, body, FAB, and Drawer
// ---------------------------------------------------------------------------
class FullScaffoldChallenge extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('5. Full Scaffold'),
        actions: [
          IconButton(icon: Icon(Icons.search), onPressed: () {}),
          IconButton(icon: Icon(Icons.more_vert), onPressed: () {}),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: BoxDecoration(color: Colors.teal),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  CircleAvatar(
                      radius: 28,
                      backgroundColor: Colors.white,
                      child: Text('A', style: TextStyle(fontSize: 24))),
                  SizedBox(height: 8),
                  Text('Alex Rivera',
                      style: TextStyle(color: Colors.white, fontSize: 18)),
                ],
              ),
            ),
            ListTile(leading: Icon(Icons.home), title: Text('Home')),
            ListTile(leading: Icon(Icons.settings), title: Text('Settings')),
            ListTile(leading: Icon(Icons.logout), title: Text('Log out')),
          ],
        ),
      ),
      body: Center(
        child: Text(
          'Open the drawer (top-left),\ntry the AppBar actions,\nor tap the + button.',
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 18),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: Icon(Icons.add),
      ),
    );
  }
}
