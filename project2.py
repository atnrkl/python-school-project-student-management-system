"""
author: @ryu




"""

admin_username, admin_password = "admin", "1924"  # identify admin

courses = {"Calculus": "3", "Chemistry": "3"}

users2 = {"ahmet": ["123", 200, ["Chemistry", "Calculus"]]}


# courses


# gets selected account from budget_menu
def bank_menu(selected_account):
    while True:
        print("1-) Add money to user\n"
              "2-) Subtract money from user\n"
              "3-) Back to admin menu\n")
        select_menu = input("Select menu: ")

        if select_menu == "1":
            money = input("How much money you want to add ?")
            print(money + "$ will be added")
            print("Are you sure ? [Y/n]")
            decision = input("")
            id = selected_account[0]
            if decision == "Y":
                try:

                    money = int(money)
                    users2[id][1] += money

                except ValueError:
                    print("cheese")

            else:
                print("İnvalid value.. Try again")
                continue
        elif select_menu == "2":
            money = input("How much money you want to subtract ?")
            print(money + "$ will be subtracted ")
            print("Are you sure ? [Y/n]")
            decision = input("")
            # controlling the input value to be sure it is wanted type
            if decision == "Y":
                try:

                    money = int(money)
                    users2[selected_account][1] -= money
                except:
                    print("invalid value .. Try again")
                    continue
            else:
                print("Invalid value.. Try again")
                continue
        elif select_menu == "3":
            admin_menu()


# lists the courses dictionary on top
def list_courses_admin():
    print("     Courses" + "         " + "Credits")
    count = 1
    for i in courses:
        print(str(count) + "-) " + i + "           " + courses[i])
        count += 1
    admin_menu()
    return


# creating course from admin menu
def create_course_admin():
    course_name = input("which course you want to add ? ")
    course_credits = input("how much credits this course has? ")
    print(course_name + " will be added with " + course_credits + " are you sure [Y/n]")
    check = input()
    if check == "Y":
        courses[str(course_name)] = str(course_credits)
        admin_menu()
    else:
        admin_menu()


# deletes the course chosen and returns its credit x 100 to users budget
def delete_course_admin():
    global courses
    while True:
        print("     Courses" + "         " + "Credits")
        count = 1
        for i in courses:
            print(str(count) + "-) " + i + "           " + courses[i])
            count += 1

        # convert
        temp_list = zip(courses.keys(), courses.values())
        temp_list = list(temp_list)
        selected_item = input("Which course you want to delete")
        try:
            print("")
            selected_item = int(selected_item)
        except ValueError:
            print("invalid value... try again")
            continue

        if selected_item <= len(temp_list):
            temp_val = temp_list.pop(selected_item - 1)

            print(str(temp_val) + " been deleted money is transferred to the bank")
            courses = dict(temp_list)
            admin_menu()
        else:
            print("invalid value... try again")

            continue


# shows students of a course given
def show_students():
    while True:
        print("Which course you want to show ?")
        selected_course = str(input())
        for i in users2:
            for dip in users2[i][2]:
                if selected_course in dip:
                    print(i)
        admin_menu()


# budget menu shown when you press 5 on admin_menu
def users_budget_menu():
    while True:
        # users2 = {"ahmet": ["123", 900, ["chemistry,calculus"]]}
        print("     Student" + "         " + "Budget")
        count = 1
        for i in users2:
            print(str(count) + "-) " + i + "           " + str(users2[i][1]))
            count += 1
        print("Select the user: ")
        temp_list = zip(users2.keys(), users2.values())
        temp_list = list(temp_list)

        try:
            selected_user = int(input())
            selected_account = temp_list[selected_user - 1]
            bank_menu(selected_account)
        except ValueError:
            print("invalid value.. please try again")
            continue
        except IndexError:
            print("invalid value")
            continue

    return


# list users from users2 dictionary keys
def list_users():
    while True:
        print("Current users")
        count = 1
        for i in users2.keys():
            print(str(count) + "-) " + i)
            count += 1
        admin_menu()


# create user on admin menu
def create_user():
    while True:
        name = str(input("What is the name of user that you want to create?"))
        password = str(input("Chose password"))

        money = str(input("How much money do you want user to have?"))
        try:
            money = int(money)

            users2[name] = [password, money, []]
            admin_menu()
        except ValueError:
            print("money must be integer !")
            continue

        return


# delete user on admin menu
def delete_user():
    global users2
    while True:
        count = 1
        for i in users2:
            print(str(count) + "-) " + i + "           " + str(users2[i]))
            count += 1
        selected_user = input("Which user you want to delete")

        try:
            temp_list = zip(users2.keys(), users2.values())
            temp_list = list(temp_list)
            deleted_user = temp_list.pop(int(selected_user) - 1)
            deleted_user = deleted_user[0]
            users2 = dict(temp_list)
            print(deleted_user + " deleted")
            login(admin_username, admin_password)

        except ValueError:
            print("invalid value.. Try again")
            continue


# main menu to call functions for menu ingrediants
def admin_menu():
    while True:
        print("1-List courses\n"
              "2-Create a course\n"
              "3-Delete a course\n"
              "4-Show students registered to a course\n"
              "5-Users Budget Menu\n"
              "6-List Users\n"
              "7-Create User\n"
              "8-Delete User\n"
              "9-Exit")
        admin_menu_input = int(input("Your coice:"))

        if admin_menu_input == 1:
            list_courses_admin()
            return
        elif admin_menu_input == 2:
            create_course_admin()
            return
        elif admin_menu_input == 3:
            delete_course_admin()
            return
        elif admin_menu_input == 4:
            show_students()
            return
        elif admin_menu_input == 5:
            users_budget_menu()
            return
        elif admin_menu_input == 6:
            list_users()
            return
        elif admin_menu_input == 7:
            create_user()
            return
        elif admin_menu_input == 8:
            delete_user()
            return
        elif admin_menu_input == 9:
            login(admin_username, admin_password)
        else:
            continue


# menu for non-admin users
def user_menu(name):
    while True:
        print("Login Succesfull Welcome " + name)
        print("1-Add courses to my courses\n"
              "2-Delete a course from my courses\n"
              "3-Show my courses\n"
              "4-Budget Menu\n"
              "5-Exit")
        select_menu = input("Select menu: ")
        if select_menu == "1":
            add_course_to_user(name)
        elif select_menu == "2":
            delete_course_from_user(name)
        elif select_menu == "3":
            show_courses(name)
        elif select_menu == "4":
            budged_menu(name)
        elif select_menu == "5":
            login(admin_username, admin_password)
        else:
            print("invalid value.. Try again")
            continue


########################################################################################################################
# users can add courses from user_menu
def add_course_to_user(id):
    while True:
        print("     Courses" + "         " + "Credits")
        count = 1
        for i in courses:
            print(str(count) + "-) " + i + "           " + courses[i])
            count += 1
        dip = input("Which course do you want to take")

        try:
            dip = int(dip)
            temp_list = list(courses)
            selected_course = temp_list[dip - 1]
            temp_money = courses[selected_course]
            if selected_course not in users2[id][2]:
                print("")
            else:
                print("this course already exist!")
            if int(users2[id][1]) >= int(temp_money) * 100:
                users2[id][2].append(selected_course)

                users2[id][1] -= int(temp_money) * 100

                print("Successful")
            else:
                print("you don't have have enough money and this is the order of the world")
            user_menu(id)


        except ValueError:
            print("Invalid value .. try again")
            continue
        except IndexError:
            print("İnvalid Value")
            continue
        return


def delete_course_from_user(id):
    while True:
        course_list = users2[id][2]
        counter = 1
        for i in course_list:
            print(str(counter) + "-) " + i)
            counter += 1
        select_d = input("Which course you want to delete")
        try:
            select_d = int(select_d)
            temp_val = course_list[select_d - 1]
            print("You have chosen" + temp_val)

            del course_list[select_d - 1]
            users2[id][2] = course_list
            temp_i = ""
            for i in courses:
                if i == temp_val:
                    temp_i = i
                    temp_int = int(courses[i]) * 100
                    print(str(temp_int) + "$ will be refunded")

            desicion = input("do you want to contiune ? [Y/n]")
            if desicion == "Y":
                users2[id][1] += int(courses[temp_i]) * 100
                user_menu(id)
            elif desicion == "n":
                user_menu(id)
            else:
                print("invalid value")
                continue

        except ValueError:
            print("invalid value .. Try again")
            continue
        except IndexError:
            print("invalid value... TRY AGAİN")
            continue


def show_courses(id):
    print("Course name               Credits")

    for i in users2[id][2]:
        if i in courses:
            print(str(i) + "                      " + str(courses[i]))

    return


# budget menu shown on user_menu
def budged_menu(id):
    while True:
        temp_budget = users2[id][1]
        print("your budges is " + str(temp_budget) + "$")
        print("1-) Add money to your budget")
        print("2-) go to main menu")
        select_menu = input("select the menu")
        if select_menu == "1":
            val = input("amount of money")
            users2[id][1] += int(val)
            print("your account has been updated")
        elif select_menu == "2":
            user_menu(id)
        else:
            print("invalid value.. Try again")
            continue

    return


def check_user_login(usern, passw):  # gets username and password from login() and checks normal user list
    for i in users2:

        print(users2[i][0])
        if usern == i and passw == users2[i][0]:
            return True
    return False


def login(au, ap):  # login screen
    while True:
        username_login = input("ID:")
        password_login = input("Password:")
        if username_login == au and password_login == ap:
            admin_menu()
            return
        elif check_user_login(username_login, password_login):
            user_menu(username_login)
            return
        print("Wrong!! try again")


login(admin_username, admin_password)
