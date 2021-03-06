#1
def a():
    return 5
print(a())
# It will print 5

#2
def a():
    return 5
print(a()+a())
# It will print 10

#3
def a():
    return 5
    return 10
print(a())
# It will print 5

#4
def a():
    return 5
    print(10)
print(a())
# It will print 5

#5
def a():    
    print(5)
x = a()
print(x)
# It will print 5

#6
def a(b,c):    
    print(b+c)
print(a(1,2) + a(2,3))
# It will print nothing since no values are saved

#7
def a(b,c):    
    return str(b)+str(c)
print(a(2,5))
# It will print 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# It will print 100 and 10

#9
def a(b,c):
    if b<c
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# It will print 7. The second will print 14. The third will print 21.

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# It will print 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# It will print 500. The second print will show 500. a() will print 300. The third print will show 500.

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# The first print will show 500. The second print will show 500. a() will print 300. The last print will show 500.

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# The first print will show 500. The second print will show 500. The third print will show 300 twice.

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# a() will print 1, 3, 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()print(y)
# It will print 1, 3, 5, 10