class Stack:
    def __init__(stack):
        stack.items = []
    def push(stack, value):
        stack.items.append(value)

    def pop(stack):
        return stack.items.pop() if not stack.is_empty() else None

    def is_empty(stack):
        return len(stack.items) == 0

    def top(stack):
        return stack.items[-1] if not stack.is_empty() else None

    def __len__(stack):
        return len(stack.items)


S = Stack()
X = Stack()
print("Operation - Stack - Return Value")

S.push(5)
print("S.push(5):",S.items)

S.push(3)
print("S.push(3):", S.items)

len(S)
print("len(S):", S.items,len(S))

S.pop()
print("S.pop():",S.items)

S.is_empty()
print("S.is_empty():", S.items,S.is_empty())

S.pop()
print("S.pop():", S.items)

print("S.is_empty():", S.items,S.is_empty())

S.pop()
print("S.pop():", S.items)

S.push(7)
print("S.push(7):", S.items)

S.push(9)
print("S.push(9):", S.items)

S.top()
print("S.top():", S.items, S.top())

S.push(4)
print("S.push(4)", S.items)

len(S)
print("len(S):", S.items, len(S))

S.pop()
print("S.pop():", S.items)

S.push(6)
print("S.push(6)", S.items)

S.push(8)
print("S.push(8)",S.items)

S.pop()
print("S.pop():", S.items)

print()

X.push(5)
print("push(5)", X.items)

X.push(3)
print("push(3)", X.items)

X.pop()
print("pop():", X.items)

X.push(2)
print("push(2)", X.items)

X.push(8)
print("push(8)", X.items)

X.pop()
print("pop():", X.items)

X.pop()
print("pop():", X.items)

X.push(9)
print("push(9)", X.items)

X.push(1)
print("push(1)", X.items)

X.pop()
print("pop():", X.items)

X.push(7)
print("push(7)", X.items)

X.push(6)
print("push(6)", X.items)

X.pop()
print("pop():", X.items)

X.pop()
print("pop():", X.items)

X.push(4)
print("push(4)", X.items)

X.pop()
print("pop():", X.items)

X.pop()
print("pop():", X.items)