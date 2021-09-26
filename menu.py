from users import User


def show_menu():
    choice = 1
    while choice != 3:
        print(
            "--------------------------------------------------------------MAIN MENU-------------------------------------------------------------------------")
        print("1.Register\n2.Sign in\n3.Log out")
        choice = int(input("Enter Number (Main Menu)"))
        if choice == 1:
            print("1.store manager\n2.Customer")
            role_selection = int(input("Enter number of your role"))
            if role_selection == 1:
                User.register_store_manager()
            elif role_selection == 2:
                User.register_customer()
            else:
                raise Exception("invalid input ")
        elif choice == 2:
            User.login_user()

        else:
            break


show_menu()



