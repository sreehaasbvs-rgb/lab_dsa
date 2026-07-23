
'''
def fun():
    print('hello world')
fun()
'''


'''
def check(a):
    if a%2==0:
        return True
    else:
        return False

a = int(input('get me the number to check even:\t'))
print('answer:\t',check(a))
'''


'''
def fun(x,y=100):
    print('x=\t',x)
    print('y=\t',y)

fun(15)
'''


'''
def greet(name1,res1):
    print('welcome to the hub ',name1)
    print('your position is ',res1)

n= input('get me the name of arrival:\t')
k = int(input('assaigned position:\t'))

greet(n,k)
'''




'''
def sq_fun(n):
    return n**2
for i in range(1,11):
    print(f'{i} square is ',sq_fun(i))
''' 



'''
check = lambda x: 'positive' if x>0 else 'negative' if x<0 else 'Zero'
print(check(5))
print(check(-5))
print(check(0))
'''



'''
res= lambda x,y: (x+y,x-y)
print(res(5,-5))
'''



a = [1,2,3,4,5]
s=[k*2 for k in a]
print(s)






      



































