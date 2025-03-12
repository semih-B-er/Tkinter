from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64

window = Tk()
window.minsize(width=400,height=600)

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrpty_notes():
    title = my_entry.get()
    message = my_text.get("1.0",END)
    master_scret = my_entry1.get()
    if len(title) == 0 or len(message) == 0 or len(master_scret) == 0:
        messagebox.showinfo(title="Eror!", message="please enter all info") # mesaj çıkarmak için çıkar.
    else:
        #encryption
        message_encryption = encode(master_scret,message)
        try:
            with open("myscret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encryption}")
        except FileNotFoundError:
            with open("myscret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encryption}")
        finally:
            my_entry.delete(0,END)
            my_text.delete("1.0",END)
            my_entry1.delete(0,END)
def dcripty_notes():
    message_encryption = my_text.get("1.0",END)
    master_scret = my_entry1.get()
    if len(message_encryption) == 0 or len(master_scret) == 0:
        messagebox.showinfo(title="Error!", message="please Enter all info")
    else:
        try:
            dcripted_message = decode(master_scret,message_encryption)
            my_text.delete("1.0",END)
            my_text.insert("1.0",dcripted_message)
        except:
            messagebox.showinfo(title="Error!",message="please info encrypted text!")

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
my_cripto = Button(text="Seve & Encpty", command=save_and_encrpty_notes)
my_cripto.pack()
my_decrypt = Button(text="Decrypt", command=dcripty_notes)
my_decrypt.pack()



window.mainloop()