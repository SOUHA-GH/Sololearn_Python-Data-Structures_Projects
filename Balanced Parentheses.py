#Given an expression as input, the program finds out whether the parentheses are balanced or not.
op= tuple('({[')
cl= tuple(')}]')
map = dict(zip(op, cl))
stack = []
def balanced(expression):
    for i in expression:
        if i in op:
            stack.append(map[i])
        elif i in cl:
            if not stack or i != stack.pop():
                return False
    if not stack:
        return True
    else:
        return False
print(balanced(input()))
