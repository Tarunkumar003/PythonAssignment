try:
    import mysql.connector as mydb
    mycon=mydb.connect(user='root',password='12345678',database='assignment',host='127.0.0.1')
    mycursor=mycon.cursor()
    print("user administration")
    print("1.sign-up")
    print("2.sign-in")
    print("3.change password")
    print("4.forget password")
    e=int(input("enter your choice="))

    if e==1:
        print("sign-up")
        username = input("enter your name:")
        mycursor.execute("SELECT * from myuser where username = '%s';" %(username))
        myuser=mycursor.fetchone()
        if (mycursor.rowcount!=0):
            print("user name equiped ! ,try diffrent username ")
        else :
            password=input("enter your password:")
            hinq=input("enter your hint question:")
            hpassword=input("enter your hpassword:")


            save_option =int(input("press 1 to save, 2 to cancle "))

            if save_option ==1:

                mycursor.execute("INSERT INTO myuser (username,password,hintq,hpassword) values (%s,%s,%s,%s)",
                                (username,password,hinq,hpassword))    
                mycon.commit()
                print("welcome")
            else :
                print("oops soory ! error404.....")
        
    elif e==2:
        print("sign-in")
        username = input("enter your name:")
        mycursor.execute("SELECT * from myuser where username = '%s';" %(username))
        myuser=mycursor.fetchone()
        if (mycursor.rowcount!=1):
            print("user name not found ! ,try diffrent username ")
        else :
            password=input("enter your password:")
            mycursor.execute("SELECT * from myuser where password = '%s';" %(password))
            myuser=mycursor.fetchone()
            if (mycursor.rowcount!=1):
                print("wrong password! ,try diffrent password ")
            else:
                save_option =int(input("press 1 to save, 2 to cancle "))

                if save_option ==1:
                    print("welcome")
                else :
                    print("oops soory ! error404.....")
    elif e==3:
        print("change password")
        username = input("enter your name:")
        mycursor.execute("SELECT * from myuser where username = '%s';" %(username))
        myuser=mycursor.fetchone()

        if (mycursor.rowcount!=1):
            print("user name not found ! ,try diffrent username ")
        else :
            password=input("enter your password:")

            mycursor.execute("SELECT * from myuser where password = '%s';" %(password))
            myuser=mycursor.fetchone()

            if (mycursor.rowcount!=1):
                print("wrong password! ,try diffrent password ")
            else:
                mycursor.execute("SELECT hintq FROM myuser where username=%s",(username,))
                myresult = mycursor.fetchone()
                for x in myresult:
                    print("your hint question was,")

                    print(x)
            


                    password=input("enter your hint password:")

                    mycursor.execute("SELECT * from myuser where hpassword = '%s';" %(password))
                    myuser=mycursor.fetchone()

                    if (mycursor.rowcount!=1):
                        print("wrong password! ,try diffrent password ")

                    else:
                        new_password=int(input("enter your new password: "))
                        save_option =int(input("press 1 to save, 2 to cancle "))

                        if save_option ==1:

                            mycursor.execute("UPDATE myuser SET password = %s WHERE username = %s", 
                                                (new_password, username))   
                            mycon.commit()
                            print("you have updated your password successfully")


                
                        else :
                            print("oops soory ! error404.....")

        
    elif e==4:
        print("forget password")
        mycursor = mycon.cursor()
        username=input("enter your name:\n")
        mycursor.execute("SELECT * from myuser where username = '%s';" %(username))
        myuser=mycursor.fetchone()

        if (mycursor.rowcount!=1):
            print("user name not found ! ,try diffrent username ")
        else :
            mycursor.execute("SELECT hintq FROM myuser where username=%s",(username,))
            myresult = mycursor.fetchone()
            for x in myresult:
                print("your hint question was,")

                print(x)
            


                password=input("enter your hint password:")

                mycursor.execute("SELECT * from myuser where hpassword = '%s';" %(password))
                myuser=mycursor.fetchone()

                if (mycursor.rowcount!=1):
                    print("wrong password! ,try diffrent password ")
                else:
                
                    save_option =int(input("press 1 to save, 2 to cancle "))

                    if save_option ==1:
                        mycursor.execute("SELECT password FROM myuser where username=%s",(username,))
                        myresult = mycursor.fetchone()
                        for x in myresult:
                            print("your password was:")
                            print(x)
                    else :
                        print ("error , password not found !")
    else:
        print("invalied input!")
except:
    print("error occured  :( ")

finally:
    mycon.close()
