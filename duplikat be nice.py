from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import customtkinter
from tkinter import ttk, Toplevel, StringVar
from tkinter import messagebox,scrolledtext,ttk
import csv
import webbrowser
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn import tree
import pandas as pd


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BackgroundGUI:
    def __init__(self,window):
        self.window =window
        self.kata_kata = ["Matematika", "Biologi", "Kimia", "Sains Data", "Fisika", "Pendidikan IPA", "Manajemen", "Ekonomi", "Akutansi", "Teknik Sipil", "Sistem Informasi","Teknik Mesin","Pendidikan Sastra Indonesia","Sastra Inggris","Pendidikan Bahasa Jerman",
                        "Pendidikan Guru Sekolah Dasar","Pendidikan Luar Biasa","Teknologi Pendidikan","Pendidikan Jasmani,Kesehatan,dan Rekreasi","Pendidikan Kepelatihan Olahraga","Ilmu Keolahragaan",
                        "Kedokteran","Hukum","D4 Teknik Sipil","D4 Desain Grafis","D4 Tata Busana"]
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.window, textvariable=self.search_var, fg='black', width=18)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_suggestions)
        self.suggestions_frame = tk.Frame(self.window, bg='white', bd=1, relief='solid')

        self.username= tk.StringVar()
        self.password = tk.StringVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.phone = tk.IntVar()

        self.pu_selesai = False
        self.ppu_selesai = False
        self.pbm_selesai = False
        self.pk_selesai = False
        self.lbi_selesai = False  
        self.lbe_selesai = False
        self.pm_selesai = False      
        self.list_skor = [] 

        self.usernamefom = ""
        self.pil1 = ""
        self.pil2 = ""
        self.recommended_programs_str = ""
        self.list_skor = [] 

        self.window.title("TryNesa")
        self.window.state('zoomed')
        self.window.resizable(0,0)
        self.bg = PhotoImage(file="trynesa.png")
        self.loginlayar = Label(self.window, image=self.bg)
        self.loginlayar.place(x=0, y=0, relheight=1, relwidth=1)

        self.current_menu = self.window

        self.start_timer()
        

    def login_dashboard(self):
        
        self.layarmasuk.destroy()
        self.window = window  
        self.bg = PhotoImage(file="dashboard.png")
        self.layardash = Label(window, image=self.bg)
        self.layardash.place(x=0, y=0, relheight=1, relwidth=1)
        username = self.username.get()


        with open('dataakun.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Username'] == username:
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    self.nama_label_dshbrd = Label(self.window, text=f"Welcome {first_name} {last_name}\nto TryNesa!", font=("sans serif", 20, "bold"), bg='#FAFDFD', justify='center', fg='#6B94B5')
                    self.nama_label_dshbrd.place(x=85, y=150)
                    break

        self.nama_label_dshbrd = tk.Label(self.window, text="Masa depan milik mereka yang kompeten. \nJadilah yang baik, jadilah lebih baik,\n dan jadilah yang terbaik! -Brian Tracy", font=("sans serif", 13, "bold"), bg='#6B94B5', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=65, y=450)

        self.search_var.trace("w", self.update_suggestions)

        self.search_entry = tk.Entry(self.window, textvariable=self.search_var, fg='black', width=20)
        self.search_entry.place(x=600, y=10)  # Place the search entry at a fixed position

        self.add_placeholder(self.search_entry, "Cari Prodi Impianmu...")

        self.suggestions_frame = tk.Frame(self.window, bg='white', bd=1, relief='solid')
        self.suggestions_frame.place(x=self.search_entry.winfo_x(), y=self.search_entry.winfo_y() + self.search_entry.winfo_height())

        # Assuming tryu.png and info.png are in the correct directory
        self.fotoA = tk.PhotoImage(file="tryu.png")
        self.fotoB = tk.PhotoImage(file="tryu.png")
        image_path10= 'tryu.png'
        original_image10 = Image.open(image_path10)
        resized_image10 = original_image10.resize((600, 145))
        self.passing_grade1 = ImageTk.PhotoImage(resized_image10)
        self.button_passing1_grade=customtkinter.CTkButton(self.window,image=self.passing_grade1, bg_color="#D6E9FC", fg_color="white",text="", width=300,command=self.passing_grade)
        self.button_passing1_grade.place(x= 540, y=500)

        self.button_tryU = customtkinter.CTkButton(self.window, image=self.fotoA, bg_color="#D6E9FC", fg_color="white", text="", width=300,command=self.formulir)
        self.button_tryU.place(x=540, y=100)
        self.buton_infonesa = customtkinter.CTkButton(self.window, image=self.fotoB, bg_color="#D6E9FC", fg_color="white", text="", width=300, command=self.infonesa)
        self.buton_infonesa.place(x=540, y=300)
        
        # Add a command to update self.search_var when the user presses Enter
        # self.search_entry.bind("<Return>", lambda event: self.update_search_var())
    
        # Add a trace to self.search_var to call update_suggestions when it changes
        # self.search_var.trace("w", self.update_suggestions)





#---------------------search bar dashboard--------------------------#
    def add_placeholder(self, entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry._placeholder = placeholder_text
        entry._placeholder_active = True
 
        def on_focus_in(event):
            if entry._placeholder_active:
                entry.delete(0, "end")
                entry._placeholder_active = False
                entry.config(fg='black')
                self.show_suggestions_frame()

        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry.config(fg='grey')
                entry._placeholder_active = True
                self.hide_suggestions_frame() 

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def update_suggestions(self, *args):
        teks_input = self.search_var.get()
        if not self.suggestions_frame or not self.suggestions_frame.winfo_exists():
            self.suggestions_frame = tk.Frame(self.current_menu, bg='white', height=150, width=300)
        for widget in self.suggestions_frame.winfo_children():
            widget.destroy()
        suggestions = self.sentinel_search(self.kata_kata, teks_input)
        displayed_suggestion = suggestions[:3]

        if suggestions:
            for kata in displayed_suggestion:
                tombol = customtkinter.CTkButton(self.suggestions_frame, text=kata, font=('Arial', 14), anchor='w', command=lambda k=kata: self.select_suggestion(k), width=250)
                tombol.pack(fill='x') 

    def sentinel_search(self, lst, key):
        lst_copy = lst[:] 
        lst_copy.append(key)  
        i = 0
        suggestions = []
        while True:
            if key.lower() in lst_copy[i].lower():
                suggestions.append(lst_copy[i])
            if lst_copy[i] == key:
                break
            i += 1
        return suggestions
    
    def show_suggestions_frame(self, jumlah_kata=0):
        if self.suggestions_frame is None or not self.suggestions_frame.winfo_exists():
            return
        entry_width = self.search_entry.winfo_width()
        tombol_height = 30
        suggestions_frame_height = min(150, jumlah_kata * tombol_height)
        # Tempatkan frame di bawah search entry
        self.suggestions_frame.configure(height=suggestions_frame_height, width=entry_width)
        self.suggestions_frame.place(x=self.search_entry.winfo_x(), y=self.search_entry.winfo_y() + self.search_entry.winfo_height())
        self.suggestions_frame.lift()



#------------------memanggil tentang prodi----------------------#
    def select_suggestion(self, suggestion):
        self.search_var.set(suggestion)
        self.hide_suggestions_frame()

        if suggestion == "Sains Data":
            self.sainsdata1()
        elif suggestion == "Matematika":
            self.matematika1()
        elif suggestion == 'Biologi':
            self.biologi1()
        elif suggestion == "Kimia":
            self.kimia1()
        elif suggestion == "Fisika":
            self.fisika1()
        elif suggestion == "Pendidikan IPA":
            self.pendipa1()
        elif suggestion == "Manajemen":
            self.manajemen1()
        elif suggestion == "Ekonomi":
            self.ekonomi1()
        elif suggestion == "Akutansi":
            self.akutansi1()
        elif suggestion == "Teknik Sipil":
            self.teksip1()
        elif suggestion == "Sistem Informasi":
            self.sisfor1()
        elif suggestion == "Teknik Mesin":
            self.tekmes1()
        elif suggestion == "Pendidikan Guru Sekolah Dasar":
            self.pgsd1()
        elif suggestion == 'Pendidikan Luar Biasa':
            self.plb1()
        elif suggestion == 'Teknologi Pendidikan':
            self.tekpen1()
        elif suggestion == 'Pendidikan Sastra Indonesia':
            self.psasin1()
        elif suggestion == "Pendidikan Bahasa Jerman":
            self.psasjer1()
        elif suggestion == 'Sastra Inggris':
            self.sasing1()
        elif suggestion == 'Pendidikan Jasmani,Kesehatan,dan Rekreasi':
            self.pjkr1()
        elif suggestion == "Pendidikan Kepelatihan Olahraga":
            self.pko1()
        elif suggestion == "Ilmu Keolahragaan":
            self.IO1()
        elif suggestion == 'Kedokteran':
            self.dokter1()
        elif suggestion == 'Hukum':
            self.hukum1()
        elif suggestion == "D4 Teknik Sipil":
            self.teksipvo1()
        elif suggestion == "D4 Tata Busana":
            self.tabus1()
        elif suggestion == "D4 Desain Grafis":
            self.desgraf1()
        
#----------------------- atur animasi masuk --------------------------------#
    def hide_suggestions_frame(self):
        if self.suggestions_frame is not None and self.suggestions_frame.winfo_exists():
            self.suggestions_frame.place_forget()

    def start_timer(self):
        self.duration = 2000
        self.timer = self.window.after(self.duration, self.masukdaftar)
    
    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()




#--------------------------------dashboard mauk /daftar ----------------------#
    def masukdaftar(self):
        self.window.after_cancel(self.timer)
        self.window.title("Click Background")
        self.window.state('zoomed')
        self.window.resizable(0,0)

     
        self.background_images = [
            "welgar.png",
            "Try U.png",
            "Infonesa.png"
        ]
        self.current_background_index = 0

       
        self.canvas = Canvas(self.window, width=1280, height=720)
        self.canvas.pack()
        
        self.daftar_button = customtkinter.CTkButton(self.canvas, text="Daftar", font=("sans serif",20, "bold"), width=650,height=40,command=self.daftar,corner_radius=30)
        self.daftar_button.place(x=300, y=520)
        
        self.masuk_button = customtkinter.CTkButton(self.canvas, text="Masuk", font=("sans serif",20, "bold"), width=650,height=40,command=self.masuk,corner_radius=30)
        self.masuk_button.place(x=300, y=570)
        self.fade_in_background() #efek kedap kedip
        self.canvas.bind("<Button-1>", self.on_click) #menggeser gambar

    def fade_in_background(self, alpha=0):
        if alpha < 1:
            self.canvas.delete("background")

            background_image = Image.open(self.background_images[self.current_background_index])

            background_image.putalpha(int(alpha * 255))

            background_photo = ImageTk.PhotoImage(background_image)

            self.canvas.create_image(0, 0, anchor=NW, image=background_photo, tags="background")
            self.canvas.image = background_photo  

            self.window.after(10, lambda: self.fade_in_background(alpha + 0.05))
        else:
          
            pass

    def next_background(self):  
        self.current_background_index = (self.current_background_index + 1) % len(self.background_images)
        self.fade_in_background()  

    def prev_background(self):
        self.current_background_index = (self.current_background_index - 1) % len(self.background_images)
        self.fade_in_background()  

    def on_click(self, event):
        if event.x > self.canvas.winfo_width() / 2:
            self.next_background()  
        else:
            self.prev_background() 

#------------------------------login-------------------------#
    
    # def login(self):
    #     username = self.username.get()
    #     password = self.password.get()

    #     if 6 <= len(password) <= 20:
    #         try:
    #             with open('dataakun.csv', 'r') as file:
    #                 reader = csv.DictReader(file)
    #                 for row in reader:
    #                     print(f"Checking row: {row}")  # Debugging statement
    #                     if row['Username'] == username and row['Password'] == password:
    #                         messagebox.showinfo("Login", "Login berhasil!")
    #                         self.login_dashboard()
    #                         return  # Keluar dari fungsi setelah login berhasil ditemukan
                    
    #             messagebox.showerror("Login", "Username atau password Invalid!")
    #         except FileNotFoundError:
    #             messagebox.showerror("Login", "File dataakun.csv tidak ditemukan.")
    #         except KeyError as e:
    #             messagebox.showerror("Login", f"KeyError: {str(e)}. Periksa header CSV.")
    #     else:
    #         messagebox.showerror("Login", "Password harus antara 6 sampai 20 karakter.")

    def masuk(self):
        self.canvas.destroy()
        self.window = self.window
        self.bg = PhotoImage(file="masuk.png")
        self.layarmasuk = Label(self.window, image=self.bg)
        self.layarmasuk.place(x=0, y=0, relheight=1, relwidth=1)

        self.label_username = Label(self.window, text="Username", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=150)
        self.entry_username = Entry(self.window, textvariable=self.username,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_username.place(x=370, y=190)

        self.label_password = Label(self.window, text="Password", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=260)
        self.entry_password = Entry(self.window, show='*',textvariable=self.password,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_password.place(x=370, y=300)
            

        self.button_lupapsw = Button(self.window,text="Forgot Password?",bg = "#ffffff", font=("sans serif",10,"underline"),fg="blue",command=self.forgot_password,
                                        highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=360,y=360)
            
            
        showpsw = Checkbutton(self.window, bg="#ffffff", command=self.show_psw, text="show password",font=("sans serif",10))
        showpsw.place(x=360,y=390)

        self.button_login = customtkinter.CTkButton(self.window,text="LOGIN",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#ecf0f3",width=480,height=40,command=self.syarat_login)
        self.button_login.place(x=395,y=450)

        self.button_back = customtkinter.CTkButton(self.window,text="back",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#B5DDF0",width=50,height=40,command=self.back)
        self.button_back.place(x=175,y=50)



    def show_psw(self):
            if self.entry_password.cget("show") == "*":
                self.entry_password.config(show='')
            else:
                self.entry_password.config(show="*")
                
    def forgot_password(self):
        self.window = Toplevel()
        self.window.geometry('500x500')
        self.window.title('Forgot Password')
        self.window.configure(background='#f8f8f8')
        self.window.resizable(0, 0)

        self.new_password_label = Label(self.window, text="New Password", bg="#f8f8f8", font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=125)
        self.new_password_entry = Entry(self.window, show='*', border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.new_password_entry.place(x=50, y=155)

        self.confirm_password_label = Label(self.window, text="Confirm Password", bg="#f8f8f8",
                                        font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=200)
        self.confirm_password_entry = Entry(self.window, show='*', border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.confirm_password_entry.place(x=50, y=230)

        self.submit_button = customtkinter.CTkButton(self.window, text="Submit", font=("sans serif", 12, "bold"), width=350,
                                                command=self.submit_new_password)
        self.submit_button.place(x=50, y=260)    
        

    def submit_new_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password == confirm_password:
            username = self.username.get()
            with open('dataakun.csv', 'r') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            ada_username = False
            for row in rows:
                if row['Username'] == username:
                    ada_username = True
                    row['Password'] = new_password
                    break  # Break setelah menemukan username yang cocok

            if ada_username:
                with open('dataakun.csv', 'w', newline='') as file:
                    fieldnames = ['First Name', 'Last Name', 'Phone', 'Username', 'Password']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                messagebox.showinfo("Password Updated", "Password updated successfully!")
            else:
                messagebox.showerror("Error", "Username tidak terdaftar")
        else:
            messagebox.showerror("Error", "Periksa confirm password Anda")
            
    def daftar(self):
        self.canvas.destroy()
        self.window = self.window
        self.bg = PhotoImage(file="daftar.png")
        self.layardaftar = Label(self.window, image=self.bg)
        self.layardaftar.place(x=0, y=0, relheight=1, relwidth=1)

        self.label_firstname = Label(self.window, text="First Name", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=150)
        self.entry_firstname = Entry(self.window, textvariable=self.firstname,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_firstname.place(x=370, y=190)

        self.label_lastname = Label(self.window, text="Last Name", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=240)
        self.entry_lastname= Entry(self.window,textvariable=self.lastname,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_lastname.place(x=370, y=280)
        
        self.label_phone= Label(self.window, text="Phone Number ", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=330)
        self.entry_phone = Entry(self.window,textvariable=self.phone,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_phone.place(x=370, y=370)
            
        self.label_username= Label(self.window, text="Username ", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=420)
        self.entry_username = Entry(self.window,textvariable=self.username,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_username.place(x=370, y=460)

        self.label_password= Label(self.window, text="Password ", bg = "#ffffff", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=510)
        self.entry_password = Entry(self.window,textvariable=self.password,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
        self.entry_password.place(x=370, y=550)

        
        self.button_login = customtkinter.CTkButton(self.window,text="DAFTAR",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#ecf0f3",width=480,height=40,command=self.daftarakun)
        self.button_login.place(x=395,y=590)

        self.button_back = customtkinter.CTkButton(self.window,text="back",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#B5DDF0",width=50,height=40,command=self.back2)
        self.button_back.place(x=175,y=50)

    def daftarakun(self):
            firstname = self.entry_firstname.get()
            lastname = self.entry_lastname.get()
            phonenumber = self.entry_phone.get()
            username = self.entry_username.get()
            password = self.entry_password.get()

            if not all([firstname, lastname, phonenumber,  username, password]):
                messagebox.showerror("Signup", "Harap isi semua kolom untuk melakukan sign in.")
                return
            elif 6 <= len(password) <= 20:
                with open('dataakun.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Username'] == username and row['Password'] == password:
                            messagebox.showerror("Signup", "Username terdaftar!")
                            return
                        
                with open('dataakun.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([firstname, lastname, phonenumber, username, password])
                messagebox.showinfo("Signup", "Signup berhasil!")

            else:
                messagebox.showerror("Sign Up", "Password must be between 6 and 20 characters.")

    def syarat_login(self):
        username = self.username.get()
        password = self.password.get()

        if 6 <= len(password) <= 20:
            with open('dataakun.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Check if the entered username and password match the ones in the CSV
                    if row['Username'] == username and row['Password'] == password:
                        messagebox.showinfo("Login", "login berhasil")
                        self.login_dashboard()

                        return  # Keluar dari fungsi setelah login berhasil ditemukan
            messagebox.showerror("Login", "Username atau password Invalid!")
        else:
            messagebox.showerror("Login", "Password must be between 6 and 20 characters.")

    
    def back(self):
        global current_screen
        global previous_screen

        current_screen = self.layarmasuk
        previous_screen = self.canvas


        if previous_screen:
            current_screen = previous_screen
            self.masukdaftar()
        else:
            print("Tidak ada layar sebelumnya.")
        
    def back2(self):
        global current_screents
        global previous_screen

        current_screen = self.layardaftar
        previous_screen = self.canvas


        if previous_screen:
            current_screen = previous_screen
            self.masukdaftar()
        else:
            print("Tidak ada layar sebelumnya.")








#____________________________________________PASSING GRADE_________________________________#
    def passing_grade(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"bgpg.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo  # Keep a reference to the image

        self.data = self.baca_data_dari_csv("datapg.csv")

        # Membuat frame utama dengan ukuran yang diatur
        self.frame = Frame(self.current_menu, width=1209, height=650)
        self.frame.place(x=70, y=239)

        # Membuat scrollbar vertikal
        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        # Membuat scrollbar horizontal
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        self.listbox_frame = Frame(self.current_menu, borderwidth=3, background="#FFF9D0")
        self.listbox_frame.place(x=1095, y=239, width=159, height=276)
        self.listbox = Listbox(self.listbox_frame)
        self.listbox.pack(fill=BOTH, expand=True)

        # Mengisi listbox dengan nama fakultas unik
        nama_fakultas = list(set(row["Fakultas"] for row in self.data))
        for fakultas in nama_fakultas:
            self.listbox.insert(END, fakultas)

        # Mengikat pemilihan listbox ke fungsi filter
        self.listbox.bind('<<ListboxSelect>>', self.pecet_listbox_jurusan)

        # Membuat tabel
        columns = list(self.data[0].keys())  # Mendapatkan nama kolom dari data
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings',
                                 yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.tree.pack(fill=BOTH, expand=True)

        # Konfigurasi scrollbar
        self.scrollbar_y.config(command=self.tree.yview)
        self.scrollbar_x.config(command=self.tree.xview)

        # Menambahkan header ke tabel dan mengubah warna
        style = ttk.Style()
        style.configure("Treeview.Heading", background="blue", foreground="black", font=('Helvetica', 12, 'bold'))
        style.map("Treeview.Heading", background=[('active', 'lightblue')])
        style.configure("Treeview", rowheight=30)  # Mengatur tinggi baris

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=0, width=165, anchor='center')  # Mengatur lebar kolom

        # Menambahkan data ke tabel dengan pewarnaan baris
        self.load_data(self.data)

        # Menambahkan gridlines dengan menambahkan tag dan style
        self.tree.tag_configure('oddrow', background='white')
        self.tree.tag_configure('evenrow', background='lightgrey')

    # kecil ke besar
        self.sort_button_utbk = customtkinter.CTkButton(self.current_menu, text="Nilai UTBK", command=self.sort_nilai_utbk, corner_radius=15, bg_color="#FFF9D0")
        self.sort_button_utbk.place(x=105, y=189)
        self.sort_button_peminat = customtkinter.CTkButton(self.current_menu, text="Peminat 2023", command=self.sort_peminat, corner_radius=15, bg_color="#FFF9D0")
        self.sort_button_peminat.place(x=250, y=189)
        self.sort_button_daya_tampung = customtkinter.CTkButton(self.current_menu, text="Daya Tampung 2024", command=self.sort_daya_tampung, corner_radius=15, bg_color="#FFF9D0")
        self.sort_button_daya_tampung.place(x=395, y=189)


    # besar ke kecil
        self.sort_button_utbk_desc = customtkinter.CTkButton(self.current_menu, text="Nilai UTBK", command=self.utbk_besar_ke_kecil, corner_radius=15, bg_color="#FFF9D0")
        self.sort_button_utbk_desc.place(x=610,y=189)   
        self.sort_button_peminat_desc = customtkinter.CTkButton(self.current_menu, text="Peminat 2023", command=self.peminat_besar_ke_kecil, corner_radius=15, bg_color="#FFF9D0")
        self.sort_button_peminat_desc.place(x=755, y=189)
        self.sort_button_dtl_desc = customtkinter.CTkButton(self.current_menu, text="Daya Tampung 2024", command=self.dt_besar_ke_kecil, corner_radius=15, bg_color="#FFF9D0")
        self.sort_button_dtl_desc.place(x=900, y=189)

        # Entry untuk pencarian jurusan
        _entry = customtkinter.CTkEntry(self.current_menu, width=163, corner_radius=15, border_color="#FFF9D0", bg_color="#7fbcd0")
        self.search_entry.place(x=1095, y=163)
        self.add_placeholder1(self.search_entry, "Cari Jurusan...")
        self.search_entry.bind('<Return>', self.search_jurusan)
        # Tombol untuk sorting Peminat
        self.sort_button_peminat = customtkinter.CTkButton(self.searchelf.current_menu, text="Peminat 2023", command=self.sort_peminat, corner_radius=15,bg_color="#FFF9D0")

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def add_placeholder1(self, entry, placeholder_text):
        # Menambahkan placeholder ke entri
        entry.insert(0, placeholder_text)
        entry._placeholder = placeholder_text  # Menyimpan teks placeholder
        entry._placeholder_active = True

        def on_focus_in1(event):
            if entry._placeholder_active:
                entry.delete(0, "end")
                entry._placeholder_active = False
                entry.configure(placeholder_text_color='#4D869C')
               

        def on_focus_out1(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry.configure(placeholder_text_color='grey')
                entry._placeholder_active = True
               
        entry.bind("<FocusIn>", on_focus_in1)
        entry.bind("<FocusOut>", on_focus_out1)

    def baca_data_dari_csv(self, file_path):
        data = []
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if ',' in row["Nilai UTBK"]:
                        row["Nilai UTBK"] = row["Nilai UTBK"].replace(',', '.')
                    if '.' in row["Peminat 2023"]:
                        row["Peminat 2023"] = row["Peminat 2023"].replace('.', '')
                    data.append(row)
        except FileNotFoundError:
            print("File not found.")
        return data

    def pecet_listbox_jurusan(self, event):
    # Mendapatkan indeks dan nama fakultas yang dipilihan
        selection = event.widget.curselection()
        if selection:
            selected_fakultas = event.widget.get(selection[0])

            # Mencari fakultas dengan metode sentinel linear search
            sentinel = {"Fakultas": selected_fakultas}  # Sentinel
            filtered_data = []

            i = 0
            n = len(self.data)

            while i < n:
                if self.data[i]["Fakultas"] == selected_fakultas:
                    filtered_data.append(self.data[i])
                i += 1

            self.load_data(filtered_data)



    def load_data(self, data):
        # Menghapus data yang ada di tabel
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Memuat ulang data awal
        columns = list(data[0].keys())  # Mendapatkan nama kolom dari data
        for index, row in enumerate(data):
            values = [row[col] for col in columns]
            if index % 2 == 0:
                self.tree.insert("", "end", values=values, tags=('evenrow',))
            else:
                self.tree.insert("", "end", values=values, tags=('oddrow',))

    # Fungsi untuk sorting data menggunakan Bubble Sort
    def bubble_sort(self, data, column, order, besar_ke_kecil=False):
        n = len(data)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if order == 1:
                    # Menggunakan kondisi berdasarkan nilai numerik
                    condition = float(data[j][column]) < float(data[j+1][column]) if besar_ke_kecil else float(data[j][column]) > float(data[j+1][column])
                elif order == 2:
                    # Menggunakan kondisi berdasarkan nilai integer
                    condition = int(data[j][column]) < int(data[j+1][column]) if besar_ke_kecil else int(data[j][column]) > int(data[j+1][column])
                if condition:
                    data[j], data[j+1] = data[j+1], data[j]

    def reset_data(self):
        self.load_data(self.data)

    def sort_by_column(self, column, order=1, besar_ke_kecil=False):
        # 'besar_ke_kecil' di sini digunakan untuk mengaktifkan pengurutan besar_ke_kecil jika True
        self.bubble_sort(self.data, column, order, besar_ke_kecil=besar_ke_kecil)
        self.reset_data()

    def sort_nilai_utbk(self):
        self.sort_by_column("Nilai UTBK", 1)

    def utbk_besar_ke_kecil(self):
        self.sort_by_column("Nilai UTBK", 1, besar_ke_kecil=True)

    def sort_peminat(self):
        self.sort_by_column("Peminat 2023", 2)

    def peminat_besar_ke_kecil(self):
        self.sort_by_column("Peminat 2023", 2, besar_ke_kecil=True)

    def sort_daya_tampung(self):
        self.sort_by_column("Daya Tampung 2024", 2)

    def dt_besar_ke_kecil(self):
        self.sort_by_column("Daya Tampung 2024", 2, besar_ke_kecil=True)

    def search_jurusan(self,event):
        search_term = self.search_entry.get().lower()

        # Menambahkan sentinel ke akhir data
        sentinel = {'Jurusan': 'sentinel', 'Nilai UTBK': '', 'Peminat 2023': '', 'Daya Tampung 2024': '', 'Fakultas': ''}
        self.data.append(sentinel)

        # Inisialisasi variabel untuk penanda dan indeks
        found = False
        i = 0

        # Melakukan pencarian sentinel linear search
        while not found and i < len(self.data):
            if self.data[i]["Jurusan"].lower() == search_term:
                found = True
            else:
                i += 1

        # Menghapus sentinel dari akhir data
        self.data.pop()

        # Menampilkan hasil pencarian
        if found:
            self.load_data([self.data[i]])
        else:
            messagebox.showinfo("Informasi", f"Jurusan '{search_term}' tidak ditemukan.")


























#__________________________________________infonesa_____________________________#
    def infonesa(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"16.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        image_path4='UNIVERSITAS NEGERI SURABAYA.png'
        original_image4=Image.open(image_path4)
        image_path1= 'fmipa.png'
        original_image1 = Image.open(image_path1)
        image_path2= 'feb.png'
        original_image2 = Image.open(image_path2)
        image_path3= '8.png'
        original_image3=Image.open(image_path3)
        image_path5="fbs.png"
        original_image5=Image.open(image_path5)
        image_path6="4.png"
        original_image6=Image.open(image_path6)
        image_path7='5.png'
        original_image7=Image.open(image_path7)
        image_path8='6.png'
        original_image8=Image.open(image_path8)
        image_path9='9.png'
        original_image9=Image.open(image_path9)
        image_path10='11.png'
        original_image10=Image.open(image_path10)

    
        # Resize the image
        resized_image1 = original_image1.resize((333, 100))
        resized_image2 = original_image2.resize((333, 100))
        resized_image3 = original_image3.resize((333, 100))
        resized_image4 = original_image4.resize((750,130))
        resized_image5 = original_image5.resize((333,100))
        resized_image6 = original_image6.resize((333,100))
        resized_image7 = original_image7.resize((333,100))
        resized_image8 = original_image8.resize((333,100))
        resized_image9 = original_image9.resize((333,100))
        resized_image10 = original_image10.resize((333,100))

        # Convert the resized image to PhotoImage
        self.fmipa = ImageTk.PhotoImage(resized_image1)
        self.feb = ImageTk.PhotoImage(resized_image2)
        self.ft =ImageTk.PhotoImage(resized_image3)
        self.unesa=ImageTk.PhotoImage(resized_image4)
        self.fbs=ImageTk.PhotoImage(resized_image5)
        self.fip=ImageTk.PhotoImage(resized_image6)
        self.fio=ImageTk.PhotoImage(resized_image7)
        self.fk=ImageTk.PhotoImage(resized_image8)
        self.fh=ImageTk.PhotoImage(resized_image9)
        self.fv=ImageTk.PhotoImage(resized_image10)

        self.button_fmipa=customtkinter.CTkButton(self.current_menu,image=self.fmipa,bg_color="#D6E9FC", fg_color="#081b47", text="", width=333,command=self.infofmipa)
        self.button_fmipa.place(x= 63, y=255)
        self.button_feb=customtkinter.CTkButton(self.current_menu, image=self.feb, bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofeb)
        self.button_feb.place(x= 476, y=255)
        self.button_ft=customtkinter.CTkButton(self.current_menu, image=self.ft, bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infoteknik)
        self.button_ft.place(x= 890, y=255)
        self.button_unesa=customtkinter.CTkButton(self.current_menu, image=self.unesa, bg_color="#D6E9FC", fg_color="#081b47", text="", width=750,command=self.unesa1)
        self.button_unesa.place(x=450,y=48)
        self.button_fbs=customtkinter.CTkButton(self.current_menu, image=self.fbs,bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofbs)
        self.button_fbs.place(x=63,y=400)
        self.button_fip=customtkinter.CTkButton(self.current_menu, image=self.fip,bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofip)
        self.button_fip.place(x=476,y=400)
        self.button_fio=customtkinter.CTkButton(self.current_menu, image=self.fio,bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofio)
        self.button_fio.place(x=890,y=400)
        self.button_fk=customtkinter.CTkButton(self.current_menu, image=self.fk,bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofk)
        self.button_fk.place(x=63,y=545)
        self.button_fh=customtkinter.CTkButton(self.current_menu, image=self.fh,bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofh)
        self.button_fh.place(x=476,y=545)
        self.button_fv=customtkinter.CTkButton(self.current_menu, image=self.fv,bg_color="#D6E9FC", fg_color="#081b47", text="", width=300,command=self.infofv)
        self.button_fv.place(x=890,y=545)

    

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def unesa1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"17.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 
    
        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=260, y=135, width=750, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Visi Unesa:
    
        UNESA memiliki visi menjadi universitas kependidikan yang tangguh, adaptif, dan inovatif yang berbasis kewirausahaan
    
        Misi Unesa:
    
        Menyelenggarakan pendidikan di bidang kependidikan dan nonkependidikan yang berkarakter tangguh, adaptif, dan inovatif yang berbasis kewirausahaan.
        Menyelenggarakan penelitian dan meningkatkan kualitas inovasi di bidang kependidikan dan nonkependidikan yang berbasis kewirausahaan.
        Menyelenggarakan pengabdian kepada masyarakat dan menyebarluaskan inovasi di bidang kependidikan dan nonkependidikan yang berbasis kewirausahaan bagi kesejahteraan masyarakat.
        Menyelenggarakan kegiatan tridharma pergunran tinggi melalui sistem multikampus secara sinergi, terintegrasi, harmonis, dan berkelanjutan dengan memperhatikan keunggulan UNESA.
        Menyelenggarakan tata kelola yang efektif, efisien, transparan, dan akuntabel yang menjamin mutu secara berkelanjutan
        Menyelenggarakan kerja sarna nasional dan internasional yang produktif dalam menciptakan, mengembangkan, dan menyebarluaskan inovasi di bidang kependidikan dan nonkependidikan yang berbasis kewirausahaan.
        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12),state=tk.DISABLED) 


        path='mars.png'
        original_image4=Image.open(path)
        self.mars=ImageTk.PhotoImage(original_image4)
        path1='PIMPINAN UNIVERSITAS.png'
        original_image=Image.open(path1)
        self.pimpinan=ImageTk.PhotoImage(original_image)
        back='kembali.png'
        imageback=Image.open(back)
        resize=imageback.resize((50,50))
        self.back=ImageTk.PhotoImage(resize)
     

        resized_image1 = original_image4.resize((300,160))
        self.mars = ImageTk.PhotoImage(resized_image1)
        resized_image2 = original_image.resize((200,50))
        self.pimpinan = ImageTk.PhotoImage(resized_image2)

        self.button1=customtkinter.CTkButton(self.current_menu,image=self.mars ,bg_color="#D6E9FC", fg_color="#081b47", text="",height=160, width=300,command=self.marsunesa)
        self.button1.place(x=482, y=372)
        self.button2=customtkinter.CTkButton(self.current_menu,image=self.pimpinan, bg_color="#D6E9FC", fg_color="#081b47", text="", height=50, width=200,command=self.rektor)
        self.button2.place(x=532, y=590)
        self.button3=customtkinter.CTkButton(self.current_menu,image=self.back, fg_color="White", height=50, width=50, text="", command=self.infonesa)
        self.button3.place(x=5,y=10)

    def marsunesa(self):
        webbrowser.open("https://youtu.be/9mq_uscrf9c?si=a1-TDoJJH3ZLhUHo")  

    def rektor(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"18.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.unesa1)
        self.button3.place(x=5, y=10)
            

    def infofmipa(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"19.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Visi
        “Fakultas MIPA yang tangguh, adaptif, inovatif, dan kolaboratif berbasis edu-ecopreneurship serta memperoleh rekognisi internasional”

        Misi:

        1. Menyelenggarakan pendidikan berbasis riset di bidang kependidikan dan nonkependidikan MIPA yang adaptif, inovatif, 
        kolaboratif, dan berciri eduecopreneurship;
        2. Menyelenggarakan penelitian dan meningkatkan kualitas inovasi di bidang kependidikan dan 
        nonkependidikan MIPA melalui kolaborasi global;
        3. Menyelenggarakan pengabdian kepada masyarakat dan menyebarluaskan inovasi di bidang kependidikan dan 
        nonkependidikan MIPA untuk pemberdayaan masyarakat;
        4. Menyelenggarakan tata kelola di FMIPA yang efektif, efisien, transparan, dan akuntabel;  
        5. Menjalin kerja sama nasional dan internasional yang produktif untuk menciptakan, mengembangkan, dan 
        menyebarluaskan inovasi di bidang kependidikan dan nonkependidikan MIPA.

        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 


        # Mengatur gaya untuk Combobox
        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Matematika","Biologi","Kimia","Sains Data", "Fisika", "Pendidikan IPA"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=730, y=490)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifmipa)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=660, y=495)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10)

    # Fungsi yang dipanggil saat tombol Next diklik
    def prodifmipa(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Sains Data":
            self.sainsdata()
        elif selected_value == "Biologi":
            self.biologi()
        elif selected_value == "Matematika":
            self.matematika()
        elif selected_value == "Kimia":
            self.kimia()
        elif selected_value == "Fisika":
            self.fisika()
        elif selected_value == "Pendidikan IPA":
            self.pendipa()

    def sainsdata(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"20.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

        Menjadi penyelenggara pendidikan, penelitian dan penerapan ilmu pengetahuan dan teknologi di bidang data science berbasis edu-technoecopreneurship dan bereputasi global.

        MISI

        1. Menyelenggarakan pendidikan penelitian ilmu data yang tangguh, adaptif, inovatif, dan berbasis edu-technopreneurship
        2. Menyelenggarakan dan meningkatkan kualitas penelitian inovasi di bidang data science yang berdaya saing global;
        3. Menyelenggarakan pengabdian kepada masyarakat dan menyebarluaskan inovasi penelitian;
        4. Menyelenggarakan tata kelola pada Program Studi Sarjana Ilmu Data yang efektif, efisien, transparan dan akuntabel;
        5. Menyelenggarakan kerja sama produktif nasional dan internasional untuk menciptakan, mengembangkan dan mendiseminasikan inovasi di bidang ilmu data

        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@sainsdata_unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsada)

        clickable_label = Label(self.current_menu, text="datascience.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websada)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofmipa)
        self.button3.place(x=5, y=10)

    def igsada(self,event):
        webbrowser.open('https://www.instagram.com/sainsdata_unesa/')
    def websada(self,event):
        webbrowser.open('https://datascience.fmipa.unesa.ac.id//')

    def sainsdata1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"20.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

        Menjadi penyelenggara pendidikan, penelitian dan penerapan ilmu pengetahuan dan teknologi di bidang data science berbasis edu-technoecopreneurship dan bereputasi global.

        MISI

        1. Menyelenggarakan pendidikan penelitian ilmu data yang tangguh, adaptif, inovatif, dan berbasis edu-technopreneurship
        2. Menyelenggarakan dan meningkatkan kualitas penelitian inovasi di bidang data science yang berdaya saing global;
        3. Menyelenggarakan pengabdian kepada masyarakat dan menyebarluaskan inovasi penelitian;
        4. Menyelenggarakan tata kelola pada Program Studi Sarjana Ilmu Data yang efektif, efisien, transparan dan akuntabel;
        5. Menyelenggarakan kerja sama produktif nasional dan internasional untuk menciptakan, mengembangkan dan mendiseminasikan inovasi di bidang ilmu data

        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@sainsdata_unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsada)

        clickable_label = Label(self.current_menu, text="datascience.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websada)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def biologi(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"24.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi 
        “Unggul dalam Pendidikan, Kuat dalam Sains”

            Misi

        1.Menyelenggarakan pendidikan dan pembelajaran yang berpusat pada peserta didik dengan menggunakan pendekatan pembelajaran dan teknologi yang efektif
        2.Menyelenggarakan penelitian di bidang pendidikan, ilmu pengetahuan alam, ilmu sosial dan budaya, seni, dan/atau olahraga, dan pengembangan teknologi yang temuannya bermanfaat bagi pengembangan ilmu pengetahuan dan kesejahteraan masyarakat.
        3.Menyebarluaskan ilmu pengetahuan, teknologi, seni, budaya, dan olah raga, serta hasil-hasil penelitian melalui pengabdian kepada masyarakat yang berorientasi pada pemberdayaan dan pembiasaan masyarakat.
        4.Mewujudkan Universitas Negeri Surabaya sebagai pusat pendidikan tidak hanya pendidikan dasar dan menengah tetapi juga pusat keilmuan yang berlandaskan nilai-nilai luhur budaya bangsa.
        5.Menyelenggarakan tata kelola yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan mutu.
        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@sbiologinanasmerah",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igbio)

        clickable_label = Label(self.current_menu, text="s1-biologi.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webbio)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofmipa)
        self.button3.place(x=5, y=10)

    def igbio(self,event):
        webbrowser.open('https://www.instagram.com/biologinanasmerah?igsh=MWg4cWgwb21naXYzag==')
    def webbio(self,event):
        webbrowser.open('https://s1-biologi.fmipa.unesa.ac.id/')

    def biologi1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"24.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi 
        “Unggul dalam Pendidikan, Kuat dalam Sains”

            Misi

        1.Menyelenggarakan pendidikan dan pembelajaran yang berpusat pada peserta didik dengan menggunakan pendekatan pembelajaran dan teknologi yang efektif
        2.Menyelenggarakan penelitian di bidang pendidikan, ilmu pengetahuan alam, ilmu sosial dan budaya, seni, dan/atau olahraga, dan pengembangan teknologi yang temuannya bermanfaat bagi pengembangan ilmu pengetahuan dan kesejahteraan masyarakat.
        3.Menyebarluaskan ilmu pengetahuan, teknologi, seni, budaya, dan olah raga, serta hasil-hasil penelitian melalui pengabdian kepada masyarakat yang berorientasi pada pemberdayaan dan pembiasaan masyarakat.
        4.Mewujudkan Universitas Negeri Surabaya sebagai pusat pendidikan tidak hanya pendidikan dasar dan menengah tetapi juga pusat keilmuan yang berlandaskan nilai-nilai luhur budaya bangsa.
        5.Menyelenggarakan tata kelola yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan mutu.

        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@sbiologinanasmerah",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igbio)

        clickable_label = Label(self.current_menu, text="s1-biologi.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webbio)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def matematika(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"21.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        “Pada tahun 2025 menjadi Program Studi S1 Matematika bereputasi dalam menghasilkan matematikawan yang kukuh dalam keilmuan, unggul dalam persaingan di dunia kerja, dan berjiwa techno – ecopreneur – maths.”

            Misi
        Dalam rangka mewujudkan visi yang telah ditetapkan, Program Studi S1 Matematika mengemban misi sebagai berikut:
        1. Pendidikan:
         Menyelenggarakan pengelolaan pendidikan yang akuntabel dengan mengedepankan pembelajaran matematika yang berkualitas, efisien, inovatif dan sesuai kebutuhan stakeholders.
         Menghasilkan lulusan yang beriman, cerdas, mandiri, jujur, peduli dan tanggap terhadap lingkungan sekitar, serta memiliki pemahaman yang baik dalam bidang keilmuan matematika dan terapannya, dan mampu memanfaatkan teknologi, sehingga mampu berperan, berkolaborasi dan berkompetisi di dunia kerja baik berwirausaha ataupun bekerja dalam suatu lembaga.
        2. Penelitian
         Melaksanakan penelitian di bidang matematika baik teori ataupun terapannya yang relevan dengan perkembangan IPTEK dan memberikan kontribusi terhadap peningkatan daya saing bangsa Indonesia.
        3. Pengabdian pada Masyarakat 
         Melaksanakan kerjasama dengan berbagai instansi dan masyarakat untuk penerapan ilmu matematika guna meningkatkan kesejahteraan dan martabat bangsa.
        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himatikaunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igmat)

        clickable_label = Label(self.current_menu, text="s1-matematika.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webmat)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofmipa)
        self.button3.place(x=5, y=10)   

    def igmat(self,event):
        webbrowser.open('https://www.instagram.com/sainsdata_unesa/')
    def webmat(self,event):
        webbrowser.open('https://datascience.fmipa.unesa.ac.id//')

    def matematika1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"21.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        “Pada tahun 2025 menjadi Program Studi S1 Matematika bereputasi dalam menghasilkan matematikawan yang kukuh dalam keilmuan, unggul dalam persaingan di dunia kerja, dan berjiwa techno – ecopreneur – maths.”

            Misi
        Dalam rangka mewujudkan visi yang telah ditetapkan, Program Studi S1 Matematika mengemban misi sebagai berikut:
        1. Pendidikan:
        Menyelenggarakan pengelolaan pendidikan yang akuntabel dengan mengedepankan pembelajaran matematika yang berkualitas, efisien, inovatif dan sesuai kebutuhan stakeholders.
        Menghasilkan lulusan yang beriman, cerdas, mandiri, jujur, peduli dan tanggap terhadap lingkungan sekitar, serta memiliki pemahaman yang baik dalam bidang keilmuan matematika dan terapannya, dan mampu memanfaatkan teknologi, sehingga mampu berperan, berkolaborasi dan berkompetisi di dunia kerja baik berwirausaha ataupun bekerja dalam suatu lembaga.
        2. Penelitian
        Melaksanakan penelitian di bidang matematika baik teori ataupun terapannya yang relevan dengan perkembangan IPTEK dan memberikan kontribusi terhadap peningkatan daya saing bangsa Indonesia.
        3. Pengabdian pada Masyarakat 
        Melaksanakan kerjasama dengan berbagai instansi dan masyarakat untuk penerapan ilmu matematika guna meningkatkan kesejahteraan dan martabat bangsa.
        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himatikaunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igmat)

        clickable_label = Label(self.current_menu, text="s1-matematika.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webmat)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)       
        

    def kimia(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"22.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Program studi Sarjana Kimia:
        Pada tahun 2020, menjadi Program Studi yang unggul dan kompetitif di tingkat nasional  dalam bidang kimia berbasis penelitian dalam pengembangan sumber daya alam yang berwawasan lingkungan.

            Misi Program studi Sarjana Kimia:
        Menyelenggarakan pendidikan akademik di bidang kimia berbasis hasil penelitian sumber daya alam yang berwawasan lingkungan.
        Mengembangkan penelitian dasar dan terapan yang inovatif dalam bidang kimia untuk mengembangkan sumber daya alam yang berwawasan lingkungan
        Mendarmabaktikan keahlian dalam bidang ilmu kimia dan terapannya untuk memberdayakan masyarakat
        Membangun dan memperluas jejaring kerjasama yang baik dengan berbagai lembaga/ instansi pemerintah maupun swasta  dan stakeholders untuk keberlanjutan pengembangan program studi kimia.
        Mewujudkan sistem tatakelola Program studi kimia yang kredibel, transparan, akuntabel, bertanggungjawab dan adil.
        Melaksanakan kerjasama dengan berbagai instansi dan masyarakat untuk penerapan ilmu matematika guna meningkatkan kesejahteraan dan martabat bangsa.
            """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmkunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igkim)

        clickable_label = Label(self.current_menu, text="s1-kimia.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webkim)
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofmipa)
        self.button3.place(x=5, y=10)  

    def igkim(self,event):
        webbrowser.open('https://www.instagram.com/hmkunesa?igsh=cjhuM3Q3cmpnd3Bs')
    def webkim(self,event):
        webbrowser.open('https://s1-kimia.fmipa.unesa.ac.id/page/visi-dan-misi')

    def kimia1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"22.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo 

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Program studi Sarjana Kimia:

        Pada tahun 2020, menjadi Program Studi yang unggul dan kompetitif di tingkat nasional  dalam bidang kimia berbasis penelitian dalam pengembangan sumber daya alam yang berwawasan lingkungan.

            Misi Program studi Sarjana Kimia:
        Menyelenggarakan pendidikan akademik di bidang kimia berbasis hasil penelitian sumber daya alam yang berwawasan lingkungan.
        Mengembangkan penelitian dasar dan terapan yang inovatif dalam bidang kimia untuk mengembangkan sumber daya alam yang berwawasan lingkungan
        Mendarmabaktikan keahlian dalam bidang ilmu kimia dan terapannya untuk memberdayakan masyarakat
        Membangun dan memperluas jejaring kerjasama yang baik dengan berbagai lembaga/ instansi pemerintah maupun swasta  dan stakeholders untuk keberlanjutan pengembangan program studi kimia.
        Mewujudkan sistem tatakelola Program studi kimia yang kredibel, transparan, akuntabel, bertanggungjawab dan adil. 
        Melaksanakan kerjasama dengan berbagai instansi dan masyarakat untuk penerapan ilmu matematika guna meningkatkan kesejahteraan dan martabat bangsa.
        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmkunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igkim)

        clickable_label = Label(self.current_menu, text="s1-kimia.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webkim)
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)  

    def fisika(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"23.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi :
        “Terwujudnya program studi yang unggul dalam bidang fisika dan terapannya pada tahun 2035”

            Misi :
        Menyelenggarakan pndidikan dan pembelajaran berbasis HOTS (High Order Thinking Skill) untuk berinovasi dan pemecahan masalah, untuk menghasilkan lulusan berpikir kritis dan kreatif untuk memecahkan masalah dalam bidangnya, berinovasi, berkarakter unggul, berjiwa wirausaha, dan berwawasan lingkungan;
        Mendukung penguatan keilmuan dibidang fisika pada Program Studi Pendidikan Fisika sesuai dengan dasar perluasan mandat (wider mandate) Universitas Negeri Surabaya;
        Menyelenggarakan penelitian fisika dan terapannya berbasis keunggulan lokal yang diakui secara nasional dan internasioanal;
        Menyelenggarakan pengabdian kepada masyarakat berbasis hasil-hasil penelitian  fisika dan terapannya dan mendukung kesejahteraan masyarakat;
        Menyelenggarakan sistem tata pamong dan pengelolaan prodi yang kredibel, transparan, akuntabel, bertanggung jawab, dan adil berbasis sistem penjaminan mutu berjenjang untuk peningkatan kualitas prodi yang berkelanjutan dan berkesinambungan;
        Membangun jejaring kerjasama dengan stakeholder dan alumni yang saling menguntungkan untuk kesejahteraan masyarakat untuk peningkatan kapasitas dan pencitraan Prodi Fisika berdasarkan prinsip tata pamong dan pengelolaan organisasi yang baik.        """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@fisika.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igfis)

        clickable_label = Label(self.current_menu, text="s1-fisika.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webfis)        
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofmipa)
        self.button3.place(x=5, y=10)    

    def igfis(self,event):
        webbrowser.open('https://www.instagram.com/fisika.unesa?igsh=N3RsbGFlaTY5NTB1')
    def webfis(self,event):
        webbrowser.open('https://s1-fisika.fmipa.unesa.ac.id/page/visi-dan-misi')  

    def fisika1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"23.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi :
        “Terwujudnya program studi yang unggul dalam bidang fisika dan terapannya pada tahun 2035”

            Misi :
        Menyelenggarakan pndidikan dan pembelajaran berbasis HOTS (High Order Thinking Skill) untuk berinovasi dan pemecahan masalah, untuk menghasilkan lulusan berpikir kritis dan kreatif untuk memecahkan masalah dalam bidangnya, berinovasi, berkarakter unggul, berjiwa wirausaha, dan berwawasan lingkungan;
        Mendukung penguatan keilmuan dibidang fisika pada Program Studi Pendidikan Fisika sesuai dengan dasar perluasan mandat (wider mandate) Universitas Negeri Surabaya;
        Menyelenggarakan penelitian fisika dan terapannya berbasis keunggulan lokal yang diakui secara nasional dan internasioanal;
        Menyelenggarakan pengabdian kepada masyarakat berbasis hasil-hasil penelitian  fisika dan terapannya dan mendukung kesejahteraan masyarakat;
        Menyelenggarakan sistem tata pamong dan pengelolaan prodi yang kredibel, transparan, akuntabel, bertanggung jawab, dan adil berbasis sistem penjaminan mutu berjenjang untuk peningkatan kualitas prodi yang berkelanjutan dan berkesinambungan;
        Membangun jejaring kerjasama dengan stakeholder dan alumni yang saling menguntungkan untuk kesejahteraan masyarakat untuk peningkatan kapasitas dan pencitraan Prodi Fisika berdasarkan prinsip tata pamong dan pengelolaan organisasi yang baik. """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@fisika.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igfis)

        clickable_label = Label(self.current_menu, text="s1-fisika.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webfis)        
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)     
        
    def pendipa(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"25.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Prodi S1 Pendidikan Sains:
        “Unggul dalam Pendidikan Sains”

            Jabaran visi tersebut adalah sebagai berikut:
        Unggul dalam layanan,
        Unggul dalam inovasi pendidikan Sains.
        Unggul dalam mutu lulusan (berkarakter, berwawasan lingkungan, dan berjiwa wirausaha).
        Unggul dalam penelitian dan pengabdian di bidang pendidikan Sains.

            Misi Prodi S1 Pendidikan Sains:
        Menyelenggarakan pendidikan Sains yang inovatif dan berbasis riset untuk menghasilkan lulusan yang berwawasan lingkungan, berjiwa wirausaha dan memiliki daya saing global.
        Menyelenggarakan penelitian pendidikan Sains yang diakui secara nasional.
        Menyelenggarakan pengabdian masyarakat berbasis riset untuk menunjang kesejahteraan masyarakat.
        Membangun jejaring kerjasama yang kuat dengan stakeholders untuk peningkatan mutu dan pencitraan pendidikan Sains. """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmppipaunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpipa)

        clickable_label = Label(self.current_menu, text="pendidikan-sains.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpipa)          
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofmipa)
        self.button3.place(x=5, y=10) 

    def igpipa(self,event):
        webbrowser.open('https://www.instagram.com/hmppipaunesa?igsh=a24wenR1NmtpdmNp')
    def webpipa(self,event):
        webbrowser.open('https://pendidikan-sains.fmipa.unesa.ac.id/page/visi-dan-misi') 

    def pendipa1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"25.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo  

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Prodi S1 Pendidikan Sains:
        “Unggul dalam Pendidikan Sains”

            Jabaran visi tersebut adalah sebagai berikut:
        Unggul dalam layanan,
        Unggul dalam inovasi pendidikan Sains.
        Unggul dalam mutu lulusan (berkarakter, berwawasan lingkungan, dan berjiwa wirausaha).
        Unggul dalam penelitian dan pengabdian di bidang pendidikan Sains.

            Misi Prodi S1 Pendidikan Sains:
        Menyelenggarakan pendidikan Sains yang inovatif dan berbasis riset untuk menghasilkan lulusan yang berwawasan lingkungan, berjiwa wirausaha dan memiliki daya saing global.
        Menyelenggarakan penelitian pendidikan Sains yang diakui secara nasional.
        Menyelenggarakan pengabdian masyarakat berbasis riset untuk menunjang kesejahteraan masyarakat.
        Membangun jejaring kerjasama yang kuat dengan stakeholders untuk peningkatan mutu dan pencitraan pendidikan Sains. """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmppipaunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpipa)

        clickable_label = Label(self.current_menu, text="pendidikan-sains.fmipa.unesa.ac.id",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpipa)          
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10) 

    def infofeb(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"26.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        Menjadi Fakultas Ekonomi dan Bisnis yang bereputasi global dalam bidang pendidikan ekonomi, ilmu ekonomi, dan bisnis berdasarkan kepemimpinan kewirausahaan pada tahun 2040

            Misi 
        1. Meningkatkan mutu program pendidikan sarjana, magister, doktoral, dan profesi pada bidang pendidikan ekonomi, ekonomi, dan bisnis. 
        2. Meningkatkan kualitas penelitian bereputasi di bidang pendidikan ekonomi, ilmu ekonomi, dan bisnis yang berkontribusi terhadap pengembangan ilmu pengetahuan dan teknologi. 
        3. Meningkatkan kualitas pelayanan masyarakat yang bereputasi pada bidang pendidikan ekonomi, ekonomi dan bisnis. 
        4. Meningkatkan Good College Governance dalam pengelolaan organisasi dan jaringan kerjasama dengan pemangku kepentingan dalam dan luar negeri. 
        5. Meningkatkan daya saing mahasiswa dan lulusan yang berjiwa wirausaha-kepemimpinan. """
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Manajemen","Ekonomi","Akutansi"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifeb)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifeb(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Manajemen":
            self.manajemen()
        elif selected_value == "Ekonomi":
            self.ekonomi()
        elif selected_value == "Akutansi":
            self.akutansi()
        

    def manajemen(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"27.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        “Menjadi program studi yang berdaya saing dalam pendidikan dan pengembangan ilmu manajemen berbasis kepemimpinan kewirausahaan dan etika bisnis di Asia Tenggara pada tahun 2025”

            Misi
        Menyelenggarakan pendidikan ilmu manajemen yang berbasis pada kepemimpinan kewirausahaan dan etika bisnis.
        Menyelenggarakan penelitian di bidang manajemen yang berlandaskan kepemimpinan wirausaha dan etika bisnis.
        Menyelenggarakan pengabdian kepada masyarakat berdasarkan kepemimpinan kewirausahaan dan etika bisnis.
        Menyelenggarakan pengelolaan program studi berdasarkan prinsip tata kelola universitas yang baik.
        Membangun kerjasama dengan pemangku kepentingan dalam dan luar negeri. """
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@manajemenunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpmanaj)

        clickable_label = Label(self.current_menu, text="manajemen.feb.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webmanaj)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofeb)
        self.button3.place(x=5, y=10)  

    def igpmanaj(self,event):
        webbrowser.open('https://www.instagram.com/manajemenunesa?igsh=MWFnYXlwNDNhNXZlMg==')
    def webmanaj(self,event):
        webbrowser.open('https://manajemen.feb.unesa.ac.id/')

    def manajemen1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"27.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        “Menjadi program studi yang berdaya saing dalam pendidikan dan pengembangan ilmu manajemen berbasis kepemimpinan kewirausahaan dan etika bisnis di Asia Tenggara pada tahun 2025”

            Misi
        Menyelenggarakan pendidikan ilmu manajemen yang berbasis pada kepemimpinan kewirausahaan dan etika bisnis.
        Menyelenggarakan penelitian di bidang manajemen yang berlandaskan kepemimpinan wirausaha dan etika bisnis.
        Menyelenggarakan pengabdian kepada masyarakat berdasarkan kepemimpinan kewirausahaan dan etika bisnis.
        Menyelenggarakan pengelolaan program studi berdasarkan prinsip tata kelola universitas yang baik.
        Membangun kerjasama dengan pemangku kepentingan dalam dan luar negeri. """
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@manajemenunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpmanaj)

        clickable_label = Label(self.current_menu, text="manajemen.feb.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webmanaj)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10) 

    def ekonomi(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"29.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = B", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            VISI PROGRAM STUDI
        “Menjadi Program Studi Ilmu Ekonomi Berbasis Ekonomi Terapan Terkemuka di Asia Tenggara pada tahun 2025”
            VISI ILMIAH
        “Menyelenggarakan Pembelajaran di Bidang Ekonomi, Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan Bereputasi di Asia Tenggara”
            MISI
        Memberikan Pendidikan Ilmu Ekonomi Berbasis Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan
        Menyelenggarakan Penelitian Ilmu Ekonomi Berbasis Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan
        Menyelenggarakan Pengabdian kepada Masyarakat Bidang Ekonomi Berbasis Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan
        Menjalin Kerjasama dengan Stakeholder dalam dan luar negeri
        Menyelenggarakan Tata Kelola Program Studi Sesuai dengan Prinsip Good University Governance """
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@ekonomifebunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpeko)

        clickable_label = Label(self.current_menu, text="ekonomi.feb.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webeko)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofeb)
        self.button3.place(x=5, y=10)  

    def igpeko(self,event):
        webbrowser.open('https://www.instagram.com/ekonomifebunesa?igsh=MXd3NXA5b3VtYnVl')
    def webeko(self,event):
        webbrowser.open('https://ekonomi.feb.unesa.ac.id/')

    def ekonomi1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"29.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = B", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            VISI PROGRAM STUDI
        “Menjadi Program Studi Ilmu Ekonomi Berbasis Ekonomi Terapan Terkemuka di Asia Tenggara pada tahun 2025”
            VISI ILMIAH
        “Menyelenggarakan Pembelajaran di Bidang Ekonomi, Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan Bereputasi di Asia Tenggara”
            MISI
        Memberikan Pendidikan Ilmu Ekonomi Berbasis Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan
        Menyelenggarakan Penelitian Ilmu Ekonomi Berbasis Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan
        Menyelenggarakan Pengabdian kepada Masyarakat Bidang Ekonomi Berbasis Perencanaan Pembangunan, Ekonomi Publik, Ekonomi Moneter dan Perbankan
        Menjalin Kerjasama dengan Stakeholder dalam dan luar negeri
        Menyelenggarakan Tata Kelola Program Studi Sesuai dengan Prinsip Good University Governance """
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@ekonomifebunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpeko)

        clickable_label = Label(self.current_menu, text="ekonomi.feb.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webeko)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)         
        
    def akutansi(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"28.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
           Visi
        Menjadi Program Studi Ilmu Akuntansi Terkemuka di Asia Tenggara pada tahun 2023

            Misi
        Meningkatkan mutu pendidikan sarjana akuntansi
        Meningkatkan potensi mahasiswa dan lulusan yang berjiwa kepemimpinan-wirausaha
        Penelitian di bidang akuntansi yang bereputasi dan berkontribusi terhadap perkembangan ilmu pengetahuan dan teknologi
        Meningkatkan kualitas pelayanan kepada masyarakat di bidang akuntansi yang bereputasi.
        Mendukung penerapan Good Department Governance dalam mengelola kerjasama organisasi dan jaringan dengan pemangku kepentingan nasional dan internasional. """
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@akutansiunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpakun)

        clickable_label = Label(self.current_menu, text="akuntansi.feb.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webakun)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofeb)
        self.button3.place(x=5, y=10)  

    def igpakun(self,event):
        webbrowser.open('https://www.instagram.com/akuntansiunesa?igsh=MWk5bjducXNraTVibA==')
    def webakun(self,event):
        webbrowser.open('https://akuntansi.feb.unesa.ac.id/')

    def akutansi1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"28.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
           Visi
        Menjadi Program Studi Ilmu Akuntansi Terkemuka di Asia Tenggara pada tahun 2023

            Misi
        Meningkatkan mutu pendidikan sarjana akuntansi
        Meningkatkan potensi mahasiswa dan lulusan yang berjiwa kepemimpinan-wirausaha
        Penelitian di bidang akuntansi yang bereputasi dan berkontribusi terhadap perkembangan ilmu pengetahuan dan teknologi
        Meningkatkan kualitas pelayanan kepada masyarakat di bidang akuntansi yang bereputasi.
        Mendukung penerapan Good Department Governance dalam mengelola kerjasama organisasi dan jaringan dengan pemangku kepentingan nasional dan internasional. """
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@akutansiunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpakun)

        clickable_label = Label(self.current_menu, text="akuntansi.feb.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webakun)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)


    def infoteknik(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"30.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Fakultas Teknik Universitas Negeri Surabaya
        "Fakultas Yang Tangguh, Adaptif, dan Inovatif Dalam Keilmuan Bidang Teknologi dan Pendidikan Kejuruan Berorientasi Kewirausahaan"

            Misi Fakultas Teknik Universitas Negeri Surabaya 
        Menyelenggarakan kualitas pendidikan di bidang teknologi dan pendidikan kejuruan yang berkarakter tangguh, adaptif, dan inovatif.
        Mengembangkan penelitian di bidang teknologi dan pendidikan kejuruan menuju hilirisasi produk inovasi dan berorientasi kewirausahaan.
        Mengembangkan pengabdian kepada masyarakat dengan menyebarluaskan inovasi di bidang teknologi dan pendidikan kejuruan berorientasi kewirausahaan bagi kesejahteraan masyarakat.
        Meningkatkan kegiatan tridharma perguruan tinggi melalui sistem multikampus secara sinergi, terintegrasi, harmonis, dan berkelanjutan dengan memperhatikan keunggulan UNESA dan Fakultas.
        Meningkatkan tata kelola yang efektif, efisien, transparan, dan akuntabel yang menjamin mutu secara berkelanjutan
        Meningkatkan kerja sama nasional dan internasional yang produktif dalam bidang teknologi dan pendidikan kejuruan untuk meningkatkan rekognisi kegiatan tridharma."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Teknik Sipil","Sistem Informasi","Teknik Mesin"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.proditeknik)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def proditeknik(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Teknik Sipil":
            self.teksip()
        elif selected_value == "Sistem Informasi":
            self.sisfor()
        elif selected_value == "Teknik Mesin":
            self.tekmes()

    def teksip(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"31.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = B", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        Kami menghasilkan lulusan teknik sipil yang profesional di bidang pelaksanaan pekerjaan teknik sipil dan siap bersaing secara internasional pada tahun 2035.

            Misi
        Menyelenggarakan pendidikan untuk menghasilkan lulusan teknik sipil yang mempunyai keahlian di bidang pekerjaan teknik sipil yang profesional, ramah lingkungan, berjiwa wirausaha, berorientasi pada keselamatan kerja, dan siap bersaing secara nasional dan internasional.
        Menyelenggarakan kegiatan penelitian di bidang teknik sipil yang ramah lingkungan dan dilandasi semangat profesionalisme.
        Menyelenggarakan kegiatan pengabdian kepada masyarakat bidang teknik sipil untuk menjalin kerjasama dan meningkatkan tanggung jawab sosial kepada masyarakat.
        Membangun suasana akademik dan tata kelola yang unggul untuk mendukung dan menjamin pelaksanaan program.
        Meningkatkan kerjasama dengan instansi lain yang melaksanakan pekerjaan teknik sipil di dalam dan luar negeri."""
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmrts.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpteksip)

        clickable_label = Label(self.current_menu, text="sipil.ft.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webteksip)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infoteknik)
        self.button3.place(x=5, y=10)  

    def igpteksip(self,event):
        webbrowser.open('https://www.instagram.com/hmrts.unesa?igsh=cTIzd3E4bjVydDVu')
    def webteksip(self,event):
        webbrowser.open('https://sipil.ft.unesa.ac.id/')

    def teksip1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"31.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = B", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi
        Kami menghasilkan lulusan teknik sipil yang profesional di bidang pelaksanaan pekerjaan teknik sipil dan siap bersaing secara internasional pada tahun 2035.

            Misi
        Menyelenggarakan pendidikan untuk menghasilkan lulusan teknik sipil yang mempunyai keahlian di bidang pekerjaan teknik sipil yang profesional, ramah lingkungan, berjiwa wirausaha, berorientasi pada keselamatan kerja, dan siap bersaing secara nasional dan internasional.
        Menyelenggarakan kegiatan penelitian di bidang teknik sipil yang ramah lingkungan dan dilandasi semangat profesionalisme.
        Menyelenggarakan kegiatan pengabdian kepada masyarakat bidang teknik sipil untuk menjalin kerjasama dan meningkatkan tanggung jawab sosial kepada masyarakat.
        Membangun suasana akademik dan tata kelola yang unggul untuk mendukung dan menjamin pelaksanaan program.
        Meningkatkan kerjasama dengan instansi lain yang melaksanakan pekerjaan teknik sipil di dalam dan luar negeri."""
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmrts.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpteksip)

        clickable_label = Label(self.current_menu, text="sipil.ft.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webteksip)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def sisfor(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"32.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik Sekali", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=470, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Program Studi S1 Sistem Infromasi
        “Program Studi yang menjadi pusat penelitian dan pengembangan keahlian Sistem Informasi yang unggul secara keilmuan dan keahlian teknis yang relevan dengan kebutuhan pasar kerja nasional dan global serta berkontribusi di bidang Sistem Informasi Indonesia.”

            Misi
        Menyelenggarakan proses pendidikan Sistem Informasi yang berlandaskan keilmuan Sistem Informasi yang berorientasi pada kebutuhan terkini.
        Menyelenggarakan penelitian dan pengembangan ilmu untuk menghasilkan karya akademik yang unggul dan menjadi rujukan dalam keilmuan Sistem Informasi.
        Mengembangkan produktivitas tenaga pendidik dalam rangka menerapkan Tridharma sehingga mampu meningkatkan nilai tambah sumber daya Sistem Informasi Indonesia.
        Secara aktif Menjalin kerjasama dan kolaborasi dengan dunia usaha/industri dan lembaga profesi baik dalam tingkat lokal, regional, nasional dan internasional untuk penerapan dan pengembangan keilmuan Sistem  Informasi."""
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@si.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsisfor)

        clickable_label = Label(self.current_menu, text="si.ft.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websisfor)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infoteknik)
        self.button3.place(x=5, y=10)  

    def igsisfor(self,event):
        webbrowser.open('https://www.instagram.com/si_unesa?igsh=Nnlqa3QzcXR2NWZm')
    def websisfor(self,event):
        webbrowser.open('https://si.ft.unesa.ac.id/')

    def sisfor1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"32.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik Sekali", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=470, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Program Studi S1 Sistem Informasi
        “Program Studi yang menjadi pusat penelitian dan pengembangan keahlian Sistem Informasi yang unggul secara keilmuan dan keahlian teknis yang relevan dengan kebutuhan pasar kerja nasional dan global serta berkontribusi di bidang Sistem Informasi Indonesia.”

            Misi
        Menyelenggarakan proses pendidikan Sistem Informasi yang berlandaskan keilmuan Sistem Informasi yang berorientasi pada kebutuhan terkini.
        Menyelenggarakan penelitian dan pengembangan ilmu untuk menghasilkan karya akademik yang unggul dan menjadi rujukan dalam keilmuan Sistem Informasi.
        Mengembangkan produktivitas tenaga pendidik dalam rangka menerapkan Tridharma sehingga mampu meningkatkan nilai tambah sumber daya Sistem Informasi Indonesia.
        Secara aktif Menjalin kerjasama dan kolaborasi dengan dunia usaha/industri dan lembaga profesi baik dalam tingkat lokal, regional, nasional dan internasional untuk penerapan dan pengembangan keilmuan Sistem  Informasi."""
        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@si.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsisfor)

        clickable_label = Label(self.current_menu, text="si.ft.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websisfor)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def tekmes(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"33.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=500, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Ilmiah
        Menjadi program studi Sarjana Teknik Mesin yang unggul di bidang teknik energi baru dan terbarukan yang berwawasan lingkungan dan berwirausaha.
        
            Misi
        Menyelenggarakan program pendidikan bidang teknik mesin yang unggul di bidang teknik energi baru terbarukan yang berwawasan lingkungan sehingga mampu memenuhi kebutuhan tenaga profesional dan kreatif di bidang teknik mesin tingkat nasional, serta mempunyai semangat kewirausahaan.
        Menyelenggarakan dan mengembangkan ilmu teknik mesin yang unggul dalam bidang rekayasa energi baru terbarukan melalui kegiatan penelitian, dan diarahkan pada pengembangan teknologi mutakhir dan ramah lingkungan.
        Menyelenggarakan dan mengembangkan penerapan ilmu teknik mesin yang unggul dalam bidang teknik energi baru dan terbarukan melalui kegiatan pengabdian kepada masyarakat, untuk mendukung peningkatan kualitas proses produksi dan produk pada usaha kecil dan menengah;
        Mengembangkan kerjasama kemitraan yang sinergis dengan usaha kecil dan menengah (UKM dan dunia industri) di bidang teknik mesin dalam negeri"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@s1_teknikmesinunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igtekmes)

        clickable_label = Label(self.current_menu, text="mesin.ft.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webtekmes)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infoteknik)
        self.button3.place(x=5, y=10)  

    def igtekmes(self,event):
        webbrowser.open('https://www.instagram.com/s1_teknikmesinunesa?igsh=aThybXRnNHE3MTBh')
    def webtekmes(self,event):
        webbrowser.open('https://mesin.ft.unesa.ac.id/')

    def tekmes1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"33.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=500, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            Visi Ilmiah
        Menjadi program studi Sarjana Teknik Mesin yang unggul di bidang teknik energi baru dan terbarukan yang berwawasan lingkungan dan berwirausaha.
        
            Misi
        Menyelenggarakan program pendidikan bidang teknik mesin yang unggul di bidang teknik energi baru terbarukan yang berwawasan lingkungan sehingga mampu memenuhi kebutuhan tenaga profesional dan kreatif di bidang teknik mesin tingkat nasional, serta mempunyai semangat kewirausahaan.
        Menyelenggarakan dan mengembangkan ilmu teknik mesin yang unggul dalam bidang rekayasa energi baru terbarukan melalui kegiatan penelitian, dan diarahkan pada pengembangan teknologi mutakhir dan ramah lingkungan.
        Menyelenggarakan dan mengembangkan penerapan ilmu teknik mesin yang unggul dalam bidang teknik energi baru dan terbarukan melalui kegiatan pengabdian kepada masyarakat, untuk mendukung peningkatan kualitas proses produksi dan produk pada usaha kecil dan menengah;
        Mengembangkan kerjasama kemitraan yang sinergis dengan usaha kecil dan menengah (UKM dan dunia industri) di bidang teknik mesin dalam negeri"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@s1_teknikmesinunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igtekmes)

        clickable_label = Label(self.current_menu, text="mesin.ft.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webtekmes)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10) 
        
    def infofbs(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"38.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            VISI

FBS UNESA menjadi fakultas yang tangguh, adaptif, dan inovatif dalam bidang bahasa, sastra, seni, dan desain dengan berlandaskan kewirausahaan di bidang pendidikan dan non kependidikan.

 

MISI

A. Menyelenggarakan pendidikan tinggi bahasa, sastra, seni, dan desain yang kolaboratif, bersahabat, empati, adaptif, tangguh, inovatif, fleksibel berdasarkan kearifan lokal dan berwawasan global berbasis kewirausahaan di bidang pendidikan dan non pendidikan;

B. Menyelenggarakan penelitian dan meningkatkan kualitas inovasi bahasa, sastra, seni, dan desain berbasis kewirausahaan di bidang pendidikan dan non-pendidikan; 

C. Menyelenggarakan pengabdian kepada masyarakat dan menyebarluaskan inovasi bahasa, sastra, seni, dan desain berbasis kewirausahaan di bidang pendidikan dan non-pendidikan untuk kesejahteraan masyarakat; 

D. Menyelenggarakan kegiatan tiga pilar pendidikan tinggi melalui sistem multikampus secara sinergis, terpadu, serasi, dan berkelanjutan dengan mempertimbangkan keunggulan UNESA dalam bidang bahasa, sastra, seni, dan desain di bidang pendidikan dan non kependidikan; 

e. Menyelenggarakan tata kelola fakultas yang efektif, efisien, transparan, dan akuntabel yang menjamin mutu secara berkelanjutan; Dan 

F. Menyelenggarakan kerja sama produktif nasional dan internasional dalam menciptakan, mengembangkan, dan menyebarluaskan inovasi bahasa, sastra, seni, dan desain berbasis kewirausahaan di bidang pendidikan dan non-pendidikan. """

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Pendidikan Sastra Indonesia","Sastra Inggris","Pendidikan Bahasa Jerman"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifbs)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifbs(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Pendidikan Sastra Indonesia":
            self.psasin()
        elif selected_value == "Sastra Inggris":
            self.sasing()
        elif selected_value == "Pendidikan Bahasa Jerman":
            self.psasjer()

    def psasin(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"39.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=525, y=160)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=230, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

"Unggul dalam kependidikan bahasa dan sastra Indonesia tingkat internasional pada 2030”



MISI

Untuk merealisaikan visi, misi Program Studi PBSI adalah:

Meningkatkan kualitas pelaksanaan tridharma perguruan tinggi pada bidang pendidikan bahasa dan sastra Indonesia yang bermanfaat, bermutu, dan bernilai inovasi serta relevan dengan kebutuhan global dan perkembangan iptek dengan beracuan standar nasional pendidikan dan asas good university governance.
Meningkatkan kompetensi tenaga pendidik dan tenaga kependidikan Program Studi Pendidikan Bahasa dan Sastra Indonesia untuk mendukung peningkatan kualitas pembelajaran dan kegiatan kemahasiswaan.
Meningkatkan kualitas pengelolaan kelembagaan Program Studi Pendidikan Bahasa dan Sastra Indonesia dengan berdasar prosedur operasional baku.
Meningkatkan sarana dan prasarana Program Studi Pendidikan Bahasa dan Sastra Indonesia yang bermutu dan berorientasi cyber campus.
Meningkatkan kerjasama kelembagaan dalam dan luar negeri yang relevan untuk meningkatkan daya saing Program Studi Pendidikan Bahasa dan Sastra Indonesia dan kualitas lulusan."""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himabastra.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpsasin)

        clickable_label = Label(self.current_menu, text="s1pbsi.fbs.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpsasin)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofbs)
        self.button3.place(x=5, y=10)  

    def igpsasin(self,event):
        webbrowser.open('https://www.instagram.com/himabastra.unesa?igsh=MXczYXp0aTRlaXY2Zw==')
    def webpsasin(self,event):
        webbrowser.open('https://s1pbsi.fbs.unesa.ac.id/')

    def psasin1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"39.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=525, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

"Unggul dalam kependidikan bahasa dan sastra Indonesia tingkat internasional pada 2030”



MISI

Untuk merealisaikan visi, misi Program Studi PBSI adalah:

Meningkatkan kualitas pelaksanaan tridharma perguruan tinggi pada bidang pendidikan bahasa dan sastra Indonesia yang bermanfaat, bermutu, dan bernilai inovasi serta relevan dengan kebutuhan global dan perkembangan iptek dengan beracuan standar nasional pendidikan dan asas good university governance.
Meningkatkan kompetensi tenaga pendidik dan tenaga kependidikan Program Studi Pendidikan Bahasa dan Sastra Indonesia untuk mendukung peningkatan kualitas pembelajaran dan kegiatan kemahasiswaan.
Meningkatkan kualitas pengelolaan kelembagaan Program Studi Pendidikan Bahasa dan Sastra Indonesia dengan berdasar prosedur operasional baku.
Meningkatkan sarana dan prasarana Program Studi Pendidikan Bahasa dan Sastra Indonesia yang bermutu dan berorientasi cyber campus.
Meningkatkan kerjasama kelembagaan dalam dan luar negeri yang relevan untuk meningkatkan daya saing Program Studi Pendidikan Bahasa dan Sastra Indonesia dan kualitas lulusan."""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himabstra.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpsasin)

        clickable_label = Label(self.current_menu, text="s1pbsi.fbs.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpsasin)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)  

    def sasing(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"40.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=525, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

Pada akhir tahun 2030, Program Studi Sastra Inggris telah mencapai keunggulan dalam menyelenggarakan pendidikan berbasis bahasa dan sastra yang didukung dengan literasi dan vokasi berbasis Bahasa Inggris sebagai Bahasa Asing untuk menghasilkan lulusan profesional yang tanggap terhadap perubahan global.


MISI

Menyelenggarakan pendidikan berbasis bahasa dan sastra yang didukung literasi EFL melalui proses belajar-mengajar yang mengupayakan mutu dan keutamaan kejujuran, otonomi, kreativitas, berpikir kritis, dan integritas akademik guna menghasilkan lulusan yang mampu memanfaatkan dan menerapkan ilmunya. pengetahuan bahasa dan sastra dalam profesinya;
Menyelenggarakan penelitian di bidang bahasa dan sastra Inggris dalam rangka mengembangkan suasana akademik yang kondusif dan proses pembelajaran yang mengupayakan mutu;
Melaksanakan pengabdian kepada masyarakat untuk meningkatkan eksistensi dan kontribusi program studi di masyarakat;
Menjalin kerja sama dengan badan-badan pemerintah dan perusahaan swasta untuk menghadapi persaingan global;
Menyelenggarakan pengelolaan program studi secara efektif, efisien, transparan, dan akuntabel."""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@edsaunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsasing)

        clickable_label = Label(self.current_menu, text="s1sing.fbs.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websasing)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofbs)
        self.button3.place(x=5, y=10)  

    def igsasing(self):
        webbrowser.open('https://www.instagram.com/edsaunesa?igsh=cnQzZ2J6eHVnYWxl')
    def websasing(self,event):
        webbrowser.open('https://s1sing.fbs.unesa.ac.id/')

    def sasing1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"40.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=525, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

Pada akhir tahun 2030, Program Studi Sastra Inggris telah mencapai keunggulan dalam menyelenggarakan pendidikan berbasis bahasa dan sastra yang didukung dengan literasi dan vokasi berbasis Bahasa Inggris sebagai Bahasa Asing untuk menghasilkan lulusan profesional yang tanggap terhadap perubahan global.


MISI

Menyelenggarakan pendidikan berbasis bahasa dan sastra yang didukung literasi EFL melalui proses belajar-mengajar yang mengupayakan mutu dan keutamaan kejujuran, otonomi, kreativitas, berpikir kritis, dan integritas akademik guna menghasilkan lulusan yang mampu memanfaatkan dan menerapkan ilmunya. pengetahuan bahasa dan sastra dalam profesinya;
Menyelenggarakan penelitian di bidang bahasa dan sastra Inggris dalam rangka mengembangkan suasana akademik yang kondusif dan proses pembelajaran yang mengupayakan mutu;
Melaksanakan pengabdian kepada masyarakat untuk meningkatkan eksistensi dan kontribusi program studi di masyarakat;
Menjalin kerja sama dengan badan-badan pemerintah dan perusahaan swasta untuk menghadapi persaingan global;
Menyelenggarakan pengelolaan program studi secara efektif, efisien, transparan, dan akuntabel."""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@edsaunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsasing)

        clickable_label = Label(self.current_menu, text="s1sing.fbs.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websasing)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10) 

    def psasjer(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"41.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = B", font=("consolas", 15, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=570, y=155)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI
"unggul dalam kependidikan Bahasa jerman"

MISI

1. Menyelenggarakan pendidikan, pengajaran, dan bimbingan dalam bidang Bahasa Jerman secara optimal sesuai dengan potensi yang dimiliki.
2. Melaksanakan dan meningkatkan penelitian serta mengembangkan bidang keilmuan Pendidikan
Bahasa Jerman secara aktif dan berkesinambungan dalam persingan internasional
3. Menerapkan hasil penelitian dan mengembangkan bidang keilmuan Pendidikan Bahasa Jerman kepada masyarakat
4. Mengembangkan kerja sama dengan masyarakat terinstitusi baik nasional dan internasional
5. Mengembangkan kompetensi yang sesai dengan kebutuhan pasar kerja"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@deutsch_unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpsasjer)

        clickable_label = Label(self.current_menu, text="s1pbjer.fbs.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpsasjer)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofbs)
        self.button3.place(x=5, y=10)    

    def igpsasjer(self):
        webbrowser.open('https://www.instagram.com/deutsch_unesa?igsh=MXNxMXRjODlid2xrNQ==')
    def webpsasjer(self,event):
        webbrowser.open('https://s1pbjer.fbs.unesa.ac.id/')  

    def psasjer1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"41.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = B", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=570, y=155)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI
"unggul dalam kependidikan Bahasa jerman"

MISI

1. Menyelenggarakan pendidikan, pengajaran, dan bimbingan dalam bidang Bahasa Jerman secara optimal sesuai dengan potensi yang dimiliki.
2. Melaksanakan dan meningkatkan penelitian serta mengembangkan bidang keilmuan Pendidikan
Bahasa Jerman secara aktif dan berkesinambungan dalam persingan internasional
3. Menerapkan hasil penelitian dan mengembangkan bidang keilmuan Pendidikan Bahasa Jerman kepada masyarakat
4. Mengembangkan kerja sama dengan masyarakat terinstitusi baik nasional dan internasional
5. Mengembangkan kompetensi yang sesai dengan kebutuhan pasar kerja"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@deutsch_unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpsasjer)

        clickable_label = Label(self.current_menu, text="s1pbjer.fbs.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpsasjer)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)     

    def infofip(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"42.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
            VISI
“Unggul dalam Ilmu Pendidikan dan Kukuh dalam Keilmuan”
MISI
Menyelenggarakan pendidikan yang bermutu dalam rangka menghasilkan tenaga pendidik dan kependidikan yang bermutu;
Menyelenggarakan penelitian di bidang ilmu pendidikan dan Psikologi;
Menyelenggarakan pengabdian pada masyarakat di bidang ilmu pendidikan dan Psikologi;
Membangun kerja sama dengan lembaga lebih baik dalam maupun luar negeri;
Menyelenggarakan tata pamong perguruan tinggi yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan kualitas"""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Pendidikan Guru Sekolah Dasar","Pendidikan Luar Biasa","Teknologi Pendidikan"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifip)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifip(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Pendidikan Guru Sekolah Dasar":
            self.pgsd()
        elif selected_value == "Pendidikan Luar Biasa":
            self.plb()
        elif selected_value == "Teknologi Pendidikan":
            self.tekpen()

    def pgsd(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"43.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 15, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=540, y=155)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI ILMIAH
Mewujudkan keilmuan pendidikan guru sekolah dasar melalui paradigma reflektif kritis berbasis kearifan lokal dan berwawasan global

MISI ILMIAH
Menyelenggarakan pendidikan calon guru sekolah dasar yang berprinsip reflektif kritis, tanggap terhadap inovasi, perkembangan teknologi informasi, perkembangan teknologi informasi, kearifan lokal, dan berwawasan global.
Memanfaatkan dan melaksanakan hasil penelitian di bidang pendidikan guru sekolah dasar dengan pendekatan multidisiplin dan interdisipliner
Melaksanakan pengabdian kepada masyarakat sesuai bidang keahlian dan hasil penelitian pada Pendidikan Guru Sekolah Dasar"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@pgsd.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpgsd)

        clickable_label = Label(self.current_menu, text="pgsd.fip.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpgsd)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofip)
        self.button3.place(x=5, y=10)     
       
    def igpgsd(self):
        webbrowser.open('https://www.instagram.com/pgsd.unesa?igsh=anBybjF6cnR6cjQ4')
    def webpgsd(self,event):
        webbrowser.open('https://pgsd.fip.unesa.ac.id/')  

    def pgsd1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"43.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=540, y=155)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI ILMIAH
Mewujudkan keilmuan pendidikan guru sekolah dasar melalui paradigma reflektif kritis berbasis kearifan lokal dan berwawasan global

MISI ILMIAH
Menyelenggarakan pendidikan calon guru sekolah dasar yang berprinsip reflektif kritis, tanggap terhadap inovasi, perkembangan teknologi informasi, perkembangan teknologi informasi, kearifan lokal, dan berwawasan global.
Memanfaatkan dan melaksanakan hasil penelitian di bidang pendidikan guru sekolah dasar dengan pendekatan multidisiplin dan interdisipliner
Melaksanakan pengabdian kepada masyarakat sesuai bidang keahlian dan hasil penelitian pada Pendidikan Guru Sekolah Dasar"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@pgsd.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpgsd)

        clickable_label = Label(self.current_menu, text="pgsd.fip.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpgsd)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def plb(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"45.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI
Keunggulan bidang pendidikan khusus di komunitas global tahun 2035

Misi

1. Menyelenggarakan pendidikan profesi di bidang Pendidikan Khusus.

2. Menyelenggarakan penelitian, pengembangan ilmu pengetahuan dan teknologi (iptek), dan publikasi di bidang pendidikan khusus

3. Menyelenggarakan pengabdian kepada masyarakat berdasarkan hasil penelitian di bidang pendidikan khusus.

4. Memperluas kerja sama dengan pemangku kepentingan di tingkat nasional, regional, dan internasional

5. Mengoptimalkan tata kelola pemerintahan yang kredibel, transparan, akuntabel, bertanggung jawab, dan berkeadilan"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmp.plbunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igplb)

        clickable_label = Label(self.current_menu, text="plb.fip.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webplb)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofip)
        self.button3.place(x=5, y=10)

    def igplb(self,event):
        webbrowser.open('https://www.instagram.com/hmp.plbunesa?igsh=OXFxcHMyYnJxbHg0')
    def webplb(self,event):
        webbrowser.open("https://plb.fip.unesa.ac.id/")

    def plb1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"45.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI
Keunggulan bidang pendidikan khusus di komunitas global tahun 2035

Misi

1. Menyelenggarakan pendidikan profesi di bidang Pendidikan Khusus.

2. Menyelenggarakan penelitian, pengembangan ilmu pengetahuan dan teknologi (iptek), dan publikasi di bidang pendidikan khusus

3. Menyelenggarakan pengabdian kepada masyarakat berdasarkan hasil penelitian di bidang pendidikan khusus.

4. Memperluas kerja sama dengan pemangku kepentingan di tingkat nasional, regional, dan internasional

5. Mengoptimalkan tata kelola pemerintahan yang kredibel, transparan, akuntabel, bertanggung jawab, dan berkeadilan"""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmp.plbunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igplb)

        clickable_label = Label(self.current_menu, text="plb.fip.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webplb)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)    

    def tekpen(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"44.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=445, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI
Unggul dan kuat dalam bidang Teknologi Pendidikan
Misi
Menyelenggarakan pendidikan dan pembelajaran yang bermutu di bidang Teknologi Pendidikan.
Menyelenggarakan penelitian yang berkualitas di bidang Teknologi Pendidikan.
Menyelenggarakan pengabdian kepada masyarakat yang berkualitas di bidang Teknologi Pendidikan.
Membangun kemitraan di bidang pendidikan, penelitian, dan pengabdian kepada masyarakat dengan pemangku kepentingan (lembaga terkait) baik di tingkat nasional maupun internasional.
Menyelenggarakan tata kelola yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan mutu berkelanjutan."""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmptpunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igtekpen)

        clickable_label = Label(self.current_menu, text="ktp.fip.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webtekpen)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofip)
        self.button3.place(x=5, y=10)

    def igtekpen(self,event):
        webbrowser.open('https://www.instagram.com/hmptpunesa?igsh=M2Fwbnd3c2U2ZTQ0')
    def webtekpen(self,event):
        webbrowser.open('https://ktp.fip.unesa.ac.id/')

    def tekpen1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"44.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI
Unggul dan kuat dalam bidang Teknologi Pendidikan
Misi
Menyelenggarakan pendidikan dan pembelajaran yang bermutu di bidang Teknologi Pendidikan.
Menyelenggarakan penelitian yang berkualitas di bidang Teknologi Pendidikan.
Menyelenggarakan pengabdian kepada masyarakat yang berkualitas di bidang Teknologi Pendidikan.
Membangun kemitraan di bidang pendidikan, penelitian, dan pengabdian kepada masyarakat dengan pemangku kepentingan (lembaga terkait) baik di tingkat nasional maupun internasional.
Menyelenggarakan tata kelola yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan mutu berkelanjutan."""

        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmptpunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igtekpen)

        clickable_label = Label(self.current_menu, text="ktp.fip.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webtekpen)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)
    
    def infofio(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"46.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
           VISI
“MEWUJUDKAN FAKULTAS YANG TANGGUH SEBAGAI PUSAT UNGGULAN INOVASI DALAM KEOLAHRAGAAN, KESEHATAN, DAN INDUSTRI OLAHRAGA MELALUI KEGIATAN TRIDHARMA YANG ADAPTIF”
misi
    Menyelenggarakan proses akademik dalam berbagai ilmu kependidikan dan non-kependidikan yang membangun bidang ilmu keolahragaan, kesehatan, dan industri olahraga;
    menyelenggarakan penelitian dan meningkatkan kualitas inovasi di bidang ilmu keolahragaan, kesehatan, dan industri olahraga yang tepat guna;
    menyelenggarakan pengabdian kepada masyarakat di bidang ilmu keolahragaan, kesehatan, dan industri olahraga yang tepat sasaran;
    menciptakan kolaborasi dengan pemerintah, organisasi, dan masyarakat untuk peningkatan derajat kesehatan dan kebugaran jasmani masyarakat melalui aktivitas fisik;
    menjadikan FIKK sebagai pusat peningkatan prestasi olahraga bagi atlet bertalenta di cabang olahraga unggulan nasional menyongsong Indonesia Emas;
    mengembangkan FIKK yang memiliki kemampuan enterpreneurship dalam bidang keolahragaan (sports industry);
    menjadikan FIKK yang mampu menyiapkan tenaga keolahragaan melalui program pendidikan akademi dan sertifikasi; 
    menyelenggarakan kegiatan tridharma perguruan tinggi melalui sistem multikampus secara sinergi, terintegrasi, harmonis, dan berkelanjutan dengan memperhatikan keunggulan FIKK; 
    menyelenggarakan tata kelola yang efektif, efisien, transparan, dan akuntabel yang menjamin mutu secara berkelanjutan; dan 
    menyelenggarakan kerja sama nasional dan internasional yang produktif dalam menciptakan, mengembangkan, dan menyebarluaskan inovasi di bidang kependidikan dan nonkependidikan yang berbasis kewirausahaan."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Pendidikan Jasmani,Kesehatan,dan Rekreasi","Pendidikan Kepelatihan Olahraga","Ilmu Keolahragaan"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifio)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifio(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Pendidikan Jasmani,Kesehatan,dan Rekreasi":
            self.pjkr()
        elif selected_value == "Pendidikan Kepelatihan Olahraga":
            self.pko()
        elif selected_value == "Ilmu Keolahragaan":
            self.IO()
    
    def pjkr(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"47.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Penglihatan

“Terwujudnya Program Studi Pendidikan Jasmani, Kesehatan dan Rekreasi yang Unggul dan Tangguh dalam mengimplementasikan dan mengembangkan Ilmu Pengetahuan bidang Pendidikan Jasmani, Kesehatan dan Rekreasi di tingkat ASEAN pada tahun 2025”


Misi

    Meningkatkan kualitas Sumber Daya Manusia (SDM) guru Pendidikan Jasmani, Olah Raga dan Kesehatan yang mempunyai keunggulan dalam ilmu pendidikan jasmani, profesional dan berkarakter, melalui penyediaan sumber daya pendidikan yang bermutu, proses penyelenggaraan pendidikan yang bermutu dan suasana akademik yang kondusif.
    Mendorong peningkatan kuantitas dan kualitas penelitian dan pengabdian kepada masyarakat baik yang dilakukan oleh dosen secara mandiri maupun kolaboratif, serta meningkatkan hasil karya ilmiah berupa jurnal ilmiah, produk inovatif dan hak asasi manusia baik di tingkat lokal, nasional, maupun internasional. tingkat. 
    Mengembangkan tata kelola program studi berdasarkan prinsip akuntabilitas, transparansi, efisiensi, dan efektivitas untuk memberikan layanan berkualitas bagi pemangku kepentingan.
    Menjalin kemitraan dengan berbagai pihak terkait dalam rangka meningkatkan upaya pengembangan dan penerapan Ilmu Pendidikan Jasmani, Olah Raga, dan Kesehatan."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmppjkr.fikkunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpjkr)

        clickable_label = Label(self.current_menu, text="pjkr.fikk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpjkr)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofio)
        self.button3.place(x=5, y=10)

    def igpjkr(self):
        webbrowser.open('https://www.instagram.com/hmppjkr.fikkunesa?igsh=M25ybmV5MW82ZG1r')
    def webpjkr(self):
        webbrowser.open('https://pjkr.fikk.unesa.ac.id/')

    def pjkr1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"47.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Penglihatan

“Terwujudnya Program Studi Pendidikan Jasmani, Kesehatan dan Rekreasi yang Unggul dan Tangguh dalam mengimplementasikan dan mengembangkan Ilmu Pengetahuan bidang Pendidikan Jasmani, Kesehatan dan Rekreasi di tingkat ASEAN pada tahun 2025”


Misi

    Meningkatkan kualitas Sumber Daya Manusia (SDM) guru Pendidikan Jasmani, Olah Raga dan Kesehatan yang mempunyai keunggulan dalam ilmu pendidikan jasmani, profesional dan berkarakter, melalui penyediaan sumber daya pendidikan yang bermutu, proses penyelenggaraan pendidikan yang bermutu dan suasana akademik yang kondusif.
    Mendorong peningkatan kuantitas dan kualitas penelitian dan pengabdian kepada masyarakat baik yang dilakukan oleh dosen secara mandiri maupun kolaboratif, serta meningkatkan hasil karya ilmiah berupa jurnal ilmiah, produk inovatif dan hak asasi manusia baik di tingkat lokal, nasional, maupun internasional. tingkat. 
    Mengembangkan tata kelola program studi berdasarkan prinsip akuntabilitas, transparansi, efisiensi, dan efektivitas untuk memberikan layanan berkualitas bagi pemangku kepentingan.
    Menjalin kemitraan dengan berbagai pihak terkait dalam rangka meningkatkan upaya pengembangan dan penerapan Ilmu Pendidikan Jasmani, Olah Raga, dan Kesehatan."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmppjkr.fikkunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpjkr)

        clickable_label = Label(self.current_menu, text="pjkr.fikk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpjkr)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def pko(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"48.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Visi Departemen Pendidikan Kepelatihan Olahraga

 “Mampu mengembangkan ilmu pengetahuan dan teknologi kepelatihan olahraga (IPTEK) yang unggul di Asia Tenggara pada tahun 2025”. Program Unggulan S-1 Pendidikan Kepelatihan Olahraga di FIK Unesa merupakan program peningkatan kompetensi pelatih, pengembangan program latihan jasmani, pengembangan manajemen olahraga secara umum, pemerataan kepelatihan, dan pengembangan teknologi melalui proses pendidikan dan pelatihan, penelitian, dan pengabdian kepada masyarakat. .


Misi Departemen Pendidikan Kepelatihan Olahraga

    Menyelenggarakan Program Studi S1 ​​Pendidikan Kepelatihan Olahraga yang berbasis ilmu pengetahuan dan teknologi untuk menghasilkan lulusan yang profesional dan mempunyai kemampuan akademis, beretika, beriman, bertakwa serta mempunyai jiwa kepemimpinan sehingga mampu berperan aktif dalam pengembangan Ilmu Kepelatihan Olahraga .
    Mengembangkan penelitian teknologi olahraga.
    Menyelenggarakan pengabdian kepada masyarakat di bidang olahraga berupa pemberian pelatihan olahraga dan seminar olahraga serta turut serta membantu pengembangan olahraga di daerah melalui pengiriman dosen dan mahasiswa.
    Membangun kerjasama dengan berbagai instansi terkait nasional dan daerah.
    Membangun tata kelola yang mampu memenuhi kebutuhan pemangku kepentingan dan masyarakat luas."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@pkounesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpko)

        clickable_label = Label(self.current_menu, text="pko.fikk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpko)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofio)
        self.button3.place(x=5, y=10)

    def igpko(self):
        webbrowser.open('https://www.instagram.com/pkounesa?igsh=MXBvcXE2aXJqeGUyag==')
    def webpko(self):
        webbrowser.open('https://pko.fikk.unesa.ac.id/')


    def pko1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"48.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Visi Departemen Pendidikan Kepelatihan Olahraga

 “Mampu mengembangkan ilmu pengetahuan dan teknologi kepelatihan olahraga (IPTEK) yang unggul di Asia Tenggara pada tahun 2025”. Program Unggulan S-1 Pendidikan Kepelatihan Olahraga di FIK Unesa merupakan program peningkatan kompetensi pelatih, pengembangan program latihan jasmani, pengembangan manajemen olahraga secara umum, pemerataan kepelatihan, dan pengembangan teknologi melalui proses pendidikan dan pelatihan, penelitian, dan pengabdian kepada masyarakat. .


Misi Departemen Pendidikan Kepelatihan Olahraga

    Menyelenggarakan Program Studi S1 ​​Pendidikan Kepelatihan Olahraga yang berbasis ilmu pengetahuan dan teknologi untuk menghasilkan lulusan yang profesional dan mempunyai kemampuan akademis, beretika, beriman, bertakwa serta mempunyai jiwa kepemimpinan sehingga mampu berperan aktif dalam pengembangan Ilmu Kepelatihan Olahraga .
    Mengembangkan penelitian teknologi olahraga.
    Menyelenggarakan pengabdian kepada masyarakat di bidang olahraga berupa pemberian pelatihan olahraga dan seminar olahraga serta turut serta membantu pengembangan olahraga di daerah melalui pengiriman dosen dan mahasiswa.
    Membangun kerjasama dengan berbagai instansi terkait nasional dan daerah.
    Membangun tata kelola yang mampu memenuhi kebutuhan pemangku kepentingan dan masyarakat luas."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@pkounesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igpko)

        clickable_label = Label(self.current_menu, text="pko.fikk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webpko)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def IO(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"49.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Penglihatan


”Memiliki lulusan yang unggul, berkompeten di bidang ilmu dan teknologi keolahragaan, berbasis riset, adaptif dan berdaya saing global pada tahun 2035 dengan memberikan pelayanan yang profesional”

 

Misi


    Menyiapkan sumber daya dan penyelenggaraan pendidikan yang bermutu untuk menunjang mutu proses pembelajaran secara terencana, terarah, disiplin dan berkelanjutan.
    Mendorong peningkatan kualitas, kuantitas, dan produktivitas dosen dalam hal penelitian dan pengabdian kepada masyarakat serta penulisan buku dan artikel/karya ilmiah yang diterbitkan pada jurnal ilmiah skala lokal, regional, nasional, dan internasional baik yang dilakukan oleh dosen sendiri dan secara kolaboratif.
    Penataan dan pengelolaan Program Studi secara transparan dan akuntabel sehingga mampu memberikan pelayanan prima terhadap pelaksanaan dan evaluasi keberhasilan proses pembelajaran.
    Berkomitmen terhadap pengembangan ilmu keolahragaan di tingkat lokal, regional, nasional, dan internasional yang mengedepankan nilai-nilai positif Ilmu Keolahragaan dalam setiap dinamika wacana dan kebijakan yang dapat dilaksanakan melalui pengabdian kepada masyarakat."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himaikorunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igIO)

        clickable_label = Label(self.current_menu, text="ikor.fikk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webIO)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofio)
        self.button3.place(x=5, y=10)

    def igIO(self):
        webbrowser.open('https://www.instagram.com/himaikorunesa?igsh=eHQ4b2o5bHF0ejUz')
    def webIO(self):
        webbrowser.open('https://ikor.fikk.unesa.ac.id/')


    def IO1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"49.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Unggul", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        Penglihatan


”Memiliki lulusan yang unggul, berkompeten di bidang ilmu dan teknologi keolahragaan, berbasis riset, adaptif dan berdaya saing global pada tahun 2035 dengan memberikan pelayanan yang profesional”

 

Misi


    Menyiapkan sumber daya dan penyelenggaraan pendidikan yang bermutu untuk menunjang mutu proses pembelajaran secara terencana, terarah, disiplin dan berkelanjutan.
    Mendorong peningkatan kualitas, kuantitas, dan produktivitas dosen dalam hal penelitian dan pengabdian kepada masyarakat serta penulisan buku dan artikel/karya ilmiah yang diterbitkan pada jurnal ilmiah skala lokal, regional, nasional, dan internasional baik yang dilakukan oleh dosen sendiri dan secara kolaboratif.
    Penataan dan pengelolaan Program Studi secara transparan dan akuntabel sehingga mampu memberikan pelayanan prima terhadap pelaksanaan dan evaluasi keberhasilan proses pembelajaran.
    Berkomitmen terhadap pengembangan ilmu keolahragaan di tingkat lokal, regional, nasional, dan internasional yang mengedepankan nilai-nilai positif Ilmu Keolahragaan dalam setiap dinamika wacana dan kebijakan yang dapat dilaksanakan melalui pengabdian kepada masyarakat."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himaikorunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igIO)

        clickable_label = Label(self.current_menu, text="ikor.fikk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webIO)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def infofk(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"50.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
          Visi

Menjadi Fakultas Kedokteran yang tangguh, adaptif, dan inovatif berbasis ke-wirausahaan, yang unggul pada bidang kedokteran dan kesehatan olahraga di tingkat internasional pada tahun 2044

Misi

1. Menelenggarakan pendidikan dalam rangka menghasilkan lulusan yang berkarakter tangguh, adaptif, inovatif, dan berjiwa kewirausahaan yang unggul pada bidang kedokteran dan kesehatan olahraga
2.Menyelenggarakan penelitian sebagai pelopor pengembangan ilmu pengetahuan dan teknologi yang unggul pada bidang kedokteran dan kesehatan olahraga
3.Menyelenggarakan pengabdian kepada masyarakat bagi kesejahteraan dan kesehatan masyarakat
4.Membangun kerja sama dengan lembaga baik calam maupun luar negeri
5.Menyelenggarakan tata pamong perguruan tinggi yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan kualit as berkelanjutan"""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Kedokteran"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifk)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifk(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Kedokteran":
            self.dokter()

    def dokter(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"51.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi

Menjadi Fakultas Kedokteran yang tangguh, adaptif, dan inovatif berbasis ke-wirausahaan, yang unggul pada bidang kedokteran dan kesehatan olahraga di tingkat internasional pada tahun 2044

Misi

1. Menelenggarakan pendidikan dalam rangka menghasilkan lulusan yang berkarakter tangguh, adaptif, inovatif, dan berjiwa kewirausahaan yang unggul pada bidang kedokteran dan kesehatan olahraga
2.Menyelenggarakan penelitian sebagai pelopor pengembangan ilmu pengetahuan dan teknologi yang unggul pada bidang kedokteran dan kesehatan olahraga
3.Menyelenggarakan pengabdian kepada masyarakat bagi kesejahteraan dan kesehatan masyarakat
4.Membangun kerja sama dengan lembaga baik calam maupun luar negeri
5.Menyelenggarakan tata pamong perguruan tinggi yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan kualit as berkelanjutan"""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@fk.uunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igdr)

        clickable_label = Label(self.current_menu, text="fk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webdr)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofk)
        self.button3.place(x=5, y=10)

    def igdr(self):
        webbrowser.open("https://www.instagram.com/fk.unesa?igsh=MXA2Y3c4ZDd5a3E4cw==")
    def webdr(self):
        webbrowser.open('https://fk.unesa.ac.id/')

    def dokter1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"51.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi

Menjadi Fakultas Kedokteran yang tangguh, adaptif, dan inovatif berbasis ke-wirausahaan, yang unggul pada bidang kedokteran dan kesehatan olahraga di tingkat internasional pada tahun 2044

Misi

1. Menelenggarakan pendidikan dalam rangka menghasilkan lulusan yang berkarakter tangguh, adaptif, inovatif, dan berjiwa kewirausahaan yang unggul pada bidang kedokteran dan kesehatan olahraga
2.Menyelenggarakan penelitian sebagai pelopor pengembangan ilmu pengetahuan dan teknologi yang unggul pada bidang kedokteran dan kesehatan olahraga
3.Menyelenggarakan pengabdian kepada masyarakat bagi kesejahteraan dan kesehatan masyarakat
4.Membangun kerja sama dengan lembaga baik calam maupun luar negeri
5.Menyelenggarakan tata pamong perguruan tinggi yang otonom, akuntabel, dan transparan untuk penjaminan mutu dan peningkatan kualit as berkelanjutan"""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@fk.uunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igdr)

        clickable_label = Label(self.current_menu, text="fk.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webdr)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def infofh(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"52.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        VISI

Kukuh dalam Keilmuan, Profesi Hukum, dan Berdedikasi Secara Kompetitif dan Komparatif serta Bermartabat di Tingkat Nasional dan Internasional

MISI

Menyelenggarakan dan mengembangkan pendidikan hukum dalam upaya menghasilkan sarjana hukum yang kompeten dalam keilmuan dan profesi hukum.
Mengembangkan kuantitas dan kualitas penelitian hukum untuk menunjang kelancaran proses belajar mengajar dan meningkatkan kualitas lulusan.
Menyelenggarakan pengabdian kepada masyarakat yang relevan dengan kebutuhan dan perkembangan masyarakat berbasis hasil penelitian
Menjalin dan mengembangkan kerjasama yang saling menguntungkan dengan semua pihak terkait baik di tingkat daerah maupun nasional dalam rangka pemajuan program studi S1 Ilmu Hukum Unesa"""        
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["Ilmu Hukum"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifh)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifh(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "Ilmu Hukum":
            self.hukum()  

    def hukum(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"53.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       VISI

Kukuh dalam Keilmuan, Profesi Hukum, dan Berdedikasi Secara Kompetitif dan Komparatif serta Bermartabat di Tingkat Nasional dan Internasional

MISI

Menyelenggarakan dan mengembangkan pendidikan hukum dalam upaya menghasilkan sarjana hukum yang kompeten dalam keilmuan dan profesi hukum.
Mengembangkan kuantitas dan kualitas penelitian hukum untuk menunjang kelancaran proses belajar mengajar dan meningkatkan kualitas lulusan.
Menyelenggarakan pengabdian kepada masyarakat yang relevan dengan kebutuhan dan perkembangan masyarakat berbasis hasil penelitian
Menjalin dan mengembangkan kerjasama yang saling menguntungkan dengan semua pihak terkait baik di tingkat daerah maupun nasional dalam rangka pemajuan program studi S1 Ilmu Hukum Unesa"""        
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@bemfhunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.ighukum)

        clickable_label = Label(self.current_menu, text="fh.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webhukum)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofh)
        self.button3.place(x=5, y=10)
   
    def ighukum(self):
        webbrowser.open('https://www.instagram.com/bemfhunesa?igsh=MXg0bjFuYTRmeDhmdw==')
    def webhukum(self):
        webbrowser.open('https://fh.unesa.ac.id/')

    def hukum1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"53.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       VISI

Kukuh dalam Keilmuan, Profesi Hukum, dan Berdedikasi Secara Kompetitif dan Komparatif serta Bermartabat di Tingkat Nasional dan Internasional

MISI

Menyelenggarakan dan mengembangkan pendidikan hukum dalam upaya menghasilkan sarjana hukum yang kompeten dalam keilmuan dan profesi hukum.
Mengembangkan kuantitas dan kualitas penelitian hukum untuk menunjang kelancaran proses belajar mengajar dan meningkatkan kualitas lulusan.
Menyelenggarakan pengabdian kepada masyarakat yang relevan dengan kebutuhan dan perkembangan masyarakat berbasis hasil penelitian
Menjalin dan mengembangkan kerjasama yang saling menguntungkan dengan semua pihak terkait baik di tingkat daerah maupun nasional dalam rangka pemajuan program studi S1 Ilmu Hukum Unesa"""        
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@bemfhunesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.ighukum)

        clickable_label = Label(self.current_menu, text="fh.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webhukum)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def infofv(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"54.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=390, y=160, width=500, height=200)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
        A. Visi

Menjadi Lembaga Pendidikan Tinggi Pengembang Ilmu Terapan dan Menghasilkan Sarjana Terapan yang Berkarakter Tangguh, Adaptif, Inovatif yang Berbabis Kewirausahaan.

B. Misi

1.    Mengembangkan ilmu terapan melalui tridarma perguruan tinggi yang adaptif, kolaboratif, dan inovatif yang berbasis kewirausahaan;

2.    Menghasilkan lulusan sarjana terapan yang berkarakter tangguh, adaptif, inovatif yang berbasis kewirausahaan;

3.    Meningkatkan kuantitas dan kualitas SDM Vokasi;

4.    Meningkatkan kualitas layanan pembelajaran melalui pengembangan kurikulum yang adaptif, fleksibel, dan agile serta kualitas sarana dan prasarana;

5.    Meningkatkan link and super match dengan IDUKA dalam bidang pendidikan, penelitian, dan pengabdian kepada masyarakat;

6.    Menciptakan tata kelola fakultas vokasi yang akuntabel, transparan, dan partisipatif."""
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED)

        self.dropdown_style = ttk.Style()
        self.dropdown_style.configure('Custom.TCombobox', fieldbackground='#081b47', background='#081b47', foreground='white')

        # Membuat objek dropdown untuk memilih program studi
        self.dropdown = ttk.Combobox(self.current_menu, values=["D4-Tata Busana","D4-Teknik Sipil","D4-Desain Grafis"], style='Custom.TCombobox', state='readonly')
        self.dropdown.set("PILIH PROGRAM STUDI IMPIANMU")
        self.dropdown.config(font=('consolas', 30), width=20)  # Mengatur font dan lebar dropdown
        self.dropdown.place(x=750, y=500)

        # Membuat tombol Next
        next_button = tk.Button(self.current_menu, text="Next", command=self.prodifv)
        next_button.config(font=('consolas', 15), width=5)
        next_button.place(x=680, y=505)

        # Menambahkan tombol kembali dengan gambar
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infonesa)
        self.button3.place(x=5, y=10) 

    def prodifv(self):
        if self.dropdown.winfo_exists():
            selected_value = self.dropdown.get()
        if selected_value == "D4-Tata Busana":
            self.tabus()
        elif selected_value == "D4-Teknik Sipil":
            self.teksipvo()
        elif selected_value == "D4-Desain Grafis":
            self.desgraf()

    def tabus(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"55.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi:
 Menjadi pusat pembelajaran Desain Fesyen berbasis seni dan budaya lokal dan berkelanjutan yang menghasilkan lulusan berjiwa Technopreneur. 
Misi: 
Menyelenggarakan pendidikan dan pembelajaran yang berpusat pada peserta didik dengan menggunakan pendekatan pembelajaran berbasis proyek, dan mengoptimalkan penggunaan teknologi dalam pembelajaran. 
Menyelenggarakan pembelajaran mandiri dengan memberikan kesempatan kepada mahasiswa untuk dapat belajar dalam konteks yang lebih beragam, dan merasakan pengalaman belajar di industri atau pengalaman belajar di luar kampus. 
Menyelenggarakan penelitian terapan di bidang desain fesyen yang fokus pada pelestarian seni dan budaya lokal serta fesyen berkelanjutan yang menghasilkan produk inovatif. 
Mendiseminasikan ilmu pengetahuan dan teknologi, serta hasil penelitian kepada masyarakat yang berorientasi pada pemberdayaan masyarakat, diterapkan dan dikembangkan pada UKM dan industri fashion. 
Bekerjasama dengan berbagai pihak terkait baik lokal, nasional maupun internasional serta dalam penyelenggaraan Tri Dharma Perguruan Tinggi"""
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himafd.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igtabus)

        clickable_label = Label(self.current_menu, text="terapan-fashion.vokasi.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webtabus)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofv)
        self.button3.place(x=5, y=10)

    def igtabus(self):
        webbrowser.open("https://www.instagram.com/himafd.unesa?igsh=MWY4dHhpZG5zcWRpaQ==")
    def webtabus(self):
        webbrowser.open('https://terapan-fashion.vokasi.unesa.ac.id')

    def tabus1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"55.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi:
 Menjadi pusat pembelajaran Desain Fesyen berbasis seni dan budaya lokal dan berkelanjutan yang menghasilkan lulusan berjiwa Technopreneur. 
Misi: 
Menyelenggarakan pendidikan dan pembelajaran yang berpusat pada peserta didik dengan menggunakan pendekatan pembelajaran berbasis proyek, dan mengoptimalkan penggunaan teknologi dalam pembelajaran. 
Menyelenggarakan pembelajaran mandiri dengan memberikan kesempatan kepada mahasiswa untuk dapat belajar dalam konteks yang lebih beragam, dan merasakan pengalaman belajar di industri atau pengalaman belajar di luar kampus. 
Menyelenggarakan penelitian terapan di bidang desain fesyen yang fokus pada pelestarian seni dan budaya lokal serta fesyen berkelanjutan yang menghasilkan produk inovatif. 
Mendiseminasikan ilmu pengetahuan dan teknologi, serta hasil penelitian kepada masyarakat yang berorientasi pada pemberdayaan masyarakat, diterapkan dan dikembangkan pada UKM dan industri fashion. 
Bekerjasama dengan berbagai pihak terkait baik lokal, nasional maupun internasional serta dalam penyelenggaraan Tri Dharma Perguruan Tinggi"""
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himafd.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igtabus)

        clickable_label = Label(self.current_menu, text="terapan-fashion.vokasi.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webtabus)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

    def teksipvo(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"56.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi:
Menjadikan program studi D4 Sarjana Terapan Teknik Sipil sebagai civitas akademika bidang infrastruktur yang berperingkat nasional dan menyiapkan lulusan yang bertakwa dan berakhlak mulia serta mampu bersaing di era globalisasi.


Misi:

1. Menyelenggarakan Tri Dharma Perguruan Tinggi meliputi pengajaran, penelitian, dan pengabdian kepada masyarakat

2. Mendidik mahasiswa memiliki kompetensi di bidang konstruksi bangunan

3. Melatih mahasiswa untuk mengembangkan dan menerapkan ilmu di bidang konstruksi bangunan

4. Melatih peserta didik untuk mengembangkan dan menerapkan ilmunya sesuai kebutuhan masyarakat"""
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmst.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsipvo)

        clickable_label = Label(self.current_menu, text="terapan-sipil.vokasi.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websipvo)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofv)
        self.button3.place(x=5, y=10)

    def igsipvo(self):
        webbrowser.open("https://www.instagram.com/hmst.unesa?igsh=MW1id3EwcXQzZGw4cw==")
    def websipvo(self):
        webbrowser.open("https://terapan-sipil.vokasi.unesa.ac.id/")
    
    def teksipvo1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"56.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi:
Menjadikan program studi D4 Sarjana Terapan Teknik Sipil sebagai civitas akademika bidang infrastruktur yang berperingkat nasional dan menyiapkan lulusan yang bertakwa dan berakhlak mulia serta mampu bersaing di era globalisasi.


Misi:

1. Menyelenggarakan Tri Dharma Perguruan Tinggi meliputi pengajaran, penelitian, dan pengabdian kepada masyarakat

2. Mendidik mahasiswa memiliki kompetensi di bidang konstruksi bangunan

3. Melatih mahasiswa untuk mengembangkan dan menerapkan ilmu di bidang konstruksi bangunan

4. Melatih peserta didik untuk mengembangkan dan menerapkan ilmunya sesuai kebutuhan masyarakat"""
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@hmst.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igsipvo)

        clickable_label = Label(self.current_menu, text="terapan-sipil.vokasi.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.websipvo)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)    

    def desgraf(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"57.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi:
       “Menciptakan lulusan Sarjana Desain Grafis Terapan yang profesional, berkompeten tinggi di bidang keahliannya, dan berwawasan global”

Misi:
1. Menyelenggarakan pendidikan untuk menghasilkan lulusan profesional terapan di bidang Desain Grafis.
2. Menyelenggarakan penelitian dan pengabdian kepada masyarakat yang berkualitas dan bernilai inovasi di bidang Desain Grafis.
3. Menjalin kemitraan dengan berbagai institusi terkait guna meningkatkan daya saing dan kualitas lulusan Desain Grafis"""
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himadega.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igdega)

        clickable_label = Label(self.current_menu, text="terapan-desain.vokasi.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webdega)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.infofv)
        self.button3.place(x=5, y=10)

    def igdega(self):
        webbrowser.open("https://www.instagram.com/himadega.unesa?igsh=OGlwcW1yZGdtZXR0")
    def webdega(self):
        webbrowser.open("https://terapan-desain.vokasi.unesa.ac.id/")

    def desgraf1(self):
        if hasattr(self, 'label_background'):
            self.label_background.destroy()
        self.current_menu = tk.Frame(self.window)  # Membuat current_menu baru
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.current_menu.place(x=0, y=0, width=screen_width, height=screen_height)
        self.background_img = Image.open(r"57.png")
        self.background_img = self.background_img.resize((screen_width, screen_height))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.label_background = Label(self.current_menu, image=self.background_photo)
        self.label_background.place(relheight=1, relwidth=1)
        self.label_background.image = self.background_photo

        self.nama_label_dshbrd = Label(self.current_menu, text="Akreditasi = Baik", font=("consolas", 20, "bold"), bg='#a4c5cc', justify='center', fg='white')
        self.nama_label_dshbrd.place(x=490, y=130)

        text_frame = tk.Frame(self.current_menu, bg='#2d2584')
        text_frame.place(x=100, y=200, width=465, height=365)

        text_box = tk.Text(text_frame, wrap=tk.WORD)
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box.config(yscrollcommand=scrollbar.set)

        text_content = """
       Visi:
       “Menciptakan lulusan Sarjana Desain Grafis Terapan yang profesional, berkompeten tinggi di bidang keahliannya, dan berwawasan global”

Misi:
1. Menyelenggarakan pendidikan untuk menghasilkan lulusan profesional terapan di bidang Desain Grafis.
2. Menyelenggarakan penelitian dan pengabdian kepada masyarakat yang berkualitas dan bernilai inovasi di bidang Desain Grafis.
3. Menjalin kemitraan dengan berbagai institusi terkait guna meningkatkan daya saing dan kualitas lulusan Desain Grafis"""
        text_box.insert(tk.END, text_content)
        text_box.insert(tk.END, text_content)
        text_box.config(font=("Times New Roman", 12), state=tk.DISABLED) 

        clickable_label = Label(self.current_menu, text="@himadega.unesa",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=710, y=601)
        clickable_label.bind("<Button-1>", self.igdega)

        clickable_label = Label(self.current_menu, text="terapan-desain.vokasi.unesa.ac.id/",font=("Times New Roman",15) ,fg="black",bg='#a4c5cc', cursor="hand2")
        clickable_label.place(x=1010, y=601)
        clickable_label.bind("<Button-1>", self.webdega)

        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(self.current_menu, image=self.back,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)


# ____________________________________________TRY-U____________________________________________________________________



    def formulir(self):
        self.window_form = Toplevel()
        
        # Mengatur properti window
        self.window_form.title("Formulir Minat Mahasiswa")
        self.window_form.geometry("548x846")
        self.window_form.configure(background='white')
        self.window_form.resizable(width=tk.FALSE,height=tk.FALSE)
       
        tk.Label(self.window_form, text="Formulir Minat Mahasiswa", font=("Arial", 16,"bold"),bg="white").place(x=90,y=50)

        def onclose():
            self.window_form.deiconify()
            self.window_form.destroy()
        self.window_form.protocol("WM_DELETE_WINDOW", onclose)
        
        self.data_minat = {
            "Minat": {
                "Bahasa Indonesia": {
                    "Literature": ["Sastra Indonesia", "Pendidikan Bahasa dan Sastra Indonesia"],
                    "teaching": ["Pendidikan Luar Sekolah"]
                },
                "Bahasa Inggris": {
                    "Literature": ["Sastra Inggris"],
                    "teaching": ["Pendidikan Bahasa Inggris"]
                },
                "Matematika": {
                    "Data Analysis": ["Matematika", "Sains Data", "Teknik Informatika", "Bisnis Digital"],
                    "Spasialis": ["Pendidikan Teknik Bangunan"],
                    "teaching": ["Pendidikan Matematika"]
                },
                "Biologi": {
                    "Genetics": ["Biologi"],
                    "Ecology": ["Biologi"],
                    "teaching": ["Pendidikan Biologi", "Pendidikan Sains"]
                },
                "Fisika": {
                    "Quantum Computing": ["Fisika", "Teknik Fisika", "Teknik Informatika"],
                    "Robotika": ["Teknik Mesin", "Teknik Elektro", "Teknik Informatika"],
                    "teaching": ["Pendidikan Fisika", "Pendidikan Sains", "Pendidikan Teknik Elektro"]
                },
                "Kimia": {
                    "Biochemistry": ["Bioteknologi", "Kimia Murni"],
                    "Pharmaceutical Chemistry": ["Farmasi", "Kimia Farmasi"],
                    "teaching": ["Pendidikan Kimia", "Pendidikan Sains"]
                },
                "Seni": {
                    "Constructor": ["Pendidikan Teknik Bangunan", "Teknik Sipil"],
                    "Seni": ["Pendidikan Seni Rupa", "Seni Rupa Murni"],
                    "Fashion": ["Pendidikan Tata Busana"],
                    "Design": ["Design Grafis", "Design Komunikasi Visual"],
                    "Culture": ["Pendidikan Seni, Drama, Tari, dan Musik"]
                },
                "Kesehatan": {
                    "Nutrition": ["Gizi"],
                    "Mental": ["Psikologi", "Bimbingan dan Konseling"],
                    "Health": ["Kedokteran"]
                },
                "Pendidikan": {
                    "Parenting": ["Pendidikan Sekolah Dasar", "Pendidikan Guru Pendidikan Anak Usia Dini"],
                    "Luar": ["Pendidikan Luar Biasa", "Pendidikan Luar Sekolah"]
                },
                "Pendidikan Kewarganegaraan": {
                    "Civic Education": ["Pendidikan Pancasila dan Kewarganegaraan"]
                },
                "Sejarah": {
                    "History": ["Sejarah", "Pendidikan Sejarah"]
                },
                "Sosiologi": {
                    "Social Work": ["Sosiologi"],
                    "teaching": ["Bimbingan dan Konseling"]
                },
                "Ekonomi": {
                    "Economics": ["Ekonomi"],
                    "Administration": ["Ilmu Administrasi Negara"]
                },
                "Geografi": {
                    "Geographical Sciences": ["Pendidikan Geografi"]
                },
                "Komputer": {
                    "Computer Science": ["Teknik Informatika", "Sains Data", "Sistem Informasi"],
                    "Programming": ["Teknik Informatika", "Sains Data", "Sistem Informasi"],
                    "Machine Learning": ["Sains Data", "Teknik Informatika"],
                    "teaching": ["Pendidikan Teknologi Informasi"]
                },
                "Bahasa Jawa": {
                    "teaching": ["Pendidikan Bahasa dan Sastra Jawa"]
                },
                "Bahasa Jerman": {
                    "Literature": ["Sastra Jerman"],
                    "teaching": ["Pendidikan Bahasa Jerman"]
                },
                "Bahasa Jepang": {
                    "Literature": ["Pendidikan Bahasa dan Sastra Jepang"],
                    "teaching": ["Pendidikan Bahasa Jepang"]
                }
            }
        }

        
        self.usnform_label = tk.Label(self.window_form, text="Username", bg="#f8f8f8", font=("sans serif", 12, "bold"), fg="#0370a9")
        self.usnform_label.place(x=26, y=135)


    
        self.name_entry = tk.Entry(self.window_form, textvariable=self.username, border=0, highlightthickness=2,
                                   highlightcolor="#0370a9", relief="groove", width=32, font=("Arial", 13),
                                   bg="white", fg="black", state ='readonly')
        self.name_entry.place(x=30, y=162)

        self.minat_label = tk.Label(self.window_form, text="Minat", bg="#f8f8f8", font=("sans serif", 12, "bold"), fg="#0370a9")
        self.minat_label.place(x=26, y=233)

        self.minat = tk.StringVar()
        self.minat_combobox = ttk.Combobox(self.window_form, width=32, textvariable=self.minat, values=list(self.data_minat["Minat"].keys()))
        self.minat_combobox.place(x=30, y=260)
        self.minat.trace('w', self.update_kategori)  # Update kategori saat minat berubah

        self.field_label = tk.Label(self.window_form, text="Bidang yang ingin dikuasai", bg="#f8f8f8", font=("sans serif", 12, "bold"), fg="#0370a9")
        self.field_label.place(x=26, y=321)

        self.bidang = StringVar()
        self.field = ttk.Combobox(self.window_form, textvariable=self.bidang, width=32, font=("Arial", 12))
        self.field.place(x=30, y=345)

        self.jurusan_label = tk.Label(self.window_form, text="Pilihan 1", bg="#f8f8f8", font=("sans serif", 12, "bold"), fg="#0370a9")
        self.jurusan_label.place(x=26, y=403)
        self.jurusan = tk.StringVar()
        self.jurusan_entry = tk.Entry(self.window_form, textvariable=self.jurusan, border=0, highlightthickness=2,
                                      highlightcolor="#0370a9", relief="groove", width=32, font=("Arial", 13),
                                      bg="white", fg="black")
        self.jurusan_entry.place(x=30, y=427)


        self.add_placeholder2(self.jurusan_entry, "Pilih prodi impianmu..")
        self.jurusan_entry.bind("<KeyRelease>", self.update_search1)  # Event binding untuk memanggil fungsi pencarian setiap kali teks dalam entri berubah

        self.jurusan_label2 = tk.Label(self.window_form, text="Pilihan 2", bg="#f8f8f8", font=("sans serif", 12, "bold"), fg="#0370a9")
        self.jurusan_label2.place(x=26, y=485)
        self.jurusan2 = tk.StringVar()
        self.jurusan_entry2 = tk.Entry(self.window_form, textvariable=self.jurusan2, border=0, highlightthickness=2,
                                      highlightcolor="#0370a9", relief="groove", width=32, font=("Arial", 13),
                                      bg="white", fg="black")
        self.jurusan_entry2.place(x=30, y=509)
        self.jurusan_entry2.bind("<KeyRelease>", self.update_search2)  # Event binding untuk memanggil fungsi pencarian setiap kali teks dalam entri berubah
        self.add_placeholder2(self.jurusan_entry2, "Pilih prodi impianmu..")

        self.resulttt = tk.Listbox(self.window_form, width=42, height=10)
        self.resulttt.bind("<<ListboxSelect>>", self.pencet_listbox_jurusan)

        self.resulttt2 = tk.Listbox(self.window_form, width=42, height=10)
        self.resulttt2.bind("<<ListboxSelect>>", self.pencet_listbox_jurusan2)

        self.button_check_delete = ttk.Button(self.window_form, text="reset try out", command=self.check_and_delete_data)
        self.button_check_delete.grid(row=1, columnspan=2, padx=5, pady=10)

        self.submit_button = ttk.Button(self.window_form, text="Submit", command=self.submit_and_save)
        self.submit_button.place(x=183, y=550)

    def add_placeholder2(self, entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry._placeholder_active = True

        def on_focus_in(event):
            if entry._placeholder_active:
                entry.delete(0, "end")
                entry._placeholder_active = False

        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry._placeholder_active = True

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def sentinel_searchform(self, array, target):
        array.append(target)  # Tambahkan sentinel
        matches = set()  # Gunakan set untuk menyimpan rekomendasi unik
        i = 0
        while True:
            if array[i].lower().startswith(target.lower()):
                matches.add(array[i])
            if array[i] == target:
                break
            i += 1
        array.pop()  # Hapus sentinel
        if target.lower() in matches:
            matches.remove(target.lower())  # Hapus target dari rekomendasi jika sudah lengkap
        return list(matches)  # Ubah set kembali menjadi list sebelum mengembalikannya

    def read_csvvv(self):
        self.data_jurusan = []
        with open("datapg.csv", 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                self.data_jurusan.append(row[1])  # Ambil nama jurusan dari kolom pertama (indeks 0)
        return self.data_jurusan

    def update_search1(self, event):
        self.update_search(1)

    def update_search2(self, event):
        self.update_search(2)

    def update_search(self, id):
        keyword = ""
        if id == 1: 
            keyword = self.jurusan.get().strip()  # Ambil teks dari entri dan hilangkan spasi di awal dan akhir
        elif id == 2: 
            keyword = self.jurusan2.get().strip()  # Ambil teks dari entri dan hilangkan spasi di awal dan akhir

        username = self.username.get()  # Get the current username
        datajur = self.read_csvvv()

        if username in datajur:
            jurusan_list = datajur[username]
            if keyword:
                # Lakukan pencarian
                recommendations = self.sentinel_searchform(jurusan_list, keyword)
                for recommendation in recommendations:
                    if id == 1:
                        self.resulttt.insert(tk.END, recommendation)
                    elif id == 2:
                        self.resulttt2.insert(tk.END, recommendation)

                if id == 1: 
                    self.resulttt.place(x=self.jurusan_entry.winfo_x(), y=self.jurusan_entry.winfo_y() + self.jurusan_entry.winfo_height())
                    self.resulttt.lift()  # Munculkan listbox di depan entri
                elif id == 2: 
                    self.resulttt2.place(x=self.jurusan_entry2.winfo_x(), y=self.jurusan_entry2.winfo_y() + self.jurusan_entry2.winfo_height())
                    self.resulttt2.lift()  # Munculkan listbox di depan entri
            else:
                self.resulttt.place_forget()
                self.resulttt2.place_forget()  # Sembunyikan listbox jika tidak ada teks di dalamnya

        if keyword:
            # Lakukan pencarian
            recommendations = self.sentinel_searchform(datajur, keyword)
            for recommendation in recommendations:
                if id == 1:
                    self.resulttt.insert(tk.END, recommendation)
                elif id == 2:
                    self.resulttt2.insert(tk.END, recommendation)

            if id == 1: 
                self.resulttt.place(x=self.jurusan_entry.winfo_x(), y=self.jurusan_entry.winfo_y() + self.jurusan_entry.winfo_height())
                self.resulttt.lift()  # Munculkan listbox di depan entri
            elif id == 2: 
                self.resulttt2.place(x=self.jurusan_entry2.winfo_x(), y=self.jurusan_entry2.winfo_y() + self.jurusan_entry2.winfo_height())
                self.resulttt2.lift()  # Munculkan listbox di depan entri
        else:
            self.resulttt.place_forget()
            self.resulttt2.place_forget()  # Sembunyikan listbox jika tidak ada teks di dalamnya

    def pencet_listbox_jurusan(self, event):
        if self.resulttt.curselection():
            selected_text = self.resulttt.get(self.resulttt.curselection())
            self.jurusan_entry.delete(0, tk.END)  # Hapus teks dalam entry
            self.jurusan_entry.insert(0, selected_text)  # Isi entry dengan teks yang dipilih
            self.resulttt.place_forget()  # Sembunyikan listbox setelah pemilihan

    def pencet_listbox_jurusan2(self, event):
        if self.resulttt2.curselection():
            selected_text = self.resulttt2.get(self.resulttt2.curselection())
            self.jurusan_entry2.delete(0, tk.END)  # Hapus teks dalam entry
            self.jurusan_entry2.insert(0, selected_text)  # Isi entry dengan teks yang dipilih
            self.resulttt2.place_forget()  # Sembunyikan listbox setelah pemilihan

    def check_and_delete_data(self):
        username = self.username.get()
        
        if not username or not selected_jurusan or not selected_minat or not selected_field or not selected_jurusan2:
            messagebox.showwarning("Input Error", "Semua kolom harus diisi!")
            return
        
        if not username:
            messagebox.showwarning("Input Error", "Username harus diisi!")
            return

        # Cek apakah username ada di kolom ke-4 dataakun.csv
        if self.check_username(username):
            self.delete_user_data(username)
            messagebox.showinfo(window,"Success", f"Data untuk username '{username}' berhasil dihapus dari hasil_kuis.csv!")
        else:
            messagebox.showwarning(window,"Not Found", f"Username '{username}' tidak ditemukan di dataakun.csv kolom ke-4!")

    def delete_user_data(self, username):
        try:
            updated_rows = []
            with open('hasil_kuis.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row['user'] != username:
                        updated_rows.append(row)

            with open('hasil_kuis.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_rows)
        except FileNotFoundError:
            messagebox.showerror("File Error", "File hasil_kuis.csv tidak ditemukan!")


    # def submit_and_save(self):
    #     self.window_form.destroy()

    #     global username_form
    #     username_form = self.username.get()
    #     global selected_minat
    #     selected_minat = self.minat.get()
    #     global selected_field
    #     selected_field = self.bidang.get()
    #     global selected_jurusan
    #     selected_jurusan = self.jurusan.get()
    #     global selected_jurusan2
    #     selected_jurusan2 = self.jurusan2.get()
    #     self.usernamefom=username_form
        
    #     if not username_form or not selected_jurusan or not selected_minat or not selected_field or not selected_jurusan2:
    #         messagebox.showwarning("Input Error", "Semua kolom harus diisi!")
    #         return

    #     # Check if data is already present in CSV
        
    #     if not self.check_username(username_form):
    #         messagebox.showerror("Invalid Username", "Username tidak ditemukan!")
    #         return
        
    #     if self.check_duplicate(username_form):
    #         messagebox.showerror("Duplicate Entry", "Tidak bisa mengerjakan lagi")
    #         return
        
    #     data = {
    #         'user': username_form,
    #         'minat': selected_minat,
    #         'bidang': selected_field,
    #         'pilihan 1': selected_jurusan,
    #         'pilihan 2': selected_jurusan2
    #     }

        
    #     messagebox.showinfo("Success", "Data berhasil disimpan!")
    #     filtered_data = {}
    #     if selected_minat in self.data_minat["Minat"]:
    #         filtered_data[selected_minat] = self.data_minat["Minat"][selected_minat]
    #         if selected_field and selected_field in filtered_data[selected_minat]:
    #             filtered_data = {selected_minat: {selected_field: filtered_data[selected_minat][selected_field]}}
        
    #     roott = self.build_tree(self.data_minat)
    #     if selected_minat and selected_field:
    #             self.recommended_programs = self.search_tree(roott, selected_minat, selected_field)
    #             self.recommended_programs_str = ', '.join(self.recommended_programs) if self.recommended_programs else "Tidak ada rekomendasi"
    #     else:
    #             self.recommended_programs_str = "Silakan pilih minat dan kategori"
    #     # Save to CSV
    #     self.fieldnames = ["user","minat","bidang","pilihan 1","pilihan 2","Skor PU", "Skor PPU", "Skor PBM", "Skor PK", "Skor LBI", "Skor LBE", "Skor PM","Skor Akhir"]

        
    #     with open('hasil_kuis.csv', mode='a', newline='') as file:
    #         writer = csv.DictWriter(file, delimiter=',', fieldnames=self.fieldnames,restval="-")
    #         if file.tell() == 0:
    #             writer.writeheader()

    #         writer.writerow(data)

    #     # self.window_form.deiconify()
    #     # self.window_form.withdraw()
    #     # self.display_data(username_form)
    #     self.tryU()
    def submit_and_save(self):
        self.window_form.destroy()

        global username_form
        username_form = self.username.get()
        global selected_minat
        selected_minat = self.minat.get()
        global selected_field
        selected_field = self.bidang.get()
        global selected_jurusan
        selected_jurusan = self.jurusan.get()
        global selected_jurusan2
        selected_jurusan2 = self.jurusan2.get()
        self.usernamefom = username_form

        if not username_form or not selected_jurusan or not selected_minat or not selected_field or not selected_jurusan2:
            messagebox.showwarning("Input Error", "Semua kolom harus diisi!")
            return

        # Check if data is already present in CSV
        if not self.check_username(username_form):
            messagebox.showerror("Invalid Username", "Username tidak ditemukan!")
            return

        if self.check_duplicate(username_form):
            messagebox.showerror("Duplicate Entry", "Tidak bisa mengerjakan lagi")
            return

        data = {
            'user': username_form,
            'minat': selected_minat,
            'bidang': selected_field,
            'pilihan 1': selected_jurusan,
            'pilihan 2': selected_jurusan2
        }

        messagebox.showinfo("Success", "Data berhasil disimpan!")
        
        roott = self.build_tree(self.data_minat)
        if selected_minat and selected_field:
            self.recommended_programs = self.search_tree(roott, selected_minat, selected_field)
            self.recommended_programs_str = ', '.join(self.recommended_programs) if self.recommended_programs else "Tidak ada rekomendasi"
        else:
            self.recommended_programs_str = "Silakan pilih minat dan kategori"

        # Save to CSV
        self.fieldnames = ["user", "minat", "bidang", "pilihan 1", "pilihan 2", "Skor PU", "Skor PPU", "Skor PBM", "Skor PK", "Skor LBI", "Skor LBE", "Skor PM", "Skor Akhir"]

        with open('hasil_kuis.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=self.fieldnames, restval="-")
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        self.tryU()

    # def update_kategori(self, *args):
    #     # Update kategori when "Minat" changes (dummy implementation)
    #     pass



    def build_tree(self,data):
        
       
        if not data:
            return None
        root_key = list(data.keys())[0]
        root = TreeNode(root_key)
        
        def add_children(node, children):
            if isinstance(children, dict):
                for key, val in children.items():
                    child = TreeNode(key)
                    if node.left is None:
                        node.left = child
                    else:
                        current = node.left
                        while current.right is not None:
                            current = current.right
                        current.right = child
                    add_children(child, val)
            elif isinstance(children, list):
                for item in children:
                    child = TreeNode(item)
                    if node.left is None:
                        node.left = child
                    else:
                        current = node.left
                        while current.right is not None:
                            current = current.right
                        current.right = child
        
        add_children(root, data[root_key])
        return root



    def search_tree(self, root, minat, kategori):
        if root is None:
            return []
        if root.val == minat:
            return self.find_kategori(root, kategori)
        return self.search_tree(root.left, minat, kategori) + self.search_tree(root.right, minat, kategori)

    def find_kategori(self, node, kategori):
        results = []
        current = node.left
        while current:
            if current.val == kategori:
                child = current.left
                while child:
                    results.append(child.val)
                    child = child.right
            current = current.right
        return results

    def extract_programs(self, root):
        if root is None:
            return []
        return [root.val] + self.extract_programs(root.right)

    def update_kategori(self,*args):
        selected_minat = self.minat.get()
        if selected_minat in self.data_minat["Minat"]:
            self.field['values'] = list(self.data_minat["Minat"][selected_minat].keys())
        else:
            self.field['values'] = []

    
    def check_username(self,username):
    # Mengecek apakah username ada dalam file dataakun.csv pada kolom ke-4
        with open('dataakun.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4 and row[3] == username:
                    return True
        return False
    
    def get_data_from_csv(self,username):
        with open('dataakun.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4 and row[3] == username:
                    # Jika username ditemukan, ambil isi kolom pertama dan kedua
                    if len(row) >= 2:
                        return row[0], row[1]  # Mengembalikan isi kolom pertama dan kedua
                    else:
                        return None, None  # Jika kolom tidak lengkap, kembalikan None
        # Jika username tidak ditemukan, kembalikan None untuk kedua kolom
        return None, None

# Fungsi untuk menampilkan data dalam GUI atau di tempat lain
    def display_data(self,username):

        kolom1, kolom2 = self.get_data_from_csv(username)
        if kolom1 is not None and kolom2 is not None:
            a = f"{kolom1} {kolom2}"
            self.nama_panjang = (a)
            return self.nama_panjang
            
        else:
            print("Username tidak ditemukan atau data tidak lengkap")


      
    def check_and_delete_data(self):
        username = self.username.get()
        if not username:
            messagebox.showwarning("Input Error", "Username harus diisi!")
            return

        # Cek apakah username ada di kolom ke-4 dataakun.csv
        if self.check_username(username):
            self.delete_user_data(username)
            messagebox.showinfo("Success", f"Data untuk username '{username}' berhasil dihapus dari hasil_kuis.csv!")
        else:
            messagebox.showwarning("Not Found", f"Username '{username}' tidak ditemukan di dataakun.csv kolom ke-4!")

    def delete_user_data(self, username):
        try:
            updated_rows = []
            with open('hasil_kuis.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row['user'] != username:
                        updated_rows.append(row)

            with open('hasil_kuis.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_rows)
        except FileNotFoundError:
            messagebox.showerror("File Error", "File hasil_kuis.csv tidak ditemukan!")

    def check_duplicate(self, first_name):
        try:
            with open('hasil_kuis.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == first_name:
                        return True
            return False
        except FileNotFoundError:
            pass
        return False

    def tryU(self):
        # self.window.deiconify()
# self.window.withdraw()

        self.window = window
        frameopo=Frame(window)
        frameopo.place(x=0,y=0,relheight=1,relwidth=1)
        self.frameopo=frameopo
        popo=Image.open("DASHTRYU.png")
        self.bg = ImageTk.PhotoImage(popo)
        self.layartryu = Label(frameopo, image=self.bg)
        self.layartryu.place(x=0, y=0, relheight=1, relwidth=1)
        # self.button_back = customtkinter.CTkButton(frameopo,text="back",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#B5DDF0",width=50,height=40,command=self.back_tryu)
        # self.button_back.place(x=175,y=50)
        back = 'kembali.png'
        imageback = Image.open(back)
        resize = imageback.resize((50, 50))
        self.back1 = ImageTk.PhotoImage(resize)
        self.button3 = customtkinter.CTkButton(frameopo, image=self.back1,fg_color='white', text="", height=50, width=50, command=self.login_dashboard)
        self.button3.place(x=5, y=10)

        if not self.pu_selesai: #jika pu belom dikerjakan maka akan nyala
            self.pu = customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Umum", width=400,height=70,command=self.msgpu)
            self.pu.place(x=115,y=185)
        else:
            self.pu = customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Umum", width=400,height=70, state=DISABLED)
            self.pu.place(x=115,y=185)

        if not self.ppu_selesai and not self.pu_selesai:
            self.ppu = customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan dan Pemahaman Umum", width=400,height=70,state=DISABLED)
            self.ppu.place(x=115,y=280)
        elif not self.ppu_selesai and self.pu_selesai:
            self.ppu = customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan dan Pemahaman Umum", width=400,height=70,command=self.msgppu)
            self.ppu.place(x=115,y=280)
        else:
            self.ppu = customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan dan Pemahaman Umum", width=400,height=70, state=DISABLED)
            self.ppu.place(x=115,y=280)



        if not self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai:
            self.pbm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Bacaan dan Menulis", width=400,height=70,state=DISABLED)
            self.pbm.place(x=115,y=375)

        elif self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai:
            self.pbm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Bacaan dan Menulis", width=400,height=70,state=DISABLED)
            self.pbm.place(x=115,y=375)

        elif self.pu_selesai and self.ppu_selesai and not self.pbm_selesai:
            self.pbm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Bacaan dan Menulis", width=400,height=70,command=self.msgpbm)
            self.pbm.place(x=115,y=375)
        else:
            self.pbm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Bacaan dan Menulis", width=400,height=70,state=DISABLED)
            self.pbm.place(x=115,y=375)
        

        if not self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai:
            self.pk= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Kuantitatif", width=400,height=70,state=DISABLED)
            self.pk.place(x=115,y=470)
        elif self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai:
            self.pk= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Kuantitatif", width=400,height=70,state=DISABLED)
            self.pk.place(x=115,y=470)
        elif self.pu_selesai and self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai:
            self.pk= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Kuantitatif", width=400,height=70,state=DISABLED)
            self.pk.place(x=115,y=470)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and not self.pk_selesai:
            self.pk= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Kuantitatif", width=400,height=70,command=self.msgpk)
            self.pk.place(x=115,y=470)
        else: 
            self.pk= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Pengetahuan Kuantitatif", width=400,height=70,state=DISABLED)
            self.pk.place(x=115,y=470)
    

        if not self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai:
            self.lbi= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Indonesia", width=400,height=70,state=DISABLED)
            self.lbi.place(x=550,y=220)
        elif self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai:
            self.lbi= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Indonesia", width=400,height=70,state=DISABLED)
            self.lbi.place(x=550,y=220)
        elif self.pu_selesai and self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai:
            self.lbi= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Indonesia", width=400,height=70,state=DISABLED)
            self.lbi.place(x=550,y=220)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai:
            self.lbi= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Indonesia", width=400,height=70,state=DISABLED)
            self.lbi.place(x=550,y=220)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and self.pk_selesai and not self.lbi_selesai:
            self.lbi= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Indonesia", width=400,height=70,command=self.msglbi)
            self.lbi.place(x=550,y=220)
        else:
            self.lbi= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Indonesia", width=400,height=70,state=DISABLED)
            self.lbi.place(x=550,y=220)

        if not self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,state=DISABLED)
            self.lbe.place(x=550,y=315)
        elif self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,state=DISABLED)
            self.lbe.place(x=550,y=315)
        elif self.pu_selesai and self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,state=DISABLED)
            self.lbe.place(x=550,y=315)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,state=DISABLED)
            self.lbe.place(x=550,y=315)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,state=DISABLED)
            self.lbe.place(x=550,y=315)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and self.pk_selesai and self.lbi_selesai and not self.lbe_selesai:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,command=self.msglbe)
            self.lbe.place(x=550,y=315)
        else:
            self.lbe= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Literasi Bahasa Inggris", width=400,height=70,state=DISABLED)
            self.lbe.place(x=550,y=315)


        if not self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)
        elif self.pu_selesai and not self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)
        elif self.pu_selesai and self.ppu_selesai and not self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and not self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and self.pk_selesai and not self.lbi_selesai and not self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and self.pk_selesai and self.lbi_selesai and not self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)
        elif self.pu_selesai and self.ppu_selesai and self.pbm_selesai and self.pk_selesai and self.lbi_selesai and self.lbe_selesai and not self.pm_selesai:
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,command=self.msgpm)
            self.pm.place(x=550,y=410)
        else: 
            self.pm= customtkinter.CTkButton(frameopo, bg_color="#D6E9FC", fg_color="#3081D0", text="Penalaran Matematika", width=400,height=70,state=DISABLED)
            self.pm.place(x=550,y=410)


    def msgpu(self): #untuk menayangkan apakah ingin mengerjakan beneran?
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Penalaran Umum?")
        if x:  
            self.pu_selesai = True
            self.mulaisoal(1)

    def msgppu(self):
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Pengetahuan dan Pemahaman Umum?")
        if x: 
            self.mulaisoal(2) 
            self.ppu_selesai = True

    def msgpbm(self):
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Pengetahuan Bacaan dan Menulis?")
        if x: 
            self.mulaisoal(3) 
            self.pbm_selesai = True

    def msgpk(self):
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Pengetahuan Kuantitatif?")
        if x: 
            self.mulaisoal(4) 
            self.pk_selesai = True


    def msglbi(self):
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Literasi Bahasa Indonesia?")
        if x: 
            self.mulaisoal(5) 
            self.lbi_selesai = True

    def msglbe(self):
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Literasi Bahasa Inggris?")
        if x: 
            self.mulaisoal(6) 
            self.lbe_selesai = True

    def msgpm(self):
        x = messagebox.showinfo("Attention!","Apakah anda ingin memulai mengerjakan subtest Penalaran Matematika?")
        if x: 
            self.mulaisoal(7) 
            self.pm_selesai = True
    
    def mulaisoal(self, id):
        self.layartryu.destroy()
        self.window = window
        frame_ini=Frame(window)
        frame_ini.place(x=0,y=0,relheight=1,relwidth=1)
        self.frame_ini= frame_ini
        papi=Image.open("Group 6.png")
        self.bg = ImageTk.PhotoImage(papi)
        self.layarsoal= Label(frame_ini, image=self.bg)
        self.layarsoal.place(x=0, y=0, relheight=1, relwidth=1)

        self.window.title("Aplikasi Kuis")
        self.soal_sekarang = 0
        self.skor = 0
        self.soal = []
        self.jawaban = []
        self.start_time = None

        # self.buat_widget_soal()
        if id == 1:
            self.soal = soal_pu
            self.jawaban = [None] * len(self.soal)
        elif id == 2:
            self.soal = soal_ppu
            self.jawaban = [None] * len(self.soal)
        elif id == 3:
            self.soal = soal_pbm
            self.jawaban = [None] * len(self.soal)
        elif id == 4:
            self.soal = soal_pk
            self.jawaban = [None] * len(self.soal)
        elif id == 5:
            self.soal = soal_lbi
            self.jawaban = [None] * len(self.soal)
        elif id == 6:
            self.soal = soal_lbe
            self.jawaban = [None] * len(self.soal)
        elif id == 7:
            self.soal = soal_pm
            self.jawaban = [None] * len(self.soal)


        self.start_time = time.time()
        self.buat_widget()
        self.update_pilihan()
        self.window.after(1000, self.update_timer)
            

    def buat_widget(self):
        self.tombol_soal = []

        x_start = 100
        y_start = 90
        x_offset = 50
        y_offset = 50

        for i in range(len(self.soal)):
            btn = customtkinter.CTkButton(self.frame_ini, text=f"{i + 1}", command=self.goto_soal(i), fg_color="white", text_color="black", corner_radius=30, width=30, height=30, bg_color="#d9d9d9")
            btn.place(x=x_start + (i % 5) * x_offset, y=y_start + (i // 5) * y_offset)
            self.tombol_soal.append(btn)

        self.update_tombol_soal()
        self.frame_pertanyaan = Frame(self.frame_ini, width=819, height=245)
        self.frame_pertanyaan.place(x=526, y=70)

        if 0 <= self.soal_sekarang < len(self.soal):
            self.pertanyaan_label = Label(self.frame_pertanyaan, text=self.soal[self.soal_sekarang]["pertanyaan"], font=("Arial", 10), bg="white", fg="black", wraplength=700)
            self.pertanyaan_label.pack(anchor="center")
        else:
            print("Indeks diluar jangkauan.")
            
        self.timer_label = Label(self.frame_ini, text="Waktu tersisa: 00:05", font=("Helvetica", 16), bg="#d9d9d9")
        self.timer_label.place(x=121, y=30)

        self.tombol_pilihan = []
        y_start = 298
        y_offset = 70

        for i in range(5):
            btn = customtkinter.CTkButton(self.frame_ini, text="", command=self.pilih_jawaban(i), fg_color="white", text_color="black", corner_radius=15, width=647, height=43, bg_color="white",compound='left')
            btn.place(x=500, y=y_start + i * y_offset)
            self.tombol_pilihan.append(btn)
        self.update_pilihan()

        self.tombol_kembali = customtkinter.CTkButton(self.frame_ini, text="Back", command=self.soal_sebelumnya, bg_color="#f8f8f8", fg_color="black", width=80, height=20, corner_radius=15, font=("Sans Serif", 13), border_color="navy")
        self.tombol_kembali.place(x=80, y=630)

        self.tombol_berikutnya = customtkinter.CTkButton(self.frame_ini, text="Next", command=self.soal_berikutnya, bg_color="#f8f8f8", fg_color="black", width=80, height=20, corner_radius=15, font=("Sans Serif", 13), border_color="navy")
        self.tombol_berikutnya.place(x=200, y=630)

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = 300 - elapsed_time
        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            self.timer_label.config(text=f"Waktu tersisa: {minutes:02}:{seconds:02}")
            self.window.after(1000, self.update_timer)
        else:
            self.end_quiz()

    def update_tombol_soal(self):
        for i, btn in enumerate(self.tombol_soal):
            if i == self.soal_sekarang:
                btn.configure(fg_color="white")
            else:
                btn.configure(fg_color="#f5f5f5")

    def update_pilihan(self):
        data_soal = self.soal[self.soal_sekarang]
        self.pertanyaan_label.config(text=data_soal["pertanyaan"])
        for i, pilihan in enumerate(data_soal["pilihan"]):
            self.tombol_pilihan[i].configure(
                text=pilihan,
                command=self.pilih_jawaban(i),
                fg_color="lightblue" if self.jawaban[self.soal_sekarang] == i else "white"
            )
        self.update_tombol_soal()
        self.update_tombol_berikutnya()

    def update_tombol_berikutnya(self):
        if hasattr(self, 'tombol_berikutnya'):
            if self.soal_sekarang == len(self.soal) - 1:
                self.tombol_berikutnya.configure(text="Finish", command=self.end_quiz)
            else:
                self.tombol_berikutnya.configure(text="Next", command=self.soal_berikutnya)

    def pilih_jawaban(self, pilihan):
        def inner():
            self.jawaban[self.soal_sekarang] = pilihan
            self.update_pilihan()
        return inner

    def soal_berikutnya(self):
        if self.soal_sekarang < len(self.soal) - 1:
            self.soal_sekarang += 1
            self.update_pilihan()

    def soal_sebelumnya(self):
        if self.soal_sekarang > 0:
            self.soal_sekarang -= 1
            self.update_pilihan()

    def goto_soal(self, indeks):
        def inner():
            self.soal_sekarang = indeks
            self.update_pilihan()
        return inner

    def hitung_skor(self):
        # Method ini menghitung skor berdasarkan jawaban yang benar dari pengguna
        self.skor = 0  # Inisialisasi skor sebelum menghitung
        for i, jawaban in enumerate(self.jawaban):
            if jawaban == self.soal[i]["jawaban"]:
                self.skor += self.soal[i]["skor"]
        self.list_skor.append(self.skor)

    def end_quiz(self):
        # Method ini dipanggil saat kuis berakhir
        messagebox.showinfo("Apakah anda ingin mengakhiri pengerjaan subtest ini?")
        self.hitung_skor()  # Hitung skor
        self.layarsoal.destroy()  # Hancurkan layar soal
        self.tryU()  # Tampilkan layar TryU
        if self.pu_selesai and self.ppu_selesai and self.pk_selesai and self.pbm_selesai and self.pm_selesai and self.lbe_selesai and self.lbi_selesai:
            # Jika semua kategori sudah selesai
            self.save_results(self.list_skor)  # Simpan hasil kuis
            print(self.list_skor)  # Cetak skor

    def save_results(self, kumpulan_skor):
        # try:5
            # Read the entire CSV content into a list of dictionaries
            with open("hasil_kuis.csv", "r", newline='') as file:
                fieldnames = ["user", "minat", "bidang", "pilihan 1","pilihan 2", "Skor PU", "Skor PPU", "Skor PBM", "Skor PK", "Skor LBI", "Skor LBE", "Skor PM","Skor Akhir"]
                reader = csv.DictReader(file, fieldnames=fieldnames)
                rows = list(reader)

            rowbaru = []

            # Update the relevant rows if the condition is met
            for row in rows:
                if row["user"] == username_form and row["Skor PU"] == "-":
                    row["Skor PU"] = kumpulan_skor[0]
                    row["Skor PPU"] = kumpulan_skor[1]
                    row["Skor PBM"] = kumpulan_skor[2]
                    row["Skor PK"] = kumpulan_skor[3]
                    row["Skor LBI"] = kumpulan_skor[4]
                    row["Skor LBE"] = kumpulan_skor[5]
                    row["Skor PM"] = kumpulan_skor[6]
                    rowbaru.append(row)

            # Write the updated content back to the CSV file
            with open("hasil_kuis.csv", "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                # writer.writeheader()  # Write the header row
                writer.writerows(rowbaru)  # Write all the rows

            print("Hasil kuis telah disimpan ke dalam file 'hasil_kuis.csv'")
        # except Exception as e:
        #     print("Gagal menyimpan hasil kuis:", str(e))

            self.calculate_and_write_average()
            self.rekomakhir()
 

    def calculate_and_write_average(self):
        # Method ini menghitung rata-rata skor akhir dan menulisnya kembali ke file CSV
        fieldnames = ["user", "minat", "bidang", "pilihan 1", "pilihan 2", "Skor PU", "Skor PPU", "Skor PBM", "Skor PK", "Skor LBI", "Skor LBE", "Skor PM", "Skor Akhir"]
        updated_rows = []

        with open("hasil_kuis.csv", "r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                skor_pelajaran = []
                for field in fieldnames[5:12]:
                    if row[field] == '-':
                        skor_pelajaran.append(0)
                    else:
                        skor_pelajaran.append(int(row[field]))
                rata_rata = sum(skor_pelajaran) / len(skor_pelajaran)
                row['Skor Akhir'] = rata_rata
                updated_rows.append(row)

        with open("hasil_kuis.csv", "w", newline='') as file:  # Ubah mode ke 'w' (write)
            writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames, restval="-")
            writer.writeheader()
            for updated_row in updated_rows:
                writer.writerow(updated_row)

    # def rekomakhir(self):
    #     self.window = Toplevel(self.window)
    #     self.window.title("Skor Akhir")
    #     self.window.geometry("410x390")
    #     self.window.configure(background='white')
    #     self.window.resizable(width=tk.FALSE, height=tk.FALSE)

    #     imji = Image.open("bg skor.png")
    #     imji_resized = imji.resize((410, 390))
    #     image_boform = ImageTk.PhotoImage(imji_resized)
    #     image_label = tk.Label(self.window, image=image_boform)
    #     image_label.place(x=0, y=0, relwidth=1, relheight=1)
    #     image_label.image = image_boform  # Keep a reference to avoid garbage collection

    #     # tk.Label(self.window, text="Skor Akhir", font=("Arial", 16, "bold"), bg="white").place(x=90, y=50)

    #     c = 0
    #     user_score = None
    #     with open('hasil_kuis.csv', mode='r', newline='') as file:
    #         reader = csv.DictReader(file)
    #         for i in reader:
    #             if str(i["user"]) == str(self.username.get()):  # Gunakan username yang sesuai
    #                 self.pil1 = str(i["pilihan 1"])
    #                 self.pil2 = str(i["pilihan 2"])
    #                 user_score = float(i["Skor Akhir"])
    #                 user_score = round(user_score, 2)
    #                 c = 1
    #                 break

    #     if c == 1 and user_score is not None:
    #         a = self.display_data(self.username.get())  # Gunakan username yang sesuai
    #         tk.Label(image_label,justify="center", text=f"{a}", bg='white', font=("Arial", 25)).place(x=140, y=15)
    #         tk.Label(image_label, justify="center", text=f"Skor Akhir:", bg='#0012B0',fg="#f4f4f4", font=("Arial", 15)).place(x=20, y=115)
    #         tk.Label(image_label, justify="center", text=f"{user_score}", bg='#0012B0', fg="#f4f4f4", font=("Arial", 35, "bold")).place(x=20, y=129)

    #         with open('datapg.csv', mode='r', newline='') as file:
    #             reader1 = csv.DictReader(file)
    #             found = False

    #             for row in reader1:
    #                 required_score = float(row["Nilai UTBK"].replace(',', '.'))
    #                 if row["Jurusan"] == self.pil1 and user_score >= required_score:
    #                     tk.Label(image_label, text=f"Selamat anda Lolos di pilihan 1:{self.jurusan.get()}",font=("Arial",20), bg='white').place(x=47, y=235)
    #                     found = True
    #                     break  # keluar loop jika lolos pilihan 1
    #                 elif row["Jurusan"] == self.pil2 and not found and user_score >= required_score:
    #                     tk.Label(image_label, text=f"Selamat anda Lolos di pilihan 2:{self.jurusan2.get()}",font=("Arial",20), bg='white').place(x=47, y=293)
    #                     found = True

    #             if not found:
    #                 tk.Label(image_label, text="Anda Tidak Lolos di pilihan 1 maupun 2", bg='white',font=("Arial",20)).place(x=47, y=235)
    #                 tk.Label(image_label, text="Semangat dan Jangan Menyerah!", bg='white',font=("Arial",20)).place(x=47, y=295)
                                                                                                  

    #             # Rekomendasi prodi lainnya
    #             if hasattr(self, 'recommended_programs_str') and self.recommended_programs_str:
    #                 tk.Label(image_label, text=f"Rekomendasi Prodi:", bg='white',font=("Arial",20),fg="#143676").place(x=22, y=366)
    #                 tk.Label(image_label, text=f"{self.recommended_programs_str}", bg='white',font=("Arial",23),fg="white").place(x=22, y=434)
    #     else:       
    #         tk.Label(self.window, text="Data user tidak ditemukan atau skor tidak valid",font=("Arial",23), bg='white').place(x=22, y=70)
    
    def rekomakhir(self):
        self.window = Toplevel(self.window)
        self.window.title("Skor Akhir")
        self.window.geometry("410x500")
        self.window.configure(background='white')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)

        imji = Image.open("bg skor.png")  # Make sure the image file is in the correct path
        imji_resized = imji.resize((410, 500))
        image_boform = ImageTk.PhotoImage(imji_resized)
        image_label = tk.Label(self.window, image=image_boform)
        image_label.place(x=0, y=0, relwidth=1, relheight=1)
        image_label.image = image_boform

        c = 0
        user_score = None
        with open('hasil_kuis.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if str(i["user"]) == str(self.username.get()):  # Gunakan username yang sesuai
                    self.pil1 = str(i["pilihan 1"])
                    self.pil2 = str(i["pilihan 2"])
                    user_score = float(i["Skor Akhir"])
                    user_score = round(user_score, 2)
                    c = 1
                    break

        if c == 1 and user_score is not None:
            a = self.display_data(self.username.get())  # Gunakan username yang sesuai
            tk.Label(image_label, justify="center", text=f"{a}", bg='white', font=("Arial", 20)).place(x=140, y=15)
            tk.Label(image_label, justify="center", text=f"Skor Akhir:", bg='#0012B0', fg="#f4f4f4", font=("Arial", 15)).place(x=140, y=105)
            tk.Label(image_label, justify="center", text=f"{user_score}", bg='#0012B0', fg="#f4f4f4", font=("Arial", 25, "bold")).place(x=150, y=135)

            with open('datapg.csv', mode='r', newline='') as file:
                reader1 = csv.DictReader(file)
                found = False

                for row in reader1:
                    required_score = float(row["Nilai UTBK"].replace(',', '.'))
                    if row["Jurusan"] == self.pil1 and user_score >= required_score:
                        tk.Label(image_label, text=f"Selamat anda Lolos di pilihan 1: {self.jurusan.get()}", font=("Arial", 12), bg='white').place(x=47, y=230)
                        found = True
                        break  # keluar loop jika lolos pilihan 1
                    elif row["Jurusan"] == self.pil2 and not found and user_score >= required_score:
                        tk.Label(image_label, text=f"Selamat anda Lolos di pilihan 2: {self.jurusan2.get()}", font=("Arial", 12), bg='white').place(x=47, y=290)
                        found = True

                if not found:
                    tk.Label(image_label, text="Anda Tidak Lolos di pilihan 1 maupun 2", bg='white', font=("Arial", 12)).place(x=47, y=230)
                    tk.Label(image_label, text="Semangat dan Jangan Menyerah!", bg='white', font=("Arial", 12)).place(x=47, y=290)

                # Rekomendasi prodi lainnya
                if hasattr(self, 'recommended_programs_str') and self.recommended_programs_str:
                    tk.Label(image_label, text=f"Rekomendasi Prodi:", fg='white', font=("Arial", 10), bg="#143676").place(x=20, y=350)
                    tk.Label(image_label, text=f"{self.recommended_programs_str}", bg='white', font=("Arial", 15), fg="black").place(x=22, y=394)
        else:
            tk.Label(self.window, text="Data user tidak ditemukan atau skor tidak valid", font=("Arial", 23), bg='white').place(x=47, y=230)
        def close_window():
            self.window.destroy()

        close_button = customtkinter.CTkButton(self.window, text="Tutup", command=close_window, font=("Arial", 15))
        close_button.place(x=150, y=444)  # Adjust position as necessary

    # def display_data1(self, username):
      
    #     return f"{username}"
    
    def run(self):
        self.window.mainloop()




soal_pbm = [
    {
        "pertanyaan": "Kata yang mengalami makna meluas terdapat pada kalimat berikut, kecuali ….",
        
        "pilihan": ["Para tokoh mengajak masyarakat untuk menggunakan hak pilihnya dengan cerdas\n dan tanpa tekanan agar kursi di DPR terwakili secara benar.",
                    "Keutuhan fungsi UN terkait dengan pemetaan indeks kompetensi, kelulusan seleksi, \ndan perbaikan terhadap infrastruktur sekolah",
                    "Para sarjana lingkungan berkumpul di Kanada untuk mengikuti konferensi internasional tentang perubahan iklim.",
                    "Kapal-kapal Australia berlayar sejak beberapa hari yang lalu mencari kotak hitam pesawat MH370.",
                    "“Maaf, apakah Bapak tahu gedung induk tempat seminar berlangsung?"],
        "jawaban": 2,
        "skor": 100
    },
    {
        "pertanyaan": "Kata yang mengalami makna menyempit terdapat pada kalimat berikut, kecuali ….",
        
        "pilihan": ["Bangunan sekolah tersebut sudah lama tidak direnovasi.",
                    "Para pendeta baru saja mengunjungi lokasi bencana.",
                    "Kami belajar membaca dan menulis kaligrafi di madrasah.",
                    "Entah dari mana sumber bau busuk yang tercium oleh mereka.",
                    "Walaupun sebagai seorang pembantu, dia tidak pernah merasa malu."],
        "jawaban": 0,
        "skor": 200
    },
    {
        "pertanyaan": "(1) Menteri Pendidikan dan Kebudayaan (Mendikbud), Nadiem Makarim, menyebutkan bahwa prioritas Merdeka Belajar 2021 akan berfokus pada beberapa hal. (2) Fokus pertama meliputi pembiayaan pendidikan yang akan menyasar pemilik Kartu Indonesia Pintar (KIP) Kuliah dengan target 1,095 juta mahasiswa dan KIP Sekolah dengan target 17,9 juta siswa. (3) “Kemudian, ada bantuan pemerintah kepada 13 SILN dan 2.236 lembaga,” ungkap Nadiem dalam acara Taklimat Media Awal Tahun 2021. (4) Dengan adanya hal itu, program-program yang dijalankan diharapkan dapat berjalan lancar. (5) Fokus kedua adalah program digitalisasi sekolah dan medium pembelajaran melalui empat sistem penguatan platform digital, dan delapan layanan terpadu Kemendikbud. (6) Fokus ketiga adalah pembinaan peserta didik, prestasi, talenta, dan penguatan karakter. (7) Prioritas ini […] diciptakan melalui tiga layanan pendampingan advokasi dan sosialisasi penguatan karakter. (8) Selain itu, prioritas ini diciptakan dengan beberapa cara, seperti pembinaan peserta didik oleh 345 pemerintah daerah serta peningkatan prestasi, manajemen talenta kepada 13.505 pelajar, dan sebagainya. Kata yang tepat untuk melengkapi … pada kalimat 7 adalah ….",
        
        "pilihan": ["bahkan", "justru", "kemudian", "akan", "selalu"],
        "jawaban": 3,
        "skor": 200
    },
    {
        "pertanyaan": "Perhatikan teks berikut. Menteri Pendidikan dan Kebudayaan (Mendikbud), Nadiem Makarim, menyebutkan bahwa prioritas Merdeka Belajar 2021 akan berfokus pada beberapa hal. (2) Fokus pertama meliputi pembiayaan pendidikan yang akan menyasar pemilik Kartu Indonesia Pintar (KIP) Kuliah dengan target 1,095 juta mahasiswa dan KIP Sekolah dengan target 17,9 juta siswa. (3) “Kemudian, ada bantuan pemerintah kepada 13 SILN dan 2.236 lembaga,” ungkap Nadiem dalam acara Taklimat Media Awal Tahun 2021. (4) Dengan adanya hal itu, program-program yang dijalankan diharapkan dapat berjalan lancar. (5) Fokus kedua adalah program digitalisasi sekolah dan medium pembelajaran melalui empat sistem penguatan platform digital, dan delapan layanan terpadu Kemendikbud.\nPenulisan kata yang salah terdapat pada kalimat nomor ….",
        
        "pilihan": ["(1)", "(2)", "(3)", "(4)", "(5)"],
        "jawaban": 1,
        "skor": 200
    },
    {
        "pertanyaan": "Kata erat kaitannya dalam kalimat (5) seharusnya ….",
        
        "pilihan": ["dibiarkan saja (sudah benar)",
                    "diganti dengan berkaitan erat",
                    "diganti dengan berhubungan",
                    "didahului kata sangat",
                    "dihilangkan kata kaitannya"],
        "jawaban": 1,
        "skor": 300
    }
]
soal_lbi= [
        {
            "pertanyaan": "Mobil listrik bukanlah inovasi baru pada abad ke-21. Akan tetapi, teknologinya baru mendapat perhatian luas beberapa tahun terakhir. Mobil listrik menggunakan motor listrik yang ditenagai baterai isi ulang sebagai mesin penggeraknya. Salah satu perkembangan signifikan terkait mobil listrik adalah upaya pembangunan infrastruktur pengisian daya yang menggantikan stasiun pengisian bahan bakar konvensional.  Stasiun pengisian daya dapat dipasang di berbagai lokasi, termasuk di rumah. Dibandingkan dengan mobil konvensional, mobil listrik punya sejumlah keunggulan, seperti lebih hening dari segi suara dan tidak ada emisi gas buang. Mobil listrik lebih ramah lingkungan dan dapat mengurangi polusi udara serta kebisingan. Sebagai alternatif, mobil listrik berpotensi mengurangi dampak negatif terhadap lingkungan, termasuk terhadap perubahan iklim yang menjadi masalah serius Tanggapan kita sebagai masyarakat adalah",
            
            "pilihan": ["mendukung kebijakan insentif nonmoneter yang memberi manfaat langsung bagi masyarakat", 
                        "mendukung kebijakan pengembangan mobil listrik untuk mengurangi konsumsi minyak bumi", 
                        "mendukung kebijakan pemerintah yang akan membangun semua stasiun pengisian daya",
                        "mendukung kebijakan penggantian semua mobil bensin dan diesel dengan mobil listrik",
                        "mendukung kebijakan insentif tunai kepada pengembang dan pengguna mobil listrik",
                        ],
            "jawaban": 1,
            "skor": 100
        },
        {
            "pertanyaan": "Salah satu perkembangan signifikan terkait mobil listrik adalah upaya pembangunan infrastruktur pengisian daya yang menggantikan stasiun pengisian bahan bakar konvensional. Stasiun pengisian daya dapat dipasang di berbagai lokasi, termasuk di rumah. Dibandingkan dengan mobil konvensional, mobil listrik punya sejumlah keunggulan, seperti lebih hening dari segi suara dan tidak ada emisi gas buang. Mobil listrik lebih ramah lingkungan dan dapat mengurangi polusi udara serta kebisingan. Sebagai alternatif, mobil listrik berpotensi mengurangi dampak negatif terhadap lingkungan, termasuk terhadap perubahan iklim yang menjadi masalah serius.Berdasarkan bacaan yang terdapat pada soal sebelumnya, alasan utama dikembangkannya mobil listrik adalah ….",
            
            "pilihan": ["cadangan minyak bumi akan segera habis","gas buang yang dihasilkannya ramah lingkungan","rumah dapat dijadikan tempat pengisian baterai mobil","mobil listrik semakin populer dalam beberapa tahun terakhir di masyarakat","baterai mobil biasa mengandung logam berbahaya yang menyebabkan polusi udara"],
            "jawaban": 0,
            "skor": 200
        },
        {
            "pertanyaan": "Namun, kendaraan listrik juga memiliki kelemahan. Salah satunya adalah ketersediaan infrastruktur pengisian daya yang belum merata, terutama di beberapa daerah. Biaya penggantian baterai mobil listrik lebih tinggi karena kapasitasnya yang besar, dan proses pengisian baterai memerlukan waktu yang lebih lama. Selain itu, baterai mobil listrik juga cenderung berat dan memiliki keterbatasan dalam kapasitas penyimpanan energi untuk perjalanan jarak jauh.Sesuai bacaan di atas, kekurangan dari mobil listrik adalah ",
            
            "pilihan": ["teknologi baterai belum berkembang baik dan harganya mahal.", "stasiun pengisian baterai tidak bisa dibangun di sembarang tempat","daya baterai mobil listrik tidak sebesar daya baterai mobil biasa","menyebabkan perubahan iklim yang harus ditangani secara serius","waktu pengisian baterai sangat lama seperti baterai untuk mobil biasa"],
            "jawaban": 0,
            "skor": 300
        },
        {
            "pertanyaan": "Pernyataan di bawah ini yang merupakan opini penulis sesuai bacaan adalah ….",
            
            "pilihan": [
                "mendukung kebijakan insentif nonmoneter yang memberi manfaat langsung bagi masyarakat",
                "mendukung kebijakan pengembangan mobil listrik untuk mengurangi konsumsi minyak bumi",
                "mendukung kebijakan pemerintah yang akan membangun semua stasiun pengisian daya",
                "mendukung kebijakan penggantian semua mobil bensin dan diesel dengan mobil listrik",
                "mendukung kebijakan insentif tunai kepada pengembang dan pengguna mobil listrik"
            ],
            "jawaban": 1,
            "skor": 300
        },
        {
            "pertanyaan": "Jika ditambahkan satu paragraf baru di antara paragraf 1 dan 2, paragraf tersebut kemungkinan akan membahas ….",
            
            "pilihan": [
                "Perbandingan tingkat polusi cahaya di berbagai negara",
                "Alasan manusia melakukan penerangan di malam hari",
                "Penelitian tentang cahaya yang tidak mengganggu",
                "Efek penerangan terhadap kelelawar sebagai makhluk nokturnal",
                "Salah satu makhluk yang terganggu, yaitu kelelawar"
            ],
            "jawaban": 4,
            "skor": 100
        }
    ]
soal_lbe= [ 
    {
        "pertanyaan": "It's hard to manage your money well in retirement unless you're realistic about what you have. The first thing to do is to make a budget and sketch out a plan to cover your expenses. Before retiring, keep track of your spending and regular expenses, like housing, food, health care, etc. Then assess how those expenses might change in retirement (e.g., if you plan to move to a less expensive home or area; and if your insurance costs will be subsidized by your old employer). You should also consider paying for a child's wedding, buying a car, or taking a major vacation. Then assess what fixed income you will have come in (e.g., Social Security or pension payments). The difference between your expected spending and your fixed income is the amount you will need to draw from your savings. It would also help to consult with a professional. What is the main idea of Text 1?",
        
        "pilihan": ["Life uncertainty is happening among newly retired people in America.",
                    "There are some reasons why retirees use their savings.",
                    "The retirees' financial condition affects how much they are willing to spend their savings.",
                    "Most retirees in America do not use their savings a lot in retirement.",
                    "How the newly retired people spend their savings is quite similar."],
        "jawaban": 3,
        "skor": 300
    },
    {
        "pertanyaan": "The first thing to do is to make a budget and sketch out a plan to cover your expenses.Which of the following best restates this sentence?",
        
        "pilihan": ["Covering all costs is the first thing to plan in relation to budget expenses.",
                    "Preparing a budget and drafting a plan of your costs is the first thing you should carry out.",
                    "Planning and calculating the budget expenses is the first thing to be carried out.",
                    "Drafting your plan that includes your costs should be done first to prepare a good budget.",
                    "Budgeting and planning should be prepared first to be able to pay your costs."],
        "jawaban": 1,
        "skor": 200
    },
    {
        "pertanyaan": "Before retiring, keep track of your spending and regular expenses, like housing, food, health care, etc. Then assess how those expenses might change in retirement (e.g., if you plan to move to a less expensive home or area; and if your insurance costs will be subsidized by your old employer). The purpose of Text is to ....",
        
        "pilihan": ["provide advice for newly retired people on how to manage their money in retirement.",
                    "explain the process of managing your expenses during retirement",
                    "explain how to get a professional financial advisor to manage your savings after you retire",
                    "discuss what newly retired people should do to monitor their expenses",
                    "Argue which investment is the best for retirement income."],
        "jawaban": 0,
        "skor": 300
    },
    {
        "pertanyaan": "Which of the following statements shows the author's positive attitude toward an investment analyst?",
        
        "pilihan": ["For some it's almost physically painful,\" said David John, a senior strategic policy advisor.",
                    "No doubt this is partly because they are among the last generation of workers to benefit from corporate pensions",
                    "They're trying to figure out who they are now that their primary career is over\n and figuring out what they can and can't do financially",
                    "It's hard to manage your money well in retirement unless you're realistic about what you have.",
                    "A financial advisor can help you strategize how to manage and use your money in the years ahead."],
        "jawaban": 4,
        "skor": 100
    },
    {
        "pertanyaan": "Do you play video games? If so, you aren't alone. Video games are becoming more common and are increasingly enjoyed by adults. The average age of gamers has been increasing. Changing technology also means that more people are exposed to video games.  Many committed gamers play on desktop computers or consoles, but a new breed of casual gamers has emerged, who play on smartphones and tablets at spare moments throughout the day, like their morning commute. So, we know that video games are an increasingly common form of entertainment, but do they have any effect on our brains and behavior? Over the years, the media have made various sensationalist claims about video games and their effect on our health and happiness. Games have sometimes been praised or demonized, often without real data backing up those claims. Moreover, gaming is a popular activity, so everyone seems to have strong opinions on the topic, says Marc Palaus, first author on the review, recently published in Frontiers in Human Neuroscience. Palaus and his colleagues wanted to see if any trends had emerged from the research to date concerning how video games affect the structure and activity of our brains. They collected the results from 116 scientific studies, 22 of which looked at structural changes in the brain and 100 of which looked at changes in brain functionality and or behavior. Studies show that playing video games can change how our brains perform, and even their structure. What can be inferred from the passage above?",
        
        "pilihan": ["Gamers are more likely to have brain damage due to the change in their brain structures.",
                    "Given its benefits, gaming will now be continuously praised on the media.",
                    "Gamers will find it easier to focus on tasks that require a lot of energy or attention.",
                    "Gaming will continue to become increasingly popular and will render other forms of entertainment useless.",
                    "Gamers are healthier and happier compared to people who don’t play video games."],
        "jawaban": 2,
        "skor": 100
    }]
soal_pm= [{
        "pertanyaan": "Pada hari Minggu, ayah mengirimkan X pesan pada ibu setiap jam selama 5 jam. Sedangkan adik mengirim Z pesan setiap jam selama 4 jam.\nManakah jawaban di bawah ini yang merepresentasikan jumlah pesan yang dikirim oleh ayah dan adik pada Minggu siang?",
        
        "pilihan": ["9XZ", "20XZ", "5X + 9Z", "4X + 5Z", "5X+4Z"],
        "jawaban": 3,
        "skor": 100
    },
    {
        "pertanyaan": "Di sebuah universitas internasional, kurang lebih 7% mahasiswa baru dan 5% mahasiswa lama sudah terdaftar sebagai relawan untuk korban bencana alam.\nApabila jumlah relawan yang terdaftar masing-masing adalah 562 mahasiswa baru dan 602 mahasiswa lama, manakah di antara pilihan berikut ini yang paling mendekati jumlah mahasiswa baru dan mahasiswa lama di universitas internasional tersebut?",
        
        "pilihan": ["160", "69", "39", "40", "15"],
        "jawaban": 1,
        "skor": 300
    },
    {
        "pertanyaan": "Pada pencalonan wali kota, ketua kampanye mempunyai dana sebesar x juta rupiah untuk dibagikan kepada para tim sukses.\nApabila setiap tim sukses mendapatkan 3 juta rupiah, dia akan mempunyai sisa 5 juta rupiah.\nNamun, jika ketua kampanye memberikan 4 juta rupiah pada setiap tim sukses, ia memerlukan tambahan 21 juta rupiah.\nBerapakah jumlah tim sukses yang akan mendapatkan dana tersebut?",
        
        "pilihan": ["16", "21", "23", "26", "15"],
        "jawaban": 3,
        "skor": 200
    },
    {
        "pertanyaan": "Sebuah bianglala (ferris wheel) bertitik pusat P (0,0). Titik P berada pada ketinggian 35 meter dari permukaan tanah. Setiap penumpang bianglala naik dari titik terbawah, yaitu titik D.\nDalam waktu 5 menit, setiap penumpang bianglala telah menjalani lintasan sepanjang 125π/4 meter. Sebuah lampu dipasang pada suatu titik di bianglala. Bianglala berputar satu putaran dalam waktu … menit.",
        
        "pilihan": ["6", "7", "8", "9", "10"],
        "jawaban": 2,
        "skor": 200
    },
    {
        "pertanyaan": "Pada suatu saat seseorang berada pada titik B. Dua puluh menit kemudian, dia berada pada titik yang jaraknya ke garis AC adalah … meter.",
        
        "pilihan": ["0", "10", "12,5", "20", "25"],
        "jawaban": 2,
        "skor": 200
    }
    
]
soal_ppu = [
    {
        
        "pertanyaan": "Susu merupakan jenis minuman yang keberadaannya sangat penting dalam lingkup masyarakat. Minuman susu mengandung banyak vitamin dan mineral yang dibutuhkan untuk meningkatkan kesehatan tubuh manusia. Harga susu berbeda-beda tergantung jenis susu. Seperti susu sapi, susu kambing dan lain-lain. Susu sapi pun sering dijadikan minuman sehari-hari manusia untuk memperkuat daya tahan tubuh. Di pasaran terdapat berbagai macam susu. Seperti susu sapi murni maupun susu yang telah dimodifikasi dalam kemasan tertentu.\n\nSetelah membaca paragraf di atas, kita dapat memahami bahwa susu mempunyai banyak manfaat bagi manusia. Apakah yang menjadi manfaat minum susu?",
        "pilihan": [
            "Rasa yang lezat",
            "Harga murah",
            "Meningkatkan kesehatan dan daya tahan tubuh",
            "Meningkatkan ekonomi",
            "Mempercerpat pertumbuhan badan"
        ],
        "jawaban": 2,
        "skor": 200
    },
    {
        "pertanyaan": "Sebagian besar orang sering mengeluh karena terlalu sibuk. Mereka umumnya ingin memiliki lebih banyak waktu luang. Namun, penelitian terbaru menemukan bahwa terlalu banyak waktu luang ternyata tidak lebih baik daripada terlalu sibuk. Menurut penelitian yang diterbitkan oleh American Psychological Association, bertambahnya waktu luang memang dapat meningkatkan rasa bahagia. Akan tetapi, perasaan itu hanya bertahan sampai titik tertentu. Jika waktu luang yang dimiliki terlalu banyak, akan ada dampak buruk yang timbul. Untuk menyelidiki fenomena tersebut, para peneliti melakukan eksperimen daring yang melibatkan lebih dari 6.000 peserta. Peneliti menemukan bahwa orang yang memiliki waktu luang sedikit merasa lebih stres daripada mereka yang memiliki jumlah waktu luang sedang. Sementara itu, mereka yang memiliki waktu luang banyak juga merasa kurang produktif daripada mereka yang berada dalam kelompok sedang. Lebih lanjut, temuan tersebut menunjukkan bahwa berakhir dengan waktu luang sepanjang hari untuk melakukan hal-hal yang diinginkan ternyata dapat membuat seseorang merasa tidak bahagia. Sebaliknya, orang harus berusaha untuk memiliki waktu luang dalam jumlah sedang agar dapat melakukan apa yang mereka inginkan.\n\nTopik bacaan tersebut adalah …",
        "pilihan": [
            "perbandingan antara orang yang memiliki waktu luang dengan orang yang sibuk",
            "kelebihan dan kekurangan dari adanya waktu luang yang terlalu banyak",
            "memiliki terlalu banyak waktu luang tidak lebih baik daripada terlalu sibuk",
            "dampak buruk yang dialami oleh orang-orang yang memiliki waktu luang",
            "Penelitian American Psychological Association tentang kesibukan dan waktu luang"
        ],
        "jawaban": 2,
        "skor": 200
    },
    {
       
        "pertanyaan": "Sebagian besar orang sering mengeluh karena terlalu sibuk. Mereka umumnya ingin memiliki lebih banyak waktu luang. Namun, penelitian terbaru menemukan bahwa terlalu banyak waktu luang ternyata tidak lebih baik daripada terlalu sibuk. Menurut penelitian yang diterbitkan oleh American Psychological Association, bertambahnya waktu luang memang dapat meningkatkan rasa bahagia. Akan tetapi, perasaan itu hanya bertahan sampai titik tertentu. Jika waktu luang yang dimiliki terlalu banyak, akan ada dampak buruk yang timbul. Untuk menyelidiki fenomena tersebut, para peneliti melakukan eksperimen daring yang melibatkan lebih dari 6.000 peserta. Peneliti menemukan bahwa orang yang memiliki waktu luang sedikit merasa lebih stres daripada mereka yang memiliki jumlah waktu luang sedang. Sementara itu, mereka yang memiliki waktu luang banyak juga merasa kurang produktif daripada mereka yang berada dalam kelompok sedang. Lebih lanjut, temuan tersebut menunjukkan bahwa berakhir dengan waktu luang sepanjang hari untuk melakukan hal-hal yang diinginkan ternyata dapat membuat seseorang merasa tidak bahagia. Sebaliknya, orang harus berusaha untuk memiliki waktu luang dalam jumlah sedang agar dapat melakukan apa yang mereka inginkan.\n\nMakna yang sama dari kata dampak pada kalimat (6) terdapat pula pada kata ….",
        "pilihan": [
            "impak",
            "efek",
            "imbas",
            "akibat",
            "implikasi"
        ],
        "jawaban": 0,
        "skor": 200
    },
    {
        
        "pertanyaan": "Setelah aksi pembumihangusan itu, gedung ini dibangun kembali menjadi sebuah pertokoan.\n\nBentukan kata ""Pembumihanguskan"" pada kalimat di atas sama dengan bentukan kata…",
        "pilihan": [
            "menindaklanjuti",
            "pengambinghitaman",
            "menganaktirikan",
            "ketidaktahuan",
            "memperdengarkan"
        ],
        "jawaban": 3,
        "skor": 200
    },
    {
        "pertanyaan": "Sebagian besar orang sering mengeluh karena terlalu sibuk. Mereka umumnya ingin memiliki lebih banyak waktu luang. Namun, penelitian terbaru menemukan bahwa terlalu banyak waktu luang ternyata tidak lebih baik daripada terlalu sibuk. Menurut penelitian yang diterbitkan oleh American Psychological Association, bertambahnya waktu luang memang dapat meningkatkan rasa bahagia. Akan tetapi, perasaan itu hanya bertahan sampai titik tertentu. Jika waktu luang yang dimiliki terlalu banyak, akan ada dampak buruk yang timbul. Untuk menyelidiki fenomena tersebut, para peneliti melakukan eksperimen daring yang melibatkan lebih dari 6.000 peserta. Peneliti menemukan bahwa orang yang memiliki waktu luang sedikit merasa lebih stres daripada mereka yang memiliki jumlah waktu luang sedang. Sementara itu, mereka yang memiliki waktu luang banyak juga merasa kurang produktif daripada mereka yang berada dalam kelompok sedang. Lebih lanjut, temuan tersebut menunjukkan bahwa berakhir dengan waktu luang sepanjang hari untuk melakukan hal-hal yang diinginkan ternyata dapat membuat seseorang merasa tidak bahagia. Sebaliknya, orang harus berusaha untuk memiliki waktu luang dalam jumlah sedang agar dapat melakukan apa yang mereka inginkan.\n\nKalimat yang tidak logis dari bacaan diatas adalah?",
        "pilihan": [
            "Kalimat 1",
            "Kalimat 2",
            "Kalimat 3",
            "Kalimat 4",
            "Kalimat 5"
        ],
        "jawaban": 1,
        "skor": 200
    },
    {
    
        "pertanyaan": "Sebagian besar orang sering mengeluh karena terlalu sibuk. Mereka umumnya ingin memiliki lebih banyak waktu luang. Namun, penelitian terbaru menemukan bahwa terlalu banyak waktu luang ternyata tidak lebih baik daripada terlalu sibuk. Menurut penelitian yang diterbitkan oleh American Psychological Association, bertambahnya waktu luang memang dapat meningkatkan rasa bahagia. Akan tetapi, perasaan itu hanya bertahan sampai titik tertentu. Jika waktu luang yang dimiliki terlalu banyak, akan ada dampak buruk yang timbul. Untuk menyelidiki fenomena tersebut, para peneliti melakukan eksperimen daring yang melibatkan lebih dari 6.000 peserta. Peneliti menemukan bahwa orang yang memiliki waktu luang sedikit merasa lebih stres daripada mereka yang memiliki jumlah waktu luang sedang. Sementara itu, mereka yang memiliki waktu luang banyak juga merasa kurang produktif daripada mereka yang berada dalam kelompok sedang. Lebih lanjut, temuan tersebut menunjukkan bahwa berakhir dengan waktu luang sepanjang hari untuk melakukan hal-hal yang diinginkan ternyata dapat membuat seseorang merasa tidak bahagia. Sebaliknya, orang harus berusaha untuk memiliki waktu luang dalam jumlah sedang agar dapat melakukan apa yang mereka inginkan.\n\nKata bijaksana dalam kalimat (8) berasosiasi dengan?",
        "pilihan": [
            "berbudi",
            "bersahaja",
            "berakal",
            "berperasaan",
            "berpengetahuan"
        ],
        "jawaban": 0,
        "skor": 200
    }
]

soal_pu = [
    {
        "pertanyaan": "P1: Semua siswa kelas XII harus berseragam batik\nP2: Sebagian siswa yang dihukum adalah siswa kelas XII\nSimpulan manakah yang benar?",
        "pilihan": [
            "Sebagian siswa yang berseragam batik bukan siswa kelas XII",
            "Sebagian siswa yang dihukum berseragam batik",
            "Semua siswa di sekolah harus berseragam batik",
            "Semua siswa kelas XII yang dihukum tidak berseragam batik",
            "Sebagian siswa yang tidak berseragam batik tidak dihukum"
        ],
        "jawaban": 1,
        "skor": 100
    },
    {
        "pertanyaan": "Dani dipromosikan untuk mendapat posisi baru di perusahaan X\n sebagai kepala Divisi Pemasaran atau Sekretaris Direksi. \nTernyata Budi terpilih sebagai Sekretaris Direksi di perusahaan X sehingga posisi tersebut telah terisi.\nSimpulan yang paling tepat adalah…",
        "pilihan": [
            "Dani tidak mendapatkan posisi baru di perusahaan X",
            "Budi tidak mendapatkan posisi baru di perusahaan X",
            "Dani tidak cocok mendapatkan posisi sebagai Sekretaris Direksi di Perusahaan X",
            "Budi tidak cocok mendapatkan posisi sebagai kepala Divisi Pemasaran di Perusahaan X",
            "Dani mendapatkan posisi baru sebagai kepala Divisi Pemasaran di Perusahaan X"
        ],
        "jawaban": 4,
        "skor": 200
    },
    {
        "pertanyaan": "Jika pola makan teratur, berat badan seseorang bisa terkontrol. Jika makan tidak terlalu kenyang, program diet dapat berhasil. Saat ini berat badan seseorang tidak dapat dikontrol atau program diet tidak berhasil.\nSimpulan yang paling tepat adalah..",
        "pilihan": [
            "Orang tersebut memiliki pola makan teratur, tetapi makan terlalu kenyang",
            "Orang tersebut makan tidak terlalu kenyang, tetapi pola makan tidak teratur",
            "Orang tersebut tidak memiliki pola makan teratur atau makan terlalu kenyang",
            "Orang tersebut makan dengan pola tidak teratur atau makan tidak terlalu kenyang",
            "Orang tersebut makan terlalu kenyang sehingga pola makannya tidak teratur"
        ],
        "jawaban": 2,
        "skor": 200
    },
    {
        "pertanyaan": "Jika bahagia itu sederhana, hal-hal sepele akan mendatangkan kebahagiaan. Jika hal-hal sepele mendatangkan kebahagiaan, orang-orang tidak perlu susah payah untuk mendapatkannya. Banyak orang yang mendapatkan kebahagiaan dengan susah payah.\nSimpulan yang tepat adalah…",
        "pilihan": [
            "Bahagia itu tidak sederhana",
            "Bahagia itu sederhana",
            "Bahagia itu butuh perjuangan yang tidak sepele",
            "Jika hal-hal sepele mendatangkan kebahagiaan, orang-orang selalu bahagia dalam hidupnya",
            "Jika bahagia itu sederhana, seseorang tidak perlu susah payah untuk mendapatkannya"
        ],
        "jawaban": 0,
        "skor": 250
    },
    {
        "pertanyaan": "Jika seorang mahasiswa mendapatkan IPK lebih dari 3,50 dan berhasil lolos seleksi mahasiswa berprestasi, dia akan memperoleh predikat cum laude dan beasiswa melanjutkan S2 di luar negeri. Teguh mendapatkan IPK 3,85 dan berhasil lolos seleksi mahasiswa berprestasi.\nSimpulan yang tepat adalah…",
        "pilihan": [
            "Teguh tidak memperoleh predikat cum laude dan beasiswa melanjutkan S2 ke luar negeri",
            "Teguh adalah mahasiswa terbaik di universitasnya",
            "Teguh akan memperoleh predikat cum laude dan beasiswa melanjutkan S2 ke luar negeri",
            "IPK Teguh yang tinggi menjadikan dia sebagai mahasiswa berprestasi",
            "Teguh dinyatakan sebagai mahasiswa cum laude, tetapi tidak melanjutkan S2 ke luar negeri"
        ],
        "jawaban": 2,
        "skor": 250
    }
]



soal_pk = [
    {
        "pertanyaan": "13. 2, 1, 6, 2…, 6,8,24, -2,.., 10\nAngka yang paling sesuai untuk mengisi suku yang kosong secara berturut-turut adalah…",
        "pilihan": [
            "-8 dan 26",
            "-6 dan 48",
            "-4 dan 48",
            "-2 dan 120",
            "0 dan 120"
        ],
        "jawaban": 3,
        "skor": 100
    },
    {
        "pertanyaan": "Segelas susu dibuat dengan mencampurkan 2 sendok makan bubuk susu dan x sendok makan gula. Perbandingan banyaknya bubuk susu dan gula dalam segelas susu adalah 2:3.\nJika P=x dan Q=9, manakah hubungan yang benar antara kuantitas P dan Q berdasarkan informasi yang diberikan?",
        "pilihan": [
            "P > Q",
            "Q > P",
            "P = Q",
            "Q=P",
            "Informasi yang diberikan tidak cukup untuk memutuskan salah satu tiga pilihan di atas"
        ],
        "jawaban": 1,
        "skor": 100
    },
    {
        "pertanyaan": "Sebuah kereta menempuh jarak Surabaya ke Bandung dengan kecepatan 50 km/jam selama 10 jam. Jika jarak tersebut ingin ditempuh dalam waktu 8 jam, kecepatan kereta tersebut menjadi.....",
        "pilihan": [
            "60,25 km/jam",
            "62,50 km/jam",
            "65,50 km/jam",
            "70,25 km/jam",
            "73,25 km/jam"
        ],
        "jawaban": 1,
        "skor": 100
    },
    {
        "pertanyaan": "Perbandingan berat badan 4 orang siswa adalah sebagai berikut, P adalah 3 kg lebih berat dari S; Q adalah 6 kg lebih ringan dari R; S adalah 2 kg lebih berat dibandingkan dengan Q. Jika diketahui berat badan S = 40kg maka pernyataan berikut yang paling tepat adalah....",
        "pilihan": [
            "Berat badan P > R",
            "Berat badan S > R",
            "Berat badan R > P",
            "Berat badan Q > p",
            "Berat badan S > P"
        ],
        "jawaban": 2,
        "skor": 100
    },
    {
        "pertanyaan": "Pak Frans memiliki peternakan sapi dan kambing. Seluruh sapi dan kambingnya punya kondisi normal dan sehat dengan jumlah kaki setiap kambing 2 dan setiap sapi 4. Jika perbandingan banyak sapi:banyak kambing adalah 3:7, dan jumlah semua hewan ternaknya 200 ekor, maka banyak sapi adalah.....",
        "pilihan": [
            "30",
            "40",
            "50",
            "60",
            "90"
        ],
        "jawaban": 3,
        "skor": 100
    },
    {
        "pertanyaan": "A telah mengikuti empat kali tes matematika dengan nilainya berturut turut adalah 2, 3, 5, dan 8. A harus mengikuti dua tes lagi. Nilai setiap tes berupa bilangan bulat dengan rentang 1 sampai 10.\nJika salah satu dari dua nilai tes tersebut merupakan nilai sempurna dan jangkauan 6 tes tersebut sama dengan 2 kali mediannya, maka nilai tes yang lainnya adalah.....",
        "pilihan": [
            "5",
            "4",
            "3",
            "2",
            "1"
        ],
        "jawaban": 2,
        "skor": 100
    }
]



window = Tk()
app = BackgroundGUI(window)
app.run()
