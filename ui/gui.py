import tkinter as tk
from PIL import Image, ImageTk
from decouple import config 

root = None
label_image = None
canvas = None
line_id = None

def sleep():
    global root, label_image, line_id, text_id
    if canvas and line_id:
        canvas.itemconfig(line_id, fill='red')
        canvas.itemconfig(text_id, text="Sleeping...Zzz...'")


def awaken():
    global root, label_image, line_id, text_id       
    root.deiconify()
    if canvas and line_id:
        canvas.itemconfig(line_id, fill='green')
        canvas.itemconfig(text_id, text="At your service")

def disappear():
    global root
    root.iconify()

def restore():
    global root
    root.deiconify()

def update_text_listener(new_text):
    global canvas, text_id
    new_text=new_text[:170] + ("..." if len(new_text) > 170 else "")
    if canvas and text_id:
        canvas.itemconfig(text_id, text=new_text, fill='#0096FF')

def update_text_speaker(new_text):
    global canvas, text_id
    new_text=new_text[:170] + ("..." if len(new_text) > 170 else "")
    if canvas and text_id:
        canvas.itemconfig(text_id, text=new_text, fill='yellow')

def update_text(new_text):
    global canvas, text_id
    if canvas and text_id:
        canvas.itemconfig(text_id, text=new_text)

def appear():
    global root, label_image, canvas, line_id, text_id

    if root is not None :
        print("Window Already Open")
        restore()
        return

    root = tk.Tk()
    root.title("The Virtual Assistant")
    root.geometry("520x300")
    root.wm_attributes("-alpha", 0.85)
    root.configure(bg='black')  

    logo = config("MEDIA_DIR") + "/" + "va.jpeg"
    image = Image.open(logo)  
    image = image.resize((150, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=photo, highlightthickness=0, bd=0)
    label_image.image = photo 
    label_image.grid(row=0, column=0, pady=(0, 0), padx=0)  # Adjusted pady to add space above image and below line
 
    canvas = tk.Canvas(root, width=500, height=300, bg='black', highlightthickness=0)
    line_id = canvas.create_line(100, 2, 400, 2, width=10, fill='green')  # Draw a white line with width 20
    text_id = canvas.create_text(240, 55, text="At your service~", fill='yellow', font=("Arial", 12), width=420)
    canvas.grid(row=1, column=0, pady=(10, 10), padx=10)  # Adjusted pady to position canvas just below the image

    root.resizable(False, False)  
    root.mainloop()

def close_window(exit_event):
    global root
    #print("Close Window called")
    if root:
        root.quit()
        root.update_idletasks()  # Handle GUI operations
        #root.destroy()
        exit_event.set()

if __name__ == "__main__":
    appear()
