from PIL import Image as img
from Crypto.Cipher import DES
from tkinter import *
from tkinter import filedialog

vector = "abcdefgh"

def pad(data):
    return data + b"\x00"*(8-len(data)%8)


def dec_pad(data):
    return data + b"\x00"*(8+len(data)%8)


def convert_to_RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r,g,b))
    return pixels

def cifrar(origen, destino, key, modo):
    imagen = img.open(origen)
    data = imagen.convert("RGB").tobytes()
    original = len(data)
    new = convert_to_RGB(des_encrypt(key, pad(data), modo)[:original])
    imagen2 = img.new(imagen.mode, imagen.size)
    imagen2.putdata(new)
    imagen2.save(destino)

def des_encrypt(key, data, modo):
    if(modo=="ECB" or modo=="ecb"):
        mode = DES.MODE_ECB
        des = DES.new(key, mode)
    if(modo=="CBC" or modo=="cbc"):
        mode = DES.MODE_CBC
        des = DES.new(key, mode, vector)
    if(modo=="CFB" or modo=="cfb"):
        mode = DES.MODE_CFB
        des = DES.new(key, mode, vector)
    if(modo=="OFB" or modo=="ofb"):
        mode = DES.MODE_OFB
        des = DES.new(key, mode, vector)
    new_data = des.encrypt(data)
    return new_data

def decifrar(origen, destino, key, modo):
    imagen = img.open(origen)
    data = imagen.convert("RGB").tobytes()
    original = len(data)
    new = convert_to_RGB(des_decrypt(key, pad(data), modo)[:original])
    imagen2 = img.new(imagen.mode, imagen.size)
    imagen2.putdata(new)
    imagen2.save(destino)

def des_decrypt(key, data, modo):
    if(modo=="ECB" or modo=="ecb"):
        mode = DES.MODE_ECB
        des = DES.new(key, mode)
    if(modo=="CBC" or modo=="cbc"):
        mode = DES.MODE_CBC
        des = DES.new(key, mode, vector)
    if(modo=="CFB" or modo=="cfb"):
        mode = DES.MODE_CFB
        des = DES.new(key, mode, vector)
    if(modo=="OFB" or modo=="ofb"):
        mode = DES.MODE_OFB
        des = DES.new(key, mode, vector)
    new_data = des.decrypt(data)
    return new_data


def get_img():
    w.filename =  filedialog.askopenfilename(initialdir = "~/",title = "Select file",filetypes = (("bmp files","*.bmp"),("all files","*.*")))
    lblimg.config(text=str(w.filename))

def encrypt():
    name = txtname.get()
    if bolvar1.get():
        cifrar(w.filename, name, txtkey.get(), "ECB")
    if bolvar2.get():
        cifrar(w.filename, name, txtkey.get(), "CBC")
    if bolvar3.get():
        cifrar(w.filename, name, txtkey.get(), "CFB")
    if bolvar4.get():
        cifrar(w.filename, name, txtkey.get(), "OFB")
    


def decrypt():
    name = txtname.get()
    if bolvar1.get():
        decifrar(w.filename, name, txtkey.get(), "ECB")
    if bolvar2.get():
        decifrar(w.filename, name, txtkey.get(), "CBC")
    if bolvar3.get():
        decifrar(w.filename, name, txtkey.get(), "CFB")
    if bolvar4.get():
        decifrar(w.filename, name, txtkey.get(), "OFB")
    
w = Tk()
w.title("DES")
w.geometry("700x400")

lblkey = Label(w, text="Key: ")
lblkey.grid(row=0, column = 0)
txtkey = Entry(w)
txtkey.grid(row=0,column = 1)

lblname = Label(w,text="Name:")
lblname.grid(row=0,column=2)
txtname = Entry(w)
txtname.grid(row=0,column=3)

lblimg = Label(w,text="img.bmp")
lblimg.grid(row=1, column = 0)
btnimg = Button(w,text="Select bmp file",command = get_img)
btnimg.grid(row=1,column=1)

btnEncrypt = Button(w, text="Encrypt",command=encrypt)
btnEncrypt.grid(row=2, column=0)
btnDecrypt = Button(w, text="Decrypt",command=decrypt)
btnDecrypt.grid(row=2, column=1)

bolvar1 = BooleanVar()
check1 = Checkbutton(w, text="ECB", variable=bolvar1)
check1.grid(row=3, column=0)

bolvar2 = BooleanVar()
check2 = Checkbutton(w, text="CBC", variable=bolvar2)
check2.grid(row=4, column=0)

bolvar3 = BooleanVar()
check3 = Checkbutton(w, text="CFB", variable=bolvar3)
check3.grid(row=5, column=0)

bolvar4 = BooleanVar()
check4 = Checkbutton(w, text="OFB", variable=bolvar4)
check4.grid(row=6, column=0)


w.mainloop()

if __name__ == '__main__':
    i = 0    
    

    '''
    i = 0
    print("\nPráctica 2: Cifrar y decifrar imagen con DES\n")
    while True:
        i = int(input("Selecciona una de las opciones:\n\n1)Cifrar imagen\n\n2)Decifrar imagen\n\n3)Salir\n\n"))
        if(i == 1):
            print("\nIngresa el nombre de la imagen a cifrar:\n")
            original = input()
            print("\nIngresa el nombre de la imagen cifrada:\n")
            nueva = input()
            print("\nIngresa la llave:\n")
            llave = input()
            print("\nIngresa el modo de operacion\n")
            modo = input()
            cifrar(original, nueva, llave, modo)
            print("\nLa imagen se ha cifrado\n")
        elif(i == 2):
            print("\nIngresa el nombre de la imagen a descifrar:\n")
            cifrada = input()
            print("\nIngresa el nombre de la imagen decifrada:\n")
            decifrada = input()
            print("\nIngresa la llave:\n")
            llave = input()
            print("\nIngresa el modo de operacion\n")
            modo = input()
            decifrar(cifrada, decifrada, llave, modo)
            print("\nLa imagen se ha descifrado\n")
        elif(i == 3):
            break
    '''