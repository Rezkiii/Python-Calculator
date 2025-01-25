import tkinter as tk  
from tkinter import font  
  
def klik_tombol(nilai):  
    current = entry.get()  
    entry.delete(0, tk.END)  
    entry.insert(0, current + nilai)  
  
def hapus():  
    entry.delete(0, tk.END)  
  
def hitung():  
    try:  
        hasil = eval(entry.get())  
        entry.delete(0, tk.END)  
        entry.insert(0, str(hasil))  
    except Exception as e:  
        entry.delete(0, tk.END)  
        entry.insert(0, "Error")  
  
# Membuat jendela utama  
root = tk.Tk()  
root.title("Kalkulator")  
root.geometry("350x500")  
root.resizable(False, False)  
  
# Mengatur gaya font  
font_style = font.Font(family="Helvetica", size=14, weight="bold")  
  
# Warna-warna tema  
bg_color = "#282c34"  
fg_color = "#ffffff"  
button_bg_color = "#44475a"  
button_fg_color = "#ffffff"  
button_active_bg_color = "#6272a4"  
entry_bg_color = "#44475a"  
entry_fg_color = "#ffffff"  
  
# Membuat entry untuk menampilkan input dan hasil  
entry = tk.Entry(root, width=15, borderwidth=0, font=font_style, bg=entry_bg_color, fg=entry_fg_color, justify="right")  
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)  
  
# Membuat tombol angka dan operasi  
tombol_angka = [  
    '7', '8', '9', '/',  
    '4', '5', '6', '*',  
    '1', '2', '3', '-',  
    '0', '.', '=', '+',  
    'C'  
]  
  
row_val = 1  
col_val = 0  
  
for tombol in tombol_angka:  
    if tombol == '=':  
        action = hitung  
        bg = "#6272a4"  
    elif tombol == 'C':  
        action = hapus  
        bg = "#ff5555"  
    else:  
        action = lambda nilai=tombol: klik_tombol(nilai)  
        bg = button_bg_color  
      
    button = tk.Button(  
        root,   
        text=tombol,   
        padx=20,   
        pady=20,   
        font=font_style,   
        bg=bg,   
        fg=button_fg_color,   
        activebackground=button_active_bg_color,  
        command=action,  
        relief=tk.FLAT,  
        bd=0,  
        highlightthickness=0  
    )  
      
    button.grid(row=row_val, column=col_val, sticky="nsew")  
      
    col_val += 1  
    if col_val > 3:  
        col_val = 0  
        row_val += 1  
  
# Mengatur ukuran kolom agar merata  
for i in range(4):  
    root.grid_columnconfigure(i, weight=1)  
  
# Mengatur ukuran baris agar merata  
for i in range(1, 6):  
    root.grid_rowconfigure(i, weight=1)  
  
# Menjalankan aplikasi  
root.mainloop()  
