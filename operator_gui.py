import tkinter as tk
from tkinter import messagebox
from op_interactions import get_op_name,get_from_it,transaction

root = tk.Tk()
root.title("Operator")

def op_gui(id):
    op_name = get_op_name(id)

    if(op_name == ""):
        messagebox.showerror("Error","Invalid Operator ID")
        return

    op_frame = tk.LabelFrame(root,padx = 10 , pady = 10)
    op_frame.grid(row = 0 , column = 0 , padx = 15 , pady = 15)
    
    tk.Label(op_frame , text = "Welcome {}".format(op_name), anchor = tk.E).grid(row = 0 , column = 3 , sticky = tk.E, padx = 10 , pady = 10)

    tk.Label(op_frame,text = "Enter current toll station's id: ").grid(row = 1 , column = 0, padx = 10 , pady = 10)
    
    toll_id = tk.Entry(op_frame, width = 40)
    toll_id.grid(row = 1 , column = 2)

    interim_frame = tk.LabelFrame(op_frame,padx = 10 , pady = 10)
    interim_frame.grid(row = 2 , column = 0 , columnspan = 3)

    def check_interim_table():
        ts_id = toll_id.get()
        if(not ts_id.isnumeric()):
            messagebox.showerror("Error","Enter Valid Toll station ID")
            return
        
        if ts_id == "":
            return
        
        for labels in interim_frame.winfo_children():
            labels.destroy()
        
        tk.Label(interim_frame,text = "Vehicle Number").grid(row = 0 , column = 0 , padx = 10 , pady = 10)
        tk.Label(interim_frame,text = "Amount").grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        result = get_from_it(ts_id)
        if (result == None):
            tk.Label(interim_frame,text = "No active transactions").grid(row = 1 , column = 0 , columnspan = 2)
            return 

        tk.Label(interim_frame, text = result[0]).grid(row = 2 , column = 0)
        tk.Label(interim_frame, text = result[1]).grid(row = 2 , column = 1)

        def validate():
            new_transaction_id = transaction(result[0],id,ts_id,result[1])
            if new_transaction_id == None:
                messagebox.showerror("ERROR","Transaction failed!!!")
                return
            
            messagebox.showinfo("Success","Transaction completed\nTransaction ID : {}".format(new_transaction_id))
            check_interim_table()

        tk.Button(interim_frame, text = "Validate", command = validate).grid(row = 3 , column = 0 , columnspan = 2 , padx = 10 , pady = 10)

         


    tk.Button(op_frame, text = "Refresh", command = check_interim_table).grid(row = 1 , column = 3, padx= 10 ,pady = 10)




op_gui(3)

tk.mainloop()