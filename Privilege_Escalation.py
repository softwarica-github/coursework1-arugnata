from tkinter import ttk
import requests
import tkinter as tk
from tkinter import messagebox

def check_privilege_escalation(url, user_role):
    headers = {'User-Agent': 'Mozilla/5.0', 'User-Role': user_role}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return f"Access granted for {user_role}."
    elif response.status_code == 403:
        return f"Access denied for {user_role}."
    else:
        return f"Unexpected status code: {response.status_code}"

def create_gui():
    def perform_check():
        url = url_entry.get()
        selected_role = role_var.get()
        result = check_privilege_escalation(url, selected_role)
        messagebox.showinfo("Privilege Escalation Detection Result", result)




    window = tk.Tk()
    window.title("Privilege Escalation Detection")
    window.geometry("800x500")
    
    
    

    title = tk.Label(text='Privilege Escalation Detection', font=('Courier', 24, 'bold'),fg='purple4')
    title.pack(pady=25, anchor='center', padx=10)

    url_frame = tk.Frame(window)
    url_frame.pack(pady=10)
    tk.Label(url_frame, text="Target URL:",fg='purple4',font=('Courier', 20, 'bold')).grid(row=0, column=0, padx=5, pady=5)
    url_entry = tk.Entry(url_frame, width=43, borderwidth=8,font=('Courier', 16, 'bold'))
    url_entry.grid(row=0, column=1, padx=5, pady=15)
    
    role_frame = tk.Frame(window)
    role_frame.pack(pady=10)
    tk.Label(role_frame, text="Select Role:",fg='purple4', font=('Courier', 20, 'bold')).grid(row=0, column=0, padx=5, pady=5)
    role_var = tk.StringVar()
    role_var.set("      guest      ")  # Default role selection
    roles_to_test = ["guest", "regular_user", "admin"]

    
    font = ('Courier', 20)
    s = ttk.Style()
    s.configure('TMenubutton', font=font) 
    
    role_dropdown = tk.OptionMenu(role_frame, role_var, *roles_to_test)
    role_dropdown.grid(row=0, column=1, padx=5, pady=5)

    check_button = tk.Button(window, text="Check", fg='purple4', command=perform_check,font=('Courier', 16, 'bold'),borderwidth=8)
    check_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
