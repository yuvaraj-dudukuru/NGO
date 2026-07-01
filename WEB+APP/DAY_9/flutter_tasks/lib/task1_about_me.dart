// Task 1: A simple "About Me" screen (StatelessWidget) with a name,
// a description, and an icon. Uses demo data only.
import 'package:flutter/material.dart';

void main() {
  runApp(AboutMeApp());
}

class AboutMeApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'About Me',
      debugShowCheckedModeBanner: false,
      home: AboutMeScreen(),
    );
  }
}

class AboutMeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('About Me'),
        backgroundColor: Colors.indigo,
      ),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Icon(Icons.face, size: 80, color: Colors.indigo),
            SizedBox(height: 16),
            Text(
              'Alex Demo',
              style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 12),
            Text(
              'A sample student learning Flutter. This is demo placeholder '
              'text describing the person — their interests, goals, and what '
              'they are currently building.',
              style: TextStyle(fontSize: 16, height: 1.4),
            ),
          ],
        ),
      ),
    );
  }
}
