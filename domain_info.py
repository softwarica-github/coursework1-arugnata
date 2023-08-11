import os
import socket
import whois
import tkinter as tk
from tkinter import Frame, messagebox

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

def get_ip_address(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return None

def get_whois_info(url):
    try:
        w = whois.whois(url)
        return str(w)
    except whois.parser.PywhoisError as e:
        return "Error: " + str(e)

def get_domain_name(url):
    domain_parts = url.split('.')
    domain_name = '.'.join(domain_parts[-2:])
    return domain_name

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    if ip_address:
        ip_address = ip_address.strip()
        info_text = f"IP Address: {ip_address}\n"
        whois_info = get_whois_info(domain_name)
        info_text += whois_info
        create_report(name, url, domain_name, ip_address, whois_info)
    else:
        info_text = "Error: Could not resolve the domain name."

    messagebox.showinfo("Information", info_text)

def create_report(name, full_url, domain_name, ip_address, whois_info):
    project_dir = 'companies/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/ip_address.txt', ip_address)
    write_file(project_dir + '/whois_info.txt', whois_info)

def on_submit():
    name = company_name_entry.get()
    url = url_entry.get()
    gather_info(name, url)



import unittest
import requests
import socket
import whois
import os

class TestGatherInfo(unittest.TestCase):

    def test_gather_info_valid_url(self):
        """Test that the `gather_info()` function correctly gathers information for a valid URL."""

        name = "Google"
        url = "https://www.google.com"

        domain_name = get_domain_name(url)
        ip_address = get_ip_address(domain_name)
        whois_info = get_whois_info(domain_name)

        info_text = f"IP Address: {ip_address}\n"
        info_text += whois_info

        gather_info(name, url)

        project_dir = 'companies/' + name
        self.assertTrue(os.path.exists(project_dir))

        full_url_file = os.path.join(project_dir, 'full_url.txt')
        self.assertTrue(os.path.exists(full_url_file))
        with open(full_url_file, 'r') as f:
            full_url = f.read()
        self.assertEqual(full_url, url)

        domain_name_file = os.path.join(project_dir, 'domain_name.txt')
        self.assertTrue(os.path.exists(domain_name_file))
        with open(domain_name_file, 'r') as f:
            domain_name = f.read()
        self.assertEqual(domain_name, domain_name)

        ip_address_file = os.path.join(project_dir, 'ip_address.txt')
        self.assertTrue(os.path.exists(ip_address_file))
        with open(ip_address_file, 'r') as f:
            ip_address = f.read()
        self.assertEqual(ip_address, ip_address)

        whois_info_file = os.path.join(project_dir, 'whois_info.txt')
        self.assertTrue(os.path.exists(whois_info_file))
        with open(whois_info_file, 'r') as f:
            whois_info = f.read()
        self.assertEqual(whois_info, whois_info)

    def test_gather_info_invalid_url(self):
        """Test that the `gather_info()` function correctly handles an invalid URL."""

        name = "Invalid"
        url = "https://www.invalid.com"

        with self.assertRaises(requests.exceptions.RequestException):
            gather_info(name, url)

        project_dir = 'companies/' + name
        self.assertFalse(os.path.exists(project_dir))

if __name__ == "__main__":
    unittest.main()


# Create the main application window
root = tk.Tk()
root.title("Web Scanner")
root.geometry('780x480')
root.resizable(width=False, height=False)
bg_color = '#474747'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='#474747')
f = Frame(root, bg=bg_color)


title = tk.Label(text='Domain Information Collector', font=('Courier', 24, 'bold'),bg=bg_color,fg='ivory2')
title.pack(pady=25, anchor='center', padx=25)

# Create input fields
company_name_label = tk.Label(root, text="Enter The Company's Name:", font=('Courier', 18 ),fg="mint cream",bg=bg_color)
company_name_label.pack(pady=5,anchor='w', padx=30)
company_name_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8)
company_name_entry.pack(pady=15)



url_label = tk.Label(root, text="Enter The Full URL:",font=('Courier', 18 ),fg="mint cream",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8)
url_entry.pack(pady=20)

submit_button = tk.Button(root, text="Scan", command=on_submit,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
submit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
