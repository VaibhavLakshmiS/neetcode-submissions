class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = ['}',')',']']
        openi = ['{','(','[']
        for i in s:
            if i in openi:
                stack.append(i)
            elif i in close:
                if not stack:
                    return False
                last_open = stack.pop()
                if openi.index(last_open)!= close.index(i):
                    print(last_open,i)
                    return False
        return len(stack)==0
