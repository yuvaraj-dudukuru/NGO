import 'package:flutter/material.dart';

void main() => runApp(ContactsApp());

// ---------------------------------------------------------------------------
// MINI PROJECT 3: Contacts App — list of contacts -> details screen
// ---------------------------------------------------------------------------
class ContactsApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Contacts',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: ContactListScreen(),
    );
  }
}

// Sample contact data.
final List<Map<String, String>> contacts = [
  {
    'name': 'Olivia Bennett',
    'phone': '+1 555-0142',
    'email': 'olivia.bennett@example.com',
    'city': 'Seattle'
  },
  {
    'name': 'Raj Malhotra',
    'phone': '+91 98765-43210',
    'email': 'raj.malhotra@example.com',
    'city': 'Mumbai'
  },
  {
    'name': 'Sofia Rossi',
    'phone': '+39 02 1234 5678',
    'email': 'sofia.rossi@example.com',
    'city': 'Milan'
  },
  {
    'name': 'Kenji Tanaka',
    'phone': '+81 3-1234-5678',
    'email': 'kenji.tanaka@example.com',
    'city': 'Tokyo'
  },
  {
    'name': 'Amara Okafor',
    'phone': '+234 801 234 5678',
    'email': 'amara.okafor@example.com',
    'city': 'Lagos'
  },
];

class ContactListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Contacts')),
      body: ListView.builder(
        itemCount: contacts.length,
        itemBuilder: (context, index) {
          final contact = contacts[index];
          return Column(
            children: [
              ListTile(
                leading: CircleAvatar(
                  backgroundColor: Colors.indigo,
                  child: Text(contact['name']![0],
                      style: TextStyle(color: Colors.white)),
                ),
                title: Text(contact['name']!),
                subtitle: Text(contact['phone']!),
                trailing: Icon(Icons.arrow_forward_ios, size: 16),
                onTap: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) =>
                        ContactDetailsScreen(contact: contact),
                  ),
                ),
              ),
              Divider(height: 1),
            ],
          );
        },
      ),
    );
  }
}

class ContactDetailsScreen extends StatelessWidget {
  final Map<String, String> contact;
  ContactDetailsScreen({required this.contact});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Contact')),
      body: ListView(
        children: [
          SizedBox(height: 24),
          Center(
            child: CircleAvatar(
              radius: 50,
              backgroundColor: Colors.indigo,
              child: Text(contact['name']![0],
                  style: TextStyle(fontSize: 40, color: Colors.white)),
            ),
          ),
          SizedBox(height: 12),
          Center(
            child: Text(contact['name']!,
                style:
                    TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
          ),
          SizedBox(height: 24),
          _infoTile(Icons.phone, 'Phone', contact['phone']!),
          _infoTile(Icons.email, 'Email', contact['email']!),
          _infoTile(Icons.location_city, 'City', contact['city']!),
        ],
      ),
    );
  }

  Widget _infoTile(IconData icon, String label, String value) {
    return ListTile(
      leading: Icon(icon, color: Colors.indigo),
      title: Text(label),
      subtitle: Text(value),
    );
  }
}
