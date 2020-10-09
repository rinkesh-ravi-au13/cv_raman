#Question 1:- https://leetcode.com/problems/generate-parentheses/submissions/


class Solution():
    def generateParenthesis(self, n):
        ans = []
        def gen(o, c, s):
            if o > c:
                 return
            if o == 0 and c == 0:
                ans.append(s)
                return
            if o == 0:
                gen(o, c-1, s+')')
            else:
                gen(o-1, c, s+'(')
                gen(o, c-1, s+')')
        gen(n,n,'')
        return ans