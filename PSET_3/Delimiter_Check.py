from Stack import Stack
import sys # for sys.argv, the command-line arguments

def delimiter_check(filename):
  stack = Stack()
  opens = '([{'
  closes = ')]}'
  text = open(filename, 'r')
  for line in text:
    for character in line:
      if character in opens:
        stack.push(character)
      if character in closes:
        if(len(stack) == 0):
          return False
        elif(character == ')' and stack.pop() != '('):
          return False
        elif(character == ']' and stack.pop() != '['):
          return False
        elif(character == '}' and stack.pop() != '{'):
          return False
  return len(stack) == 0

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


