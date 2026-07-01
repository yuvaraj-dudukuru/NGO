// Challenge 5: Create a List of skills and a Map of contact info, then print them.
void main() {
  // A List (ordered collection)
  List<String> skills = ['HTML', 'CSS', 'JavaScript', 'Flutter & Dart'];

  // A Map (key-value pairs)
  Map<String, String> contact = {
    'email': 'demo@example.com',
    'phone': '+00 00000 00000',
    'city': 'Demo City',
  };

  print('Skills:');
  for (String skill in skills) {
    print('  - $skill');
  }

  print('\nContact:');
  contact.forEach((key, value) {
    print('  $key: $value');
  });

  // You can also print the whole collection directly:
  print('\nRaw list: $skills');
  print('Raw map:  $contact');
}
