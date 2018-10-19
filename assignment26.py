class InvalidString(Exception):
    def __init__(self):
        Exception.__init__(self,"Found Asterisk")
def asteriskChecker(myString):
    for i in myString:
        if(i=="*"):
            raise InvalidString()
            
mymessage="abcde*fz"
try:
    asteriskChecker(mymessage)
except InvalidString as e :
    print(e) #statement1else:print("String has no Asterisk ")