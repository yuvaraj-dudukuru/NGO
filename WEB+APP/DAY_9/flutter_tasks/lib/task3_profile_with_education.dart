// Task 3: Student Profile App with a fourth section added ("Education").
import 'package:flutter/material.dart';

void main() {
  runApp(StudentProfileApp());
}

class StudentProfileApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Student Profile',
      debugShowCheckedModeBanner: false,
      home: ProfileScreen(),
    );
  }
}

class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Student Profile'),
        backgroundColor: Colors.blue,
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // ===== PROFILE SECTION =====
            Center(
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 50,
                    backgroundColor: Colors.blue,
                    child: Icon(Icons.person, size: 50, color: Colors.white),
                  ),
                  SizedBox(height: 10),
                  Text('Alex Demo',
                      style: TextStyle(
                          fontSize: 24, fontWeight: FontWeight.bold)),
                  Text('Web Development Student',
                      style: TextStyle(fontSize: 16, color: Colors.grey)),
                ],
              ),
            ),
            SizedBox(height: 20),

            // ===== ABOUT SECTION =====
            Text('About',
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue)),
            SizedBox(height: 8),
            Text(
              'A first-year student passionate about building websites and '
              'mobile apps. Currently learning Flutter to build cross-platform '
              'applications.',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 20),

            // ===== SKILLS SECTION =====
            Text('Skills',
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue)),
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
            SizedBox(height: 20),

            // ===== EDUCATION SECTION (the new 4th section) =====
            Text('Education',
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue)),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.school, color: Colors.deepPurple, size: 20),
              SizedBox(width: 8),
              Expanded(
                child: Text('B.Tech in Computer Science — Demo University',
                    style: TextStyle(fontSize: 16)),
              ),
            ]),
            SizedBox(height: 4),
            Row(children: [
              Icon(Icons.calendar_today, color: Colors.deepPurple, size: 20),
              SizedBox(width: 8),
              Text('2024 - 2028 (expected)', style: TextStyle(fontSize: 16)),
            ]),
            SizedBox(height: 20),

            // ===== CONTACT SECTION =====
            Text('Contact',
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue)),
            SizedBox(height: 8),
            Row(children: [
              Icon(Icons.email, color: Colors.blue, size: 20),
              SizedBox(width: 8),
              Text('alex@example.com', style: TextStyle(fontSize: 16)),
            ]),
            SizedBox(height: 4),
            Row(children: [
              Icon(Icons.phone, color: Colors.blue, size: 20),
              SizedBox(width: 8),
              Text('+00 00000 00000', style: TextStyle(fontSize: 16)),
            ]),
          ],
        ),
      ),
    );
  }
}
