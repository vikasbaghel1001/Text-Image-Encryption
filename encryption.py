from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb #pip install stegano
from Crypto.Cipher import AES
import hashlib
from cryptography.fernet import Fernet


# Create the main window
root = tk.Tk()
root.title("Image encrytion and Steganography ")
root.geometry("700x580")
root.resizable (False, False) 
root.configure(bg="#2f4155")



def showimage():
    global filename
    filename=filedialog.askopenfilename (initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG File","*.jpg"), ("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage (img)
    lbl.configure (image=img , width =250 ,height = 250 )
    lbl.image=img 


def Hide():
    global secret
    message=text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

def Show():
    clear_message = lsb.reveal (filename)
    text1.delete (1.0, END)
    text1.insert (END, clear_message)

def save():
    y = filename
    secret.save("image.png") 



def generate_key():
    """Generate a new symmetric encryption key"""
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def encrypt():
    file_path = filedialog.askopenfilename()
    with Image.open(file_path) as img:
        # Convert the image to bytes
        img_bytes = img.tobytes()
        # Encrypt the bytes using the shared key
        key = key_entry.get().encode()
        f = Fernet(key)
        encrypted_bytes = f.encrypt(img_bytes)
        # Save the encrypted bytes to a new file
        save_path = filedialog.asksaveasfilename(defaultextension=".enc")
        with open(save_path, "wb") as f:
            f.write(encrypted_bytes)

def decrypt():


    file_path = filedialog.askopenfilename()
    with open(file_path, "rb") as f:
        encrypted_bytes = f.read()
    # Decrypt the bytes using the shared key
    key = key_entry.get().encode()
    f = Fernet(key)
    decrypted_bytes = f.decrypt(encrypted_bytes)

    # Convert the decrypted bytes back to an image
    img = Image.frombytes(mode="RGB",  size=(250, 250),data=decrypted_bytes)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    img.save(save_path)


key_entry = tk.Entry(root, width=50)
key_entry.grid(row=0, column=1)
key_button = tk.Button(root, text="Generate Key", command=generate_key ,  bg='#ffffff', activebackground='darkgrey')
key_button.grid(row=0, column=2, padx=10, pady=10)

# Encryption button
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt)
encrypt_button.grid(row=1, column=1, padx=10, pady=10)

# Decryption button
decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt)
decrypt_button.grid(row=1, column=2, padx=10, pady=10)
# Pack everything into the main window

#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto (False,image_icon)




#first Frame
f=Frame (root, bd=3, bg="black",width=340,height=300, relief=GROOVE)
f.place(x=10, y=100) 

lbl=Label(f, bg="black")
lbl.place(x=40, y=10)    



#Second Frame
frame2=Frame (root, bd=3,width=330,height=300, bg="white", relief=GROOVE)
frame2.place(x=360,y=100)
text1=Text (frame2, font="Arial 10", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0,width=320,height=295)
scrollbar1=Scrollbar (frame2)
scrollbar1.place (x=320, y=0,height=300)
scrollbar1.configure (command=text1.yview)
text1.configure (yscrollcommand=scrollbar1.set) 


#third Frame
frame3=Frame (root, bd=3, bg="#2f4155",width=340,height=80, relief=GROOVE)
frame3.place(x=10, y=390)
Button(frame3, text="Open Image",width=9, height=2, font="arial 10 bold" , command=showimage , bg='#ffffff', activebackground='#00ff00' ).place(x=50,y=20)
Button(frame3, text="Save Image",width=9, height=2, font="arial 10 bold" , command=save ,  bg='#ffffff', activebackground='#00ff00').place(x=180,y=20)

#fourth Frame
frame4=Frame (root, bd=3, bg="#2f4155",width=330,height=80, relief=GROOVE)
frame4.place(x=360, y=390)
Button (frame4, text="Hide Data",width=9, height=2, font="arial 10 bold", command=Hide , bg='#ffffff', activebackground='#00ff00').place(x=50, y=20)
Button (frame4, text="Show Data",width=9,height=2, font="arial 10 bold" , command=Show , bg='#ffffff', activebackground='#00ff00').place (x=180, y=20)




logo=PhotoImage (file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10,y=470)
Label (root, text="CYBER SCIENCE", bg="#2d4155",fg="white", font="arial 25 bold").place(x=100, y=490)


root.mainloop()
