num = 331
a = num
rev = 0;
rem = 0;
while (num >0):
    rem = num % 10
    rev = rev+ rem
    num = num // 10
print(rev)
if (rev == a):
    print("given number is palindrome")
else:
    print("given number is not palindrome")
