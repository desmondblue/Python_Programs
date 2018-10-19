class Store:
    
    __item_count = 100
    @classmethod
    def addItem(self,count):
        self.__item_count = self.__item_count + count
        
    @classmethod    
    def issueItem(self,count):
        self.__item_count-=count
        
    @staticmethod  
    def getItemCount():
       return Store.__item_count
counter1 = Store()
counter1.addItem(2)
counter1.issueItem(1)
counter2 =Store()

print("Counter 1 item count",counter1.getItemCount())
print("Counter 2 item count",counter2.getItemCount())
