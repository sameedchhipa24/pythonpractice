# colors:int="sameed";

# for color in colors:
#     print(color)

# a=3
# def abc(a):
#     num1=4
#     print(num1)
# abc(a)

# x=[1,2,3,4];

# y=x.copy()

# print(id(x))
# print(id(y))



def fibonacci_Series(f):
    if f==0 or f==1:
        return 1
    else:
        return f* (fibonacci_Series(f-1) + fibonacci_Series(f-2))
print(fibonacci_Series(8))