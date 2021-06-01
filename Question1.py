# 1 Question


def sumList(l):
    count=0
    for i in l:
        count=count+i
    return count

l=eval(input("Enter the Elements of List:"))
print("Sum of All Elements in the List = " ,sumList(l))
