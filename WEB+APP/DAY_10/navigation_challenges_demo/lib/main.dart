import 'package:flutter/material.dart';

void main() => runApp(NavigationChallengesApp());

// ---------------------------------------------------------------------------
// ROOT WIDGET — registers named routes (used by Challenge 2 & 4) and opens a menu
// ---------------------------------------------------------------------------
class NavigationChallengesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Day 10 Navigation Challenges',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      initialRoute: '/',
      // Challenge 2 & 4: named routes registered centrally.
      routes: {
        '/': (context) => MenuScreen(),
        '/named-a': (context) => NamedScreenA(),
        '/named-b': (context) => NamedScreenB(),
        '/red': (context) => ColorScreen(title: 'Red Screen', color: Colors.red),
        '/green': (context) =>
            ColorScreen(title: 'Green Screen', color: Colors.green),
        '/blue': (context) =>
            ColorScreen(title: 'Blue Screen', color: Colors.blue),
      },
    );
  }
}

class MenuScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Day 10 — Navigation Challenges')),
      body: ListView(
        children: [
          _tile(context, '1. push / pop (two screens)',
              () => _pushWidget(context, PushScreenOne())),
          _tile(context, '2. Named routes',
              () => Navigator.pushNamed(context, '/named-a')),
          _tile(context, '3. List -> Details (pass data)',
              () => _pushWidget(context, PeopleListScreen())),
          _tile(context, '4. Home -> three screens',
              () => _pushWidget(context, HubScreen())),
          _tile(context, '5. Return data on pop',
              () => _pushWidget(context, PickerHomeScreen())),
        ],
      ),
    );
  }

  Widget _tile(BuildContext context, String label, VoidCallback onTap) {
    return Card(
      margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        title: Text(label),
        trailing: Icon(Icons.arrow_forward_ios, size: 16),
        onTap: onTap,
      ),
    );
  }
}

void _pushWidget(BuildContext context, Widget screen) {
  Navigator.push(context, MaterialPageRoute(builder: (context) => screen));
}

// ---------------------------------------------------------------------------
// CHALLENGE 1: Two screens connected with Navigator.push / pop
// ---------------------------------------------------------------------------
class PushScreenOne extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('1. Screen One')),
      body: Center(
        child: ElevatedButton(
          child: Text('Go to Screen Two (push)'),
          onPressed: () => _pushWidget(context, PushScreenTwo()),
        ),
      ),
    );
  }
}

class PushScreenTwo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('1. Screen Two')),
      body: Center(
        child: ElevatedButton(
          child: Text('Go back (pop)'),
          onPressed: () => Navigator.pop(context),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 2: The same flow, but using named routes (registered above)
// ---------------------------------------------------------------------------
class NamedScreenA extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('2. Screen A (named)')),
      body: Center(
        child: ElevatedButton(
          child: Text("pushNamed('/named-b')"),
          onPressed: () => Navigator.pushNamed(context, '/named-b'),
        ),
      ),
    );
  }
}

class NamedScreenB extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('2. Screen B (named)')),
      body: Center(
        child: ElevatedButton(
          child: Text('Back to A (pop)'),
          onPressed: () => Navigator.pop(context),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 3: List -> Details, passing data through the constructor
// ---------------------------------------------------------------------------
class PeopleListScreen extends StatelessWidget {
  // Placeholder data.
  final List<Map<String, String>> people = const [
    {'name': 'Nova Carter', 'role': 'Designer'},
    {'name': 'Liam Brooks', 'role': 'Engineer'},
    {'name': 'Maya Singh', 'role': 'Product Manager'},
    {'name': 'Theo Park', 'role': 'QA Analyst'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('3. People List')),
      body: ListView.builder(
        itemCount: people.length,
        itemBuilder: (context, index) {
          final person = people[index];
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            child: ListTile(
              leading: CircleAvatar(child: Text(person['name']![0])),
              title: Text(person['name']!),
              subtitle: Text(person['role']!),
              trailing: Icon(Icons.arrow_forward_ios, size: 16),
              onTap: () {
                // Pass the tapped person's data via the constructor.
                _pushWidget(context, PersonDetailsScreen(person: person));
              },
            ),
          );
        },
      ),
    );
  }
}

class PersonDetailsScreen extends StatelessWidget {
  final Map<String, String> person; // received data

  PersonDetailsScreen({required this.person});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('3. Details')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(
              radius: 50,
              child: Text(person['name']![0],
                  style: TextStyle(fontSize: 40)),
            ),
            SizedBox(height: 16),
            Text(person['name']!,
                style:
                    TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            Text(person['role']!,
                style: TextStyle(fontSize: 18, color: Colors.grey)),
          ],
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 4: A home screen that navigates to three different screens
// (uses the named routes /red, /green, /blue)
// ---------------------------------------------------------------------------
class HubScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('4. Hub')),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _navButton(context, 'Open Red Screen', Colors.red, '/red'),
            SizedBox(height: 16),
            _navButton(context, 'Open Green Screen', Colors.green, '/green'),
            SizedBox(height: 16),
            _navButton(context, 'Open Blue Screen', Colors.blue, '/blue'),
          ],
        ),
      ),
    );
  }

  Widget _navButton(
      BuildContext context, String label, Color color, String route) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        backgroundColor: color,
        minimumSize: Size(double.infinity, 50),
      ),
      onPressed: () => Navigator.pushNamed(context, route),
      child: Text(label),
    );
  }
}

class ColorScreen extends StatelessWidget {
  final String title;
  final Color color;

  ColorScreen({required this.title, required this.color});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(title), backgroundColor: color),
      backgroundColor: color.withOpacity(0.2),
      body: Center(
        child: Text(title, style: TextStyle(fontSize: 28)),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// CHALLENGE 5: A screen that returns data on pop, received by the previous one
// ---------------------------------------------------------------------------
class PickerHomeScreen extends StatefulWidget {
  @override
  State<PickerHomeScreen> createState() => _PickerHomeScreenState();
}

class _PickerHomeScreenState extends State<PickerHomeScreen> {
  String _selected = 'Nothing yet';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('5. Return Data on Pop')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('You picked:', style: TextStyle(fontSize: 18)),
            SizedBox(height: 8),
            Text(_selected,
                style:
                    TextStyle(fontSize: 26, fontWeight: FontWeight.bold)),
            SizedBox(height: 24),
            ElevatedButton(
              child: Text('Pick a fruit'),
              onPressed: () async {
                // Wait for the pushed screen to pop and return a value.
                final result = await Navigator.push<String>(
                  context,
                  MaterialPageRoute(builder: (context) => FruitPickerScreen()),
                );
                if (result != null) {
                  setState(() => _selected = result);
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}

class FruitPickerScreen extends StatelessWidget {
  final List<String> fruits = const ['Apple', 'Banana', 'Cherry', 'Mango'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Pick a fruit')),
      body: ListView(
        children: fruits
            .map((fruit) => ListTile(
                  title: Text(fruit),
                  // Return this fruit to the previous screen.
                  onTap: () => Navigator.pop(context, fruit),
                ))
            .toList(),
      ),
    );
  }
}
