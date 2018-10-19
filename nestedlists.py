#Nested lists hackerrank
if __name__ == '__main__':
    mylist = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        mylist.append([name,score])
    z = min(scores)
    while z == min(scores):
        del scores[scores.index(z)]
    secondlowest = min(scores)
    l = []
    for i in mylist:
        if i[1] == secondlowest:
            l.append(i[0])
    l = sorted(l)
    for i in l:
        print(i)
