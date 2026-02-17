s = "110001"

stack = []

for ch in s:
    if stack and ch==stack[-1]:
        stack.pop()
    else:
        stack.append(ch)

print(len(stack))

