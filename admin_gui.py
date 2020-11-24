import tkinter as tk
from admin_interactions import search_results
from tkinter import messagebox
from register import register_admin,register_op,register_tollstation

root = tk.Tk()
root.title("Administrator")
tk.Button(root,text = "Logout" , command = root.quit,anchor = tk.E).grid(row = 1 , column = 1, sticky = tk.E, padx = 5 , pady = 5)

def reg_admin(frame):
    tk.Label(frame,text = "First Name: ").grid(row = 0 , column = 0)
    tk.Label(frame,text = "Last Name: ").grid(row = 1 , column = 0)
    tk.Label(frame,text = "Phone number: ").grid(row = 2 , column = 0)
    tk.Label(frame,text = "Password: ").grid(row = 3 , column = 0)

    fname = tk.Entry(frame ,width = 40)
    fname.grid(row = 0 , column = 1)
    lname = tk.Entry(frame ,width = 40)
    lname.grid(row = 1 , column = 1)
    phno = tk.Entry(frame ,width = 40)
    phno.grid(row = 2 , column = 1)
    password = tk.Entry(frame ,width = 40, show = "*")
    password.grid(row = 3 , column = 1)

    def regbut():
        if fname.get() == "" or lname.get() == "" or phno.get() == "" or password.get() == "":
            messagebox.showerror("Erre","One or more of the input fields are empty.")
            return

        id = 0
        id = register_admin(fname.get(),lname.get(),phno.get(),password.get())
        if(id == 0):
            messagebox.showerror("Error","Registration Unsuccessful")
        else:
            messagebox.showinfo("Success","Registration complete\n new Admin ID = {}".format(id))
        
    tk.Label(frame,text = "").grid(row = 4 , column = 0)
    tk.Button(frame,text = "Register" , command = regbut).grid(row = 5 , column = 0 , columnspan = 2)


def reg_op(frame):
    tk.Label(frame,text = "First Name: ").grid(row = 0 , column = 0)
    tk.Label(frame,text = "Last Name: ").grid(row = 1 , column = 0)
    tk.Label(frame,text = "Phone number: ").grid(row = 2 , column = 0)
    tk.Label(frame,text = "Password: ").grid(row = 3 , column = 0)

    fname = tk.Entry(frame ,width = 40)
    fname.grid(row = 0 , column = 1)
    lname = tk.Entry(frame ,width = 40)
    lname.grid(row = 1 , column = 1)
    phno = tk.Entry(frame ,width = 40)
    phno.grid(row = 2 , column = 1)
    password = tk.Entry(frame ,width = 40, show = "*")
    password.grid(row = 3 , column = 1)

    def regbut():
        if fname.get() == "" or lname.get() == "" or phno.get() == "" or password.get() == "":
            messagebox.showerror("Erre","One or more of the input fields are empty.")
            return

        id = 0
        id = register_op(fname.get(),lname.get(),phno.get(),password.get())
        if(id == 0):
            messagebox.showerror("Error","Registration Unsuccessful")
        else:
            messagebox.showinfo("Success","Registration complete\n new Operator ID = {}".format(id))
        
    tk.Label(frame,text = "").grid(row = 4 , column = 0)
    tk.Button(frame,text = "Register" , command = regbut).grid(row = 5 , column = 0 , columnspan = 2)

    return id

def reg_ts(frame):
    tk.Label(frame,text = "One way cost: ").grid(row = 0 , column = 0)
    tk.Label(frame,text = "Two way cost: ").grid(row = 1 , column = 0)

    owc = tk.Entry(frame ,width = 40)
    owc.grid(row = 0 , column = 1)
    twc = tk.Entry(frame ,width = 40)
    twc.grid(row = 1 , column = 1)

    def regbut():
        if owc.get() == "" or twc.get() == "":
            messagebox.showerror("Erre","One or more of the input fields are empty.")
            return

        id = 0
        id = register_tollstation(owc.get(),twc.get())
        if(id == 0):
            messagebox.showerror("Error","Registration Unsuccessful")
        else:
            messagebox.showinfo("Success","Registration complete\n new Toll ID = {}".format(id))
        
    tk.Label(frame,text = "").grid(row = 4 , column = 0)
    tk.Button(frame,text = "Register" , command = regbut).grid(row = 5 , column = 0 , columnspan = 2)

    return id
        

def admin_gui():
    global root
    admin_frame = tk.LabelFrame(root, padx = 10 , pady = 10)
    admin_frame.grid(row = 0, column = 0, padx = 15 , pady = 15)
    tk.Label(admin_frame, text = "Search parameter: ").grid(row = 0 , column = 0)

    options = [
        "Transaction id",
        "Vehicle No.",
        "Operator ID",
        "Toll ID",
        "Transaction amount",
        ]

    chosen_option = tk.StringVar()
    chosen_option.set(options[0])

    dropdown = tk.OptionMenu(admin_frame,chosen_option,*options)
    dropdown.grid(row = 0 , column = 1)

    input = tk.Entry(admin_frame,width = 40)
    input.grid(row = 0 , column = 2)

    search_results_frame = tk.LabelFrame(admin_frame,padx = 10 , pady = 10)
    search_results_frame.grid(row = 1 , column = 0 , columnspan = 4,sticky = tk.N)
    def srchbtn():
        for labels in search_results_frame.winfo_children():
            labels.destroy()

        entrd_param = input.get()
        if entrd_param == "":
            messagebox.showerror("Error","No search parameter given")
            return False
        
        columns = {        
            "Transaction id":"transaction_id",
            "Vehicle No.":"vehicleno",
            "Operator ID":"op_id",
            "Toll ID":"toll_id",
            "Transaction amount":"amount",
            "Date":"date_time"
            }

        tk.Label(search_results_frame,text = "Transaction ID").grid(row = 1 , column = 0, padx = 5 , pady = 5)
        tk.Label(search_results_frame,text = "Vehicle No.").grid(row = 1 , column = 1 ,padx = 5 , pady = 5)
        tk.Label(search_results_frame,text = "Operator ID").grid(row = 1 , column = 2,padx = 5 , pady = 5)
        tk.Label(search_results_frame,text = "Toll_id").grid(row = 1 , column = 3,padx = 5 , pady = 5)
        tk.Label(search_results_frame,text = "Amount").grid(row = 1 , column = 4,padx = 5 , pady = 5)
        tk.Label(search_results_frame,text = "Date").grid(row = 1 , column = 5,padx = 5 , pady = 5)

        tk.Label(search_results_frame,text = "").grid(row = 2 , column = 0, columnspan = 6)

        results = search_results(columns[chosen_option.get()],entrd_param)
        for row,records in enumerate(results):
            for column,record in enumerate(records):
                tk.Label(search_results_frame,text = record).grid(row = 3 + row , column = column,padx = 5 , pady = 5)
        
        return True

    tk.Button(admin_frame, text = "Search" , command = srchbtn).grid(row = 0 , column = 3)

    def registrations():
        reg_window = tk.Toplevel()
        reg_window.title("Registrations Menu")
        #reg_window.geometry("200x200")
        tk.Label(reg_window,text = "Registration type: ").grid(row = 0 , column = 0)
        reg_type = tk.IntVar()
        reg_type.set(-1)
        tk.Radiobutton(reg_window,text = "Administrator", variable = reg_type, value = 0).grid(row = 1 , column = 0)
        tk.Radiobutton(reg_window,text = "Operator", variable = reg_type, value = 1).grid(row = 2 , column = 0)
        tk.Radiobutton(reg_window,text = "Toll Station", variable = reg_type, value = 2).grid(row = 3 , column = 0)

        data_entry_frame = tk.LabelFrame(reg_window, padx = 10 , pady = 10)
        data_entry_frame.grid(row = 4 ,column = 0 , columnspan = 3)

        def dataentry():
            if reg_type.get() == -1:
                messagebox.showerror("Error","Please choose a registration type")
                return False

            for labels in data_entry_frame.winfo_children():
                labels.destroy()

            chosen_reg_type = reg_type.get()
            if chosen_reg_type == 0:
                reg_admin(data_entry_frame)

            elif chosen_reg_type == 1:
                reg_op(data_entry_frame)
                
            elif chosen_reg_type == 2:
                reg_ts(data_entry_frame)
                
            else:
                messagebox.showerror("Error","Not valid registration type")
            


        enter_data_button= tk.Button(reg_window,text = "Enter Data", command = dataentry)
        enter_data_button.grid(row = 2 , column = 2)

    tk.Button(root, text = "Registrations" , command = registrations).grid(row = 1 , column = 0)

admin_gui()
tk.mainloop()