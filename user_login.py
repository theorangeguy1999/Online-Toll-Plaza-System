import tkinter as tk
from tkinter import messagebox
from login import customer_login
from register import register_customer
from user_gui import cust_gui

def userlogin(root):

    for labels in root.winfo_children():
        labels.destroy()

    root.title("Login")
    login_frame = tk.LabelFrame(root,padx = 10 , pady = 10)
    login_frame .grid(row = 0 , column = 0 , padx = 15 , pady = 15)

    tk.Button(root,text = "Exit" , command = root.quit, relief = tk.SUNKEN, anchor = tk.E).grid(row = 1 , column = 0, padx = 2 , pady = 2, sticky = tk.E)

    tk.Label(login_frame, text = "Vehicle Registration Number: ").grid(row = 0 , column = 0)
    tk.Label(login_frame,text = "Password: ").grid(row = 1, column = 0)
    vno = tk.Entry(login_frame, width = 40)
    vno.grid(row = 0 , column  = 1)
    password = tk.Entry(login_frame,width = 40,show = "*")
    password.grid(row = 1 , column = 1)

    def login_btn():
        if(vno.get() == "" or password.get() == ""):
            messagebox.showerror("Error","One or more of the input fields are empty")
            return
        
        vehicleno =  vno.get()
        pd = password.get()

        if(customer_login(vehicleno,pd)):
            messagebox.showinfo("SUCCESS","Login successful")
            cust_gui(vehicleno,root)

        else:
            messagebox.showerror("Failure","Login Failed")
        
    tk.Button(login_frame,text = "Login" , command = login_btn).grid(row = 2 , column = 0 , columnspan = 2 , padx = 10 , pady = 10)

    tk.Label(login_frame).grid(row = 3 , column = 0)
    
    def register_btn():
        reg_window = tk.Toplevel()
        reg_window.title("Registration")

        tk.Label(reg_window , text = "Enter details below").grid(row = 0 , column = 0, columnspan = 2)
        tk.Label(reg_window , text = "Vehicle Reg. No.").grid(row = 1 , column = 0, padx = 5 , pady = 5)
        tk.Label(reg_window , text = "First Name").grid(row = 2 , column = 0, padx = 5 , pady = 5)
        tk.Label(reg_window , text = "Last Name").grid(row = 3 , column = 0, padx = 5 , pady = 5)
        tk.Label(reg_window , text = "Phone no.").grid(row = 4 , column = 0, padx = 5 , pady = 5)
        tk.Label(reg_window , text = "Password").grid(row = 5 , column = 0, padx = 5 , pady = 5)

        vno_button = tk.Entry(reg_window,width = 40)
        vno_button.grid(row = 1 , column = 1, padx = 5 , pady = 5)
        fname_button = tk.Entry(reg_window,width = 40)
        fname_button.grid(row = 2 , column = 1, padx = 5 , pady = 5)
        lname_button = tk.Entry(reg_window,width = 40)
        lname_button.grid(row = 3 , column = 1, padx = 5 , pady = 5)
        phno_button = tk.Entry(reg_window,width = 40)
        phno_button.grid(row = 4 , column = 1, padx = 5 , pady = 5)
        password_button = tk.Entry(reg_window,width = 40,show = "*")
        password_button.grid(row = 5 , column = 1, padx = 5 , pady = 5)

        def reg_btn():
            vno =vno_button.get()
            fname = fname_button.get()
            lname = lname_button.get()
            phno = phno_button.get()
            password = password_button.get()

            if (vno == "" or fname == "" or lname == "" or phno == "" or password == ""):
                messagebox.showerror("Error", " One or more input fields were left empty")
                return
            
            success = register_customer(vno,fname,lname,phno,password)

            if not success:
                messagebox.showerror("Error","Account already exists for this Vehicle")
                return
            
            messagebox.showinfo("Success","Registration successful \n Log in now using registered credentials")
            reg_window.destroy()
            return
            

        
        tk.Label(reg_window).grid(row = 6 , column = 0)
        tk.Label(reg_window).grid(row = 6 , column = 2)
        tk.Button(reg_window,text = "Register", command = reg_btn).grid(row = 7 , column = 0 , columnspan = 2 , padx = 10 , pady = 10)
    
    tk.Button(login_frame, text = "Register new vehicle",command = register_btn, padx = 5 , pady = 5).grid(row = 4 , column = 0 , columnspan = 2, padx = 10 , pady = 10)


if __name__ == "__main__":
    userlogin(tk.Tk())
    tk.mainloop()