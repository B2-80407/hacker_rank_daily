# l = [ 23,24,24,5,4,5,5454,3,5,3,33,4,2,43,1,2344,3,1,12,44,2,4,5554,3,221,3332,3,33,32,112,2,4,32,3,42,3,332,2,3,566,554,322,]
#
#
# re = list(filter( lambda x : x % 8 == 0 , range(0,78) ))
# for i in range(0,4):
#     print(re[i])
# print(re)


def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller  = x
    for i in range(smaller , 0 , -1):
        if (y % i == 0 and x % i == 0):
            print(f"{i} is a hcf of {x} and {y}")
            break
        else:
            pass

hcf(10,310)