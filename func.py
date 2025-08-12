def func1():
    print('a')
    print('b')

# func1()
# for i in [1,2,3]:
#     func1()

# def func2(element):
#     print(element, element*2)
#
# for i in [1,2,3]:
#     func2(i)

# def func3(name,surname="Sidorov"):
#     print(f"name is {name}, surname is {surname}")
#
# func3('ivan', 'petrov')
# func3('ivan')

# def sum2(a,b):
#     result=a+b
#     return result
#
# print(sum2(3,4))
#
# def any(a,b):
#     return a*b
# print(any(2,3))
#
#
# def mult(a,b):
#     res1=a+b
#     res2=a-b
#     return res1,res2
#
# v1,v2=mult(3,4)
# print(v1,v2)

# def func123(a:int):
#     return a*2
#
# print(func123(3))

def loop1():
    for element in [1,2,3,4,5,6,7,8]:
        print(element)
        if element > 3:
            return None

loop1()

