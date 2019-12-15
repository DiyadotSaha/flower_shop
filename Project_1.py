# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 08:57:36 2018
@author: Diya
"""
import numpy as np
import random 
class FlowerShop :
    chance = random.randint(0,10) 
    dictOfTrans = {}
    listofFlower = ['peony','rose', 'buttercup','lily','gladiolus','orchids','lisianthus','carnations','daffodils']
    DictOfFlowers={}
    # name : quantity, price, lowest quantity, description, event
    DictOfFlowers['peony'] = [10,10,5,'a herbaceous or shrubby plant of north temperate regions, which has long been cultivated for its showy flowers.','wedding']
    DictOfFlowers['rose'] = [25,10,10,'a prickly bush or shrub that typically bears red, pink, yellow, or white fragrant flowers, native to north temperate regions. Numerous hybrids and cultivars have been developed and are widely grown as ornamentals.','wedding']
    DictOfFlowers['buttercup'] = [25,10,4,'a herbaceous plant with bright yellow cup-shaped flowers, common in grassland and as a garden weed. All kinds are poisonous and generally avoided by livestock.','wedding']
    DictOfFlowers['lily'] = [12,10,2,'The lily is a genus of flowering plant. There are many species of lilies, like trumpet lilies and tiger lilies. They are usually quite tall, and are perennials. Most lilies grow from a bulb, which in some species develops into a rhizome, which carries small bulbs.','funeral']
    DictOfFlowers['gladiolus'] = [12,10,5,'an Old World plant of the iris family, with sword-shaped leaves and spikes of brightly colored flowers, popular in gardens and as a cut flower.','funeral']
    DictOfFlowers['orchids'] = [10,10,5,'a plant with complex flowers that are typically showy or bizarrely shaped, having a large specialized lip (labellum) and frequently a spur. Orchids occur worldwide, especially as epiphytes in tropical forests, and are valuable hothouse plants.','funeral']
    DictOfFlowers['lisianthus'] = [15,10,5,'Lisianthus (Eustoma Grandiflorum) is a genus of 3 species in the family Gentianaceae. Lisianthus are large gentian-like bell-shaped flowers with flaring pale purple petal-like lobes. They bloom in summer from the upper leaf axils.','baby shower']
    DictOfFlowers['carnations'] = [20,10,10,'a double-flowered cultivated variety of clove pink, with gray-green leaves and showy pink, white, or red flowers.','baby shower']
    DictOfFlowers['daffodils'] = [30,10,10,'a bulbous plant that typically bears bright yellow flowers with a long trumpet-shaped center (corona).','baby shower']
     
# this displays the current flowers and the number of flowers the shp has 
    def displayInventory(self):
       print(' CURRENT INVENTORY')
       print('-'*40)
       print('Flower         Quantity       ')
       for i in self.DictOfFlowers:
           d = self.DictOfFlowers[i][0]
           print('%-10s  %10d'%(i, d))
       print('-'*40)
       
#This   displays the prices of each of the flowers in the flowershop
    def displayCatalog(self):
        print('CURRENT CATALOG')
        print('-'*40)
        print('Flower           Unit Price($)       ')
        for i in self.listofFlower:
            price = self.DictOfFlowers[i][1]
            print('%-10s  %10d'%(i, price))
        print('-'*40)
    
# helps the customers place an order and buy the flowers
    def placeOrder(self):
        order = {}
        continueApp = True
        discountedTotal = 0 
        while(continueApp):
            verify = input('Would you like to add a flower to your order?([y]yes/[n]no)')
            if verify is 'y':
                name = input('Flower: ')    
                if name in self.DictOfFlowers:
                    quan = int(input('Quantity: '))
                    availQuan = self.DictOfFlowers[name][0]
                    if quan <= availQuan:
                        order[name] = quan
                        self.DictOfFlowers[name][0]-= quan  
                    else:
                        print('Sorry. '+str(quan)+' '+ name +' not available.')
                        print(str(availQuan)+' '+ name +' available')
                else:
                    print('Sorry!' +name+ ' is not in the inventory !')
                    self.displayCatalog(self)
            elif verify is 'n':
                continueApp = False
                name = input("Please enter your name to finalize your order: ")
                print('\n')
                print('YOUR ORDER')
                print('\n')
                print('FLOWER   QUANTITY   UNIT PRICE($)   TOTAL PRICE')
                for i in order:
                    total =int(order[i])*self.DictOfFlowers[i][1]
                    print('%-10s %3s %10d %18d'%(i,order[i], self.DictOfFlowers[i][1],total))
                print('---------------------------')
                total = 0 
                totalQuantity = 0
                for i in order:
                    unitPrice = self.DictOfFlowers[i][1]
                    quan = int(order[i])
                    totalQuantity += quan
                    total= total + (quan * unitPrice)
                    print('Your total price is $'+str(total))
                #Offering a discount 90% of the time. 
                if self.chance is not 0:
                    print('Congratulations you have won our deal of the day!!')
                    print('You will recieve a 5% discount on your purchase!')
                    total  = total - (total * 5 / 100)
                    print('\n')     
                    print('\n')
                    print('Your discounted price is $'+ str(total))
                    print('\n')
                listofInfo = [total,totalQuantity]
                self.dictOfTrans[name]=listofInfo
                self.displayInventory(self)
            else:
                print('Invalid Input')
                print("please print 'y' or 'n' ")
   
# This method displays description of the flowers    
    def disFlower(self):
        continueApp = True 
        while(continueApp):
            choice = input('Would you like to discover a flower ? ([y]yes/[n]no) ')
            if choice is 'y':
                flower = input('Flower: ')
                if flower in self.listofFlower:
                    des = self.DictOfFlowers[flower][3]
                    print('\n')
                    print('The description of '+flower)
                    print(des)
                else:
                    print('Invalid input!')
                    print('Please enter the name of a flower from this list' + str(self.listofFlower))
            elif choice is 'n':
                print('Hope we were helpful ')
                continueApp = False
            else:
                print('Invalid input!')
                print("Please print 'y' or 'n' ")
#    This a   method will suggest a particular flower from three events. 
    def suggestingFlowers(self):
        continueApp = True 
        index_occasion = 4
        while(continueApp):
            choice = input('Would you like us to suggest a flower ? ([y]yes/[n]no) ')
            if choice is 'y':
                event = input('Event [wedding, funeral or baby shower]: ')
                if event == 'wedding':
                    print('\n')
                    print('For a '+event+' we are suggesting: ')
                    for d in self.DictOfFlowers:
                        if self.DictOfFlowers[d][index_occasion] == 'wedding':
                            print(d)                   
                elif event == 'funeral':
                    print('\n')
                    print('For a '+event+' we are suggesting: ')
                    for d in self.DictOfFlowers:
                        if self.DictOfFlowers[d][index_occasion] == 'funeral':
                            print(d)
                elif event == 'baby shower':
                    print('\n')
                    print('For a '+event+' we are suggesting: ')
                    for d in self.DictOfFlowers:
                        if self.DictOfFlowers[d][index_occasion] == 'baby shower':
                            print(d)
                else:
                    print('Invalid input!')
                    print('Please choose an event from the listed events')
            elif choice is 'n':
                print('Hope we were helpful ')
                continueApp = False
            else:
                print('Invalid input!')
                print("Please print 'y' or 'n' ")
                
    def showTransHist(self):
        print('NAME       PRICE     QUANTITY')
        for d in self.dictOfTrans:
            print('%-10s %4s %5s'%(d,self.dictOfTrans[d][0],self.dictOfTrans[d][1]))
            
    def visualizeInventory(self):
        Quantity = []
        names =[]
        for d in self.DictOfFlowers:
            Quantity += [self.DictOfFlowers[d][0]]
            names+=[d]
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10,4))
        y_pos = np.arange(len(names)) 
        plt.bar(y_pos, Quantity)
        plt.xticks(y_pos, names) 
        plt.show()
      
    def exitApp(self):
        print('\n'*3)
        print('Hope we were helpful!')
        print('Thank you for visiting us!')
        print('Have a nice day!')
        
# this is the entry point on the code. 
    def showMainMenu(self):
        print('')
        print('\n'*5)
        print(' MAIN MENU')
        print('-'*40)
        print('\n')
        print('ACTIONS FOR CUSTOMERS')
        print('1. Display catalog')
        print('2. Place an order')
        print('3. Discover a flower')
        print('4. Want a suggestion')
        print('\n')
        print('ACTIONS FOR SHOP OWNERS')
        print('5. Display inventory')
        print('6. Visualize inventory')
        print('7. Order from supplier')
        print('8. Show transaction history')
        print('9. Exit')
        print('-'*40)
        
# this has a method from which the stocks need to be replenished manually.     
    def orderSupplies(self):
        order = {}
        continueApp = True
        while(continueApp):
            chose = str(input('Would you like to order a flower ? ([y]yes/[n]no)'))
            if chose is 'y':
                n = input('Flower: ')
                if n in self.listofFlower:
                    q = int(input('Quantity: '))
                    if q > 3:
                        q = int(q)
                        order[n]= q 
                    else:
                        print('This quantity is too less! Order something higher than 3')
                else:
                    print('This flower does not exist in the inventory!')
                    print('Existing flowers are: ')
                    for f in self.listofFlower:
                        print(f)
                    print('\n')
            else:
                print('\n'*3)
                break
        self.Auto_orderSupplies(self,order)
        self.displayInventory(self)
        
#helper method that is called in many functions when the ordering of the flower's needs be taken care of. 
    def Auto_orderSupplies(self, dict_order):
        for flower in dict_order:
           self.DictOfFlowers[flower][0]+= dict_order[flower]
           print('Added '+str(dict_order[flower])+' '+ flower+'(s) to invetory')
    
# This automatically call the suppliers when the levels of the inventory are  
    def replenish(self):
        order = {}
        for d in self.DictOfFlowers:
            qty = self.DictOfFlowers[d][0]
            min_inventory = self.DictOfFlowers[d][2]
            if  qty < min_inventory:
                order[d]= min_inventory - qty
                print('\n')
                print("ALERT! Inventory gone below minimum level. Placing automatic order to replenish stocks")
                self.Auto_orderSupplies(self,order)  
            else:
                pass
                        
# this is the central function of the program. This calls all  the approprite functions based on the user's choice   
    def main(self):
        continueApp = True
        while(continueApp):
            self.replenish(self)
            self.showMainMenu(self)
            choice = str(input ('Enter an option: '))
            if choice is '5':
                print('\n')
                self.displayInventory(self)
                print('\n')
            elif choice is '1':
                print('\n'*5)
                self.displayCatalog(self) 
            elif choice is '2':
                print('\n'*4)
                print('YOUR ORDER')
                print('-'*40)
                print ()
                self.placeOrder(self)
            elif choice is '3':  
                print('-'*40)
                self.disFlower(self)
                print('-'*40)
                print('\n'*4)
            elif choice is '4':
                print('-'*40)
                self.suggestingFlowers(self)
                print('-'*40)
                print('\n'*4)
            elif choice is '6':
                self.visualizeInventory(self)
            elif choice is '7':
                print('\n'*4)
                print('-'*40)
                self.orderSupplies(self)
                print('-'*40)
                print('\n'*3)
            elif choice is '8':
                print('TRANSACTION HISTORY')
                print('-'*40)
                self.showTransHist(self)
                print('\n'*5)
                print('-'*40)
            elif choice is '9':
                print('\n'*5)
                print('-'*40)
                continueApp = False
                self.exitApp(self)
                break
            else:
                print('Invalid Input!')
                print('If you are a customer')
                print('Please choose an option between 1 to 4')
                print('If you are the owner')
                print('Please choose an option between 5 to 9')

flowerShop = FlowerShop
FlowerShop.main(flowerShop)


      