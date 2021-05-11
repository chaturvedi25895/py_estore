#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#import time as time
import random  as r
import datetime
#datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
overall_data_captured = pd.read_csv("finalised_by_meghamgaadu.csv")
#print(overall_data_captured)
def fn_otp():
    for i in range(0,3):
        generated_otp = r.randrange(111111,999999)
        user_provided_otp = int(input("Please enter OTP to proceed further: {} # ".format(str(generated_otp))))
        if(generated_otp==user_provided_otp):
            print("Your Transaction is successful")
            break
        else:
            print("Wrong OTP! Please provide a valid OTP")
            
def fn_available_quantities():
    for i in sno_products.keys():
        print("There are only {available_quantity} {products}'s available in the store".format(available_quantity = total_items_in_showroom - overall_data_captured['quantity'][overall_data_captured["product"]==sno_products[i]].sum(),products = sno_products[i]))
            
sno_products =  {1:'AC',2:'Cooler',3:'Fan',4:'Heater'}
products_costs =  {'AC':40000,'Cooler':20000,'Fan':10000,'Heater': 5000}
total_items_in_showroom = 500
print(sno_products,products_costs)
print("Welcome to online shopping.")
username  = input("Please provide your Username: ")
print(" Please choose your aspect of interest.")
# print("1.Booking 2.Cancellation")
user_type_of_transaction = int(input("1.Booking 2.Cancellation"))

while True:
    if(user_type_of_transaction == 1):
        print("Awesome! Lets go for Booking") 
        for i in sno_products.keys():
            print(i,'.', sno_products[i])
        product_choice  = int(input("Please choose your product number below: "))
        if product_choice in range(1,len(sno_products.keys())):
            n_items = int(input("Please enter number of items: "))
            product_choice_availability_check = total_items_in_showroom - overall_data_captured['quantity'][overall_data_captured["product"]==sno_products[product_choice]].sum()
            if(int(n_items) < product_choice_availability_check):
                print("You chose to buy {items} {products}'s ".format(items = n_items, products = sno_products[product_choice]))
                price = n_items*products_costs[sno_products[int(product_choice)]]
                disc_price = price
                if(price > 10000):
                    disc_price = price-  (price * 20 / 100)
                    print("Discount:\nYou have saved 20%")
                elif price < 5000:
                    print("you have won a gift hamper")
                    disc_price = price
                print("Final price: " + str(disc_price))
                #OTP function is being called        
                fn_otp()
                #transaction_level_data = {'transaction_time': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") ,'transaction_type':user_type_of_transaction ,'Product':sno_products[product_choice] ,"no_of_items": n_items ,"overall_price": price, "disc_pr":disc_price}
                transaction_level_data = [username, datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") ,user_type_of_transaction ,sno_products[product_choice] , n_items ,price, disc_price]
                #print(transaction_level_data)
                transaction_level_data_df = pd.DataFrame(transaction_level_data).T
                #print(transaction_level_data_df)
                transaction_level_data_df.rename(columns = {0:"username",1:"trans_date",2:"trans_type", 3:"product",4:"quantity",5:"cost",6:"disc_cost"},inplace =True)
                #print(transaction_level_data_df)
                overall_data_captured = overall_data_captured.append(transaction_level_data_df,ignore_index= True)
                #print(finalised_df)
                overall_data_captured.to_csv("finalised_by_meghamgaadu.csv",index=False)
                #print("Total available items are {}".format(total_items_in_showroom))
            else:
                print("We regret for the inconvenience caused and we have only {available_items} {products}'s available in the store".format(available_items = str(product_choice_availability_check),products = sno_products[product_choice]))
                print("Please choose with in the availability range. Thanks!")
                fn_available_quantities()
        else:
            print("Please provide a valid input")
    elif(user_type_of_transaction == 2): #Cancellation
        cancellation_availability = overall_data_captured["username"][overall_data_captured["username"].isin([username])].count()
        if (cancellation_availability == 0):
            print("Sorry, We were unable to find any transaction with this username")
        else:
            print("Awesome! Lets go for Cancellation") 
            fn_otp()
            df_after_deleting=overall_data_captured[overall_data_captured["username"] != username]
            df_after_deleting.to_csv("finalised_by_meghamgaadu.csv",index=False)
    user_shopping_decision = input("Do you want to continue shopping with us[y/n]:".lower())        
    if (user_shopping_decision != "y"):
        print("Thanks for shoppping and We are looking forward to see you again")
        break
        


# In[ ]:




