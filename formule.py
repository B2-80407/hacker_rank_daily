# 1.Below are the scores obtained by a student in tests Find variance,standard deviation and Range using python and formula.
#      45,36,40,41,41,34,39,42,41,49,36,56,38,41,38,42,40,39



n = int(input("Enter no of value you want to enter : "))
l1 = []
for i in range(n):
    a = int(input())
    l1.append(a)
print(l1)
print("calculate mean of a given list :")
def meanoflist(li):
    list1 = list(li)
    mean = 0
    for i in list1:
        mean = mean + int(i)
    return mean/n

print(meanoflist(l1))

print('range of a given list :')
def range1():
    max_num =  max(l1)
    min_num = min(l1)
    return (max_num - min_num)

print(range1())


print("standard deviation of a numbers :")
def standardDeviation():
    diffSquare  = 0
    m = meanoflist(l1)
    for i in l1:
        diffSquare = diffSquare + ((int(i) - m) ** 2  )
    diffSquareByTotalNum = diffSquare / n
    return  diffSquareByTotalNum ** 0.5

print(standardDeviation())


print('variance of a number :')
def variance():
    var = standardDeviation() ** 2
    return var

print(variance())



print(" median of a number :")
def median():
    if n % 2 == 0:
        return (int(l1[n//2]) + int(l1[n//2 + 1]) ) / 2
    else:
        return int(l1[n//2])
print(median())

print(" mode of a number :")


def mode():

    keyvalue = {}
    for  i in l1:
        count = 0
        for j in range(len(l1)):
            if i == l1[j]:
                count += 1
            else:
                pass
        keyvalue[i] = count
    modelist = []
    a = max( keyvalue.values())
    if a == 1 :
        pass
    else:

        for i in keyvalue:
            if keyvalue[i] == a:
                modelist.append(i)
            else:
                pass
    return modelist



print(mode())