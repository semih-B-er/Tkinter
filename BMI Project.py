from tkinter import *

uygulama = Tk()
uygulama.minsize(width=200,height=300)

def hesaplama():
    x = int(entry1.get())
    y = float(entry2.get())
    z = y*y
    bmi = round(x/z,2)
    t = Label(text=f"{bmi}")
    t.pack()

    if bmi >= 40:
        t.config(text=f"BMI:{bmi} 3.derece obezsiniz Dikkat edin!")
    elif bmi >=35:
        t.config(text=f"BMI:{bmi} 2.derece obezsiniz Dikkat edin!")
    elif bmi >= 30:
        t.config(text=f"BMI:{bmi} obezsiniz Dikkat edin!")
    elif bmi >= 25:
        t.config(text=f"BMI:{bmi} Fazla kilonuz var Spora başlayın")
    elif bmi >= 18:
        t.config(text=f"BMI:{bmi} Normal bir kiloya sahipsiniz")
    else:
        t.config(text=f"BMI:{bmi} Çok Zayıfsınız Kilo almalısınız")


soru1 = Label(text="Kilonuzu girin:")
soru1.pack()
entry1 = Entry(width=30)
entry1.pack()
soru2 = Label(text="Boyunuzu Giriniz: ")
soru2.pack()
entry2 = Entry(width=30)
entry2.pack()

buton = Button(text="Hesapla", command=hesaplama)
buton.pack()


cevap = Label(text=f"{hesaplama}")








uygulama.mainloop()
