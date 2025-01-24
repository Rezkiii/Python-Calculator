import tkinter as tk  
  
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
 
root = tk.Tk()  
root.title("Kalkulator Python")  
  
entry = tk.Entry(root, width=40, borderwidth=5)  
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  
  
tombol_angka = [  
    '1', '2', '3', '=',  
    '4', '5', '6', '*',  
    '7', '8', '9', '-',  
    '.', '0', '/', '+'  
]  
  
row_val = 1  
col_val = 0  
  
for tombol in tombol_angka:  
    if tombol == '=':  
        action = hitung  
    elif tombol == 'C':  
        action = hapus  
    else:  
        action = lambda nilai=tombol: klik_tombol(nilai)  
      
    tk.Button(root, text=tombol, padx=40, pady=20, command=action).grid(row=row_val, column=col_val)  
      
    col_val += 1  
    if col_val > 3:  
        col_val = 0  
        row_val += 1  
  
# Menjalankan aplikasi  
root.mainloop()  
