// Task 4: A Container with padding, margin, and a background color,
// holding a Text inside it.
import 'package:flutter/material.dart';

void main() {
  runApp(ContainerDemoApp());
}

class ContainerDemoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Container Demo',
      debugShowCheckedModeBanner: false,
      home: ContainerScreen(),
    );
  }
}

class ContainerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Container Demo'),
        backgroundColor: Colors.teal,
      ),
      body: Center(
        child: Container(
          margin: EdgeInsets.all(24),      // space OUTSIDE the box
          padding: EdgeInsets.all(20),     // space INSIDE the box
          decoration: BoxDecoration(
            color: Colors.teal.shade100,   // background color
            borderRadius: BorderRadius.circular(12),
          ),
          child: Text(
            'This Text lives inside a Container with padding, margin, '
            'and a background color.',
            style: TextStyle(fontSize: 18, color: Colors.teal.shade900),
          ),
        ),
      ),
    );
  }
}
