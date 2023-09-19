if __name__ == '__main__':
    N = int(input())
    list1 = []

    for i in range(N):
        str1 = input()
        cm1 = str1.split(" ")
        cmd = list(cm1)
        if cmd[0] == "insert":
            a = int(cmd[1])
            b = int(cmd[2])
            list1.insert(a, b)
        elif cmd[0] == "print":
            print(list1)
        elif cmd[0] == "remove":
            n = int(cmd[1])
            list1.remove(n)
        elif cmd[0] == "sort":
            list1.sort()
        elif cmd[0] == "append":
            a = int(cmd[1])
            list1.append(a)
        elif len(list1) > 0 and cmd[0] == "pop":
            list1.pop()
        elif cmd[0] == "reverse":
            list1.reverse()
        else:
            pass

