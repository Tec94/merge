def reverseString(s):
    if len(s)==0:
        return s
    else:
        s[0], s[len(s)-1] = s[len(s)-1], s[0]
        reverseString(s[1:len(s)-2:])

s = ["h","e","l","l","o"]
reverseString(s)
print(s)