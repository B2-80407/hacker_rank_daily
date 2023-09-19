def main():
    n = int(input())
    l1 = input().split()
    new_list = []
    for i in range(n):
        new_list.append(int(l1[i]))

    t = tuple(new_list)
    print(hash(t))


main()