
#-----------------------------------------------------------------------------------#
###################### DataBase for customer and stock  #############################
#-----------------------------------------------------------------------------------#

# store all the exsisting customer names #
customer_names =[ 'srujan','basavaraj','Daneil','gererd']

# storing the product cost and product above will be replaced by this #
stock_list= [['shampoo','soap','books','pens'],['10','20','-1',''],[0,50,50,50]]

# function defination to replenish
def replenish( x ):
    replinish_list=[]
    # value given by user is set to stock of all products
    for i in range(0,len(stock_list[2])):
        replinish_list.append(x)
        stock_list[2] = replinish_list

valuable_customer=[[],[],[]]
# Main Loop for software
software_loop = True
while software_loop:

#----------------------------------------------------------------------------------------#
#####################               Menu Screen           ################################
#----------------------------------------------------------------------------------------#
    
    # Menu options for user to choose

    print("\n     Warehouse Inventory Management Software        \n")
    print("\n                    Menu                            \n")
    print("1.For Billing Desk                                         "+"          Press '1'")
    print("2.For Updating the Inventory                               "+"          Press '2'")
    print("3.For Customer and Inventory Stock Data                    "+"          press '3'")
    print("4.For 'Replenish' to stock up inventory to desired value   "+"          press '4'")
    print("5.Most valuable customer                                   "+"          press '5'")    
    print("6.To exit from the software                                "+"          Press '6'")
    
    #option selected from the menu option is placed in menu_key

    menu_key = input("\nEnter the number to access the respective menu : ")

    menu_key_check = True
    
    # main loop which has all the conditions for menu attributes
    while menu_key_check:

#----------------------------------------------------------------------------------------#
#####################           Billing Desk              ################################
#----------------------------------------------------------------------------------------#        

        # If Billing desk is selected by pressing 1 in menu options 
        if menu_key == '1':
            menu_key_check = False
            keep_in_loop_bill = True
            # if user wants to entre one more bill loop is used
            while keep_in_loop_bill:

                # printing the lable
                print("\n\n               Billing Desk                          \n")
                           

                # user Enters the customer name #
                name_of_Customer = input("\nEnter the name of the customer : ")
                
                product_check = True

                #Loop is used to check is the product entered is avilable in  product list
                while product_check == True:

                    # user Enters the produt name #
                    name_of_Product = input("\nEnter the name of a product : ")

                    # if conditions check the product enterd is in product list
                    if name_of_Product.lower() in stock_list[0]:
                            index_product = stock_list[0].index(name_of_Product.lower())
                            product_check = False
                            if ( name_of_Customer not in customer_names ) and (stock_list[1][index_product] == ''):

                                    print('\nNew customer is not eligible to buy free product. Kindly choose other product')

                                    product_check = True

                            # if product is out of stock i.e 0 and if the price is negative is checked in this section
                            if (stock_list[1][index_product].isdigit() == False  and (stock_list[1][index_product]) != '' ):
                                
                                # if user had entred a negative price while updating the inventory this condtion checks and halts 
                                # the billing process and 
                                if(float(stock_list[1][index_product]) < 0 ):
                                    print('\n The price is not valid kindly select other product')
                                    product_check = True

                            #if the entred product is out of stock    
                            if (stock_list[2][index_product] <= 0):
                                    
                                print("\nProduct is currently out of stock. kindly select other product")
                                product_check = True

                    # when user entres a product which is not avilable in inventory
                   
                    else:
                        print("\n You have enterd " + name_of_Product + " which is not a valid product." + 
                         "Kindly check the spelling or re enter the product name.\n")
                        
                    # This condition checks is the customer is already avilable in databse or a new customer if the price is empty
                

                quantity_check = True
                # this loop is used to check weather the user enterd a valid quantity
                while quantity_check == True:
                    #user Enters the quantity of product #
                    quantity = input("\nEnter the quantity of the product : ")

                    # this checks is the input a integer number or not if not it asks again to enter correct value
                    #this checks weather the entred number is a integer value
                    if (quantity.isdigit()):
                        quantity = int(quantity)
                        quantity_check = False
                    # if other than integer is entred it throws error
                    else:
                        print("\nYou have enterd a wrong quantity. Kindly enter a proper value \n ")
                    # when user entrs the quantity more than the available quantity
                    if (stock_list[2][index_product] < quantity ):

                        print('Current stock of the product is ' + str(stock_list[2][index_product]) + '. Kindly re-enter the quantity ')
                        quantity_check = True
                
                

                #---------------------------------------------------------------------------------------------------------#    
                                            # Calculating the price of the product #
                #---------------------------------------------------------------------------------------------------------#
                discount = 0

                ### Check for existing user in available customer names if not then appending his name to list so that he/she 
                # can be eligible for discount ###

                for i in customer_names:
                
                    if i == name_of_Customer:
                        discount = 0.1

                # calculating the price of the product #  
                price = stock_list[1][index_product]


                # for free good the price is kept zero
                if stock_list[1][index_product] == '':
                    price = 0
                
                #Price calculator and bill statment
                price_calculate = ( float(price) * quantity) - ((float(price) * quantity) * discount)
                print ("\n" + str(name_of_Customer) +" purchased " + str(quantity) + " x " + name_of_Product + "\n"
                "Unit price: $"  + str(price)  + "\n"
                "Total price: $" + str(price_calculate)+"\n")

                # if the customer is not avilable in the data base.  name is  included to DB so that he/she is eligible for 
                # discount from next purchase
                if discount == 0:
                    customer_names.append(name_of_Customer)                
                
                #updating the stock after billing 
                stock_list[2][index_product]  = int(stock_list[2][index_product]) - quantity
               


                #-----------------------------------------------------------------------------#
                #                           Most Valuable customer                            #
                #-----------------------------------------------------------------------------#
                
                # this block is used to provide data for most valuable customer calculation
                #  
                # if the user had already billed atlest once 
                if name_of_Customer in valuable_customer[0]:
                    index_name = valuable_customer[0].index(name_of_Customer)
                    valuable_customer[1][index_name] += price_calculate
                    valuable_customer[2][index_name] += 1

                # for customer billing for 1st time    
                elif name_of_Customer not in valuable_customer[0]:
                    valuable_customer[0].append(name_of_Customer)
                    valuable_customer[1].append(price_calculate)
                    valuable_customer[2].append(1)

                 # if user wants to bill one more customer then he presses 1    
                want_to_bill_one_more = input("\nWant to bill one more customer : Press '1' \n")
                
                if want_to_bill_one_more != '1':
                    keep_in_loop_bill = False


#----------------------------------------------------------------------------------------#
# #####################          Stock Section            ################################
#----------------------------------------------------------------------------------------#

        # If Stock Section is selected by pressing 2 in menu options 
        elif menu_key == '2':
            menu_key_check = False
            # user enters the price of products one after the other
            price_list = input("\nEnter the price list of the products : ")
            
            # price enterd is split at white space and set to a list
            price_list = price_list.split()

            # user enters the products list one after the other
            product_list = input("\nEnter the product list : ")

            # product enterd is split at white space and set to a list
            product_list= product_list.split()

            stock_avilable_list = []
            # if any of the price is not given its append by blank
            if len(price_list) != len(product_list):

                for i in range(0,len(product_list) - len(price_list)):
                    price_list.append('')
            # Stock is appended to 50 by default
            for i in range(0,len(product_list)):
                    stock_avilable_list.append(50)

            # product list price list and stock available list is set to stock list this over rides the predifined list
            stock_list[0] = product_list
            stock_list[1] = price_list
            stock_list[2]= stock_avilable_list
            #print(stock_list)

#------------------------------------------------------------------------------------------------#
##########################            customer and inventory data         ########################
#------------------------------------------------------------------------------------------------#
        
        elif menu_key == '3':
            menu_key_check = False
            data_info_loop = True
            # loop is used for database functionalities
            while data_info_loop:
                print('\n')
                print("1.For Customer Data                   "+"  Press 1")
                print("2.For Inventory data with price list  "+"  Press 2")
                data_info = input("\nEnter the number to access the respective data : ")
                data_info_loop = False
                #if the user needs the customer data he press 1 and its respective code
                if data_info == '1':
                    
                    #prints the customer names
                    print('\nCustomer Data:\n')
                    for i in range (0,len(customer_names)):
                        print('')
                        print(str(i+1) +' ' + customer_names[i])
                    data_info_loop = False
                #if the user needs the inventory data he press 2 and its respective code
                elif data_info == '2':
                    stock_list_1=[]

                    for i in range(len(stock_list[0])):
                            row1 =[]
                            for list_1 in stock_list:

                                row1.append(list_1[i])
                            stock_list_1.append(row1)

                    # formating block this block is udes to show data in a nice manner to user
                    heading = f"{ 'Product Name':20s}{'Price':10s}{'Stock Available':15s}"
                    
                    print('\n')
                    print('Inventory Data')
                    print('-'*45)
                    print(heading)
                    print('-'*45)
                    

                    for i in range (0,len(stock_list_1)):
                    
                        out_put = f"{ str(stock_list_1[i][0]):20s}{str(stock_list_1[i][1]):10s}{str(stock_list_1[i][2]):15s}"
                        print(out_put)
                    print('-'*45)
                    print('\n')
                # if user selects number other than 1 or 2
                else:
                    print('Please enter a correct the number')
#------------------------------------------------------------------------------------------------#
##########################            Replinish                           ########################
#------------------------------------------------------------------------------------------------#

        elif menu_key == '4':
            menu_key_check = False
            replinish_loop = True
            print('a')

            while replinish_loop:

                replinish_value = input('\nEnter a value to stock up the inventory : ')
                
                # checks that data entred is a integer

                if (replinish_value.isdigit()):
                        replinish_value = int(replinish_value)
                        replenish( replinish_value )
                        replinish_loop = False
                
                #if the entred value is not a integer
                else:
                    print('\nValue entered is not an interger kindly enter a integer value')


#----------------------------------------------------------------------------------------#
# #####################     Most valuable customer calculation     #######################
#----------------------------------------------------------------------------------------#
        elif menu_key == '5':
            menu_key_check = False
            # this checks if there is a data to calculate the most valuable customer
            if valuable_customer != [[],[],[]]:
                max_order_value = max(valuable_customer[1])
                max_order_value_index = valuable_customer[1].index(max_order_value)
                valu_customer = valuable_customer[0][max_order_value_index]
                orders = valuable_customer[2][max_order_value_index]
                print("\nThe most valuable customer is ' {name} ' with '{totalorders}' orders. which is of a order value '${ordervalue}'".format(name = valu_customer, totalorders= orders, ordervalue = max_order_value ))
            
            # if user has not billed anyone till now 
            else:
                print('\nPlease come here after entrying the 1st bill')

        # If EXIT is selected by pressing 4 in menu options 
        elif menu_key == '6':
            exit() # programm exits 

        #elif (menu_key != '1'  or menu_key != '2'  or menu_key != '3' or menu_key != '4' or menu_key != '5' or menu_key != '6' ):
        else:
            
            print('Please enter a correct the number')
            break
        
###################################################################################################################

##############################################  End of Programme ###################################################

####################################################################################################################


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                   Documentation                                                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

####################################################################################################################
#                                                                                                                  #
# 1. The missed out feature  is part 3.6 as we cannot use any external libraries its quite difficult to store the  #
# data  dispaly in a recomemded format.:                                                                           #
#   1.Problems faced during this implementation was manipulating many lists at a same time for the prescribed      #
#       Format                                                                                                     #
#   2.As i had tried to manipulate the lists of lists. Main problem was id of the variables came same when i was   #
#       manipulating the lists certain things it used to copy the same in other list as well so this was a failure #
#        for menu_key                                                                                              #
#   3. very time consuming to design list inside a list inside a list and manipulating it is a very diffucult.     #
#       without external libraries                                                                                 #
####################################################################################################################
