class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        s = [0]
        """
        stack = []
        res = -1
        for i in tokens:
            if  i not in ["+","*","/","-"]:
                stack.append(i)
            else:
                a = stack.pop() #0
                b = stack.pop() #10
                if i == "+":
                    res = int(a)+int(b)
                elif i =="-":
                    res = int(b)-int(a)
                elif i == "*":
                    res = int(a)*int(b)
                else:
                    res = int(int(b)/int(a))

                stack.append(res)
                print(stack)
        return int(stack.pop())


