'''factorial of a number
def fact(n):
    if n>0:
        if n==0 or n==1:
            return 1
        else:
            return fact(n-1)*n
n = int(input("get me number:\t"))
print(f"factorial of {n} is :\t",fact(n))'''


'''amgstrom number
n = int(input("get me the number to check:\t"))
p = len(str(n))
s = sum(int(d)**p for d in str(n))
if s==n:
    print("yes")
else:
    print("nope")'''


'''nth multiple of m in fibonacci series
m = int(input("get me the number to check divisibility:\t"))
n = int(input("get me the nth multiple:\t"))
a,b,count = 0,1,0
while True:
    a,b = b,a+b
    if b%m==0:
        count+=1
        if count == n:
            print(b)
            break'''


'''sum of squares upto n natural numbers
n = int(input('get me the limit:\t'))
r= sum(d**2 for d in range(n+1))
print(r)'''


'''palindrome check
str = input("get me word to check:\t")
s = str.replace(" ","")
if s==s[::-1]:
    print('yes')
else:
    print('no')'''


''' symmetric and palindrome check
str = input('get me the string to check\t')
s = str.replace(" ","")
half=len(s)//2
sym = s[:half]==s[half:] if half%2==0 else s[:half]==s[half+1:]
pal= s==s[::-1]

print("symmetrical" if sym else "not symmetrical")
print("palindrome" if pal else "not palindrom")'''


'''reversing a string
s = input('gte me the string to perform the action:\t')
res = ' '.join(s.split()[::-1])
print(res)'''


'''removing letter in word
import re
s = "hello amrita"
print(s+"\n which letter wanted to be removed:")
l = input()
s = re.sub(l,"",s)
print(s)'''














