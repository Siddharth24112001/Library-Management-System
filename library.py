from tkinter import *
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1550x956+0+0')

        lbltitle = Label(self.root, text='LIBRARY MANAGEMENT SYSTEM', bg= 'powder blue', fg='green', bd=20, relief= RIDGE, font= ("times new roman", 50, 'bold'), padx = 2, pady = 6)
        lbltitle.pack(side= TOP, fill= X)

        frame = Frame(self.root, bd=12, relief= RIDGE, padx = 20, bg = "powder blue")
        frame.place(x=0, y=130, width= 1530, height= 400)
        
        # DataFrameLeft
        DataFrameLeft = LabelFrame(frame, text='Library Member Info', bg= 'powder blue', fg='green', bd=12, relief= RIDGE, font= ("times new roman", 12, 'bold'), padx = 2, pady = 6)
        DataFrameLeft.place(x=0, y=5, width= 900, height= 350)

        lblMember = Label(DataFrameLeft, bg= "powder blue" ,text= "Member Type", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblMember.grid(row= 0, column= 0, sticky= W)

        comMember = ttk.Combobox(DataFrameLeft, font= ("times new roman", 15, "bold"), width= 27, state= "readonly")
        comMember['value'] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column= 1)

        lblPRN_No = Label(DataFrameLeft, bg= "powder blue" ,text= "PRN No.", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblPRN_No.grid(row= 1, column= 0, sticky= W)
        txtPRN_No = Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg= "powder blue" ,text= "ID No.", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblTitle.grid(row= 2, column= 0, sticky= W)
        txtTitle = Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg= "powder blue" ,text= "First Name", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblFirstName.grid(row= 3, column= 0, sticky= W)
        txtFirstName= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg= "powder blue" ,text= "Last Name", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblLastName.grid(row= 4, column= 0, sticky= W)
        txtLastName= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg= "powder blue" ,text= "Address 1", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblAddress1.grid(row= 5, column= 0, sticky= W)
        txtAddress1= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg= "powder blue" ,text= "Address 2", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblAddress2.grid(row= 6, column= 0, sticky= W)
        txtAddress2= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg= "powder blue" ,text= "Post Code", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblPostCode.grid(row= 7, column= 0, sticky= W)
        txtPostCode= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg= "powder blue" ,text= "Mobile", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblMobile.grid(row= 8, column= 0, sticky= W)
        txtMobile= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtMobile.grid(row=8, column=1)

        lblBookID= Label(DataFrameLeft, bg= "powder blue" ,text= "Book ID", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblBookID.grid(row= 0, column= 2, sticky= W)
        txtBookID= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtBookID.grid(row=0, column=3)

        lblBookTitle= Label(DataFrameLeft, bg= "powder blue" ,text= "Book ID", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblBookTitle.grid(row= 1, column= 2, sticky= W)
        txtBookTitle= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor= Label(DataFrameLeft, bg= "powder blue" ,text= "Author", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblAuthor.grid(row= 2, column= 2, sticky= W)
        txtAuthor= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed= Label(DataFrameLeft, bg= "powder blue" ,text= "Date Borrowed", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDateBorrowed.grid(row= 3, column= 2, sticky= W)
        txtDateBorrowed= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtDateBorrowed.grid(row=3, column=3, sticky = W)

        lblDateDue= Label(DataFrameLeft, bg= "powder blue" ,text= "Date Due", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDateDue.grid(row= 4, column= 2, sticky= W)
        txtDateDue= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook= Label(DataFrameLeft, bg= "powder blue" ,text= "Days on Book", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDaysOnBook.grid(row= 5, column= 2, sticky= W)
        txtDaysOnBook= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFee= Label(DataFrameLeft, bg= "powder blue" ,text= "Late Return Fee", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblLateReturnFee.grid(row= 6, column= 2, sticky= W)
        txtLateReturnFee= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtLateReturnFee.grid(row=6, column=3)

        lblDateOverDue= Label(DataFrameLeft, bg= "powder blue" ,text= "Date Over Due", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblDateOverDue.grid(row= 7, column= 2, sticky= W)
        txtDateOverDue= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice= Label(DataFrameLeft, bg= "powder blue" ,text= "Actual Price", font= ("times new roman", 15, "bold"), padx = 2, pady= 6)
        lblActualPrice.grid(row= 8, column= 2, sticky= W)
        txtActualPrice= Entry(DataFrameLeft, font= ("times new roman", 15, "bold"),  width= 29)
        txtActualPrice.grid(row=8, column=3)
        

        DataFrameRight = LabelFrame(frame, text='Book Details', bg= 'powder blue', fg='green', bd=12, relief= RIDGE, font= ("times new roman", 12, 'bold'), padx = 2, pady = 6)
        DataFrameRight.place(x=910, y=5, width= 540, height= 350)

        # Frame for buttons
        FrameButton = Frame(self.root, bd=12, relief= RIDGE, padx = 20, bg = "powder blue")
        FrameButton.place(x=0, y=530, width= 1530, height= 70)

        # Information Frame
        # Frame for buttons
        FrameDetails = Frame(self.root, bd=12, relief= RIDGE, padx = 20, bg = "powder blue")
        FrameDetails.place(x=0, y=600, width= 1530, height= 195)

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()