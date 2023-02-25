from PIL import Image
import random
import tkinter as tk
import time
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
root = tk.Tk()
root.title("RenderBird IM")
root.withdraw() #use tkinter for file choose, do not display root window
print("Image noise generator by Wojtekb30, 2023, v0.2")
print("Choose image file.")
#input("Press ENTER/RETURN to continue ")
plik = filedialog.askopenfilename(filetypes=(('JPG image','*.jpg'),('PNG image','*.png'))) #open image

if plik=="":
    quit()
im = Image.open(plik) 
print("Chosen: "+str(plik))

print(" ")
print("Now you will have to set some settings. They give different effects. Choosing nothing or a nonexistent option will close the program:")
print("First setting is RGB modifier. Choose Separate or Single.")
print("Separate changes values of each pixel's Red, Green and Blue values separately.")
print("Single treats pixel as one color and affects value of its RGB as one.")
print("Both give different effects.")
print("Second option is max range number to randomise. It must be a value from 2 to 510.")
print("NEVER overwrite the original image! This program might destroy it entirely.")
time.sleep(5) #wait to make people read the text
model = int(input("Type 0 for Separate mode, 1 for Single mode: "))
if model=="" or not (model==0 or model==1):
    quit()

n = int(input("Type the max range randomising number (2-510): "))
if not (n>=2 and n<=510):
    quit()

def jpgjeden(x, n): #mode 1, jpg or bmp
    r, g, b = x
    liczba = random.randint(-1*n, n)
    r = r + liczba
    g = g + liczba
    b = b + liczba
    if r<0:
        r=0
    if r>255:
        r=255
    if g<0:
        g=0
    if g>255:
        g=255
    if b<0:
        b=0
    if b>255:
        b=255
    x = r, g, b
    return x

def pngjeden(x, n): #mode 1, png
    r, g, b, t = x
    liczba = random.randint(-1*n, n)
    r = r + liczba
    g = g + liczba
    b = b + liczba
    t = t + liczba
    if r<0:
        r=0
    if r>255:
        r=255
    if g<0:
        g=0
    if g>255:
        g=255
    if b<0:
        b=0
    if b>255:
        b=255
    if t<0:
        t=0
    if t>255:
        t=255
    x = r, g, b, t
    return x

def jpgzero(x, n): #mode 0, jpg or bmp
    r, g, b = x
    r = r + random.randint(-1*n, n)
    if r<0:
        r=0
    if r>255:
        r=255
    g = g + random.randint(-1*n, n)
    if g<0:
        g=0
    if g>255:
        g=255
    b = b + random.randint(-1*n, n)
    if b<0:
        b=0
    if b>255:
        b=255
    x = r, g, b
    return x

def pngzero(x, n): #mode 0, png
    r, g, b, t = x
    r = r + random.randint(-1*n, n)
    if r<0:
        r=0
    if r>255:
        r=255
    g = g + random.randint(-1*n, n)
    if g<0:
        g=0
    if g>255:
        g=255
    b = b + random.randint(-1*n, n)
    if b<0:
        b=0
    if b>255:
        b=255
    t = t + random.randint(-1*n, n)
    if t<0:
        t=0
    if t>255:
        t=255
    x = r, g, b, t
    return x



time.sleep(1)
input("Press ENTER/RETURN to start ") #after getting all info and its verification
print("Working... May take a long while.")
x=0
y=0
n = n//2
pix = im.load()
szerokosc, wysokosc = im.size #load image and get size
szerokosc = szerokosc -1
wysokosc = wysokosc -1 #fix size so it doesn't leave bounds
while (x<=szerokosc and y<=wysokosc): #iterate through every pixel
    kolor = pix[x, y]
    if model==1:
        try:
            im.putpixel((x, y), (pngjeden(kolor, n)))
        except:
            im.putpixel((x, y), (jpgjeden(kolor, n)))
    elif model==0:
        try:
            im.putpixel((x, y), (pngzero(kolor, n)))
        except:
            im.putpixel((x, y), (jpgzero(kolor, n)))

    
    if y==wysokosc and x==szerokosc:
        break #end if done
    if x==szerokosc: #iterate through every pixel - if reached last pixel in a row switch to the next row
        x=-1
        y=y+1
    x=x+1

print("")
print("Done. Now let's save the result file.")
savepath = filedialog.asksaveasfilename(initialfile="result",defaultextension="png",filetypes=[("PNG","png")])

if savepath:
    im.save(savepath)
    print("Save path:")
    print(savepath)
    input('Done. Press ENTER/RETURN to quit.') 
else:
    input('Image not saved. Press ENTER/RETURN to quit.')
