from file_Handler import FileHandler
import functions
class Customer:
    read_stores_file = FileHandler("Stores.csv")
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def Show_store(self):
        reader = self.read_stores_file.read_file()
        #product_list = []
        for i in reader:
            #Todo shart bezaram vase time
            print("Store Name:",i["store_name"])
            print("products:", i["products"])

    def buy_from_store(self,store_name,product_name,number_of_product):
        reader = self.read_stores_file.read_file()
        for i in reader:
            if i["store_name"] == store_name:
                products = i["products"]
                new_result = functions.list_parser(products)
                for j in new_result:
                    if j["product_name"] == product_name and j["number_available"] >= number_of_product:
                        pass




