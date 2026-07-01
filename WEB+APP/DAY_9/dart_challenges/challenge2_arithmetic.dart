// Challenge 2: Demonstrate all arithmetic operators, including ~/ (integer division).
void main() {
  int a = 17;
  int b = 5;

  print('a = $a, b = $b');
  print('Addition       a + b  = ${a + b}');
  print('Subtraction    a - b  = ${a - b}');
  print('Multiplication a * b  = ${a * b}');
  print('Division       a / b  = ${a / b}');   // gives a double
  print('Int division   a ~/ b = ${a ~/ b}');  // integer (truncated) result
  print('Modulo         a % b  = ${a % b}');   // remainder
  print('Negation      -a      = ${-a}');
}
