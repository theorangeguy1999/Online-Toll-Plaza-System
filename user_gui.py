import tkinter as tk
from tkinter import messagebox
from user_interactions import get_balance,get_name,update_balance,get_toll_amount,enter_into_it,check_status_from_it
from admin_interactions import search_results


#root = tk.Tk()
#root.title("Toll plaza system")

def cust_gui(vno,root):



    for labels in root.winfo_children():
        labels.destroy()

    root.title("Toll Plaza")
    user_name = get_name(vno)
    user_frame = tk.LabelFrame(root, padx = 10 , pady = 10)
    user_frame.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

    def logout():
        ans = messagebox.askyesno("Confirm","Are you sure you want to logout?")
        if ans == True:
            root.quit()
            return
        else:
            return
        pass

    tk.Button(root,text = "Logout", command = logout, anchor = tk.W).grid(row = 1 , column = 0 , sticky = tk.W, padx = 5 , pady = 5)

    tk.Label(user_frame,text = "Welcome {}".format(user_name), anchor = tk.W).grid(row = 0,column = 0,columnspan = 2 , sticky = tk.W, padx = 10 , pady = 10)

    current_balance_label = tk.Label(user_frame,text = "Current Balance : {}".format(get_balance(vno)))
    current_balance_label.grid(row = 1 , column = 0 , columnspan = 2 , padx = 10 , pady = 10)
    
    def refresh_balance():
        global current_balance_label
        current_balance_label = tk.Label(user_frame,text = "Current Balance : {}".format(get_balance(vno)))
        current_balance_label.grid(row = 1 , column = 0 , columnspan = 2 , padx = 10 , pady = 10)
        return

    def recharge_account():
        recharge_win = tk.Toplevel()
        recharge_win.title("Recharge")

        tk.Label(recharge_win,text = "Enter recharge amount: ").grid(row = 0 , column = 0 , padx = 10 , pady =10 )
        amount = tk.Entry(recharge_win,width = 10)
        amount.grid(row = 0 , column = 1 , padx = 10 , pady = 10)


        def recharge_btn():
            if(amount.get == "" or not amount.get().isnumeric()):
                messagebox.showwarning("","Input Error")
                return
            
            success = update_balance(vno,amount.get())
            if not success:
                messagebox.showerror("Error","Recharge Failed")
                return
            
            messagebox.showinfo("","Recharge Successfull")
            refresh_balance()
            recharge_win.destroy()
            return

        tk.Button(recharge_win,text = "Recharge" , command = recharge_btn).grid(row = 2 , column = 0 , columnspan = 2 , padx = 10 , pady = 10)


    tk.Button(user_frame, text = "Check Balance", command = refresh_balance).grid(row = 2 , column = 0 ,columnspan = 2, padx = 10 , pady = 10)
    tk.Button(user_frame,text = "Recharge", command = recharge_account).grid(row = 2, column = 2,columnspan = 2 , padx = 10 ,pady = 10)
    
    def transaction_btn():
        trn_win = tk.Toplevel()
        trn_win.title("Transaction")

        owtw = tk.IntVar()
        owtw.set(-1)
        tk.Radiobutton(trn_win,text = "One Way Trip", variable = owtw, value = 0).grid(row = 1 , column = 1 , padx = 10 , pady = 10)    
        tk.Radiobutton(trn_win,text = "Same day return", variable = owtw, value = 1).grid(row = 2 , column = 1 , padx = 10 , pady = 10)
        tk.Label(trn_win,text = "Enter toll ID: ").grid(row = 0 , column = 0 , padx = 5 , pady = 5)
        toll_id = tk.Entry(trn_win,width = 10)
        toll_id.grid(row = 1 , column = 0, padx = 10 , pady = 10)

        def enter_button():
            if owtw.get() == -1:
                messagebox.showerror("Error","Please select trip type")
                return
            tid = toll_id.get()
            if (not tid.isnumeric()):
                messagebox.showerror("Error","Invalid toll id")
                return
            
            t_type = {0 : 'one_way_cost', 1 : 'two_way_cost'}
            trn_amount = get_toll_amount(tid,t_type[owtw.get()])

            tk.Label(trn_win,text = "Transaction amount = {}".format(trn_amount)).grid(row = 3, column = 0, padx = 5 , pady = 5)
            cur_bal = get_balance(vno)

            if cur_bal < trn_amount:
                tk.Button(trn_win,text = "Pay", state = tk.DISABLED).grid(row = 3 , column = 1 , padx = 5 , pady = 5)
                messagebox.showwarning("Warning","Insufficient Balance")
                return

            status_frame = tk.LabelFrame(trn_win , padx = 10 , pady = 10)

            def Pay_btn():
                success = enter_into_it(vno,tid,trn_amount)
                if not success:
                    messagebox.showwarning("Warning","Transaction already processing")
                    return
                
                status_frame.grid(row = 5 , column = 1 , columnspan = 2)
                for labels in status_frame.winfo_children():
                    labels.destroy()
                
                def check_status():
                    status = check_status_from_it(vno,tid,trn_amount)
                    if(status):
                        messagebox.showinfo("Transaction Complete","Your transaction has been completely processed\nHave a happy journey")
                        trn_win.destroy()
                        refresh_balance()
                        return
                    else:
                        messagebox.showinfo("Transaction Processing","Transaction is still processing\nPlease wait")
                        return 


                tk.Button(status_frame,text = "Check Status", command = check_status).grid(row = 0 , column = 1 ,columnspan = 2, padx = 10 , pady =10)



                pass

            tk.Button(trn_win,text = "PAY", command = Pay_btn).grid(row = 3 , column = 1 , padx = 5 , pady = 5)


            pass

        tk.Button(trn_win,text = "Enter", command = enter_button).grid(row = 2, column = 0, padx = 10 , pady = 10)

    tk.Button(user_frame, text = "Initialize Transaction", command = transaction_btn, anchor = tk.CENTER).grid(row = 4 , column = 0 , columnspan = 4, padx = 10 , pady = 10,sticky = tk.W + tk.E)

    history_frame = tk.LabelFrame(user_frame,padx = 10 , pady= 10)
    history_frame.grid(row = 6,column = 0 , columnspan = 4)

    def history_btn():
        for labels in history_frame.winfo_children():
            labels.destroy()
        
        tk.Label(history_frame,text = "Transaction ID ").grid(row = 0 , column = 0, padx = 5 , pady = 5)
        tk.Label(history_frame,text = "Toll ID ").grid(row = 0 , column = 1, padx = 5 , pady = 5)
        tk.Label(history_frame,text = "Amount ").grid(row = 0 , column = 2, padx = 5 , pady = 5)
        tk.Label(history_frame,text = "Date and Time ").grid(row = 0 , column = 3, padx = 5 , pady = 5)

        results = search_results("vehicleno",vno)
        for row , records in enumerate(results):
            tk.Label(history_frame,text = records[0]).grid(row = 1 + row , column = 0, padx = 5 , pady = 5)
            tk.Label(history_frame,text = records[3]).grid(row = 1 + row , column = 1, padx = 5 , pady = 5)
            tk.Label(history_frame,text = records[4]).grid(row = 1 + row , column = 2, padx = 5 , pady = 5)
            tk.Label(history_frame,text = records[5]).grid(row = 1 + row , column = 3, padx = 5 , pady = 5)
    
    tk.Button(user_frame, text = "Check transaction history", command = history_btn).grid(row = 5 , column = 0 , columnspan = 4 , padx = 15 , pady = 15)




if __name__ == "__main__":
    cust_gui('trial_no',tk.Tk())
    tk.mainloop()