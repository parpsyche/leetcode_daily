class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for char in tokens:
            if char not in {'+', '-', '/', '*'}:
                s.append(int(char))
            else:
                second = s.pop()
                first = s.pop()
                val = None
                # print(first,char,second)
                if char == '+': val = first + second
                elif char == '-': val = first - second
                elif char == '*': val = first*second
                elif char == '/': val = int(first/second)
                s.append(val)
            
        return s[0]
                    