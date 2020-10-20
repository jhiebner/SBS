from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageFilter


root = Tk()
root.title("Striv Splash Screen Generator")

    

def get_logo_file():
    logo_name = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    selected_logo = Label()
    if logo_name:
        greeting.destroy()
        selected_logo = Label(root, text = f'Selected logo: {logo_name}')
        selected_logo.pack()
        print(logo_name)
        return logo_name

    else: pass
    

# Main window config
selected_logo = None
select_logo_button = Button(
    text = "Select Logo",
    command = get_logo_file
    )
select_logo_button.pack()
greeting = Label(root, text = "No logo selected!")
greeting.pack()



root.mainloop()
