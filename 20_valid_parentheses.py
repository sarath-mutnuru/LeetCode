class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets = {')':'(', ']':'[', '}':'{'}
        for e in s:
            if e in brackets.values():
                st.append(e)
            if e in brackets:
                if not len(st) or st.pop() != brackets[e]:
                    return False
        if len(st):
            return False
        return True
        