import ast
import hashlib
from file_Handler import FileHandler
from functions import hash_password
from storemanager import StoreManager


class User:
    users_file = FileHandler("users.csv")
    check_username = False

    @classmethod
    def register_customer(cls):

        username = input("Enter user name")
        while True:
            if len(username) != 11 or not username.isnumeric():
                print("Your username should be 11 character and should be number")
                username = input("Enter Password")
            else:
                break

        password = input("Enter Password")
        repeat_password = input("Repeat Password")
        h_password =hash_password(password)
        # hash_password = password.encode()
        # hasher_pass = hashlib.sha256(hash_password).hexdigest()
        customer_dict = {"type": "Customer", "information": {"username": username, "password": h_password}}
        list_users = cls.users_file.read_file()
        if list_users:
            #print(list_users)
            for item in list_users:
                i = item["information"]
                convertedDict = ast.literal_eval(i)
                if convertedDict["username"] == username:
                    print("username exist")
                    cls.check_username = True
                    break

            if password == repeat_password:
                if not cls.check_username:
                    cls.users_file.add_to_file(customer_dict)
        else:
            cls.users_file.add_to_file(customer_dict)

    @classmethod
    def register_store_manager(cls):
        username = input("Enter user name")
        while True:
            if len(username) != 11 or not username.isnumeric():
                print("Your username should be 11 character and should be number")
                username = input("Enter Password")
            else:
                break
        password = input("Enter Password")
        repeat_password = input("Repeat Password")
        store_name = input(" Enter Store name")
        open_time = int(input("enter open time"))
        close_time = int(input("enter close time"))
        # hash_password = password.encode()
        # hasher_pass = hashlib.sha256(hash_password).hexdigest()
        h_pass = hash_password(password)
        store_manager_dict = {"type": "StoreManager", "information": {"username": username, "password": h_pass,
                                                                      "store_name": store_name, "open_time": open_time,
                                                                     "close_time": close_time}}
        list_users = cls.users_file.read_file()
        if list_users:
            #print(list_users)
            for item in list_users:
                i = item["information"]
                convertedDict = ast.literal_eval(i)
                if convertedDict["username"] == username:
                    print("username exist")
                    cls.check_username = True
                    break

            if password == repeat_password:
                if not cls.check_username:
                    cls.users_file.add_to_file(store_manager_dict)
        else:
            cls.users_file.add_to_file(store_manager_dict)

    @classmethod
    def login_user(cls):
        bool_logout = False
        username_login = input("Enter your username")
        password_login = input("Enter password")
        hash_pass = hash_password(password_login)
        list_users = cls.users_file.read_file()
        if list_users:
            for item in list_users:
                i = item["information"]
                convertedDict = ast.literal_eval(i)
                if convertedDict["username"] == username_login and convertedDict["password"] == hash_pass:
                    if item["type"] == "StoreManager":
                        username=convertedDict["username"]
                        store_name=convertedDict["store_name"]
                        open_time=convertedDict["open_time"]
                        close_time =convertedDict["close_time"]
                        print(username,store_name,open_time,close_time)
                        stor_manager = StoreManager(username,store_name,open_time,close_time)
                        stor_manager.alarm()

                        n=10

                        while n != 8:
                            print(
                                "--------------------------------------------------------Store Manage Menu--------------------------------------------------")
                            print(
                                "StoreManager\n1.Add Product List\n2.View inventory\n3.alarm\n4.View customer invoices\n"
                                "5.Search invoices\n6.View customer information\n7.Block Customer\n8.exit")

                            n = int(input("choose number access"))
                            if n == 1:
                                stor_manager.add_product()
                            elif n == 2:
                                stor_manager.view_remaining_inventory()
                            elif n == 3:
                                stor_manager.alarm()
                            elif n == 4:
                                stor_manager.view_invoices()
                            elif n == 5:
                                #امتیازی
                                pass
                            elif n == 6:
                                stor_manager.view_information_all_customer()
                            elif n == 7 :
                                stor_manager.block_customer_from_store()
                            elif n == 8:
                                stor_manager.sign_out()
                                break

                    else:
                        print("Customer\ndastresi customer")

        # elif bool_logout:
        #     menu.show_menu()

                # else:
                #     print("wrong user name or password")
        else:
            print("no value")














