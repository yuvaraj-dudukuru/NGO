import 'package:flutter/material.dart';

void main() => runApp(MyApp());

// ---------------------------------------------------------------------------
// ROOT WIDGET
// ---------------------------------------------------------------------------
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),
    );
  }
}

// ---------------------------------------------------------------------------
// STEP 2 + 4: HOME SCREEN — a title bar and a button that navigates to the list
// ---------------------------------------------------------------------------
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Home')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Step 4: navigate to the list screen (auto back button)
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ListScreen()),
            );
          },
          child: Text('View List'),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// STEP 3 + 5: LIST SCREEN — a ListView of names; tapping one opens details
// ---------------------------------------------------------------------------
class ListScreen extends StatelessWidget {
  final List<String> items = ['Priya', 'Arjun', 'Sara', 'Ravi'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('List')),
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              leading: Icon(Icons.person),
              title: Text(items[index]),
              onTap: () {
                // Step 5: navigate to details, passing the tapped name
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => DetailsScreen(name: items[index]),
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
// STEP 5: DETAILS SCREEN — receives a name and displays it (data passed in)
// ---------------------------------------------------------------------------
class DetailsScreen extends StatelessWidget {
  final String name;

  DetailsScreen({required this.name});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Details')),
      body: Center(
        child: Text(name, style: TextStyle(fontSize: 32)),
      ),
    );
  }
}
