def palindrome(s) :
    return s == s[ ::-1]
s = "aba"
out = palindrome (s)
if out :
    print ('YES')
else :
    print ("NO")