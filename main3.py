from tkinter import Tk, Frame, Label, Button
from tkinter.font import Font
from PIL import Image, ImageTk

# Custom functions
from in_out import in_out
from Full_Window import noise
from Area import rect_noise
from record import record
from find_motion import find_motion
from Training import capturing
from Testing import testing

# Load icons
icons = {
    "monitor": ImageTk.PhotoImage(Image.open("icons/monitor.png").resize((50, 50))),
    "rectangle": ImageTk.PhotoImage(Image.open("icons/rectangle-of-cutted-line-geometrical-shape.png").resize((50, 50))),
    "camera": ImageTk.PhotoImage(Image.open("icons/security-camera.png").resize((50, 50))),
    "recording": ImageTk.PhotoImage(Image.open("icons/recording.png").resize((50, 50))),
    "exit": ImageTk.PhotoImage(Image.open("icons/exit.png").resize((50, 50))),
    "incognito": ImageTk.PhotoImage(Image.open("icons/incognito.png").resize((50, 50))),
}

# Define styles
button_font = Font(size=25)
button_style = {
    "font": button_font,
    "width": 180,
    "height": 90,
    "fg": "green",
    "bg": "#FFE6B6",
}

label_title_style = {
    "font": title_font,  # Define title_font elsewhere
    "borderwidth": 2,
    "relief": "solid",
}

grid_options = {
    "padx": 20,
    "pady": (20, 10),
}


window = Tk()
window.title("Smart Surveillance System")
window.geometry("1200x650")
window.iconphoto(False, tk.PhotoImage(file="favicon.png"))
window.configure(bg="lightblue")

frame1 = Frame(window, bg="#53CCEC")


label_title = Label(frame1, text="Smart Surveillance System", **label_title_style)
label_title.grid(pady=grid_options["pady"], column=2)


icon = Image.open("icons/spy.png")
icon = icon.resize((150, 150))
label_icon = Label(frame1, image=ImageTk.PhotoImage(icon))
label_icon.grid(row=1, pady=grid_options["pady"], column=2)


# Button creation with styling
btn1 = Button(frame1, text="Monitor", image=icons["monitor"], compound="left", **button_style, command=find_motion)
btn1.grid(row=3, **grid_options)

btn2 = Button(frame1, text="Frame", image=icons["rectangle"], compound="left", **button_style, command=rect_noise)
btn2.grid(row=3, pady=grid_options["pady"], column=3, padx=(20, 5))

btn3 = Button(frame1, text="Noise", image=icons["camera"], compound="left", **button_style, command=noise)
btn3.grid(row=5, **grid_options)

btn4 = Button(frame1, text="Record", image=icons["recording"], compound="left", **button_style, command=record)
btn4.grid(row=5, pady=grid_options["pady"], column=3)


btn6 = Button(frame1, text="Intruder", image=icons["incognito"], compound="left", **button_style, command=in_out)
btn6.grid(row=5, pady=grid_options["pady"], column=2)

btn5 = Button(frame1, text="Exit", image=icons["exit"], compound="left", **button_style, command=window.quit)
btn5.grid(row=6, pady=grid_options["pady"], column=3, padx=(20, 10))

btn7 = Button(frame1, text="Add", fg="green", command=capturing, compound="left", image=icons["recording"], height=90, width=180, bg="#FFE6)
