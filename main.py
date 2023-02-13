import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.set_page_config(page_title="Library Management System",page_icon="https://www.pngitem.com/pimgs/m/665-6657133_library-management-system-logo-png-transparent-png.png")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
                  background: #ffffff;
                  secondary_background:#7A9CE6;
                  
                  
                  background: linear-gradient(to left, #ffffff,#ffff49 );
                  font: Serif

         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()








st.title("LIBRARY MANAGEMENT SYSTEM")
st.sidebar.image("https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/HOW-DO-YOU-DESIGN-A-LIBRARY-MANAGEMENT-SYSTEM-min.png")
choice=st.sidebar.selectbox("My Menu",("Home","Student","Librarian","Read Online"))
if(choice=="Home"):
    st.write("This Application is Developed by Saurabh as a part of Training Project")
    st.image("https://www.pngkit.com/png/detail/443-4433043_library-management-system-library-management-system-png.png")
elif(choice=="Student"):
    
    if 'login' not in st.session_state:
        st.session_state['login']=False
    sid=st.text_input("Enter Student ID")
    pwd=st.text_input("Enter Password",type="password")
    btn=st.button("Login")    
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
        c=mydb.cursor()
        c.execute("select * from Students")
        for row in c:
            if(row[0]==sid and row[1]==pwd):
                st.session_state['login']=True
                st.header("Login Successfull")
                
                
                break
        if(st.session_state['login']==False):
            st.header("Incorrect ID or Password")
    
    
        
    if(st.session_state['login']==True):
       
        
        choice2=st.selectbox("Features",("None","Search Book","Issue Book"))
        if(choice2=="Search Book"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
            c=mydb.cursor()
            c.execute("select * from Books")
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=['BookID','BookName','AuthorName'])
            st.dataframe(df)
        elif(choice2=="Issue Book"):
            bid=st.text_input("Enter Book ID")
            sid=st.text_input("Enter Your ID")
            btn2=st.button("Issue Book")
            if btn2:
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
                c=mydb.cursor()
                c.execute("insert into Issued values(%s,%s,%s)",(doi,bid,sid))
                mydb.commit()
                st.header("Book Issued Successfully")



elif(choice=="Read Online"):
    st.markdown("<iframe width='100%' height='400px'src='https://juser.fz-juelich.de/record/891478/files/python-2021.pdf'></iframe>",unsafe_allow_html=True)


elif(choice=="Librarian"):
    
    if 'login' not in st.session_state:
       st.session_state['login']=False
    ssid=st.text_input("Enter Librarian ID")
    pswd=st.text_input("Enter Password",type="password")
    btn2=st.button("Login")    
    if btn2:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
        d=mydb.cursor()
        d.execute("select * from Librarian")
        for row in d:
            if(row[0]==ssid and row[1]==pswd):
                st.session_state['login']=True
                break
        if(st.session_state['login']==False):
            st.header("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.header("Login Successfull")
        choice3=st.selectbox("Features:",("select below:","BookDatabase","IssuedBooks"))
        if(choice3=="BookDatabase"):
             choice4=st.selectbox("Choose:",("None","ShowDatabase","AddBooks","RemoveBooks"))
             if(choice4=="ShowDatabase"):
             
                  mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
                  d=mydb.cursor()
                  d.execute("select * from Books")
                  t=[]
                  for r in d:
                      t.append(r)
                  ef=pd.DataFrame(data=t,columns=['BookID','BookName','AuthorName'])
                  st.dataframe(ef)
             if(choice4=="AddBooks"):
                 st.write("Please update the information below:")
                 bkn=st.text_input("Enter Book ID:")
                 bkname=st.text_input("Enter the name of book:")
                 bkauthor=st.text_input("Enter the author name:")
                 btn3=st.button("Add")
                 if btn3:
                     mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
                     e=mydb.cursor()
                     e.execute("insert into Books values(%s,%s,%s)",(bkn,bkname,bkauthor))
                     mydb.commit()
                     st.caption("Library Updated")

                         
                         
             if(choice4=="RemoveBooks"):
                  t=st.text_input("Enter Book Id you want to remove:")
                  btn4=st.button("Remove-")
                  if btn4:
                      mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
                      e=mydb.cursor()
                      f="delete from books where BookID='"+t+"'"
                      e.execute(f)
                      mydb.commit()
                      st.caption("Library Updated")
                       
                        
                        
                            
                         
                 
                      
                      
                     
                     
                
        elif(choice3=="IssuedBooks"):
            
              mydb=mysql.connector.connect(host='localhost',user='root',password='Saurabh2103@',database='lms')
              f=mydb.cursor()
              f.execute("select * from Issued")
              w=[]
              for r in f:
                  w.append(r)
              mf=pd.DataFrame(data=w,columns=['DateofIssue','BookID','StudentID'])
              st.dataframe(mf)
