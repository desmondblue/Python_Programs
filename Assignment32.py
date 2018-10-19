import unittest
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist
def listcmp(x,y):
    for i in x:
            for j in y:
                if i == j:
                    z = True
                else:
                    z = False
    return z
class Test(unittest.TestCase):
    z = False
    def setUp(self):
        name = self.shortDescription()
        if name == "one":
            self.a = [54,26,93,17,77,31,44,55,20]
            print("Test Case #",name, "Expected sorted list:\n",sorted(self.a))
        elif name == "two":
            self.a = [78,56,100,95,40,230,11,56,70]
            print("Test Case #",name, "Expected sorted list:\n",sorted(self.a))
        elif name == "three":
            self.a = [84,50,192,78,49,8,220,13]
            print("Test Case #",name, "Expected sorted list:\n",sorted(self.a))
        elif name == "four":
            self.a = [38,55,10,65,70,21,111,96,120]
            print("Test Case #",name, "Expected sorted list:\n",sorted(self.a))    
        elif name == "five":
            self.a = [782,536,145,125,403,2,191,563,270]
            print("Test Case #",name, "Expected sorted list:\n",sorted(self.a))        
        elif name == "six":
            self.a = [728,356,400,544,10,200,321,546,780]
            print("Test Case #",name, "Expected sorted list:\n",sorted(self.a))      
    def tearDown(self):
        print("\nEnd of test",self.shortDescription())
    def test1(self):
        """one"""
        x = sorted(self.a)
        y = bubbleSort(self.a)
        z = listcmp(x, y)
        self.assertTrue(z,"Result is False")    
    def test2(self):
        """two"""
        x = sorted(self.a)
        y = bubbleSort(self.a)
        z = listcmp(x, y)
        self.assertTrue(z,"Result is False")
    def test3(self):
        """three"""
        x = sorted(self.a)
        y = bubbleSort(self.a)
        z = listcmp(x, y)
        self.assertTrue(z,"Result is False")
    def test4(self):
        """four"""
        x = sorted(self.a)
        y = bubbleSort(self.a)
        z = listcmp(x, y)
        self.assertTrue(z,"Result is False")        
    def test5(self):
        """five"""
        x = sorted(self.a)
        y = bubbleSort(self.a)
        z = listcmp(x, y)
        self.assertTrue(z,"Result is False")
    def test6(self):
        """six"""
        x = sorted(self.a)
        y = bubbleSort(self.a)
        z = listcmp(x, y)
        self.assertTrue(z,"Result is False")
if __name__ == "__main__":
    unittest.main()