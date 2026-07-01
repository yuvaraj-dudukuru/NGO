import 'package:flutter/material.dart';

void main() => runApp(ExercisesDemoApp());

// ---------------------------------------------------------------------------
// ROOT WIDGET — a menu that opens each of the five exercises
// ---------------------------------------------------------------------------
class ExercisesDemoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Day 10 Practical Exercises',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: MenuScreen(),
    );
  }
}

class MenuScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Day 10 — Practical Exercises')),
      body: ListView(
        children: [
          _tile(context, '1. Row + mainAxisAlignment', RowExercise()),
          _tile(context, '2. Column + Expanded', ColumnExpandedExercise()),
          _tile(context, '3. Stack + Positioned badge', StackExercise()),
          _tile(context, '4. ListView.builder (10 items)', ListViewExercise()),
          _tile(context, '5. GridView.count (2 columns)', GridViewExercise()),
        ],
      ),
    );
  }

  Widget _tile(BuildContext context, String label, Widget screen) {
    return Card(
      margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        title: Text(label),
        trailing: Icon(Icons.arrow_forward_ios, size: 16),
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => screen),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// EXERCISE 1: A Row of three widgets, showing different mainAxisAlignment values
// ---------------------------------------------------------------------------
class RowExercise extends StatefulWidget {
  @override
  State<RowExercise> createState() => _RowExerciseState();
}

class _RowExerciseState extends State<RowExercise> {
  // Cycle through alignment options with the buttons below.
  final List<MainAxisAlignment> _alignments = const [
    MainAxisAlignment.start,
    MainAxisAlignment.center,
    MainAxisAlignment.end,
    MainAxisAlignment.spaceBetween,
    MainAxisAlignment.spaceAround,
    MainAxisAlignment.spaceEvenly,
  ];
  int _index = 0;

  @override
  Widget build(BuildContext context) {
    final current = _alignments[_index];
    return Scaffold(
      appBar: AppBar(title: Text('1. Row + mainAxisAlignment')),
      body: Column(
        children: [
          SizedBox(height: 20),
          Text('mainAxisAlignment: ${current.toString().split('.').last}',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 20),
          Container(
            color: Colors.indigo.shade50,
            padding: EdgeInsets.symmetric(vertical: 24),
            child: Row(
              mainAxisAlignment: current, // <-- the property being demonstrated
              children: [
                _box(Colors.red, 'A'),
                _box(Colors.green, 'B'),
                _box(Colors.blue, 'C'),
              ],
            ),
          ),
          SizedBox(height: 30),
          Wrap(
            spacing: 8,
            children: List.generate(_alignments.length, (i) {
              return ChoiceChip(
                label: Text(_alignments[i].toString().split('.').last),
                selected: _index == i,
                onSelected: (_) => setState(() => _index = i),
              );
            }),
          ),
        ],
      ),
    );
  }

  Widget _box(Color color, String label) {
    return Container(
      width: 60,
      height: 60,
      color: color,
      alignment: Alignment.center,
      child: Text(label, style: TextStyle(color: Colors.white, fontSize: 20)),
    );
  }
}

// ---------------------------------------------------------------------------
// EXERCISE 2: A Column where one child (Expanded) fills the available space
// ---------------------------------------------------------------------------
class ColumnExpandedExercise extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('2. Column + Expanded')),
      body: Column(
        children: [
          Container(
            height: 80,
            color: Colors.red.shade300,
            alignment: Alignment.center,
            child: Text('Fixed top (80px)', style: _label),
          ),
          // Expanded makes this child grow to fill all remaining space.
          Expanded(
            child: Container(
              color: Colors.green.shade300,
              alignment: Alignment.center,
              child: Text('Expanded — fills the space', style: _label),
            ),
          ),
          Container(
            height: 80,
            color: Colors.blue.shade300,
            alignment: Alignment.center,
            child: Text('Fixed bottom (80px)', style: _label),
          ),
        ],
      ),
    );
  }

  static const _label = TextStyle(color: Colors.white, fontSize: 18);
}

// ---------------------------------------------------------------------------
// EXERCISE 3: A Stack with a background container and a Positioned corner badge
// ---------------------------------------------------------------------------
class StackExercise extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('3. Stack + Positioned badge')),
      body: Center(
        child: Stack(
          children: [
            // Background container
            Container(
              width: 200,
              height: 200,
              decoration: BoxDecoration(
                color: Colors.indigo,
                borderRadius: BorderRadius.circular(12),
              ),
              alignment: Alignment.center,
              child: Icon(Icons.notifications, color: Colors.white, size: 80),
            ),
            // Positioned badge in the top-right corner
            Positioned(
              top: 8,
              right: 8,
              child: Container(
                padding: EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.red,
                  shape: BoxShape.circle,
                ),
                child: Text('3',
                    style: TextStyle(color: Colors.white, fontSize: 16)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// EXERCISE 4: A ListView.builder showing 10 items from data
// ---------------------------------------------------------------------------
class ListViewExercise extends StatelessWidget {
  // 10 items generated from data.
  final List<String> items =
      List.generate(10, (index) => 'Item ${index + 1}');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('4. ListView.builder (10 items)')),
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            child: ListTile(
              leading: CircleAvatar(child: Text('${index + 1}')),
              title: Text(items[index]),
            ),
          );
        },
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// EXERCISE 5: A GridView.count with 2 columns of colored containers
// ---------------------------------------------------------------------------
class GridViewExercise extends StatelessWidget {
  final List<Color> colors = const [
    Colors.red,
    Colors.green,
    Colors.blue,
    Colors.orange,
    Colors.purple,
    Colors.teal,
    Colors.pink,
    Colors.brown,
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('5. GridView.count (2 columns)')),
      body: GridView.count(
        crossAxisCount: 2, // two columns
        padding: EdgeInsets.all(12),
        crossAxisSpacing: 12,
        mainAxisSpacing: 12,
        children: List.generate(colors.length, (index) {
          return Container(
            decoration: BoxDecoration(
              color: colors[index],
              borderRadius: BorderRadius.circular(12),
            ),
            alignment: Alignment.center,
            child: Text('${index + 1}',
                style: TextStyle(color: Colors.white, fontSize: 28)),
          );
        }),
      ),
    );
  }
}
