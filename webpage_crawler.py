import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tkinter as tk
from tkinter import Frame, scrolledtext

def get_internal_links(soup, base_url):
    internal_links = set()
    for link in soup.find_all('a', href=True):
        url = link['href']
        absolute_url = urljoin(base_url.geturl(), url)
        parsed_url = urlparse(absolute_url)
        if parsed_url.netloc == base_url.netloc:
            internal_links.add(absolute_url)
    return internal_links

def get_assets(soup, base_url):
    assets = set()
    for tag in soup.find_all(['img', 'link'], src=True):
        url = tag['src']
        absolute_url = urljoin(base_url.geturl(), url)
        assets.add(absolute_url)
    return assets

def crawl_website():
    website_url = url_entry.get()
    try:
        response = requests.get(website_url)
        response.raise_for_status()
        base_url = urlparse(website_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        internal_links = get_internal_links(soup, base_url)
        assets = get_assets(soup, base_url)

        internal_links_text.delete(1.0, tk.END)
        for link in internal_links:
            internal_links_text.insert(tk.END, link + '\n')

        assets_text.delete(1.0, tk.END)
        for asset in assets:
            assets_text.insert(tk.END, asset + '\n')

    except requests.exceptions.RequestException as e:
        internal_links_text.delete(1.0, tk.END)
        internal_links_text.insert(tk.END, "Error: " + str(e))
        assets_text.delete(1.0, tk.END)


import unittest
import requests
from bs4 import BeautifulSoup

class TestGetInternalLinks(unittest.TestCase):

    def test_get_internal_links_no_links(self):
        """Test that the `get_internal_links()` function returns an empty set when there are no links in the HTML."""

        soup = BeautifulSoup("<html></html>", "html.parser")

        internal_links = get_internal_links(soup, None)

        self.assertEqual(internal_links, set())

    def test_get_internal_links_one_link(self):
        """Test that the `get_internal_links()` function correctly returns the internal links."""

        soup = BeautifulSoup("<html><a href='/about'>About</a></html>", "html.parser")

        internal_links = get_internal_links(soup, None)

        self.assertEqual(internal_links, {"/about"})

    def test_get_internal_links_multiple_links(self):
        """Test that the `get_internal_links()` function correctly returns the internal links."""

        soup = BeautifulSoup("<html><a href='/about'>About</a><a href='/contact'>Contact</a></html>", "html.parser")

        internal_links = get_internal_links(soup, None)

        self.assertEqual(internal_links, {"/about", "/contact"})

class TestGetAssets(unittest.TestCase):

    def test_get_assets_no_assets(self):
        """Test that the `get_assets()` function returns an empty set when there are no assets in the HTML."""

        soup = BeautifulSoup("<html></html>", "html.parser")

        assets = get_assets(soup, None)

        self.assertEqual(assets, set())

    def test_get_assets_one_asset(self):
        """Test that the `get_assets()` function correctly returns the assets."""

        soup = BeautifulSoup("<html><img src='/img/logo.png'></html>", "html.parser")

        assets = get_assets(soup, None)

        self.assertEqual(assets, {"/img/logo.png"})

    def test_get_assets_multiple_assets(self):
        """Test that the `get_assets()` function correctly returns the assets."""

        soup = BeautifulSoup("<html><img src='/img/logo.png'><link href='/css/style.css'></html>", "html.parser")

        assets = get_assets(soup, None)

        self.assertEqual(assets, {"/img/logo.png", "/css/style.css"})

if __name__ == "__main__":
    unittest.main()


# Create the main window
root = tk.Tk()
root.title("Web Crawler")
root.geometry('780x780')
root.resizable(width=False, height=False)
bg_color = 'purple4'  
root.configure(bg=bg_color)
root.configure(borderwidth=0.5, relief="solid",bg='purple4')
f = Frame(root, bg=bg_color)

title = tk.Label(text='Web Crawler', font=('Courier', 24, 'bold'),bg=bg_color,fg='ivory2')
title.pack(pady=25, anchor='center', padx=10)

# Create and place the widgets
url_label = tk.Label(root, text="Enter URL:", font=('Courier', 18 ),fg="mint cream",bg=bg_color)
url_label.pack(pady=5,anchor='w', padx=10)

        
url_entry = tk.Entry(root, width=60, font=('Courier', 16, 'bold'), borderwidth=8 )
url_entry.pack(pady=10)



button_crawl = tk.Button(root, text="Crawl Website", command=crawl_website,font=('Courier', 16,'bold'),fg="black",bg='dark grey',borderwidth=8)
button_crawl.pack(pady=10)

internal_links_text = scrolledtext.ScrolledText(root, font=('Courier', 12,'bold'),borderwidth=5,width=95, height=10, wrap=tk.WORD)
internal_links_text.pack()
internal_links_text.insert(tk.END, "Internal Links:\n")

assets_text = scrolledtext.ScrolledText(root,font=('Courier', 12,'bold'),borderwidth=5, width=95, height=10, wrap=tk.WORD)
assets_text.pack()
assets_text.insert(tk.END, "Assets:\n")

# Start the main event loop
root.mainloop()
