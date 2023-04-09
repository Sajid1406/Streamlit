# Food Order System App

import streamlit as st
import pandas as pd
from PIL import Image

def main():
    #title
    st.title("Food Moments :hamburger:")
    menu = ["Home","Login","SignUp","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":

        #multiselection
        options=st.multiselect("Food Category",['Fast Food','Main Dishes','Drinks','Desert'])
        st.write("You Selected")
        for each_op in options:
            st.write(each_op)

        #image
        st.header("Food Items:")
        img = Image.open('Kacchi.png')
        img1 = Image.open('Cheeseburger.png')
        img2 = Image.open('Falooda.jpg')
        img3 = Image.open('Orange Juice.jpg')
        img4 = Image.open('pizza.png')

        #display images in a row
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(img, caption='Kacchi(700 TK)')
            st.image(img4, caption='Pizza(600 TK)')
        with col2:
            st.image(img1, caption='Cheeseburger(220 TK)')
        with col3:
            st.image(img2, caption='Falooda(300 TK)')
        with col4:
            st.image(img3, caption='Orange Juice(150 TK)')

        #number input
        number=st.number_input("Selected Item")
        st.write("The current item is",number)

        #button
        st.button("OK!")
        st.subheader("Payment Method:")
        if(st.button("PAYMENT")):
            st.text("PAYMENT SUCSESSFULLY!!") 

    #login section
    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        st.sidebar.button("Login")
        st.success("Logged In as {}".format(username))
        task = st.selectbox("Tasks",["Add Post","Profiles"])
        if task == "Add Post":
                    st.subheader("Add Your Post")
        elif task == "Profiles":
                st.subheader("User Profile")
                sign=pd.DataFrame({
                'Username':[username],
                'Password':[password]
            })
                st.write(sign)

    #signup section
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_Password = st.text_input("Password",type="password")

        if st.button("Signup"):
            st.success("You have successfully created an valid account")
            st.info("Go to login Menu")
       
    #about section
    elif choice == "About":
        st.subheader("About Us")
        st.write("Food Moments is an online food ordering system designed to make your dining experience easy and hassle-free." 
                " Our app is user-friendly and allows you to browse menus, select items, and track your orders in real-time." 
                " So whether you're craving pizza, burger, or something delicious, Food Moments has got you covered." 
                " Try us today and enjoy a delicious meal without ever leaving your home!")

if __name__ =='__main__':
    main()

