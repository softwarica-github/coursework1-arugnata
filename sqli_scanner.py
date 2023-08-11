import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import Frame, messagebox
from urllib.parse import urljoin

# Function to get all forms
def get_forms(url):
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({
            "type": input_type, 
            "name": input_name,
            "value": input_value,
        })

    detailsOfForm['action'] = action
    detailsOfForm['method'] = method
    detailsOfForm['inputs'] = inputs
    return detailsOfForm

def vulnerable(response):
    errors = {
        "quoted string not properly terminated",
        "unclosed quotation mark after the character string",
        "you have an error in your SQL syntax"
    }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def scan_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

    forms = get_forms(url)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"[+] Detected {len(forms)} forms on {url}.\n")

    for form in forms:
        details = form_details(form)

        for i in "\"'":
            data = {}
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag['name']] = input_tag["value"] + i
                elif input_tag["type"] != "submit":
                    data[input_tag['name']] = f"test{i}"

            try:
                s = requests.Session()
                s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

                if details["method"] == "post":
                    res = s.post(url, data=data)
                elif details["method"] == "get":
                    res = s.get(url, params=data)
                if res and res.status_code in range(200, 300) and vulnerable(res):
                    result_text.insert(tk.END, f"SQL injection attack vulnerability in link: {url}\n")
                    return
            except Exception as e:
                pass

    result_text.insert(tk.END, "No SQL injection attack vulnerability detected\n")

# Create the GUI
root = tk.Tk()
root.title("SQLI")
root.geometry('770x630')
root.resizable(width=False, height=False)
bg_color = 'grey20'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='grey20')
f = Frame(root, bg=bg_color)


title = tk.Label(text='SQL Injection Scanner', font=('Courier', 24, 'bold'),bg=bg_color,fg='white')
title.pack(pady=25, anchor='center', padx=10)





url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="white",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)


scan_button = tk.Button(root, text="Scan Webpage", command=scan_url,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
scan_button.pack(pady=10)




result_text = tk.Text(root, width=93, height=18,font=('Courier', 10), borderwidth=5)
result_text.pack(pady=5)


root.mainloop()
