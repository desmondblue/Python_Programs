import unittest
def getDiscount(age,gender):
    discount = 0
    if age >= 60:
        if gender == 'F':
            discount = 25
        discount = 20
    elif gender == 'F':
        discount = 15
    return discount
def expectedDiscount(age,gender):
    discount = 0
    if age >=60:
        if gender == 'F':
            discount = 25
        elif gender == 'M':
            discount = 20
    elif age<60 and gender == 'F':
        discount = 15

    return discount

def input():
    age = int(input("Enter age:"))
    gender = input("Enter Gender as M or F:")   
    return age,gender
class Test(unittest.TestCase):
    def setUp(self):
        name = self.shortDescription()
        if name == "one":
            self.age = 55
            self.gender = 'M'
            self.a = expectedDiscount(self.age,self.gender)
            self.b = getDiscount(self.age, self.gender)
            print("Test Case #",name,"Age:",self.age,"Gender:",self.gender,"Expected Discount:",self.a,"Actual Discount:",self.b)
        elif name == "two":
            self.age = 60
            self.gender = 'M'
            self.a = expectedDiscount(self.age,self.gender)
            self.b = getDiscount(self.age, self.gender)
            print("Test Case #",name,"Age:",self.age,"Gender:",self.gender,"Expected Discount:",self.a,"Actual Discount:",self.b)
        elif name == "three":
            self.age = 55
            self.gender = 'F'
            self.a = expectedDiscount(self.age,self.gender)
            self.b = getDiscount(self.age, self.gender)
            print("Test Case #",name,"Age:",self.age,"Gender:",self.gender,"Expected Discount:",self.a,"Actual Discount:",self.b)    
        elif name == "four":
            self.age = 60
            self.gender = 'F'
            self.a = expectedDiscount(self.age,self.gender)
            self.b = getDiscount(self.age, self.gender)
            print("Test Case #",name,"Age:",self.age,"Gender:",self.gender,"Expected Discount:",self.a,"Actual Discount:",self.b)
    def tearDown(self):
        print("End of test",self.shortDescription(),"\n")
    def test1(self):
        """one"""
        self.assertEqual(self.b,self.a,"Assertion Fails")
    def test2(self):
        """two"""
        self.assertEqual(self.b,self.a,"Assertion Fails")
    def test3(self):
        """three"""
        self.assertEqual(self.b,self.a,"Assertion Fails")                         
    def test4(self):
        """four"""
        self.assertEqual(self.b,self.a,"Assertion Fails")
   
if __name__ == "__main__":
    unittest.main()