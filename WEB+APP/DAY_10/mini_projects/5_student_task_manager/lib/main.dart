import 'package:flutter/material.dart';

void main() => runApp(StudentTaskManagerApp());

// ---------------------------------------------------------------------------
// MINI PROJECT 5: Student Task Manager (planned on Day 8) — multi-screen UI
//   Home -> Task List -> Task Details, plus an Add Task screen that returns
//   data on pop. Sample data only.
// ---------------------------------------------------------------------------
class StudentTaskManagerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Student Task Manager',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      home: TaskHomeScreen(),
    );
  }
}

// A simple task model.
class Task {
  String title;
  String subject;
  String priority; // Low / Medium / High
  bool done;

  Task({
    required this.title,
    required this.subject,
    required this.priority,
    this.done = false,
  });
}

class TaskHomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Student Task Manager')),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.checklist, size: 80, color: Colors.deepPurple),
            SizedBox(height: 16),
            Text('Stay on top of your studies',
                textAlign: TextAlign.center,
                style:
                    TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            SizedBox(height: 40),
            ElevatedButton.icon(
              icon: Icon(Icons.list),
              label: Text('My Tasks'),
              style: ElevatedButton.styleFrom(
                  minimumSize: Size(double.infinity, 50)),
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => TaskListScreen()),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class TaskListScreen extends StatefulWidget {
  @override
  State<TaskListScreen> createState() => _TaskListScreenState();
}

class _TaskListScreenState extends State<TaskListScreen> {
  // Sample starting tasks.
  final List<Task> tasks = [
    Task(title: 'Read Chapter 5', subject: 'History', priority: 'Medium'),
    Task(title: 'Math problem set', subject: 'Mathematics', priority: 'High'),
    Task(title: 'Lab report', subject: 'Chemistry', priority: 'High'),
    Task(title: 'Essay draft', subject: 'English', priority: 'Low'),
  ];

  Color _priorityColor(String priority) {
    switch (priority) {
      case 'High':
        return Colors.red;
      case 'Medium':
        return Colors.orange;
      default:
        return Colors.green;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('My Tasks')),
      body: ListView.builder(
        itemCount: tasks.length,
        itemBuilder: (context, index) {
          final task = tasks[index];
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            child: ListTile(
              leading: Checkbox(
                value: task.done,
                onChanged: (value) =>
                    setState(() => task.done = value ?? false),
              ),
              title: Text(
                task.title,
                style: TextStyle(
                  decoration:
                      task.done ? TextDecoration.lineThrough : null,
                ),
              ),
              subtitle: Text(task.subject),
              trailing: Chip(
                label: Text(task.priority,
                    style: TextStyle(color: Colors.white, fontSize: 12)),
                backgroundColor: _priorityColor(task.priority),
              ),
              onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => TaskDetailsScreen(task: task),
                ),
              ),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () async {
          // Add Task screen returns a new Task on pop.
          final newTask = await Navigator.push<Task>(
            context,
            MaterialPageRoute(builder: (context) => AddTaskScreen()),
          );
          if (newTask != null) {
            setState(() => tasks.add(newTask));
          }
        },
      ),
    );
  }
}

class TaskDetailsScreen extends StatelessWidget {
  final Task task;
  TaskDetailsScreen({required this.task});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Task Details')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(task.title,
                style:
                    TextStyle(fontSize: 26, fontWeight: FontWeight.bold)),
            SizedBox(height: 16),
            Card(
                child: ListTile(
                    leading: Icon(Icons.book),
                    title: Text('Subject'),
                    subtitle: Text(task.subject))),
            Card(
                child: ListTile(
                    leading: Icon(Icons.flag),
                    title: Text('Priority'),
                    subtitle: Text(task.priority))),
            Card(
                child: ListTile(
                    leading: Icon(
                        task.done ? Icons.check_circle : Icons.pending),
                    title: Text('Status'),
                    subtitle:
                        Text(task.done ? 'Completed' : 'Pending'))),
          ],
        ),
      ),
    );
  }
}

class AddTaskScreen extends StatefulWidget {
  @override
  State<AddTaskScreen> createState() => _AddTaskScreenState();
}

class _AddTaskScreenState extends State<AddTaskScreen> {
  final _titleController = TextEditingController();
  final _subjectController = TextEditingController();
  String _priority = 'Medium';

  @override
  void dispose() {
    _titleController.dispose();
    _subjectController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Add Task')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _titleController,
              decoration: InputDecoration(
                  labelText: 'Task title', border: OutlineInputBorder()),
            ),
            SizedBox(height: 16),
            TextField(
              controller: _subjectController,
              decoration: InputDecoration(
                  labelText: 'Subject', border: OutlineInputBorder()),
            ),
            SizedBox(height: 16),
            DropdownButtonFormField<String>(
              value: _priority,
              decoration: InputDecoration(
                  labelText: 'Priority', border: OutlineInputBorder()),
              items: ['Low', 'Medium', 'High']
                  .map((p) =>
                      DropdownMenuItem(value: p, child: Text(p)))
                  .toList(),
              onChanged: (value) =>
                  setState(() => _priority = value ?? 'Medium'),
            ),
            SizedBox(height: 24),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                  minimumSize: Size(double.infinity, 50)),
              child: Text('Save Task'),
              onPressed: () {
                final title = _titleController.text.trim();
                if (title.isEmpty) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text('Please enter a title')),
                  );
                  return;
                }
                // Return the new task to the list screen.
                Navigator.pop(
                  context,
                  Task(
                    title: title,
                    subject: _subjectController.text.trim().isEmpty
                        ? 'General'
                        : _subjectController.text.trim(),
                    priority: _priority,
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
