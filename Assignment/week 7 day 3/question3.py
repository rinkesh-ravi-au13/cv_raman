#Question3:- https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balancer  = 0 
        counter = 0   
        for i in range(len(s)): 
            if s[i] == 'L': 
                balancer += 1
            else:             
                balancer -= 1
            
            if balancer == 0:  
                counter += 1
    
        return counter 