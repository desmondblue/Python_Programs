#Python 3
if __name__ == '__main__':
    i = input()
    a=b=c=d=e=0
    for s in i:
        if s.isalnum():
            a = 1
        if s.isalpha():
            b=1
        if s.isdigit():
            c=1
        if s.islower():
            d=1
        if s.isupper():
            e=1
    if a==1:
        print("True")
    else:
            print("False")
        
    if b==1:
        print("True")
    else:
            print("False")
    if c==1:
        print("True")
    else:
            print("False")
    if d==1:
        print("True")
    else:
            print("False")
    if e==1:
        print("True")
    else:
            print("False")

# I know I chose a very lengthy approach but this is traditional flag check
