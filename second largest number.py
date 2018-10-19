if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist  = list(arr)
    a = max(mylist)
    b = mylist.index(a)
    del mylist[b]
    print(max(mylist))
    print(len(mylist))
