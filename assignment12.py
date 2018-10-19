class Calculator:
    lastprime = 0
    def isPrime(self,num):
        div = int(num / 2)
        div +=1
        flag = 0
        
        for i in range (2,div):
            
            if num % i == 0:
                flag = 1
                break
        if flag == 1 :
            return 0
        elif flag == 0 or num == 2:
            return 1
    def getNextPrime(self):
        
        if self.lastprime == 0:
            self.lastprime = 2
            return 2
        else:
            self.nextprime = self.lastprime + 1 
            while(self.isPrime(self.nextprime)== 0):
                self.nextprime +=1
            self.lastprime = self.nextprime
            return self.nextprime

a = Calculator()

for i in range(50):
    x = a.getNextPrime()
    print(i+1,'.',x)