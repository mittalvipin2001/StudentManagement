import mysql.connector as mysql

conn = mysql.connect(host="localhost",user="root",password="tirupati2587",database="college")
cursor = conn.cursor()

def student_session(username):
    while 1:
        print("")
        print("Student menu")
        print("1. Change password ")
        print("2. Log out")
        
        user_option = input(str("option : "))
        if user_option =="1":
            print("")
            print("Change password")
            new_password = input(str("New password : "))
            cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE username = '{username}'")
            conn.commit()
        elif user_option =="2":
            break
        else:
            print("No valid option selected")
        
def teacher_session(username):
     while 1:
        print("")
        print("Teacher menu")
        print("1. Change password ")
        print("2. Log out")
        
        user_option = input(str("option : "))
        if user_option =="1":
            print("")
            print("Change password")
            new_password = input(str("New password : "))
            cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE username = '{username}'")
            conn.commit()
        elif user_option =="2":
            break
        else:
            print("No valid option selected")

def admin_session():
    while 1:
        print("")
        print("Admin menu")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. Delete existing teacher")
        print("5. See all users")
        print("6. Logout")
        

        user_option = input(str("option : "))
        if user_option =="1":
            print("")
            print("Register new student")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            query_vals = (username,password)
            cursor.execute("INSERT INTO users(username, password, privilege) VALUES (%s,%s,'student')",query_vals)
            conn.commit()
        elif user_option =="2":
            print("")
            print("Register new teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            query_vals = (username,password)
            cursor.execute("INSERT INTO users(username, password, privilege) VALUES (%s,%s,'teacher')",query_vals)
            conn.commit()
        elif user_option =="3":
            print("")
            print("Delete existing student")
            username = input(str("Student username : "))
            query_vals = (username)
            cursor.execute("DELETE FROM users WHERE username = %s",query_vals)
            conn.commit()
        elif user_option =="4":
            print("")
            print("Delete existing teacher")
            username = input(str("Teacher username : "))
            query_vals = (username)
            cursor.execute("DELETE FROM users WHERE teacher = %s",query_vals)
            conn.commit()
        elif user_option == "5":
            cursor.execute("SELECT id,username,privilege FROM users")
            print(cursor.fetchall())
        elif user_option =="6":
            break
        else:
            print("No valid option selected")

def auth(privilege):
    print("")
    print(f"{privilege} login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    cursor.execute(f"SELECT username,password FROM users WHERE privilege = '{privilege}'")
    users = cursor.fetchall()
    for user in users :
        if username == user[0]:
            if password == user[1]:
                if privilege == 'student':
                    student_session(username)
                elif privilege == 'teacher':
                    teacher_session(username)
                elif privilege == 'admin':
                    admin_session()
            else:
                print("Incorrect password")
            break

def main():
    while 1:
        print("\nWelcome to my college\n")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        print("4. Exit")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth('student')
        elif user_option == "2":
            auth('teacher')
        elif user_option == "3":
            auth('admin')
        elif user_option == "4":
            break
        else:
            print("No valid option was selected")
    conn.close()

main()

