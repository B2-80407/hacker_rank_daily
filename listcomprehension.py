

# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())
y = int(input())
z = int(input())

n = int(input())



# list1=[]
# for i in range(x+1):
#     for j in range (y+1):
#         for k in range (z+1):
#             if i+j+k != n:
#                 list2=[i,j,k]
#                 list1.append(list2)

# print(list1)



list1 = [
        [a, b, c]
        for a in range(x + 1)
        for b in range(y + 1)
        for c in range(z + 1)
        if a + b + c != n
    ]
print(list1)
