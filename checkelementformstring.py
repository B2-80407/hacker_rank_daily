if __name__ == '__main__':
    s = input()
    l1 = list(s)
    print(
        any(map(str.isalnum, s)),
        any(map(str.isalpha, s)),
        any(map(str.isdigit, s)),
        any(map(str.islower, s)),
        any(map(str.isupper, s)), sep="\n"
    )


