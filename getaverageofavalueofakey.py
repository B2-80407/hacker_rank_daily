if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    l1 = list(student_marks[query_name])
    sum1 = 0.00
    for i in l1:
        sum1 = sum1 + i

    sum1 = "{:.2f}".format(sum1 / 3)
    print(sum1)