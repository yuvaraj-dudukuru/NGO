import 'package:flutter/material.dart';

void main() => runApp(PortfolioApp());

// ---------------------------------------------------------------------------
// MINI PROJECT 4: Portfolio App — home, projects, and contact screens
// ---------------------------------------------------------------------------
class PortfolioApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Portfolio',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.teal),
      initialRoute: '/',
      routes: {
        '/': (context) => PortfolioHomeScreen(),
        '/projects': (context) => ProjectsScreen(),
        '/contact': (context) => ContactScreen(),
      },
    );
  }
}

class PortfolioHomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('My Portfolio')),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(
              radius: 60,
              backgroundColor: Colors.teal,
              child: Text('SK',
                  style: TextStyle(fontSize: 44, color: Colors.white)),
            ),
            SizedBox(height: 16),
            Text('Sam Keller',
                style:
                    TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
            Text('Mobile App Developer',
                style: TextStyle(fontSize: 16, color: Colors.grey[700])),
            SizedBox(height: 40),
            ElevatedButton.icon(
              icon: Icon(Icons.work),
              label: Text('View Projects'),
              style: ElevatedButton.styleFrom(
                  minimumSize: Size(double.infinity, 50)),
              onPressed: () => Navigator.pushNamed(context, '/projects'),
            ),
            SizedBox(height: 16),
            OutlinedButton.icon(
              icon: Icon(Icons.email),
              label: Text('Contact Me'),
              style: OutlinedButton.styleFrom(
                  minimumSize: Size(double.infinity, 50)),
              onPressed: () => Navigator.pushNamed(context, '/contact'),
            ),
          ],
        ),
      ),
    );
  }
}

class ProjectsScreen extends StatelessWidget {
  final List<Map<String, String>> projects = const [
    {
      'name': 'Weather Now',
      'desc': 'A clean weather app with 7-day forecasts.'
    },
    {
      'name': 'TaskFlow',
      'desc': 'A productivity app for managing daily tasks.'
    },
    {
      'name': 'FitTrack',
      'desc': 'A fitness tracker with charts and goals.'
    },
    {
      'name': 'BookNest',
      'desc': 'A reading list app with progress tracking.'
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Projects')),
      body: ListView.builder(
        itemCount: projects.length,
        itemBuilder: (context, index) {
          final project = projects[index];
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            child: ListTile(
              leading: CircleAvatar(child: Text('${index + 1}')),
              title: Text(project['name']!),
              subtitle: Text(project['desc']!),
            ),
          );
        },
      ),
    );
  }
}

class ContactScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Contact')),
      body: ListView(
        padding: EdgeInsets.all(8),
        children: [
          ListTile(
              leading: Icon(Icons.email, color: Colors.teal),
              title: Text('Email'),
              subtitle: Text('sam.keller@example.com')),
          ListTile(
              leading: Icon(Icons.phone, color: Colors.teal),
              title: Text('Phone'),
              subtitle: Text('+1 555-0199')),
          ListTile(
              leading: Icon(Icons.public, color: Colors.teal),
              title: Text('Website'),
              subtitle: Text('www.samkeller.example')),
          ListTile(
              leading: Icon(Icons.location_on, color: Colors.teal),
              title: Text('Location'),
              subtitle: Text('Austin, TX')),
        ],
      ),
    );
  }
}
