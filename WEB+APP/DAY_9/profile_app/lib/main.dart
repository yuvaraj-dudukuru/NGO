import 'package:flutter/material.dart';

void main() {
  runApp(StudentProfileApp());
}

// The root widget of the app (a StatelessWidget - it does not change)
class StudentProfileApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // MaterialApp sets up the app with Material Design
    return MaterialApp(
      title: 'Student Profile',
      debugShowCheckedModeBanner: false, // hide the "debug" banner
      home: ProfileScreen(),             // the first screen to show
    );
  }
}

// The profile screen (a StatelessWidget - the info does not change)
class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // The top app bar with a title
      appBar: AppBar(
        title: Text('Student Profile'),
        backgroundColor: Colors.blue,
      ),
      // The main content area
      body: SingleChildScrollView(   // makes the content scrollable
        padding: EdgeInsets.all(16), // space around the content
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start, // align to the left
          children: [
            // ===== PROFILE SECTION =====
            Center(
              child: Column(
                children: [
                  // A circular profile icon
                  CircleAvatar(
                    radius: 50,
                    backgroundColor: Colors.blue,
                    child: Icon(Icons.person, size: 50, color: Colors.white),
                  ),
                  SizedBox(height: 10), // spacing
                  // The student's name
                  Text(
                    'Priya Sharma',
                    style:
                        TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                  ),
                  // The student's role
                  Text(
                    'Web Development Student',
                    style: TextStyle(fontSize: 16, color: Colors.grey),
                  ),
                ],
              ),
            ),
            SizedBox(height: 20),

            // ===== ABOUT SECTION =====
            Text(
              'About',
              style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue),
            ),
            SizedBox(height: 8),
            Text(
              'A first-year student passionate about building websites and '
              'mobile apps. Currently learning Flutter to build cross-platform '
              'applications.',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 20),

            // ===== SKILLS SECTION =====
            Text(
              'Skills',
              style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue),
            ),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.check_circle, color: Colors.green, size: 20),
              SizedBox(width: 8),
              Text('HTML, CSS, JavaScript', style: TextStyle(fontSize: 16)),
            ]),
            SizedBox(height: 4),
            Row(children: [
              Icon(Icons.check_circle, color: Colors.green, size: 20),
              SizedBox(width: 8),
              Text('Flutter & Dart', style: TextStyle(fontSize: 16)),
            ]),
            SizedBox(height: 4),
            Row(children: [
              Icon(Icons.check_circle, color: Colors.green, size: 20),
              SizedBox(width: 8),
              Text('Git & GitHub', style: TextStyle(fontSize: 16)),
            ]),
            SizedBox(height: 20),

            // ===== CONTACT SECTION =====
            Text(
              'Contact',
              style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue),
            ),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.email, color: Colors.blue, size: 20),
              SizedBox(width: 8),
              Text('priya@example.com', style: TextStyle(fontSize: 16)),
            ]),
            SizedBox(height: 4),
            Row(children: [
              Icon(Icons.phone, color: Colors.blue, size: 20),
              SizedBox(width: 8),
              Text('+91 98765 43210', style: TextStyle(fontSize: 16)),
            ]),
          ],
        ),
      ),
    );
  }
}
