
#URL Session & Manipulation Detection

import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def check_url_manipulation(base_url):
    urls_to_check = [
        base_url,  # Original URL
        base_url + "?param=1",  # URL with a query parameter
        base_url + "/../",  # URL with directory traversal
        # Add more URL variations to check for manipulation
    ]

    results = []
    for url in urls_to_check:
        response = requests.get(url)
        result = f"URL: {url}, Status Code: {response.status_code}, Content: {response.text}\n"
        results.append(result)

    return results

def check_session_expiration(base_url):
    login_url = f"{base_url}/login"
    
    response = requests.post(login_url)
    session_cookie = response.cookies.get("session_cookie_name")  # Replace "session_cookie_name" with the actual session cookie name

    protected_resource_url = f"{base_url}/protected_resource"
    protected_response = requests.get(protected_resource_url, cookies={"session_cookie_name": session_cookie})

    if protected_response.status_code == 200:
        return "Session is valid. Able to access protected resource."
    elif protected_response.status_code == 401:
        return "Session has expired. Unable to access protected resource."
    else:
        return f"Unexpected status code: {protected_response.status_code}"

def create_gui():
    def perform_session_check():
        base_url = base_url_entry.get()
       
        result = check_session_expiration(base_url)
        messagebox.showinfo("Session Expiration Check Result", result)

    def perform_url_manipulation_check():
        base_url = base_url_manipulation_entry.get()
        results = check_url_manipulation(base_url)
        result_text = "\n".join(results)
        output_text.config(state=tk.NORMAL)  # Enable editing of the text widget
        output_text.delete(1.0, tk.END)  # Clear previous content
        output_text.insert(tk.END, result_text)  # Insert new content
        output_text.config(state=tk.DISABLED)  # Disable editing of the text widget
    





    

    window = tk.Tk()
    window.title("Security Checks")
    window.geometry("800x600")


    
    title = tk.Label(text='URL Session & Manipulation Detection', font=('Courier', 24, 'bold'),fg='brown4')
    title.pack(pady=25, anchor='center', padx=10)

    session_frame = tk.Frame(window)
    session_frame.pack(pady=10)
    tk.Label(session_frame, text="Base URL:",font=('Courier', 20, 'bold'),fg='brown4').grid(row=0, column=0, padx=5, pady=5)
    
    base_url_entry = tk.Entry(session_frame, width=45,font=('Courier', 16, 'bold'), borderwidth=8 )
    base_url_entry.grid(row=0, column=1, padx=5, pady=5)
   

    session_button = tk.Button(window, text="Session_Expiration", command=perform_session_check,font=('Courier', 15,'bold'),fg="blue",bg='dark grey',borderwidth=8)
    session_button.pack(pady=5)

    url_frame = tk.Frame(window)
    url_frame.pack(pady=10)
    tk.Label(url_frame, text="Base URL:",font=('Courier', 20, 'bold'),fg='brown4').grid(row=0, column=0, padx=5, pady=5)
    
    base_url_manipulation_entry = tk.Entry(url_frame, width=45,font=('Courier', 16, 'bold'), borderwidth=8)
    base_url_manipulation_entry.grid(row=0, column=1, padx=5, pady=5)

    url_button = tk.Button(window, text="URL_Manipulation", command=perform_url_manipulation_check,font=('Courier', 15,'bold'),fg="blue",bg='dark grey',borderwidth=8)
    url_button.pack(pady=5)

    # Text widget to display the output
    output_text = scrolledtext.ScrolledText(window, width=95, height=15, wrap=tk.WORD, state=tk.DISABLED, font=('Courier', 10), borderwidth=5)
    output_text.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
