class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        stack = []
        stack.append('-1')
        top = 0
        if len(s)%2 ==0:
            for i in range(n):
                if stack[top]+s[i] in ['()','{}','[]']:
                    stack.pop()
                    top -= 1
                else:
                    top += 1
                    stack.insert(top,s[i])
            if stack[-1] == '-1' :
                return True
            else:
                return False

        else:
            return False
            


            

        

             
        