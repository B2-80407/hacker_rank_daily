s = "0011101101011111101"

c0 = ''
c1= ''
for i in s:
    if i == '0':
        c0 = c0 + i
    else:
        c1 = c1 + i
l1 = list(c1)
new =''
for i in  range(len(l1)-1):
     new = new + l1[i]

print(new + c0 + "1")