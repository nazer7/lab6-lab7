def count(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count
string = input("enter word to check:")
upper, lower = count(string)
print("Upper case letters:", upper)
print("Lower case letters:", lower)