import json
import os
import csv
import pandas as pd
import ast



import functions
from file_Handler import FileHandler
class StoreManager:
    add_stores_to_file = FileHandler("Stores.csv")
    read_stores_file = FileHandler("Stores.csv")
    read_invoices = FileHandler("invoice.csv")
    read_users_file = FileHandler("users.csv")

    def __init__(self,user_name,store_name,open_time,close_time):
        self.user_name = user_name
        self.store_name = store_name
        self.open_time = open_time
        self.close_time = close_time
        self.products =None
        self.block_customer = None
        #اینجا چک می کنیم اگر یوزرنیم مدیر فروشگاه وجود نداشت بعد تو فایل اددش کنه
        reader = self.read_stores_file.read_file()
        bool_result = True
        for i in reader:
            if i["user_name"] == self.user_name:
                bool_result = False
                break
        if bool_result:
            self.add_stores_to_file.add_to_file(self.__dict__)

    def add_product(self):
        number_of_product  = int(input("Enter number of  product "))
        product_list = []
        for i in range(1, number_of_product+1):
            print(f"product{i}:")
            product_name = input("Enter product name")
            barcode = int(input(" Enter Barcode"))
            price = int(input(" Enter price"))
            brand = input("Enter Brand")
            number_available = int(input(" Enter number of product"))
            expire_date = int(input(" Enter expire Date"))
            product_list.append({"product_name": product_name ,"barcode":barcode,"price":price,"brand":brand,
                             "number_available":number_available,"expire_date":expire_date})


#اینجا چون من داخل init اومدم یکبار اطلاعات رو داخل فایل stores ذخیره کردم ،بار اول که اطلاعات ذخیره میشن مقدار محصولات خالی هست
        #باید اول چک بشه اگر مقدار محصول خالی هست فایل رو ادیت کن اگرم پر هست مقدار قبلی رو یه جا نگه میداریم و مقدار جدید هم بهش اضافه میکنیم بعد فایل رو ادیت می کنیم
        # ادیت فایل دقیقا مثل نوشتن تو فایل با ایت تفائت که مدش a هست یعنی یه دور فایل رو پاک می کنم بعد دوباره با اطلاعات جدید می نویسم
        reader=self.read_stores_file.read_file()
        final_list = []
        for i in reader:
            if i["user_name"] != self.user_name:
                final_list.append(i)
        for item_dict in reader:
            if item_dict["user_name"] == self.user_name:
                if item_dict["products"] == '':
                    self.block_customer = item_dict["block_customer"]
                    self.products = product_list
                    final_list.append(self.__dict__)
                    self.add_stores_to_file.edit_to_file(final_list)
                else:
                    result = item_dict["products"]
                    new_product_list = functions.list_parser(result)
                    print(new_product_list)
                    for i in new_product_list:
                        product_list.append(i)
                    print(product_list)
                    self.block_customer = item_dict["block_customer"]
                    self.products = product_list
                    final_list.append(self.__dict__)
                    self.add_stores_to_file.edit_to_file(final_list)

    def view_remaining_inventory(self):
        self.alarm()
        reader = self.read_stores_file.read_file()
        for item in reader:
            if item["user_name"] == self.user_name:
                product_of_store = item['products']
                list_product_of_store=functions.list_parser(product_of_store)
                break
        if list_product_of_store:
            print("---------------------------------------Product List -----------------------------------------")
            for item_dict in list_product_of_store:
                #
                # print(item_dict)
                # print(type(item_dict))
                print("Product Name:",item_dict["product_name"],"Barcode:",item_dict['barcode'],"Price:",
                      item_dict["price"],"Brand:",item_dict["brand"],"Number Available:",item_dict["number_available"],
                      "Expire Date:",item_dict["expire_date"])
        else:
            print("No Product Please Add Product")

    def update_vlue_of_product_list(self,store_name,product_name,number):
        reader = self.read_stores_file.read_file()
        final_list = []
        product_list =[]
        bool_update = False
        for i in reader:
            if i["user_name"] == self.user_name and i["store_name"] == store_name :
                bool_update = True
        if bool_update:
            for i in reader:
                if i["user_name"] != self.user_name:
                    final_list.append(i)
                elif i["user_name"] == self.user_name:
                    self.block_customer = i["block_customer"]
                    if i["store_name"] == store_name :
                        if i["products"]:
                            result = i["products"]
                            new_result = functions.list_parser(result)
                            for i in new_result:
                                if i["product_name"] == product_name:
                                    if i["number_available"] >= number:
                                        new_available_number = i["number_available"] - number
                                        i["number_available"] = new_available_number
                                        product_list.append(i)
                                else:
                                    product_list.append(i)
            print(product_list)
            self.products = product_list
            #self.block_customer =
            final_list.append(self.__dict__)
            self.add_stores_to_file.edit_to_file(final_list)
        else:
            print("product name or user name is wrong")

                    #     product_list.append(i)
                    # print(product_list)
                    # self.products = product_list
                    # final_list.append(self.__dict__)
                    # self.add_stores_to_file.edit_to_file(final_list)

    def alarm(self):
        reader = self.read_stores_file.read_file()
        alarm_list = []
        for i in reader:
            if i["user_name"] == self.user_name:
                if i["products"]:
                    result = i["products"]
                    new_result = functions.list_parser(result)
                    #print(new_result)
                    for j in new_result:
                        if j["number_available"] <=3:
                            alarm_list.append(j)
        if alarm_list:
            print("---------------------------------------alarm list ---------------------------------------")
            for i in alarm_list:
                print(i)
            print("-----------------------------------------------------------------------------------------")

    def view_invoices(self):
        ivoice_list = self.read_invoices.read_file()
        for i in ivoice_list:
            invoices=i["invoice"]
            #print(invoices)
            #print(type(invoices))
            list_invoices = functions.list_parser(invoices)
           # print(type(list_invoices))
            list_invoices_with_store_name =[]
            for j in list_invoices :
                if j['store_name'] == self.store_name:
                    list_invoices_with_store_name.append(j)
            print("username:",i["user_name"],",","list_invoices:",list_invoices_with_store_name)

        # print(list_invoices_with_store_name)

    def view_information_all_customer(self):
        list_users = self.read_users_file.read_file()
        if list_users:
            for item in list_users:
                i = item["information"]
                convertedDict = ast.literal_eval(i)
                if item["type"] == "Customer":
                    print(convertedDict['username'])
                    print(type(convertedDict['username']))
    #todo complete
    def block_customer_from_store(self):
        block_list = []
        self.view_information_all_customer()
        choose_block_customer = int(input("please enter username that you want delete:"))
        block_list.append(choose_block_customer)
        reader = self.read_stores_file.read_file()
        final_list = []
        for i in reader:
            if i["user_name"] != self.user_name:
                final_list.append(i)
        for item_dict in reader:
            if item_dict["user_name"] == self.user_name:
                if item_dict["block_customer"] == '':
                    self.block_customer = block_list
                    self.products = item_dict['products']
                    final_list.append(self.__dict__)
                    self.add_stores_to_file.edit_to_file(final_list)
                else:
                    result = item_dict["block_customer"]
                    new_block_list = functions.list_parser(result)
                    print(new_block_list)
                    for i in new_block_list:
                        block_list.append(i)
                    print(block_list)
                    self.block_customer = block_list
                    self.products = item_dict['products']
                    final_list.append(self.__dict__)
                    self.add_stores_to_file.edit_to_file(final_list)

    @staticmethod
    def sign_out():
        print("you logged out")



























store1 = StoreManager("789","kouroush",1,8)
store2 = StoreManager("123","refah",2,24)
#store1.alarm()
#store1.view_invoices()
#store2.view_invoices()
#store2.view_information_all_customer()
#store1.block_customer_from_store()
#store1.update_vlue_of_product_list("kouroush","rice",2)
#store2.update_vlue_of_product_list("kouroush","apple",1)
#store1.add_product()
# store1.view_remaining_inventory()
#store2.add_product()
# # store1.save_to_json_file()
store1.view_remaining_inventory()