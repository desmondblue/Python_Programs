import unittest

def getDiscount(age):
    discount = 0
    if age > 60 and age < 70:
        discount = 15
    elif age > 70:
        discount = 30 
    return discount
class Test(unittest.TestCase):
    def setUp(self):
        name = self.shortDescription()
        if name == "one":
            self.a = 60
            print("Test Case #",name, "Customer Age =",self.a,"Expected Discount",15)
        elif name == "two":
            self.a = 50
            print("Test Case #",name, "Customer Age =",self.a,"Expected Discount",0)
        elif name == "three":
            self.a = 65
            print("Test Case #",name, "Customer Age =",self.a,"Expected Discount",15)  
        elif name =="four":
            self.a = 68
            print("Test Case #",name, "Customer Age =",self.a,"Expected Discount",15) 
        elif name == "five":
            self.a = 80
            print("Test Case #",name, "Customer Age =",self.a,"Expected Discount",30)   
        elif name =="six":
            self.a = 70
            print("Test Case #",name, "Customer Age =",self.a,"Expected Discount",30)  
    def tearDown(self):
        print("\nEnd of test",self.shortDescription())
    def test1(self):
        """one"""
        self.assertEqual(getDiscount(self.a),15)    
    def test2(self):
        """two"""
        self.assertEqual(getDiscount(self.a),0)
    def test3(self):
        """three"""
        self.assertEqual(getDiscount(self.a),15)                
    def test4(self):
        """four"""
        self.assertEqual(getDiscount(self.a),15)
    def test5(self):
        """five"""
        self.assertEqual(getDiscount(self.a),30)
    def test6(self):
        """six"""
        self.assertEqual(getDiscount(self.a),30)
    
        
if __name__ == '__main__':
    unittest.main()

