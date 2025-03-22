def checkforpalindrome(s):
    return s == s[::-1]

string =input("enter word")
result = checkforpalindrome(string)
print("Is palindrome:", result)