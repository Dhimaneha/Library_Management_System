from tkinter import *
from tkinter import messagebox
import pymysql
from IssueBook import*
from ReturnBook import*
from AddBook import*
from ViewBook import*
from DeleteBook import*


mypass="Neha@2001"
mydatabase="mysql"

con=pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur=con.cursor()


root = Tk()
root.title("Library")
root.geometry("800x400")
bg=PhotoImage(file="lib.png")
Canvas1 = Canvas(root,width=400,height=200)
Canvas1.pack(fill="both",expand=True)
Canvas1.create_image(0,0,image=bg,anchor="nw")



headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome To IGDTUW Library", bg='black', fg='#FFBB00', font=('Algerian',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1=Button(root,text="Add Book",bg='black',
            fg='white',font=('Gill Sans Ultra Bold',18),command=addBook)
btn1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)


btn2=Button(root,text="Issue Book",bg='#4D4F63',
            fg='white',font=('Gill Sans Ultra Bold',18),command=issueBook)
btn2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)


btn3=Button(root,text="Return Book",bg='black',
            fg='white',font=('Gill Sans Ultra Bold',18),command=returnBook)
btn3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)


btn4=Button(root,text="View Book",bg='#4D4F63',
            fg='white',font=('Gill Sans Ultra Bold',18),command=View)
btn4.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)


btn5=Button(root,text="Delete Book",bg='black',
            fg='white',font=('Gill Sans Ultra Bold',18),command=delete)
btn5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)


root.mainloop()
