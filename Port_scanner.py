import tkinter as tk
from tkinter import Frame, messagebox
import requests
import requests



def custom_code():
    s = requests.Session()
    website = url_entry.get()
    startport = int(start_port_entry.get())
    endport = int(end_port_entry.get())
    try:
        for port in range(startport, endport + 1):
            try:
                s.connect((website, port))
                result_text.insert(tk.END, f"The port {port} is open for {website}\n")
            except:
                result_text.insert(tk.END, f"The port {port} is closed for {website}\n")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# GUI Setup
root = tk.Tk()
root.title("Web Scanner")
root.geometry('760x680')
root.resizable(width=False, height=False)
bg_color = 'dark slate gray'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='dark slate gray')
f = Frame(root, bg=bg_color)

title = tk.Label(root, text='Port Scanner', font=('Courier', 24, 'bold'), bg=bg_color, fg='ivory2')
title.pack(pady=25)

url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="mint cream",bg=bg_color)
url_label.pack(pady=1,anchor='w', padx=10)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)


port_frame = tk.Frame(root,bg = bg_color)
port_frame.pack(pady=15)


start_port_label = tk.Label(port_frame, text="Starting port number:", font=('Courier', 18), fg="mint cream", bg=bg_color)
start_port_label.grid(row=0, column=0, padx=5, sticky='w')

start_port_entry = tk.Entry(port_frame, width=22, font=('Courier', 16, 'bold'), borderwidth=8)
start_port_entry.grid(row=1, column=0, padx=5,sticky='w')

end_port_label = tk.Label(port_frame, text="Ending port number:", font=('Courier', 18), fg="mint cream", bg=bg_color)
end_port_label.grid(row=0, column=1, padx=130,sticky='e')

end_port_entry = tk.Entry(port_frame, width=22, font=('Courier', 16, 'bold'), borderwidth=8)
end_port_entry.grid(row=1, column=1, padx=95,sticky='e',pady=10)

scan_button = tk.Button(root, text="Scan Ports", command=custom_code, font=('Courier', 17, 'bold'), fg="black", bg='dark grey', borderwidth=8)
scan_button.pack(pady=10)

result_label = tk.Label(root, text="Scan Results:", font=('Courier', 18), fg="mint cream", bg=bg_color)
result_label.pack(pady=5,anchor="w")

result_text = tk.Text(root, width=85, height=20, font=('Courier', 16, 'bold'), borderwidth=8)
result_text.pack(pady=5)

root.mainloop()
