import 'package:flutter/material.dart';

void main() => runApp(StudentManagementApp());

// ---------------------------------------------------------------------------
// MINI PROJECT 1: Student Management App (Section 31) — with sample data
// ---------------------------------------------------------------------------
class StudentManagementApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Student Management',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        scaffoldBackgroundColor: Colors.grey[100],
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => HomeScreen(),
        '/students': (context) => StudentListScreen(),
        '/profile': (context) => ProfileScreen(),
        '/settings': (context) => SettingsScreen(),
      },
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Student Management')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.school, size: 80, color: Colors.blue),
            SizedBox(height: 20),
            Text('Welcome',
                style:
                    TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
            SizedBox(height: 40),
            _navButton(context, 'View Students', Icons.people, '/students'),
            SizedBox(height: 16),
            _navButton(context, 'Profile', Icons.person, '/profile'),
            SizedBox(height: 16),
            _navButton(context, 'Settings', Icons.settings, '/settings'),
          ],
        ),
      ),
    );
  }

  Widget _navButton(
      BuildContext context, String label, IconData icon, String route) {
    return ElevatedButton.icon(
      onPressed: () => Navigator.pushNamed(context, route),
      icon: Icon(icon),
      label: Text(label),
      style: ElevatedButton.styleFrom(
        minimumSize: Size(double.infinity, 50),
        padding: EdgeInsets.all(16),
      ),
    );
  }
}

class StudentListScreen extends StatelessWidget {
  // Sample data.
  final List<Map<String, String>> students = const [
    {'name': 'Aisha Verma', 'course': 'Data Science', 'year': '2nd Year'},
    {'name': 'Ben Carter', 'course': 'Robotics', 'year': '1st Year'},
    {'name': 'Chen Wei', 'course': 'Architecture', 'year': '3rd Year'},
    {'name': 'Diego Lopez', 'course': 'Biotechnology', 'year': '2nd Year'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Students')),
      body: ListView.builder(
        itemCount: students.length,
        itemBuilder: (context, index) {
          final student = students[index];
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.blue,
                child: Text(student['name']![0],
                    style: TextStyle(color: Colors.white)),
              ),
              title: Text(student['name']!),
              subtitle: Text(student['course']!),
              trailing: Icon(Icons.arrow_forward_ios, size: 16),
              onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) =>
                      StudentDetailsScreen(student: student),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}

class StudentDetailsScreen extends StatelessWidget {
  final Map<String, String> student;
  StudentDetailsScreen({required this.student});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Student Details')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            CircleAvatar(
              radius: 50,
              backgroundColor: Colors.blue,
              child: Text(student['name']![0],
                  style: TextStyle(fontSize: 40, color: Colors.white)),
            ),
            SizedBox(height: 16),
            Text(student['name']!,
                style:
                    TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
            SizedBox(height: 24),
            _detailCard(Icons.book, 'Course', student['course']!),
            _detailCard(Icons.calendar_today, 'Year', student['year']!),
          ],
        ),
      ),
    );
  }

  Widget _detailCard(IconData icon, String label, String value) {
    return Card(
      child: ListTile(
        leading: Icon(icon, color: Colors.blue),
        title: Text(label),
        subtitle: Text(value),
      ),
    );
  }
}

class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Profile')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(radius: 50, child: Icon(Icons.person, size: 50)),
            SizedBox(height: 16),
            Text('Admin User', style: TextStyle(fontSize: 24)),
            Text('admin@school.com', style: TextStyle(color: Colors.grey)),
          ],
        ),
      ),
    );
  }
}

class SettingsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Settings')),
      body: ListView(
        children: [
          ListTile(
              leading: Icon(Icons.notifications),
              title: Text('Notifications')),
          Divider(),
          ListTile(leading: Icon(Icons.lock), title: Text('Privacy')),
          Divider(),
          ListTile(leading: Icon(Icons.help), title: Text('Help')),
          Divider(),
          ListTile(leading: Icon(Icons.info), title: Text('About')),
        ],
      ),
    );
  }
}
