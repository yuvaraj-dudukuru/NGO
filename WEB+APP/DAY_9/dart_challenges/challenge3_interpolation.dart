// Challenge 3: Use string interpolation to build and print a sentence.
void main() {
  String name = 'Demo User';
  String course = 'Flutter';
  int year = 1;

  // $variable inserts a value; ${expression} evaluates an expression.
  print('$name is a year-$year student learning $course.');
  print('Next year they will be in year ${year + 1}.');
}
