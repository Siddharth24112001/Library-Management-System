from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1550x956+0+0')

        # Variables
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()


        lbltitle = Label(self.root, text='LIBRARY MANAGEMENT SYSTEM', bg= 'powder blue', fg='green', bd=20, relief= RIDGE, font= ("times new roman", 50, 'bold'), padx = 2, pady = 6)
        lbltitle.pack(side= TOP, fill= X)

        frame = Frame(self.root, bd=12, relief= RIDGE, padx = 20, bg = "powder blue")
        frame.place(x=0, y=130, width= 1530, height= 400)
        
        # DataFrameLeft
        DataFrameLeft = LabelFrame(frame, text='Library Member Info', bg= 'powder blue', fg='green', bd=12, relief= RIDGE, font= ("times new roman", 12, 'bold'), padx = 2, pady = 6)
        DataFrameLeft.place(x=0, y=5, width= 900, height= 350)

        lblMember = Label(DataFrameLeft, bg= "powder blue" , text= "Member Type", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblMember.grid(row= 0, column= 0, sticky= W)

        comMember = ttk.Combobox(DataFrameLeft, font= ("times new roman", 15, "bold"), width= 27, textvariable=self.member_var,  state= "readonly")
        comMember['value'] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column= 1)

        lblPRN_No = Label(DataFrameLeft, bg= "powder blue" ,text= "PRN No.", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblPRN_No.grid(row= 1, column= 0, sticky= W)
        txtPRN_No = Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.prn_var)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg= "powder blue" ,text= "ID No.", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblTitle.grid(row= 2, column= 0, sticky= W)
        txtTitle = Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.id_var)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg= "powder blue" ,text= "First Name", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblFirstName.grid(row= 3, column= 0, sticky= W)
        txtFirstName= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.firstname_var)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg= "powder blue" ,text= "Last Name", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblLastName.grid(row= 4, column= 0, sticky= W)
        txtLastName= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.lastname_var)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg= "powder blue" ,text= "Address 1", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblAddress1.grid(row= 5, column= 0, sticky= W)
        txtAddress1= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.address1_var)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg= "powder blue" ,text= "Address 2", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblAddress2.grid(row= 6, column= 0, sticky= W)
        txtAddress2= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.address2_var)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg= "powder blue" ,text= "Post Code", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblPostCode.grid(row= 7, column= 0, sticky= W)
        txtPostCode= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.postcode_var)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg= "powder blue" ,text= "Mobile", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblMobile.grid(row= 8, column= 0, sticky= W)
        txtMobile= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.mobile_var)
        txtMobile.grid(row=8, column=1)

        lblBookID= Label(DataFrameLeft, bg= "powder blue" ,text= "Book ID", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblBookID.grid(row= 0, column= 2, sticky= W)
        txtBookID= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.bookid_var)
        txtBookID.grid(row=0, column=3)

        lblBookTitle= Label(DataFrameLeft, bg= "powder blue" ,text= "Book ID", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblBookTitle.grid(row= 1, column= 2, sticky= W)
        txtBookTitle= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.booktitle_var)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor= Label(DataFrameLeft, bg= "powder blue" ,text= "Author", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblAuthor.grid(row= 2, column= 2, sticky= W)
        txtAuthor= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.author_var)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed= Label(DataFrameLeft, bg= "powder blue" ,text= "Date Borrowed", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDateBorrowed.grid(row= 3, column= 2, sticky= W)
        txtDateBorrowed= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3, column=3, sticky = W)

        lblDateDue= Label(DataFrameLeft, bg= "powder blue" ,text= "Date Due", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDateDue.grid(row= 4, column= 2, sticky= W)
        txtDateDue= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.datedue_var)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook= Label(DataFrameLeft, bg= "powder blue" ,text= "Days on Book", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDaysOnBook.grid(row= 5, column= 2, sticky= W)
        txtDaysOnBook= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.daysonbook_var)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFee= Label(DataFrameLeft, bg= "powder blue" ,text= "Late Return Fee", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblLateReturnFee.grid(row= 6, column= 2, sticky= W)
        txtLateReturnFee= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.latereturnfine_var)
        txtLateReturnFee.grid(row=6, column=3)

        lblDateOverDue= Label(DataFrameLeft, bg= "powder blue" ,text= "Date Over Due", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDateOverDue.grid(row= 7, column= 2, sticky= W)
        txtDateOverDue= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice= Label(DataFrameLeft, bg= "powder blue" ,text= "Actual Price", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblActualPrice.grid(row= 8, column= 2, sticky= W)
        txtActualPrice= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29, textvariable=self.finalprice_var)
        txtActualPrice.grid(row=8, column=3)
        

        # DataFrame Right
        DataFrameRight = LabelFrame(frame, text='Book Details', bg= 'powder blue', fg='green', bd=12, relief= RIDGE, font= ("times new roman", 12, 'bold'), padx = 2, pady = 6)
        DataFrameRight.place(x=910, y=5, width= 540, height= 350)

        self.txtBox = Text(DataFrameRight, font=("times new roman", 12, "bold"), width= 32, height = 16, padx = 2, pady = 6 )
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky= "ns")

        listBooks = ["Introduction to Algorithms","Artificial Intelligence: A Modern Approach",
    "Operating System Concepts","Computer Networks","Database System Concepts","Machine Learning",
    "Clean Code","Design Patterns","The Pragmatic Programmer","Head First Design Patterns",
    "Data Structures and Algorithms in Python","Cracking the Coding Interview","Python for Data Analysis",
    "The C Programming Language","Discrete Mathematics and Its Applications","Modern Operating Systems",
    "Programming in Haskell","Deep Learning with Python","Compilers: Principles, Techniques, and Tools",
    "Introduction to the Theory of Computation","Introduction to Linear Algebra",
    "Digital Design and Computer Architecture","Elements of the Theory of Computation","Engineering Mechanics: Dynamics",
    "Calculus: Early Transcendentals","Essentials of Statistics","Fundamentals of Thermodynamics",
    "Thermodynamics: An Engineering Approach","Physics for Scientists and Engineers",
    "Fundamentals of Fluid Mechanics","Introduction to Electrodynamics","Linear Algebra and Its Applications","Organic Chemistry",
    "Molecular Biology of the Cell","Biochemistry","Anatomy and Physiology","Cell and Molecular Biology",
    "Human Anatomy","Fundamentals of Human Resource Management","Organizational Behavior",
    "Principles of Marketing","Essentials of Economics","Business Law","Corporate Finance","Fundamentals of Corporate Finance",
    "Managerial Accounting","Macroeconomics","Microeconomics","International Business","Strategic Management",
    "Principles of Accounting","Principles of Microeconomics","Principles of Macroeconomics","Essentials of Investments",
    "Econometrics","Project Management: A Systems Approach","Operations Management","Entrepreneurship: Theory and Practice",
    "Information Systems Management","Quantitative Methods for Business","Financial Management: Theory and Practice","Principles of Risk Management and Insurance",
    "Statistics for Business and Economics","Operations Research: An Introduction","Introduction to Probability Models",
    "Mathematical Statistics with Applications","Real Analysis","Topology","Abstract Algebra",
    "Complex Analysis","Introduction to Graph Theory","Numerical Analysis","Quantum Mechanics: Concepts and Applications",
    "Introduction to Quantum Mechanics","Statistical Mechanics","Classical Mechanics","Mechanics of Materials",
    "Engineering Electromagnetics","Introduction to Robotics","Control Systems Engineering","Signals and Systems",
    "Digital Signal Processing","Artificial Neural Networks","Foundations of Machine Learning","Computer Vision: Algorithms and Applications",
    "Pattern Recognition and Machine Learning","Natural Language Processing with Python",
    "The Art of Computer Programming","Data Mining: Concepts and Techniques","Introduction to Statistical Learning",
    "Blockchain Basics","Financial Accounting","Corporate Governance","International Finance",
    "Game Theory","Economics of Strategy","Business Statistics","Principles of Econometrics","Strategic Marketing",
    "Consumer Behavior","Global Marketing Management"
]
        def SelectBook(event= ""):
            value = str(listbox.get(listbox.curselection()))
            x = value
            if x=="Introduction to Algorithms":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Algorithms")
                self.author_var.set("Thomas Cormen")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("$10")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("$70")

        listbox = Listbox(DataFrameRight, font= ("arial", 12, "bold"), width= 20, height= 16)
        listbox.bind("<<ListboxSelect>>", SelectBook)
        listbox.grid(row=0, column=0, padx = 4)
        listScrollbar.config(command= listbox.yview)

        for item in listBooks:
            listbox.insert(END, item)
        # Frame for buttons
        FrameButton = Frame(self.root, bd=12, relief= RIDGE, padx = 20, bg = "powder blue")
        FrameButton.place(x=0, y=530, width= 1530, height= 70)
        
        btnAddData = Button(FrameButton,command= self.add_data, text= "Add Data", font= ("times new roman", 12, "bold"), width= 23, bg = "blue", fg= "black")
        btnAddData.grid(row = 0, column= 0)

        btnAddData = Button(FrameButton, command= self.showData,  text= "Show Data", font= ("times new roman", 12, "bold"), width= 23, bg = "blue", fg= "black")
        btnAddData.grid(row = 0, column= 1)
        
        btnAddData = Button(FrameButton, command= self.update, text= "Update", font= ("times new roman", 12, "bold"), width= 23, bg = "blue", fg= "black")
        btnAddData.grid(row = 0, column= 2)

        btnAddData = Button(FrameButton, command=self.delete,  text= "Delete", font= ("times new roman", 12, "bold"), width= 23, bg = "blue", fg= "black")
        btnAddData.grid(row = 0, column= 3)

        btnAddData = Button(FrameButton, command=self.reset, text= "Reset", font= ("times new roman", 12, "bold"), width= 23, bg = "blue", fg= "black")
        btnAddData.grid(row = 0, column= 4)

        btnAddData = Button(FrameButton,command=self.iExit,  text= "Exit", font= ("times new roman", 12, "bold"), width= 23, bg = "blue", fg= "black")
        btnAddData.grid(row = 0, column= 5)


        # Information Frame
        # Frame for buttons
        FrameDetails = Frame(self.root, bd=12, relief= RIDGE, padx = 20, bg = "powder blue")
        FrameDetails.place(x=0, y=600, width= 1530, height= 195)

        tableFrame = Frame(FrameDetails, bd=6, relief= RIDGE, bg = "powder blue")
        tableFrame.place(x=0, y=2, width= 1460, height= 180)

        xscroll = ttk.Scrollbar(tableFrame, orient= HORIZONTAL)
        yscroll = ttk.Scrollbar(tableFrame, orient= VERTICAL)
        
        self.library_table = ttk.Treeview(tableFrame, columns  = ("Member Type", "PRN No.", "Title","First Name", "Last Name", "Address 1", "Address 2",
        "Post ID", "Mobile", "Book ID", "Book Title", "Author", "Date Borrowed", "Date Due", "Days", "Late Return Fine", "Date Over Due" , "Final Price")
        , xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side= BOTTOM, fill=X)
        yscroll.pack(side= RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("Member Type", text = "Member Type")
        self.library_table.heading("PRN No.", text = "PRN No.")
        self.library_table.heading("Title", text = "Title")
        self.library_table.heading("First Name", text = "First Name")
        self.library_table.heading("Last Name", text = "Last Name")
        self.library_table.heading("Address 1", text = "Address1")
        self.library_table.heading("Address 2", text = "Address2")
        self.library_table.heading("Post ID", text = "Post ID")
        self.library_table.heading("Mobile", text = "Mobile")
        self.library_table.heading("Book ID", text = "Book ID")
        self.library_table.heading("Book Title", text = "Book Title")
        self.library_table.heading("Author", text = "Author")
        self.library_table.heading("Date Borrowed", text = "Date of Borrow")
        self.library_table.heading("Date Due", text = "Date Due")
        self.library_table.heading("Days", text = "Days on Book")
        self.library_table.heading("Late Return Fine", text = "Late Return Fine")
        self.library_table.heading("Date Over Due", text = "Date Over Due")
        self.library_table.heading("Final Price", text = "Final Price")

        self.library_table["show"]= "headings"
        self.library_table.pack(fill= BOTH, expand=1)

        self.library_table.column("Member Type", width = 100)
        self.library_table.column("PRN No.", width = 100)
        self.library_table.column("Title", width = 100)
        self.library_table.column("First Name", width = 100)
        self.library_table.column("Last Name", width = 100)
        self.library_table.column("Address 1", width = 100)
        self.library_table.column("Address 2", width = 100)
        self.library_table.column("Post ID", width = 100)
        self.library_table.column("Mobile", width = 100)
        self.library_table.column("Book ID", width = 100)
        self.library_table.column("Book Title", width = 100)
        self.library_table.column("Author", width = 100)
        self.library_table.column("Date Borrowed", width = 100)
        self.library_table.column("Date Due", width = 100)
        self.library_table.column("Days", width = 100)
        self.library_table.column("Late Return Fine", width = 100)
        self.library_table.column("Date Over Due", width = 100)
        self.library_table.column("Final Price", width = 100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "PARCIVAL@24", database= "Library Management System")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into LIBRARY values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
        self.member_var.get(),
        self.prn_var.get(),
        self.id_var.get(),
        self.firstname_var.get(),
        self.lastname_var.get(),
        self.address1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.author_var.get(),
        self.dateborrowed_var.get(),
        self.datedue_var.get(),
        self.daysonbook_var.get(),
        self.latereturnfine_var.get(),
        self.dateoverdue_var.get(),
        self.finalprice_var.get()
        ))
        
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Success", "Member has been inserted successfully")
    
    def update(self):
        
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="PARCIVAL@24",
                database="Library Management System"
            )
            my_cursor = conn.cursor()

            
            my_cursor.execute("""
                UPDATE LIBRARY 
                SET Member=%s, `PRNNO.`=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostID=%s, Mobile=%s, BookID=%s, BookTitle=%s, Author=%s, DateBorrowed=%s, DateDue=%s, DaysonBook=%s, LateReturnFee=%s, DateOverDue=%s, FinalPrice=%s 
                WHERE `PRNNO.`=%s
            """, (
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.latereturnfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get(),
                self.prn_var.get()  # This identifies the row to update
            ))

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been updated")

       


    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "PARCIVAL@24", database= "Library Management System")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0: 
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event= ""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    


    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No.:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No.:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No.\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date Due:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days on Book:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late return fine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Date over due:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"Final Price:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)
    
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit ?")
        if iExit > 0: 
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "Select a member to delete")
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "PARCIVAL@24", database= "Library Management System")
            my_cursor = conn.cursor()
            query = "delete from library where `PRNNO.`=%s"
            value  = (self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted")






    



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()