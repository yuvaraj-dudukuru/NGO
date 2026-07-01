import 'package:flutter/material.dart';

void main() => runApp(RecipeApp());

// ---------------------------------------------------------------------------
// MINI PROJECT 2: Recipe App — list of recipes -> recipe details
// ---------------------------------------------------------------------------
class RecipeApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Recipes',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.orange),
      home: RecipeListScreen(),
    );
  }
}

// Sample recipe data.
final List<Map<String, dynamic>> recipes = [
  {
    'name': 'Margherita Pizza',
    'time': '30 min',
    'difficulty': 'Easy',
    'color': Colors.red,
    'ingredients': ['Dough', 'Tomato sauce', 'Mozzarella', 'Basil'],
    'steps': [
      'Roll out the dough.',
      'Spread tomato sauce.',
      'Add mozzarella and basil.',
      'Bake at 250C for 10 minutes.',
    ],
  },
  {
    'name': 'Veggie Stir Fry',
    'time': '20 min',
    'difficulty': 'Easy',
    'color': Colors.green,
    'ingredients': ['Bell peppers', 'Broccoli', 'Soy sauce', 'Garlic'],
    'steps': [
      'Chop all vegetables.',
      'Heat oil and add garlic.',
      'Stir fry the vegetables.',
      'Add soy sauce and serve.',
    ],
  },
  {
    'name': 'Pancakes',
    'time': '15 min',
    'difficulty': 'Easy',
    'color': Colors.brown,
    'ingredients': ['Flour', 'Milk', 'Egg', 'Sugar'],
    'steps': [
      'Mix all ingredients into a batter.',
      'Heat a non-stick pan.',
      'Pour batter and cook each side.',
      'Serve with syrup.',
    ],
  },
  {
    'name': 'Caesar Salad',
    'time': '10 min',
    'difficulty': 'Easy',
    'color': Colors.lightGreen,
    'ingredients': ['Lettuce', 'Croutons', 'Parmesan', 'Dressing'],
    'steps': [
      'Chop the lettuce.',
      'Add croutons and parmesan.',
      'Toss with dressing.',
      'Serve fresh.',
    ],
  },
];

class RecipeListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Recipes')),
      body: ListView.builder(
        itemCount: recipes.length,
        itemBuilder: (context, index) {
          final recipe = recipes[index];
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: recipe['color'] as Color,
                child: Icon(Icons.restaurant, color: Colors.white),
              ),
              title: Text(recipe['name'] as String),
              subtitle:
                  Text('${recipe['time']}  •  ${recipe['difficulty']}'),
              trailing: Icon(Icons.arrow_forward_ios, size: 16),
              onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => RecipeDetailsScreen(recipe: recipe),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}

class RecipeDetailsScreen extends StatelessWidget {
  final Map<String, dynamic> recipe;
  RecipeDetailsScreen({required this.recipe});

  @override
  Widget build(BuildContext context) {
    final ingredients = recipe['ingredients'] as List<String>;
    final steps = recipe['steps'] as List<String>;
    return Scaffold(
      appBar: AppBar(title: Text(recipe['name'] as String)),
      body: ListView(
        padding: EdgeInsets.all(16),
        children: [
          // Placeholder "image" header.
          Container(
            height: 160,
            decoration: BoxDecoration(
              color: (recipe['color'] as Color).withOpacity(0.25),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(Icons.restaurant_menu,
                size: 72, color: recipe['color'] as Color),
          ),
          SizedBox(height: 16),
          Row(
            children: [
              Chip(
                  avatar: Icon(Icons.timer, size: 18),
                  label: Text(recipe['time'] as String)),
              SizedBox(width: 8),
              Chip(
                  avatar: Icon(Icons.bar_chart, size: 18),
                  label: Text(recipe['difficulty'] as String)),
            ],
          ),
          SizedBox(height: 16),
          Text('Ingredients',
              style:
                  TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          ...ingredients.map((i) => ListTile(
                leading: Icon(Icons.check_circle_outline),
                title: Text(i),
                dense: true,
              )),
          SizedBox(height: 8),
          Text('Steps',
              style:
                  TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
          ...List.generate(
            steps.length,
            (index) => ListTile(
              leading: CircleAvatar(
                  radius: 14, child: Text('${index + 1}')),
              title: Text(steps[index]),
            ),
          ),
        ],
      ),
    );
  }
}
