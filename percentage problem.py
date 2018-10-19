#percentage problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    q = input()
    lits = student_marks[q]
    sum =0 
    for i in lits:
        sum +=i
    sum /=3
    sum/=100
    sum*=100
    print("%.2f"%sum)
