# LinkedStack class for evaluating postfix expressions
def precedence(op):

    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):

    stack = []
    output = []
    for char in expression.split():
        if char.isdigit():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)


    while stack:
        output.append(stack.pop())
    return " ".join(output)


# PositionalList class for sorting numbers
class PositionalList:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, value):
        new_node = self._Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def to_list(self):
        return list(self)

def insertion_sort(positional_list, ascending=True):
    sorted_list = PositionalList()
    for value in positional_list:
        current = sorted_list.head
        new_node = PositionalList._Node(value)
        if ascending:
            while current and current.value < value:
                current = current.next
        else:
            while current and current.value > value:
                current = current.next
        if current is None:  # Insert at the end
            sorted_list.add_last(value)
        else:  # Insert before current
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            else:
                sorted_list.head = new_node
            current.prev = new_node
            sorted_list.size += 1

    return sorted_list


# Main loop for user input
while True:
    print("\nMenu:")
    print("1. Postfix expression")
    print("2. Sort a list of numbers")
    print("3. Exit")
    choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        expression = input("Enter an expression: (e.g ((5+2) ∗ (8−3))/4” is “5 2 + 8 3 − ∗ 4 / )").strip()
        postfix = infix_to_postfix(expression)
        print("Postfix expression:", postfix)

    elif choice == '2':
        user_input = input("Enter numbers separated by spaces (e.g., '1 72 81 25 65 91 11'): ")
        try:
            numbers = list(map(int, user_input.split()))
            positional_list = PositionalList()

            for number in numbers:
                positional_list.add_last(number)

            sorted_asc = insertion_sort(positional_list, ascending=True)
            sorted_desc = insertion_sort(positional_list, ascending=False)

            print("Sorted in ascending order:", sorted_asc.to_list())
            print("Sorted in descending order:", sorted_desc.to_list())
        except ValueError:
            print("Please enter valid integers.")

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")