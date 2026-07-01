import 'package:flutter/material.dart';

void main() {
  runApp(StudentManagementApp());
}

// ---------------------------------------------------------------------------
// ROOT WIDGET: app setup with a centralized theme and named routes (Section 23)
// ---------------------------------------------------------------------------
class StudentManagementApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Student Management',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        // Centralized theme (Section 3.7)
        primarySwatch: Colors.blue,
        scaffoldBackgroundColor: Colors.grey[100],
      ),
      initialRoute: '/', // start at home
      routes: {
        // Register all simple screens. The details screen is pushed with data,
        // so it is not registered here.
        '/': (context) => HomeScreen(),
        '/students': (context) => StudentListScreen(),
        '/profile': (context) => ProfileScreen(),
        '/settings': (context) => SettingsScreen(),
      },
    );
  }
}

// ---------------------------------------------------------------------------
// HOME SCREEN: the hub with navigation buttons
// ---------------------------------------------------------------------------
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
            Text(
              'Welcome',
              style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 40),
            // Navigation buttons
            _buildNavButton(context, 'View Students', Icons.people, '/students'),
            SizedBox(height: 16),
            _buildNavButton(context, 'Profile', Icons.person, '/profile'),
            SizedBox(height: 16),
            _buildNavButton(context, 'Settings', Icons.settings, '/settings'),
          ],
        ),
      ),
    );
  }

  // A reusable helper that builds a navigation button (composition, Section 2.5)
  Widget _buildNavButton(
      BuildContext context, String label, IconData icon, String route) {
    return ElevatedButton.icon(
      onPressed: () => Navigator.pushNamed(context, route), // navigate by name
      icon: Icon(icon),
      label: Text(label),
      style: ElevatedButton.styleFrom(
        minimumSize: Size(double.infinity, 50), // full-width button
        padding: EdgeInsets.all(16),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// STUDENT LIST SCREEN: a ListView of students
// ---------------------------------------------------------------------------
class StudentListScreen extends StatelessWidget {
  // The data: a list of students (Section 12.3)
  final List<Map<String, String>> students = [
    {'name': 'Priya Sharma', 'course': 'Computer Science', 'year': '2nd Year'},
    {'name': 'Arjun Reddy', 'course': 'Electronics', 'year': '1st Year'},
    {'name': 'Sara Khan', 'course': 'Mechanical', 'year': '3rd Year'},
    {'name': 'Ravi Kumar', 'course': 'Civil', 'year': '2nd Year'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Students')),
      body: ListView.builder(
        // efficient list (Section 12.3)
        itemCount: students.length,
        itemBuilder: (context, index) {
          final student = students[index];
          return Card(
            // each student in a card (Section 14)
            margin: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.blue,
                child: Text(
                  student['name']![0], // first letter of the name
                  style: TextStyle(color: Colors.white),
                ),
              ),
              title: Text(student['name']!),
              subtitle: Text(student['course']!),
              trailing: Icon(Icons.arrow_forward_ios, size: 16),
              onTap: () {
                // Navigate to details, passing this student's data (Section 24)
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) =>
                        StudentDetailsScreen(student: student),
                  ),
                );
              },
            ),
          );
        },
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// STUDENT DETAILS SCREEN: shows one student (data passed in)
// ---------------------------------------------------------------------------
class StudentDetailsScreen extends StatelessWidget {
  final Map<String, String> student; // the data this screen receives

  StudentDetailsScreen({required this.student}); // constructor (Section 24)

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Student Details')), // auto back button
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            // Profile header
            CircleAvatar(
              radius: 50,
              backgroundColor: Colors.blue,
              child: Text(
                student['name']![0],
                style: TextStyle(fontSize: 40, color: Colors.white),
              ),
            ),
            SizedBox(height: 16),
            Text(
              student['name']!,
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 24),
            // Detail cards
            _buildDetailCard(Icons.book, 'Course', student['course']!),
            _buildDetailCard(Icons.calendar_today, 'Year', student['year']!),
          ],
        ),
      ),
    );
  }

  // A reusable detail row (composition, Section 2.5)
  Widget _buildDetailCard(IconData icon, String label, String value) {
    return Card(
      child: ListTile(
        leading: Icon(icon, color: Colors.blue),
        title: Text(label),
        subtitle: Text(value),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// PROFILE SCREEN
// ---------------------------------------------------------------------------
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

// ---------------------------------------------------------------------------
// SETTINGS SCREEN
// ---------------------------------------------------------------------------
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
