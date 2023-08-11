import requests
import tkinter as tk
from tkinter import Frame, scrolledtext

def check_cookie_security(url):
    try:
        response = requests.get(url)
        cookies = response.cookies

        if cookies:
            result = "Cookies found:\n"
            for cookie in cookies:
                result += f"- {cookie.name}: {cookie.value}\n"
                result += f"  Secure: {cookie.secure}\n"
                result += f"  HttpOnly: {cookie.has_nonstandard_attr('httponly')}\n"
        else:
            result = "No cookies found."
        
        return result
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def perform_check():
    target_url = url_entry.get()
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)  # Clear previous content
    result = check_cookie_security(target_url)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)



import unittest
import requests

class TestCheckCookieSecurity(unittest.TestCase):

    def test_check_cookie_security_no_cookies(self):
        """Test that the `check_cookie_security()` function returns `No cookies found.` when there are no cookies in the response."""

        url = "https://www.google.com"

        result = check_cookie_security(url)

        self.assertEqual(result, "No cookies found.")

    def test_check_cookie_security_secure_httponly(self):
        """Test that the `check_cookie_security()` function correctly returns the security settings of the cookies."""

        url = "https://example.com/cookies/secure-httponly/"

        result = check_cookie_security(url)

        self.assertIn("- SESSIONID: foobar", result)
        self.assertIn("  Secure: True", result)
        self.assertIn("  HttpOnly: True", result)

    def test_check_cookie_security_insecure_not_httponly(self):
        """Test that the `check_cookie_security()` function correctly returns the security settings of the cookies."""

        url = "https://example.com/cookies/insecure-not-httponly/"

        result = check_cookie_security(url)

        self.assertIn("- NAME: foo", result)
        self.assertIn("  Secure: False", result)
        self.assertIn("  HttpOnly: False", result)

if __name__ == "__main__":
    unittest.main()







root = tk.Tk()
root.title("cookie Scanner")
root.geometry('780x680')
root.resizable(width=False, height=False)
bg_color = 'cornsilk4'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='cornsilk4')
f = Frame(root, bg=bg_color)

title = tk.Label(text='cookie Scanner', font=('Courier', 24, 'bold'),bg=bg_color,fg='black')
title.pack(pady=25, anchor='center', padx=10)


url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="black",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=30)

        
url_entry = tk.Entry(root, width=55, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)

scan_button = tk.Button(root, text="Scan Webpage", command=perform_check,font=('Courier', 19,'bold'),fg="black",bg='dark grey',borderwidth=8)
scan_button.pack(pady=10)

result_label = tk.Label(root, text="Cookies found on the webpage:",font=('Courier', 18),fg="black",bg=bg_color)
result_label.pack(pady=10,anchor='w', padx=30)

result_text = tk.Text(root, width=93, height=18,font=('Courier', 10), borderwidth=5)
result_text.pack(pady=5)

root.mainloop()


