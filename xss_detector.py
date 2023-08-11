import sys
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import tkinter as tk
from tkinter import Frame, scrolledtext
from tkinter import messagebox
import pprint

from requests.exceptions import MissingSchema

is_windows = sys.platform.startswith('win')
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white
    try:
        import win_unicode_console, colorama

        win_unicode_console.enable()
        colorama.init()
        # Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''
else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white

def no_color():
    global G, Y, B, R, W
    G = Y = B = R = W = ''


def get_all_forms(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'  # or 'ISO-8859-1'
        soup = bs(response.content, "html.parser")
    except MissingSchema:
        print('%s[*] Please make sure to put your right schema [ex: https://example.com]' % Y)
    except:
        raise UnboundLocalError("%sPlease make sure to put your right schema [ex: https://example.com]" % R)
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    
    action = form.attrs.get("action")
   
    method = form.attrs.get("method", "get").lower()
  
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
  
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, url, value):
   
    target_url = urljoin(url, form_details["action"])
   
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
       
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
           
            data[input_name] = input_value

    if form_details["method"] == "post":
        response = requests.post(target_url, data=data)
    else:
      
        response = requests.get(target_url, params=data)

    return response


def scan_xss(url):
    forms = get_all_forms(url)
    result = f"[+] Detected {len(forms)} forms on {url}\n\n"
    js_script = "<Script>alert('hi')</scripT>"
    is_vulnerable = f"%s[-] No xss found !!%s\n" % (R, W)
    detected_xss = ""
    for form in forms:
        form_details = get_form_details(form)
        response = submit_form(form_details, url, js_script)
        content = response.content.decode('utf-8', errors='ignore')  
        if js_script in content:
            detected_xss += f"[+] XSS Detected on {url}\n"
            detected_xss += f"{R}[*] Form details:{W}\n"
            detected_xss += f"{pprint.pformat(form_details, indent=4)}\n"  
            is_vulnerable = True          
    if detected_xss:
        result += detected_xss
    return result if is_vulnerable else result




    




# GUI Function
def scan_xss_gui():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a target URL.")
        return

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"[*] Scan begin for {url}\n\n")
    result = scan_xss(url)
    result_text.insert(tk.END, result)
    result_text.insert(tk.END, "\n[*] Scan complete !!")


# Create the main GUI window
'''
import unittest
import requests
import bs4 as bs
import pprint

class TestScanXSS(unittest.TestCase):

    def test_scan_xss_vulnerable_form(self):
        """Test that the `scan_xss()` function correctly detects a vulnerable form."""

        url = "https://xss-example.com/basic/"

        result = scan_xss(url)

        self.assertIn("[+] XSS Detected on https://xss-example.com/basic/", result)
        self.assertIn("[*] Form details:", result)
        self.assertIn(pprint.pformat({"action": "/basic/", "method": "post", "inputs": [{"type": "text", "name": "name"}]}), result)

    def test_scan_xss_not_vulnerable_form(self):
        """Test that the `scan_xss()` function correctly does not detect a non-vulnerable form."""

        url = "https://www.google.com"

        result = scan_xss(url)

        self.assertIn("[-] No xss found !!", result)

if __name__ == "__main__":
    unittest.main()


'''


root = tk.Tk()
root.title("XSS Detection Tool")
root.geometry("700x700")

root.resizable(width=False, height=False)
bg_color = '#2F2F4F'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='#2F2F4F')
f = Frame(root, bg=bg_color)


title = tk.Label(text='XSS detector', font=('Courier', 24, 'bold'),bg=bg_color,fg='ivory2')
title.pack(pady=25, anchor='center', padx=10)


url_label = tk.Label(root, text="Enter your target [ex: https://example.com]:", font=('Courier', 18 ),fg="mint cream",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)




scan_button = tk.Button(root, text="Scan Webpage", command=scan_xss_gui,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
scan_button.pack(pady=10)

result_label = tk.Label(root, text="Results found on the webpage:",font=('Courier', 18),fg="mint cream",bg=bg_color)
result_label.pack(pady=10,anchor='w', padx=30)

result_text = tk.Text(root, width=93, height=18,font=('Courier', 10), borderwidth=5)
result_text.pack(pady=5)



# Main GUI loop
root.mainloop()
