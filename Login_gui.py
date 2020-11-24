import tkinter as tk
from tkinter import messagebox
from login import admin_login,op_login

root = tk.Tk()
root.title("Toll Plaza")

login_frame = tk.LabelFrame(root, padx = 10 , pady = 10)
login_frame.grid(row = 0 , column = 0, padx = 15 , pady = 15)

role = tk.IntVar()
role.set(-1)
tk.Radiobutton(login_frame,text = "Operator", variable = role , value = 0).grid(row = 0 , column = 0)
tk.Radiobutton(login_frame,text = "Administrator", variable = role , value = 1).grid(row = 1 , column = 0)

tk.Label(login_frame,text = "User ID").grid(row = 0 , column = 1)
id = tk.Entry(login_frame,width = 40)
id.grid(row = 0 , column = 2)

tk.Label(login_frame,text = "Password").grid(row = 1 , column = 1)
password = tk.Entry(login_frame,width = 40,show = "*")
password.grid(row = 1 , column = 2)

def button_press():
    if (role.get() == -1):
        messagebox.showerror("ERROR", "You haven't selected a role")
        return
    
    #tk.Label(root,text = "first hurdle crossed").grid()
    #print(type(id.get()))
    entrd_id = id.get()
    entrd_password = password.get()

    if(entrd_id == "" or entrd_password == ""):
        messagebox.showerror("Error","One or more input fields were left empty")
        return

    if role.get() == 0:
        if(op_login(entrd_id,entrd_password)):
            messagebox.showinfo("Login succesful","Login Successfull")
        else:
            messagebox.showerror("Login failed", "incorrect id password combination")
    elif role.get() == 1:
        if(admin_login(entrd_id,entrd_password)):
            messagebox.showinfo("Login succesful","Login Successfull")
        else:
            messagebox.showerror("Login failed", "incorrect id password combination")
    else:
        messagebox.showwarning("EHHHH", "Invalid role")

tk.Button(login_frame, text = "Login", command = button_press).grid(row = 2 , column = 0, columnspan = 3)


tk.Button(root,text = "Exit" , command = root.quit,anchor = tk.E).grid(row = 1 , column = 0, sticky = tk.E, padx = 5 , pady = 5)
tk.mainloop()



if __name__ == "__main__":
    pass