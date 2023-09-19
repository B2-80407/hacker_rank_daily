s = input()


ans = []
#
# n = len(string);
i = 0

while(i < n):
    if string[i] == ' ':
        ans.append(word)
        word = ""
    else:
        word += string[i]
    i += 1

ans.append(word)

# print(ans)