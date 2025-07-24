# Login & Sign Up App

import streamlit as st
import pandas as pd

# DB Management
import mysql.connector
mydb = mysql.connector.connect(host="localhost",username="root",password="") # ('ls.sql')
# print(mydb) 
c = mydb.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT.password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,oasswird) VALUES (?,?)',(username,password))
    mydb.commit()

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password=?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data

# mycursor.execute("drop database if exists bscit")
# print("Database Deleted")
# mycursor.execute("create database bscit")
# print("Database Created")

def main():
    st.title("LS App")

    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            result = login_user(username,password)
            if result:

                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task,",["Add Post","Analytics","Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_sql = pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_sql)
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_Password = st.text_input("Password",type="password")

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,new_Password)
            st.success("You have successfully created an valid account")
            st.info("Go to login Menu")

if __name__ == '__main__':
    main()