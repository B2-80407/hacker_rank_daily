if __name__ == '__main__':
    l1 = []
    N = int(input())
    for i in range(N):
        name = input()
        score = float(input())
        l1.append([score, name])

    l1.sort()

    ans = []
    i = 1
    while i < N and l1[i][0] == l1[i - 1][0]:
        i = i + 1
    while i < N - 1 and l1[i][0] == l1[i + 1][0]:
        ans.append(l1[i][1])
        i += 1

    if i < N:
        ans.append(l1[i][1])

    for i in ans:
        print(i)



