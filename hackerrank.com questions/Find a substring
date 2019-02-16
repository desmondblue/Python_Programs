#to count number of times a substring repeats itself in a string

def count_substring(string, sub_string):
    lt = len(sub_string) # length of substring
    ctr = 0 # counter var
    for i in range(0,len(string)):
        if (string[i:lt]==sub_string):
            ctr +=1
        lt+=1
    return ctr

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
