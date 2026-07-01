// Challenge 4: Use a ternary operator with % to print even or odd.
void main() {
  int number = 7;

  // condition ? valueIfTrue : valueIfFalse
  String result = (number % 2 == 0) ? 'even' : 'odd';

  print('$number is $result.');
}
