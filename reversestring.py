s = input()
reverse = ""
for i in s:
    reverse = i + reverse
if s == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
