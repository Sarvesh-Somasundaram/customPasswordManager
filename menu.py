from hash_maker import password
from database_manager import store_passwords, find_password 
import clipboard
import tkinter as tk
from tkinter import messagebox


def menu():
   root = tk.Tk()
   root.title("Password Manager")

   canvas1 = tk.Canvas(root, width = 500, height = 100)
   canvas1.grid(row = 0, column = 0)

   tk.Label(root, text='-'*30).grid(row = 1, column = 0)
   tk.Label(root, text=('-'*13) + 'Menu'+ ('-' *13)).grid(row = 2, column = 0)
   tk.Label(root, text='1. Create new password').grid(row = 3, column = 0)
   tk.Label(root, text='2. Find a password for a site or app').grid(row = 5, column = 0)
   tk.Label(root, text='3. Add an existing account').grid(row = 6, column = 0)
   tk.Label(root, text='Q. Exit').grid(row = 7, column = 0)
   tk.Label(root, text='-'*30).grid(row = 8, column = 0)
   
   entry1 = tk.Entry(root)
   entry1.grid(row = 9, column = 0)

   def check():
      choice = entry1.get()
      while choice != 'Q':
         if choice == '1':
            root.destroy()
            create()
         if choice == '2':
            root.destroy()
            find()
         if choice == '3':
            root.destroy()
            add_password()
      root.destroy()

   tk.Button(root, text='Enter', command=check).grid(row = 10, column = 0)
   root.mainloop()

def create():
   create = tk.Tk()
   create.title("Password Manager")

   canvas1 = tk.Canvas(create, width = 650, height = 100)
   canvas1.grid(row = 0, column = 0)

   tk.Label(create, text='Please provide the name of the site or app you want to generate a password for').grid(row = 1, column = 0)
   tk.Label(create, text='Please provide a simple password for this site: ').grid(row = 2, column = 0)
   tk.Label(create, text='Please provide a user email for this app or site').grid(row = 3, column = 0)
   tk.Label(create, text='Please provide a username for this app or site (if applicable)').grid(row = 4, column = 0)
   tk.Label(create, text='Please provide the url to the site that you are creating the password for').grid(row = 5, column = 0)

   name = tk.Entry(create)
   name.grid(row = 1, column = 1, padx = (0, 25))

   textpswd = tk.Entry(create)
   textpswd.grid(row = 2, column = 1, padx = (0, 25))

   email = tk.Entry(create)
   email.grid(row = 3, column = 1, padx = (0, 25))

   user = tk.Entry(create)
   user.grid(row = 4, column = 1, padx = (0, 25))

   website = tk.Entry(create)
   website.grid(row = 5, column = 1, padx = (0, 25))

   def check():
      plaintext = textpswd.get()
      app_name = name.get()
      user_email = email.get()
      url = website.get()
      passw = password(plaintext, app_name, 15)
      clipboard.copy(passw)
      messagebox.showinfo('Password Manager', 'Your password has now been created and copied to your clipboard')
      username = user.get()
      if username == None:
         username = ''
      store_passwords(passw, user_email, username, url, app_name)
      create.destroy()
      menu()

   tk.Button(create, text='Enter', command=check).grid(row = 6, column = 0)
   create.mainloop()

def find():
   root = tk.Tk()
   root.title("Password Manager")

   canvas1 = tk.Canvas(root, width = 650, height = 100)
   canvas1.grid(row = 0, column = 0)

   tk.Label(root, text='Please proivide the name of the site or app you want to find the password to').grid(row = 0, column = 0)
   
   name = tk.Entry(root)
   name.grid(row = 1, column = 0, padx = (0, 25))

   def check():
      app_name = name.get()
      find_password(app_name)
      messagebox.showinfo('Password Manager', 'Your password has now been created and copied to your clipboard')
      root.destroy()
      menu()

   tk.Button(root, text='Enter', command=check).grid(row = 2, column = 0)
   root.mainloop()


def add_password():
   root = tk.Tk()
   root.title("Password Manager")

   canvas1 = tk.Canvas(root, width = 650, height = 100)
   canvas1.grid(row = 0, column = 0)

   tk.Label(root, text='Please provide the name of the site or app you want to add a password for').grid(row = 1, column = 0)
   tk.Label(root, text='Please provide the password for this site: ').grid(row = 2, column = 0)
   tk.Label(root, text='Please provide a user email for this app or site').grid(row = 3, column = 0)
   tk.Label(root, text='Please provide a username for this app or site (if applicable)').grid(row = 4, column = 0)
   tk.Label(root, text='Please provide the url to the site that you are creating the password for').grid(row = 5, column = 0)

   name = tk.Entry(root)
   name.grid(row = 1, column = 1, padx = (0, 25))

   textpswd = tk.Entry(root)
   textpswd.grid(row = 2, column = 1, padx = (0, 25))

   email = tk.Entry(root)
   email.grid(row = 3, column = 1, padx = (0, 25))

   user = tk.Entry(root)
   user.grid(row = 4, column = 1, padx = (0, 25))

   website = tk.Entry(root)
   website.grid(row = 5, column = 1, padx = (0, 25))

   def check():
      passw = textpswd.get()
      app_name = name.get()
      user_email = email.get()
      url = website.get()
      clipboard.copy(passw)
      messagebox.showinfo('Password Manager', 'Your password has now been added and copied to your clipboard')
      username = user.get()
      if username == None:
         username = ''
      store_passwords(passw, user_email, username, url, app_name)
      root.destroy()
      menu()

   tk.Button(root, text='Enter', command=check).grid(row = 6, column = 0)
   root.mainloop()
