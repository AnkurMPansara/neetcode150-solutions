class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        parser = []
        for c in tokens:
            print(c)
            if c == "+":
                num1 = parser.pop()
                num2 = parser.pop()
                parser.append(num1+num2)
            elif c == "-":
                num1 = parser.pop()
                num2 = parser.pop()
                parser.append(num2-num1)
            elif c == "*":
                num1 = parser.pop()
                num2 = parser.pop()
                parser.append(num2*num1)
            elif c == "/":
                num1 = parser.pop()
                num2 = parser.pop()
                div = math.floor(num2/num1) if num2/num1 > 0 else math.ceil(num2/num1)
                parser.append(div)
            else:
                parser.append(int(c))
            print(parser)
        return parser[-1]