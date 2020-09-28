class bruteforce:
    
    def twoSum(self, num, target):
        result = 
        
        for i in range(len(num)):
            for j in range(len(num)):
                if  (i != j) and (num[i] + num[j]) == target:
                    result = [i, j]
                else:
                    continue
    
        return result