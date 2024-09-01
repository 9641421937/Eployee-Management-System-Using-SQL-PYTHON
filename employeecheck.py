from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_marrital = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idtype = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        # Title
        lbl_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1530, height=50)

        # Logo
        img_logo = Image.open('College_images/emp_logo.jpg')
        img_logo = img_logo.resize((55, 55))
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=270, y=0, width=50, height=50)

        # Image frame
        img_frame = Frame(self.root, border=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1530, height=160)

        # 1st image
        img1 = Image.open('College_images/first_image.jpeg')
        img1 = img1.resize((540, 160))
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(self.root, image=self.photo1)
        self.img_1.place(x=0, y=50, width=540, height=160)

        # 2nd image
        img2 = Image.open('College_images/second_images.png')
        img2 = img2.resize((540, 160))
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(self.root, image=self.photo2)
        self.img_2.place(x=460, y=50, width=540, height=160)

        # 3rd image
        img3 = Image.open('College_images/third_images.jpeg')
        img3 = img3.resize((540, 160))
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(self.root, image=self.photo3)
        self.img_3.place(x=1000, y=50, width=540, height=160)

        # Main Frame
        Main_frame = Frame(self.root, border=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=220, width=1500, height=560)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, border=2, relief=RIDGE, bg='white', text='Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Label and Entry Fields
        # Department
        lbl_dep = Label(upper_frame, text='Department', font=('arial', 12, 'bold'), fg='black', bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('arial', 12, 'bold'), width=21, state='readonly')
        combo_dep['value'] = ['Select Department', 'HR', 'Software Engineer', 'Manager']
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Name
        lbl_Name = Label(upper_frame, text="Name:", font=('arial', 12, 'bold'), bg='white')
        lbl_Name.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=('arial', 12, 'bold'))
        txt_name.grid(row=0, column=3, padx=2, pady=7)

        # Designation
        lbl_Designation = Label(upper_frame, text="Designation:", font=('arial', 12, 'bold'), bg='white')
        lbl_Designation.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_Designation = ttk.Entry(upper_frame, textvariable=self.var_designation, width=22, font=('arial', 12, 'bold'))
        txt_Designation.grid(row=1, column=1, padx=2, pady=7)

        # Email
        lbl_Email = Label(upper_frame, text="Email:", font=('arial', 12, 'bold'), bg='white')
        lbl_Email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_Email = ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=('arial', 12, 'bold'))
        txt_Email.grid(row=1, column=3, padx=2, pady=7)

        # Address
        lbl_Address = Label(upper_frame, text="Address:", font=('arial', 12, 'bold'), bg='white')
        lbl_Address.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_Address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=('arial', 12, 'bold'))
        txt_Address.grid(row=2, column=1, padx=2, pady=7)

        # Marital Status
        lbl_MarritaStatus = Label(upper_frame, text='Marital Status:', font=('arial', 12, 'bold'), fg='black', bg='white')
        lbl_MarritaStatus.grid(row=2, column=2, padx=2, sticky=W)

        combo_MarritaStatus = ttk.Combobox(upper_frame, textvariable=self.var_marrital, font=('arial', 11, 'bold'), width=23, state='readonly')
        combo_MarritaStatus['value'] = ['Select', 'Married', 'Unmarried']
        combo_MarritaStatus.current(0)
        combo_MarritaStatus.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # DOB
        lbl_DOB = Label(upper_frame, text="DOB:", font=('arial', 12, 'bold'), bg='white')
        lbl_DOB.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_DOB = ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=('arial', 12, 'bold'))
        txt_DOB.grid(row=3, column=1, padx=2, pady=7)

        # DOJ
        lbl_DOJ = Label(upper_frame, text="DOJ:", font=('arial', 12, 'bold'), bg='white')
        lbl_DOJ.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_DOJ = ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=('arial', 12, 'bold'))
        txt_DOJ.grid(row=3, column=3, padx=2, pady=7)

        # ID
        combo_id = ttk.Combobox(upper_frame, textvariable=self.var_idtype, font=('arial', 11, 'bold'), width=17, state='readonly')
        combo_id['value'] = ['AADHAR CARD', 'VOTER CARD', 'PAN CARD']
        combo_id.current(0)
        combo_id.grid(row=4, column=0, padx=2, pady=10, sticky=W)

        # ID no.
        txt_id = ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22, font=('arial', 12, 'bold'))
        txt_id.grid(row=4, column=1, padx=2, pady=7)

        # Gender
        lbl_Gender = Label(upper_frame, text='Gender:', font=('arial', 12, 'bold'), fg='black', bg='white')
        lbl_Gender.grid(row=4, column=2, padx=2, sticky=W)

        combo_Gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('arial', 11, 'bold'), width=23, state='readonly')
        combo_Gender['value'] = ['Select', 'Male', 'Female']
        combo_Gender.current(0)
        combo_Gender.grid(row=4, column=3, padx=2, pady=10, sticky=W)

        # Phone Number
        lbl_Mobile = Label(upper_frame, text="Mobile No:", font=('arial', 12, 'bold'), bg='white')
        lbl_Mobile.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_Mobile = ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=('arial', 12, 'bold'))
        txt_Mobile.grid(row=0, column=5, padx=2, pady=7)

        # Country
        lbl_Country = Label(upper_frame, text="Country:", font=('arial', 12, 'bold'), bg='white')
        lbl_Country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_Country = ttk.Entry(upper_frame, textvariable=self.var_country, width=22, font=('arial', 12, 'bold'))
        txt_Country.grid(row=1, column=5, padx=2, pady=7)

        # Salary
        lbl_Salary = Label(upper_frame, text="Salary:", font=('arial', 12, 'bold'), bg='white')
        lbl_Salary.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_Salary = ttk.Entry(upper_frame, textvariable=self.var_salary, width=22, font=('arial', 12, 'bold'))
        txt_Salary.grid(row=2, column=5, padx=2, pady=7)

        # Buttons Frame
        button_frame = Frame(upper_frame, border=2, relief=RIDGE, bg='white')
        button_frame.place(x=1290, y=0, width=170, height=270)

        btn_add = Button(button_frame, text='Save', command=self.add_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update = Button(button_frame, text='Update', command=self.update_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text='Delete', command=self.delete_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(button_frame, text='Clear', command=self.clear_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_clear.grid(row=3, column=0, padx=1, pady=5)

        # Down Frame
        down_frame = LabelFrame(Main_frame, border=2, relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)

        # Search Frame
        search_frame = LabelFrame(down_frame, border=2, relief=RIDGE, bg='white', text='Search Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, text='Search By:', font=('arial', 12, 'bold'), fg='black', bg='white')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_com_search = StringVar()
        combo_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=('arial', 11, 'bold'), width=18, state='readonly')
        combo_txt_search['value'] = ['Select Option', 'Phone', 'IDProof']
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=('arial', 12, 'bold'))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, text='Search', command=self.search_data, font=('arial', 11, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=5)

        btn_ShowAll = Button(search_frame, text='Show All', command=self.fetch_data, font=('arial', 11, 'bold'), width=14, bg='blue', fg='white')
        btn_ShowAll.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = Frame(down_frame, border=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=('dep', 'name', 'degi', 'email', 'address', 'marrital', 'dob', 'doj', 'idtype','idproof', 'gender', 'phone', 'country', 'salary'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('degi', text='Designation')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('marrital', text='Marrital Status')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idtype', text='ID_type')
        self.employee_table.heading('idproof', text='ID Proof')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary')

        self.employee_table['show'] = 'headings'

        self.employee_table.column('dep', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('degi', width=100)
        self.employee_table.column('email', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('marrital', width=100)
        self.employee_table.column('dob', width=100)
        self.employee_table.column('doj', width=100)
        self.employee_table.column('idtype', width=100)
        self.employee_table.column('idproof', width=100)
        self.employee_table.column('gender', width=100)
        self.employee_table.column('phone', width=100)
        self.employee_table.column('country', width=100)
        self.employee_table.column('salary', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()

    # Add Data
    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="project_database")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into proj_employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s)", (
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_marrital.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idtype.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee has been added!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="project_database")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from proj_employee1")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_marrital.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idtype.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    # Update Data
    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                Update = messagebox.askyesno("Update", "Are you sure you want to update this employee's data?")
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="project_database")
                    my_cursor = conn.cursor()
                    my_cursor.execute('update proj_employee1 set Deperetment=%s ,Name=%s , Designation =%s ,Email=%s,Address=%s ,Marrid_Status=%s, DOB=%s ,DOJ=%s ,ID_type=%s ,Gender=%s,Phone=%s ,Country=%s ,Salary=%s  where ID_proof=%s', (
                        self.var_dep.get(),
                        self.var_name.get(),
                        self.var_designation.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_marrital.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_idtype.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_country.get(),
                        self.var_salary.get(),
                        self.var_idproof.get()
                    ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee data has been updated!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    # Delete Data
    def delete_data(self):
        if self.var_idproof.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                delete = messagebox.askyesno("Delete", "Are you sure you want to delete this employee?")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="project_database")
                    my_cursor = conn.cursor()
                    sql = "delete from proj_employee1 where ID_Proof=%s"
                    value = (self.var_idproof.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee has been deleted!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    # Clear Data
    def clear_data(self):
        self.var_dep.set("")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_marrital.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idtype.set("")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    # Search Data
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select an option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="project_database")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from proj_employee1 where " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
