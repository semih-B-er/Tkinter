from tkinter import *
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

window = Tk()
window.minsize(width=400,height=600)

def kripto_dosya():
    value = my_text.get("1.0",'end-1c')
    my_not = my_entry.get("1.0",'end-1c')
    Ent = my_entry1.get()                                   #eklenmedi henüz
#    x = open(Ent,"w")
 #   x.write(value)
    def write_key():
        key = Fernet.generate_key() # key ürettik
        with open(Ent,"wb") as dosya:
            dosya.write(key)

    def load_key():
        return open(Ent, "rb").read()  # Dosyayı açar, dosyada kayıtlı key'i okur ve return eder
    mesaj = value.encode()
    write_key()

    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(mesaj)
    x.write(encrypted_message)

def çözüm():                                        #bitmedi
    decrypted_message = f.decrypt(encrypted_message)
    print(decrypted_message)
    with open(Ent)
#Fotoğraf ekleme
image = Image.open("foto.jpg")
new_size = (150, 150)
resized_image = image.resize(new_size)
my_image = ImageTk.PhotoImage(resized_image)
label = Label(image=my_image, pady=30)
label.pack()
my_label = Label(text="Enter Your Title..")
my_label.pack()
my_entry = Entry(width=30)
my_entry.pack()
my_label1 = Label(text="Enter Your Scret..")
my_label1.pack()
my_text = Text(width=40,height=10)
my_text.pack()
my_label2 = Label(text="Enter Your Title..")
my_label2.pack()
my_entry1 = Entry(width=30,)
my_entry1.pack()
my_cripto = Button(text="Seve & Encpty", command=kripto_dosya)
my_cripto.pack()
my_decrypt = Button(text="Decrypt")
my_decrypt.pack()



window.mainloop()