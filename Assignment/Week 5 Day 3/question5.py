 def toggle(s): 
    word_list = s.split() 
    for word in word_list: 
        flag = 1
        if word[0].islower(): 
            r = 1
            
            for j in word: 
                  
                if j.isupper(): 
                    flag = 0
                    break
        else: 
            r = 0
            for j in word: 
               if j.islower(): 
                
                    flag = 0
                    break
          
             
        if flag == 0: print(word, end =" ") 
      
        else: 
          
            if r == 1: print(word.upper(), end =" ") 
              
            else: print(word.lower(), end =" ") 

s = 'abcdE'
toggle(s) 