// Task 5: A screen that centers a CircleAvatar and a name
// using Center and Column.
import 'package:flutter/material.dart';

void main() {
  runApp(CenteredAvatarApp());
}

class CenteredAvatarApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Centered Avatar',
      debugShowCheckedModeBanner: false,
      home: CenteredAvatarScreen(),
    );
  }
}

class CenteredAvatarScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Centered Avatar'),
        backgroundColor: Colors.orange,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center, // center vertically
          children: [
            CircleAvatar(
              radius: 60,
              backgroundColor: Colors.orange,
              child: Icon(Icons.person, size: 60, color: Colors.white),
            ),
            SizedBox(height: 16),
            Text(
              'Alex Demo',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
