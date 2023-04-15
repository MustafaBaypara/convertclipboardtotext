from PIL import ImageGrab, Image
from pytesseract import pytesseract

import tkinter as tk

# Buton tıklandığında çalışacak olan fonksiyon
def buton_tiklandi():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  
    # Opening the image & storing it in an image object
    img = ImageGrab.grabclipboard()
    img.save('thelastextract.png', 'PNG')
    img = Image.open("thelastextract.png")
    
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img, lang="tur")
    cikti = text
    # Çıktıyı metin kutusuna ekle
    metin_kutusu.insert(tk.END, cikti + "\n") # \n: Yeni satır
    # Metin kutusunu en son çıktıya kaydır
    metin_kutusu.see(tk.END)

# Tkinter penceresi oluşturma
pencere = tk.Tk()
pencere.title("yazıya dönüştür!")

# Metin kutusunu eklemek
metin_kutusu = tk.Text(pencere, wrap=tk.WORD)
metin_kutusu.pack()

# Butonu eklemek
buton = tk.Button(pencere, text="Tıkla!", command=buton_tiklandi)
buton.pack()

# Pencereyi başlatma
pencere.mainloop()

