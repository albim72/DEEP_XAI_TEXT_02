import lambdy as lb

print("Pierwszy program w języku Python!")

def policz(a:int,b:float,c:float,y:int=5)->float:
    n = (a+b)*y-c
    return n
print(policz(4,6.6,1.2,56))
print(policz(4,6.6,1.2))
print(policz(4,4,True,1.9))

t = policz(1,1,1,1)
print(t)
print(type(t))

print((lambda a:a+11)(8))

d = lambda a,b,c=1:(a+b)*c
print(d(15,3,2))
print(d(2,2))

print("__________ listy z biblioteki lambdy ______________")

print(lb.nbparzyste)
print(lb.cube)
