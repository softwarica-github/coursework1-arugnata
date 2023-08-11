import tkinter as tk
from tkinter import Frame, messagebox
import subprocess

def on_button_click(button_number):
    try:
        if button_number == 1:
            subprocess.run(['python', 'Link_Scanner.py'])
    
        elif button_number == 2:
            subprocess.run(['python', 'Port_scanner.py'])
        elif button_number == 3:
            subprocess.run(['python', 'Url_detector.py'])
        elif button_number == 4:
            subprocess.run(['python', 'Status_checker.py'])
        elif button_number == 5:
            subprocess.run(['python', 'Version_checker.py'])
        elif button_number == 6:
            subprocess.run(['python', 'Privilege_Escalation.py'])
        
        elif button_number == 7:
            subprocess.run(['python', 'sqli_scanner.py'])
        elif button_number == 8:
            subprocess.run(['python', 'xss_detector.py'])
        elif button_number == 9:
            subprocess.run(['python', 'csrf_detector.py'])
        elif button_number == 10:
            subprocess.run(['python', 'cookie_scanner.py'])
        elif button_number == 11:
            subprocess.run(['python', 'webpage_crawler.py'])
        elif button_number == 12:
            subprocess.run(['python', 'domain_info.py'])
        else:
            messagebox.showwarning("Invalid Button", "Invalid button number.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Web_scannner")
root.geometry('850x600')
root.resizable(width=False, height=False)
bg_color = 'black'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='black')
f = Frame(root, bg=bg_color)



title = tk.Label(text='WebSec Suite: All-in-One Web Security Scanner and Analysis', font=('Courier', 18, 'bold'),bg=bg_color,fg='ivory2')
title.grid(pady=25,  padx=10,columnspan=100)


button1 = tk.Button(root, text="  Link Scanner   ", command=lambda: on_button_click(1),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button1.grid(row=1, column=0, pady=10, padx=100, sticky='e')


button2 = tk.Button(root, text="  Port Scanner   ", command=lambda: on_button_click(2),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button2.grid(row=2, column=0, pady=10, padx=100, sticky='e')

button3 = tk.Button(root, text="  URL detector   ", command=lambda: on_button_click(3),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button3.grid(row=3, column=0, pady=10, padx=100, sticky='e')

button4 = tk.Button(root, text="  Status checker ", command=lambda: on_button_click(4),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button4.grid(row=4, column=0, pady=10, padx=100, sticky='e')

button5 = tk.Button(root, text=" version checker ", command=lambda: on_button_click(5),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button5.grid(row=5, column=0, pady=10, padx=100, sticky='e')


button6 = tk.Button(root, text="Privilege Scanner", command=lambda: on_button_click(6),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button6.grid(row=6, column=0, pady=10, padx=100, sticky='e')



button7 = tk.Button(root, text="  XSS detector   ", command=lambda: on_button_click(8),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button7.grid(row=2, column=4, pady=10, padx=10, sticky='w')



button8 = tk.Button(root, text="  CSRF detector  ", command=lambda: on_button_click(9),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button8.grid(row=3, column=4, pady=10, padx=10, sticky='w')



button9 = tk.Button(root, text="  SQLI Scanner   ", command=lambda: on_button_click(7),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button9.grid(row=1, column=4, pady=10, padx=10, sticky='w')



button10 = tk.Button(root, text=" Webpage Crawler ", command=lambda: on_button_click(11),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button10.grid(row=5, column=4, pady=10, padx=10, sticky='w')


button11 = tk.Button(root, text="  Cookie Scanner ", command=lambda: on_button_click(10),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button11.grid(row=4, column=4, pady=10, padx=10, sticky='w')



button12 = tk.Button(root, text="Domain-infomation", command=lambda: on_button_click(12),font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=12)
button12.grid(row=6, column=4, pady=10, padx=10, sticky='w')

root.mainloop()
