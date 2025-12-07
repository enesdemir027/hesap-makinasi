import tkinter as tk
import json
import time
print("-"*20)
print("aciliyor kanka")
print("-"*20)
time.sleep(0.1)
print("S")
time.sleep(0.1)
print("-"*10)
print("T")
time.sleep(0.1)
print("-"*10)
print("A")
time.sleep(0.1)
print("-"*10)
print("R")
time.sleep(0.1)
print("-"*10)
print("T")
time.sleep(0.1)
print("-"*10)

a="{status: True(200)}"
b="{status: False(400)}"
c="{sayi tikladi kanka}"
s="{veri sildi kanka}"
d="{sonuc verdi kanka}"
e="{bilinmeyen hata verdi}"
tiklama=(a,c)
sonucv=(a,d)
hatav=(b,e)
silme=(a,s)
pencere = tk.Tk()
pencere.geometry("500x500")
pencere.title("hesap makinasi")
ekran = tk.Entry(pencere, width=40, borderwidth=5, font=('Arial', 16), justify='right')
ekran.grid(row=0, column=0, columnspan=4, padx=40, pady=10)
print("hesap makinasi logu start...")
def tus_bas(metin):
    
    time.sleep(0.2)
    print(json.dumps(tiklama,ensure_ascii=False,indent=2))
    if metin == "C":
        ekran.delete(0, tk.END)
        time.sleep(0.1)
        print(json.dumps(silme,ensure_ascii=False,indent=2))
    elif metin == "%":
        try:
            ifade = ekran.get()
            if ifade == "":
                raise ValueError
            deger = eval(ifade)
            ekran.delete(0, tk.END)
            ekran.insert(0, deger / 100)
            print(json.dumps((sonucv, deger/100), ensure_ascii=False, indent=2))
        except:
            ekran.delete(0, tk.END)
            ekran.insert(0, "Hata")
            print(json.dumps(hatav, ensure_ascii=False, indent=2))


    elif metin == "=":
        try:
            sonuc = eval(ekran.get())
            ekran.delete(0, tk.END)
            ekran.insert(0, sonuc)
            time.sleep(0.1)
            print(json.dumps((sonucv,sonuc),ensure_ascii=False,indent=2))
        except:
            ekran.delete(0, tk.END)
            ekran.insert(0, "Hata")
            time.sleep(0.1)
            print(json.dumps(hatav,ensure_ascii=False,indent=2))
    else:
        ekran.insert(tk.END, metin)
tus_listesi = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('%', 5, 0)
]

for (metin, satir, sutun) in tus_listesi:
    btn_color = "#eeeee4"
    btn_fg = "black"
    if metin == 'C':
        btn_color = "black"
        btn_fg = "white"
    elif metin == '=':
        btn_color = "orange"
        btn_fg = "white"

    button = tk.Button(
        pencere,
        text=metin,
        padx=20,
        pady=20,
        font=('Arial', 14, 'bold'),
        bg=btn_color,
        fg=btn_fg,
        command=lambda m=metin: tus_bas(m) 
    )

    button.grid(row=satir, column=sutun, sticky="nsew", padx=2, pady=2)
for i in range(4):
    pencere.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    pencere.grid_rowconfigure(i, weight=1)
pencere.mainloop()
#coder : enesdemir