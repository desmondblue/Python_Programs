#Assignment 34

enumerate = dict()
y = []
with open("e:/executables/python/rhyme.txt") as f1:
    for line in f1:
        keys = line.split()
        for key in keys:
            key = key.lower()
            y.append(key)
            if key in enumerate:
                enumerate[key] += 1
            else:
                enumerate[key] = 1

with open("e:/executables/python/keys.txt","w+") as f1:
    for keys in enumerate.keys():
        f1.write(keys + ":" + str(enumerate[keys]) + "\n")
print(str(enumerate))
print("Total number of keys :",(len(y)))
