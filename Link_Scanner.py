import tkinter as tk
from tkinter import Frame, messagebox
import requests
from bs4 import BeautifulSoup


def scan_webpage():
    url = url_entry.get()

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        result_text.delete('1.0', tk.END)  # Clear previous results

        if links:
            for link in links:
                href = link.get('href')
                if href and href.startswith('http'):
                    result_text.insert(tk.END, f"{href}\n")
        else:
            result_text.insert(tk.END, "No links found on the webpage.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# GUI Setup
root = tk.Tk()
root.title("Web Scanner")
root.geometry('770x630')
root.resizable(width=False, height=False)
bg_color = '#15222a'
'#000080'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='#15222a')
f = Frame(root, bg=bg_color)

title = tk.Label(text='Webpage Link Scanner', font=('Courier', 24, 'bold'),bg=bg_color,fg='ivory2')
title.pack(pady=25, anchor='center', padx=10)


url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="mint cream",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)

scan_button = tk.Button(root, text="Scan Webpage", command=scan_webpage,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
scan_button.pack(pady=10)

result_label = tk.Label(root, text="Links found on the webpage:",font=('Courier', 18),fg="mint cream",bg=bg_color)
result_label.pack(pady=10,anchor='w', padx=30)

result_text = tk.Text(root, width=93, height=18,font=('Courier', 10), borderwidth=5)
result_text.pack(pady=5)

root.mainloop()
