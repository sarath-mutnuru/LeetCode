class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval_terms(a, b, op):
            a, b = int(a), int(b)
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            return a // b if a * b >= 0 else -1 * ((-1 * a) // b )
        res = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                b = res.pop()
                a = res.pop()
                res.append(str(eval_terms(a, b, tokens[i])))
            else:
                res.append(tokens[i])
        return res.pop()
            
        
            