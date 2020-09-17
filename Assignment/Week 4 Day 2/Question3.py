#Q3. Write a program which counts the no of vowels in a string.
def vowel_count(str): 
    count = 0
    vowel = set("aeiouAEIOU") 
    for alphabet in str: 
        if alphabet in vowel: 
            count = count + 1
            print("The Numbers of Vowels is :", count)
str = "My Name Is Rinkesh"
vowel_count(str) 