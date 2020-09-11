#ques 2 -Write a Python program that accepts a word from the user and 
# reverse it

word = input("Enter Any  Word To Reverse: ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
    