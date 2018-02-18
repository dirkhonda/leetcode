#!/usr/bin/python

def valid_parentheses(s):
    dic = {'(':')', '{':'}', '[':']'}
    stack = []
    for c in s:
        if c in dic:
            stack.append(dic[c])
        elif not stack or c != stack.pop():
            return False
    return len(stack) == 0

if __name__ == "__main__":
    print(valid_parentheses("[)]"))

