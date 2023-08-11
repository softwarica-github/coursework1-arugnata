import requests
import tkinter as tk
from tkinter import Frame, messagebox
from urllib.parse import urlparse
import re
import uuid

def generate_csrf_token():
    return str(uuid.uuid4())

def create_headers():
    headers = {
        # Your custom headers can go here (if any)
        # Example: 'X-My-Custom-Header': 'MyCustomValue'
    }
    return headers

def csrf_protected_request(url, method, csrf_token=None):
    headers = create_headers()
    cookies = {}
    
    # SameSite cookie configuration
    cookies['mycookie'] = 'mycookievalue; SameSite=Strict'

    if csrf_token:
        headers['X-CSRF-Token'] = csrf_token

    if method == 'GET':
        response = requests.get(url, headers=headers, cookies=cookies)
    else:  # POST
        response = requests.post(url, headers=headers, cookies=cookies)

    return response

def check_csrf_vulnerability():
    target_url = url_entry.get()
    csrf_token = generate_csrf_token()
    try:        
        response = csrf_protected_request(target_url, 'GET', csrf_token=None)
        csrf_token = response.headers.get('X-CSRF-Token') or csrf_token
        response = csrf_protected_request(target_url, 'POST', csrf_token=csrf_token)      
        if response.status_code == 200:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "The website is not vulnerable to CSRF attacks.")
            result_text.config(state=tk.DISABLED)
            messagebox.showinfo("CSRF Vulnerability", "The website is not vulnerable to CSRF attacks.")
        else:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "The website may be vulnerable to CSRF attacks.\n\n")
            result_text.insert(tk.END, "CSRF protection measures in place:\n")
            
            if 'X-CSRF-Token' in response.headers:
                result_text.insert(tk.END, "1. CSRF Tokens (Found in the response headers)\n")
            else:
                result_text.insert(tk.END, "1. CSRF Tokens (Not found in the response headers)\n")

            # Additional checks for other security measures can be added here

            result_text.config(state=tk.DISABLED)
            messagebox.showinfo("CSRF Vulnerability", "The website may be vulnerable to CSRF attacks.")
    except requests.exceptions.RequestException as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"An error occurred while making the request: {e}")
        result_text.config(state=tk.DISABLED)
        messagebox.showerror("Error", f"An error occurred while making the request: {e}")

# GUI Setup



root = tk.Tk()
root.title("CSRF Vulnerability Checker")
root.geometry('770x630')
root.resizable(width=False, height=False)
bg_color = 'honeydew4' 
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='honeydew4')
f = Frame(root, bg=bg_color)

title = tk.Label(text='CSRF Vulnerability Checker', font=('Courier', 24, 'bold'),bg=bg_color,fg='black')
title.pack(pady=25, anchor='center', padx=10)


url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="black",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)

scan_button = tk.Button(root, text="Check Vulnerability", command=check_csrf_vulnerability,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
scan_button.pack(pady=10)



result_text = tk.Text(root, wrap=tk.WORD, width=93, height=18,font=('Courier', 10), borderwidth=5)
result_text.pack(pady=5)

info_label = tk.Label(root, text="Note: While this application can detect the presence of CSRF, doesn't mean that the website is vulnerable "
                                 "to CSRF attacks.")
info_label.pack()

root.mainloop()
'''
app = tk.Tk()
app.title("CSRF Vulnerability Checker")

info_label = tk.Label(app, text="While this application can detect the presence of, doesn't mean that the website is vulnerable "
                                 "to CSRF attacks.")
info_label.pack()

url_label = tk.Label(app, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(app)
url_entry.pack()

check_button = tk.Button(app, text="Check Vulnerability", command=check_csrf_vulnerability)
check_button.pack()

result_text = tk.Text(app, wrap=tk.WORD, height=10, state=tk.DISABLED)
result_text.pack()

app.mainloop()
'''