import tkinter as tk
import requests




def scan_webpage():
    url = url_entry.get()

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        result_text.delete('1.0', tk.END)  # Clear previous results

        if response.headers.get('Server'):
            result_text.insert(tk.END, f"Web server version: {response.headers['Server']}\n")
        else:
            result_text.insert(tk.END, "Web server version information not available.\n")

    except requests.exceptions.RequestException as e:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"An error occurred: {str(e)}\n")
'''
# GUI SetupWeb Server Version Checker
import requests
import unittest

def test_scan_webpage_valid_url():
    """Test that the `scan_webpage()` function returns the web server version for a valid URL."""

    url = "https://www.google.com"

    response = requests.get(url)
    response.raise_for_status()

    scan_webpage(url)

    assert "Web server version: " in result_text

def test_scan_webpage_invalid_url():
    """Test that the `scan_webpage()` function raises an exception for an invalid URL."""

    url = "https://www.invalid-domain.com"

    with unittest.raises(requests.exceptions.RequestException):
        scan_webpage(url)

    assert "An error occurred: " in result_text

'''



root = tk.Tk()
root.title("Web Scanner")
root.geometry('770x680')
root.resizable(width=False, height=False)
bg_color = 'black'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='black')
f = tk.Frame(root, bg=bg_color)

title = tk.Label(text='Web Server Version Checker', font=('Courier', 24, 'bold'),bg=bg_color,fg='ivory2')
title.pack(pady=25, anchor='center', padx=10)


url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="mint cream",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)

scan_button = tk.Button(root, text="Scan Webpage", command=scan_webpage,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
scan_button.pack(pady=10)

result_label = tk.Label(root, text="Version of the webpage:",font=('Courier', 18),fg="mint cream",bg=bg_color)
result_label.pack(pady=10,anchor='w', padx=30)

result_text = tk.Text(root, width=93, height=18,font=('Courier', 10), borderwidth=5)
result_text.pack(pady=5)

root.mainloop()


