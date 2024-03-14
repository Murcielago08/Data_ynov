# pile -> stack
    # LIFO
    # push : Ajouter sur la pile
    # pop : Retirer et renvoyer
    # peek : lire le dernier

def valider_parentheses(chaine):
    stack = []
    for char in chaine:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return len(stack) == 0

print(valider_parentheses("()"))
print(valider_parentheses("()()"))
print(valider_parentheses("(())((())(()))"))