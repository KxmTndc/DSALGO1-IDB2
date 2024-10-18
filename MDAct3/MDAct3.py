
from ArrayStack import ArrayStack as Stack

from ArrayStack import ArrayStack as Stack

def is_matched(expression):

    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = Stack()  # Using ArrayStack instead of list

    for char in expression:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return "The symbols are not balanced"

    return "The symbols are balanced" if stack.is_empty() else "The symbols are not balanced"

def main():
    print("Balanced Symbols Checker")
    print("-------------------------")

    while True:
        user_input = input("Enter an expression (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        result = is_matched(user_input)
        print(result)
        print()

if __name__ == "__main__":
    main()
def reverse_file(myfile):
        stack = []

        with open(myfile, 'r') as file:
            for line in file:
                stack.append(line.rstrip('\n'))

        with open(myfile, 'w') as file:
            while stack:
                file.write(stack.pop() + '\n')

myfile = 'myfile.txt'
reverse_file('myfile.txt')
print("File Contents Reversed!")