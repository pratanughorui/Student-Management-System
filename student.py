from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1550x900+0+0")

        title_label=Label(self.root,text="Student Management System",font=("Comic Sans MS",25,"bold"),bg="slateblue",fg="white")
        title_label.pack(side=TOP,fill="x")

        #----------------create varriable---------#
        self.student_name=StringVar()
        self.student_roll=StringVar()
        self.student_class=StringVar()
        self.student_sec=StringVar()
        self.student_gender=StringVar()
        self.student_cont=StringVar()
        self.student_dob=StringVar()
        self.student_parents=StringVar()
        self.student_pcont=StringVar()
        self.student_adhar=StringVar()
        self.student_search_class=StringVar()
        self.student_search_sec=StringVar()
        self.student_search_roll=StringVar()
        self.student_search_name=StringVar()



        #--------------Manage frame---------------#
        manage_frame=Frame(self.root)
        manage_frame.place(x=10,y=50,width=500,height=725)

        manage_label=Label(manage_frame,text="Manage Student",font=("Comic Sans MS",25,"bold"))
        manage_label.grid(row=0,columnspan=2,pady=15)

        name_label = Label(manage_frame, text="Name:", font=("Times New Roman", 15, "bold"))
        name_label.grid(row=1, column=0, pady=10)

        name_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_name, bd=3, relief=GROOVE, width=25)
        name_entry.grid(row=1, column=1)

        roll_label = Label(manage_frame, text="Roll No:", font=("Times New Roman", 15, "bold"))
        roll_label.grid(row=2, column=0)

        roll_entry=Entry(manage_frame,font=("Times New Roman",15,"bold"),textvariable=self.student_roll,bd=3,relief=GROOVE,width=25)
        roll_entry.grid(row=2,column=1)

        class_label = Label(manage_frame, text="Class:", font=("Times New Roman", 15, "bold"))
        class_label.grid(row=3, column=0, pady=10)

        class_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_class,bd=3, relief=GROOVE, width=25)
        class_entry.grid(row=3, column=1)


        sec_label = Label(manage_frame, text="Section:", font=("Times New Roman", 15, "bold"))
        sec_label.grid(row=4, column=0, pady=10)

        sec_entry = ttk.Combobox(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_sec, width=23, state="readonly")
        sec_entry['values'] = ("A", "B", "C")
        sec_entry.grid(row=4, column=1)

        gender_label = Label(manage_frame, text="Gender:", font=("Times New Roman", 15, "bold"))
        gender_label.grid(row=5, column=0, pady=10)

        combo_gender=ttk.Combobox(manage_frame,font=("Times New Roman", 15, "bold"),textvariable=self.student_gender,width=23,state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=5,column=1)

        cont_label = Label(manage_frame, text="Contact No:", font=("Times New Roman", 15, "bold"))
        cont_label.grid(row=6, column=0, pady=10)

        cont_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_cont, bd=3, relief=GROOVE, width=25)
        cont_entry.grid(row=6, column=1)

        dob_label = Label(manage_frame, text="D.O.B:", font=("Times New Roman", 15, "bold"))
        dob_label.grid(row=7, column=0, pady=10)

        dob_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_dob, bd=3, relief=GROOVE, width=25)
        dob_entry.grid(row=7, column=1)

        parents_label = Label(manage_frame, text="parents Name:", font=("Times New Roman", 15, "bold"))
        parents_label.grid(row=8, column=0, pady=10)

        parents_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_parents, bd=3, relief=GROOVE, width=25)
        parents_entry.grid(row=8, column=1)

        pcont_label = Label(manage_frame, text="parents Contact No:", font=("Times New Roman", 15, "bold"))
        pcont_label.grid(row=9, column=0, pady=10)

        pcont_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_pcont, bd=3, relief=GROOVE, width=25)
        pcont_entry.grid(row=9, column=1)

        adhar_label = Label(manage_frame, text="Adharcard No:", font=("Times New Roman", 15, "bold"))
        adhar_label.grid(row=10, column=0, pady=10)

        adhar_entry = Entry(manage_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_adhar, bd=3, relief=GROOVE, width=25)
        adhar_entry.grid(row=10, column=1)

        address_label = Label(manage_frame, text="Address:", font=("Times New Roman", 15, "bold"))
        address_label.grid(row=11, column=0, pady=10)

        self.address_text=Text(manage_frame,width=25,height=4, font=("Times New Roman", 15, "bold"), bd=3, relief=GROOVE)
        self.address_text.grid(row=11,column=1)

        #--------------button1 frame------------#
        button1_frame=Frame(manage_frame)
        button1_frame.place(x=6,y=660,width=480,height=70)

        add_button=Button(button1_frame,text="ADD",bd=5,relief=RIDGE,width=10,height=2,command=self.insert_data,font=("Times New Roman", 13, "bold"))
        add_button.grid(row=0,column=0)

        update_button = Button(button1_frame,text="UPDATE",bd=5,relief=RIDGE,width=10,height=2,command=self.update_data,font=("Times New Roman", 13, "bold"))
        update_button.grid(row=0, column=1)

        delete_button = Button(button1_frame, text="DELETE", bd=5, relief=RIDGE, width=10, height=2,command=self.delete_data,font=("Times New Roman", 13, "bold"))
        delete_button.grid(row=0, column=2)

        clear_button = Button(button1_frame, text="CLEAR", bd=5, relief=RIDGE, width=10, height=2,font=("Times New Roman", 13, "bold"),command=self.clear_field)
        clear_button.grid(row=0, column=3)

       #---------------details frame------------#
        details_frame = Frame(self.root)
        details_frame.place(x=520, y=50, width=1000, height=725)

        search_frame=Frame(details_frame)
        search_frame.place(x=10,y=10,width=970,height=143)

        search_label=Label(search_frame,text="Search By",font=("Comic Sans MS", 20, "bold"))
        search_label.grid(row=0,columnspan=9,pady=5)

        search_class=Label(search_frame,text="Class:",font=("Times New Roman", 15, "bold"))
        search_class.grid(row=2,column=0)

        search_class_entry=Entry(search_frame,font=("Times New Roman", 15, "bold"),textvariable=self.student_search_class, bd=3, relief=GROOVE,width=12)
        search_class_entry.grid(row=2,column=1)

        search_sec=Label(search_frame,text="Section:",font=("Times New Roman", 15, "bold"))
        search_sec.grid(row=2,column=4)

        search_sec = ttk.Combobox(search_frame, font=("Times New Roman", 15, "bold"), textvariable=self.student_search_sec,width=10, state="readonly")
        search_sec['values'] = ("A", "B", "C")
        search_sec.grid(row=2, column=5)



        search_roll = Label(search_frame, text="Roll No:", font=("Times New Roman", 15, "bold"))
        search_roll.grid(row=2, column=2)

        search_roll_entry = Entry(search_frame, font=("Times New Roman", 15, "bold"),textvariable=self.student_search_roll, bd=3, relief=GROOVE,width=12)
        search_roll_entry.grid(row=2, column=3)

        search_name = Label(search_frame, text="Student Name:", font=("Times New Roman", 15, "bold"))
        search_name.grid(row=2, column=6)

        search_name_entry = Entry(search_frame, font=("Times New Roman", 15, "bold"), bd=3, relief=GROOVE,width=23,textvariable=self.student_search_name)
        search_name_entry.grid(row=2, column=7)

        search_button=Button(search_frame,text="Search", bd=5, relief=RIDGE, width=10, font=("Times New Roman", 13, "bold"),command=self.show_data)
        search_button.grid(row=3,column=1,pady=10,sticky="w")

#-------------------table frame----------------------------------------#
        table_frame=Frame(details_frame,bd=4,relief=RIDGE)
        table_frame.place(x=6,y=165,width=970,height=540)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("name","roll","class","sec","gender","cont","dob","pname","pcont","adhar","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("class", text="Class")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("cont", text="Contact No.")
        self.student_table.heading("dob", text="Date Of Birth")
        self.student_table.heading("pname", text="Parents Name")
        self.student_table.heading("pcont", text="parents contact no.")
        self.student_table.heading("adhar", text="Adhar No.")
        self.student_table.heading("address", text="Address")
        self.student_table['show']='headings'
        self.student_table.column("name", width=40)
        self.student_table.column("roll", width=15)
        self.student_table.column("class", width=15)
        self.student_table.column("sec", width=15)
        self.student_table.column("gender", width=30)
        self.student_table.column("cont", width=30)
        self.student_table.column("dob", width=25)
        self.student_table.column("pname", width=40)
        self.student_table.column("pcont", width=60)
        self.student_table.column("adhar", width=35)
        self.student_table.column("address", width=40)
        self.student_table.pack(fill=BOTH,expand=True)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursore)

    # -------------------table frame----------------------------------------#

    #-----------------------show data from database to table---------------------#

    def show_data(self):
        if(self.student_search_class.get()=="" and self.student_search_sec.get()=="" and self.student_search_roll.get()=="" and self.student_search_name.get()==""):
            messagebox.showerror("Error", "at least one field is required")
        elif(self.student_search_sec.get()=="" and self.student_search_roll.get()==""and self.student_search_name.get()==""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where class=%s order by sec,roll",self.student_search_class.get())
            rows = cur.fetchall()
            for row in rows:
               self.student_table.insert('', END, values=row)
               con.commit()
            con.close()
            self.clear_search_field()
        elif(self.student_search_class.get()=="" and self.student_search_sec.get()==""and self.student_search_name.get()==""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where roll=%s order by class,sec",self.student_search_roll.get())
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()
        elif (self.student_search_class.get() == "" and self.student_search_roll.get() == "" and self.student_search_name.get() == ""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where sec=%s order by class,roll",self.student_search_sec.get())
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()
        elif (self.student_search_class.get() == "" and self.student_search_roll.get() == "" and self.student_search_sec.get() == ""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where name=%s order by class",self.student_search_name.get())
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()
        elif (self.student_search_sec.get() == "" and self.student_search_name.get()==""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where class=%s and roll=%s order by sec",(self.student_search_class.get(),self.student_search_roll.get()))
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()

        elif (self.student_search_roll.get() == "" and self.student_search_name.get()==""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where class=%s and sec=%s order by roll",(self.student_search_class.get(),self.student_search_sec.get()))
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()

        elif (self.student_search_class.get() == "" and self.student_search_name.get()==""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where roll=%s and sec=%s order by class",(self.student_search_roll.get(),self.student_search_sec.get()))
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()

        elif (self.student_search_name.get() == ""):
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where class=%s and roll=%s and sec=%s",(self.student_search_class.get(),self.student_search_roll.get(),self.student_search_sec.get()))
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()


        else:
            self.clear_table()
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            cur.execute("select * from student_data where class=%s and roll=%s and sec=%s and name=%s",(self.student_search_class.get(), self.student_search_roll.get(), self.student_search_sec.get(),self.student_search_name.get()))
            rows = cur.fetchall()
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.clear_search_field()

    # -----------------------show data from database to table---------------------#

#---------------------pick data from table to managed frame--------------------#
    def get_cursore(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.student_name.set(row[0])
        self.student_roll.set(row[1])
        self.student_class.set(row[2])
        self.student_sec.set(row[3])
        self.student_gender.set(row[4])
        self.student_cont.set(row[5])
        self.student_dob.set(row[6])
        self.student_parents.set(row[7])
        self.student_pcont.set(row[8])
        self.student_adhar.set(row[9])
        self.address_text.delete(1.0, END)
        self.address_text.insert(END,row[10])
# ---------------------pick data from table to managed frame--------------------#

#------------------------------data managed-------------------------------#
    def insert_data(self):
        if (self.student_name.get() == "" or self.student_roll.get() == "" or self.student_class.get() == "" or self.student_sec.get() == "" or self.student_gender.get() == "" or self.student_cont.get() == "" or self.student_dob.get() == "" or self.student_parents.get() == "" or self.student_pcont.get() == "" or self.student_adhar.get() == "" or self.address_text.get(
                1.0, END) == ""):
            messagebox.showerror("Error", "all field are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
            cur = con.cursor()
            result=cur.execute("select * from student_data where roll=%s and class=%s and sec=%s",(self.student_roll.get(),self.student_class.get(),self.student_sec.get()))
            final=bool(result)
            if(final):
                messagebox.showerror("Error", "This field already exists")
            else:
                con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
                cur = con.cursor()
                cur.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.student_name.get(),
                                                                                                 self.student_roll.get(),
                                                                                                 self.student_class.get(),
                                                                                                 self.student_sec.get(),
                                                                                                 self.student_gender.get(),
                                                                                                 self.student_cont.get(),
                                                                                                 self.student_dob.get(),
                                                                                                 self.student_parents.get(),
                                                                                                 self.student_pcont.get(),
                                                                                                 self.student_adhar.get(),
                                                                                                 self.address_text.get('1.0', END)
                                                                                                 ))
                con.commit()
                con.close()
                messagebox.showinfo("Successfully", "data inserted successfully")
                self.clear_field()
                self.clear_table()

    def update_data(self):
        if (self.student_name.get() == "" or self.student_roll.get() == "" or self.student_class.get() == "" or self.student_sec.get() == "" or self.student_gender.get() == "" or self.student_cont.get() == "" or self.student_dob.get() == "" or self.student_parents.get() == "" or self.student_pcont.get() == "" or self.student_adhar.get() == "" or self.address_text.get(1.0, END) == ""):
            messagebox.showerror("Error", "all field are required")

        else :
                con = pymysql.connect(host="localhost", user="root", password="", database="studentmangement")
                cur = con.cursor()
                cur.execute("update student_data set name=%s,roll=%s,class=%s,sec=%s,gender=%s,cont=%s,dob=%s,pname=%s,pcont=%s,address=%s where adhar=%s",(self.student_name.get(),
                                                                                             self.student_roll.get(),
                                                                                             self.student_class.get(),
                                                                                             self.student_sec.get(),
                                                                                             self.student_gender.get(),
                                                                                             self.student_cont.get(),
                                                                                             self.student_dob.get(),
                                                                                             self.student_parents.get(),
                                                                                             self.student_pcont.get(),
                                                                                             self.address_text.get('1.0',END),
                                                                                             self.student_adhar.get(),
                                                                                             ))
                con.commit()
                con.close()
                messagebox.showinfo("Successfully", "data updated successfully")
                self.clear_field()
                self.clear_table()
    def delete_data(self):
        if (self.student_name.get() == "" or self.student_roll.get() == "" or self.student_class.get() == "" or self.student_sec.get() == "" or self.student_gender.get() == "" or self.student_cont.get() == "" or self.student_dob.get() == "" or self.student_parents.get() == "" or self.student_pcont.get() == "" or self.student_adhar.get() == "" or self.address_text.get(1.0, END) == ""):
            messagebox.showerror("Error", "all field are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="studentmangement")
            cur=con.cursor()
            cur.execute("delete from student_data where adhar=%s",self.student_adhar.get())
            con.commit()
            con.close()
            messagebox.showinfo("Successfully", "data deleted successfully")
            self.clear_field()
            self.clear_table()
    #-----------------------------------data managed-----------------------------------#

    #-----------------------------------clear data from different field------------------------------#
    def clear_field(self):
        self.student_name.set("")
        self.student_roll.set("")
        self.student_class.set("")
        self.student_sec.set("")
        self.student_gender.set("")
        self.student_cont.set("")
        self.student_dob.set("")
        self.student_parents.set("")
        self.student_pcont.set("")
        self.student_adhar.set("")
        self.address_text.delete(1.0,END)
    def clear_search_field(self):
        self.student_search_class.set("")
        self.student_search_roll.set("")
        self.student_search_sec.set("")
        self.student_search_name.set("")
    def clear_table(self):
        for i in self.student_table.get_children():
            self.student_table.delete(i)
    # -----------------------------------clear data from different field------------------------------#


root=Tk()
ob=student(root)
root.config(bg="slateblue")
root.mainloop()