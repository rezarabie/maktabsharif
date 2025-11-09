
#define and initial variables
file_records=[]

class data_store:
    def readFile(self):
        with  open("sales.txt","r") as nb:
                data_store_analyze=nb.readlines()
                return(data_store_analyze)
        
    def buildResport(self) ->str:
        totalItems=0
        totalCosts=0
        allRecords=0
        maxQuantity=0
        totalAverage=0.0
        maxQuantityProduct=""
        averageShopping=0.0
        file_records=self.readFile()

        for record in file_records:
            try:
                temp=record.strip().split(",")
                totalCosts=totalCosts+(float(temp[1])*int(temp[2]))
                totalItems=totalItems+int(temp[2])
                allRecords=allRecords+1
            
                if(int(temp[2]) > maxQuantity):
                    maxQuantity=int(temp[2])
                    maxQuantityProduct=(temp[0])
            except ValueError:
                pass    
        totalAverage= f"{totalCosts/totalItems:.2f}"

        strReport=f" total transaction  :{totalItems}  \n total sale :${totalCosts} \n max sale is :{maxQuantityProduct}  :( {maxQuantity} ) \n the average is {(totalAverage)} number of lines is : {allRecords}" 
        
        return (strReport)

    def menu(self)->int:
        print("1-build report..")
        print("2-add new sale..")
        print("3-exit..")
        menu=input()
        
        if(menu!=" "):
            return (int(menu))
        else:
            return 0
        
      
myStore=data_store()
     
while (True):
        seletMenu=myStore.menu()
        #print("your chooosen menu is : ",seletMenu)
        
        match seletMenu:
            case 1:
                print (myStore.buildResport())
            case 2:
                item=[]
                prodcut=input("input your prodcut name : ")+","
                cost=input("input your cost : ")+","
                quantity=input ("input your qunatity: ")
                item=[prodcut,cost,quantity]
                            
                
                with open("sales.txt ","a") as sales:
                    sales.writelines("\n")
                    sales.writelines(item)

            case 3:
                break
            case _:
                    print ("plz try again ...")



