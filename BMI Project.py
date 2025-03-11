from tkinter import *

uygulama = Tk()
uygulama.minsize(width=200,height=300)

def hesaplama():
    x = entry1.get()
    y = entry2.get()
    if x == "" or y == "":
        t.config(text=f"Değerleri tam doldurum")


    try:
        bmi = round(float(x)/(float(y)/100)**2,2)
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
    except:
        t.config(text="Bir sayı gir")



soru1 = Label(text="Kilonuzu girin:(kg)")
soru1.pack()
entry1 = Entry(width=30)
entry1.pack()
soru2 = Label(text="Boyunuzu Giriniz:(cm) ")
soru2.pack()
entry2 = Entry(width=30)
entry2.pack()

buton = Button(text="Hesapla", command=hesaplama)
buton.pack()

t = Label()
t.pack()









uygulama.mainloop()
