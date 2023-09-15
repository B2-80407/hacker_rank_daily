n = int(input())
arr = map(int, input().split())
set1 = set(arr)
list1 = list(set1)
list1.sort()
if len(list1) == 1:
    print(list1)
else:
    print(list1[-2])

