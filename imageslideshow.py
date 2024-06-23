from itertools import cycle
from PIL import Image , ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image slideshow View") 

# image list path 
image_paths = [
    r"C:\Users\chada\Desktop\RP\images\84-e1423044259345.webp" ,
    r"C:\Users\chada\Desktop\RP\images\Inspirational-quote-14.webp" ,
    r"C:\Users\chada\Desktop\RP\images\motivational-message-collage_23-2150801186.webp" ,
    r"C:\Users\chada\Desktop\RP\images\motivational-quote-your-focus-determines-your-reality_805187-973.webp"
]

# resize image 
image_size = (1080,1080)
# images = [Image.open(path).resize(image_size) for path in image_paths]
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]


label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    next_image = next(slideshow)
    label.config(image=next_image)
    root.after(3000, update_image)  # Update the image every 3 seconds

        
play_button = tk.Button(root, text='Play slideshow', command = update_image)
play_button.pack()

root.mainloop()