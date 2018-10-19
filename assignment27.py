file = open("e:/executables/python/textfile.txt",'r')
string = file.read()
print(string)

try:
    file.write("hello")
except IOError as xcptn:
    print("Error!\nClosing file:",xcptn)
    file.close()