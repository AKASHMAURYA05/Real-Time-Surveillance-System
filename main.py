import tkinter as tk
import tkinter.font as font
from in_out import in_out
from Full_Window import full_frame
from Area import Frame
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from Training import capturing
from Testing import testing
window = tk.Tk()
window.title("Smart Surveillance System")
window.geometry('1200x650')
window.iconphoto(False, tk.PhotoImage(file='favicon.png'))
window.configure(bg="lightblue")
frame1 = tk.Frame(window, bg="#53CCEC")


label_title = tk.Label(frame1, text="Smart Surveillance System", borderwidth=2, relief="solid")
label_font = font.Font(size=30, weight='bold',family='Arial')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/spy.png')
icon = icon.resize((150,150))
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/monitor.png')
btn1_image.thumbnail((50, 50))
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50,50))
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50))
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50))
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50,50))
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50))
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/recording.png')
btn7_image = btn7_image.resize((50,50))
btn7_image = ImageTk.PhotoImage(btn7_image)

btn8_image = Image.open('icons/recording.png')
btn8_image = btn8_image.resize((50,50))
btn8_image = ImageTk.PhotoImage(btn8_image)


btn_font = font.Font(size=25) 
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green',command = find_motion, image=btn1_image, compound='left',bg="#FFE6B6")
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Frame', height=90, width=180, fg='green', command=Frame, compound='left', image=btn2_image,bg="#FFE6B6")
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Window', height=90, width=180, fg='green', command=full_frame, image=btn3_image, compound='left',bg="#FFE6B6")
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='green', command=record, image=btn4_image, compound='left',bg="#FFE6B6")
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)


btn6 = tk.Button(frame1, text='Intruder', height=90, width=180, fg='green', command=in_out, image=btn6_image, compound='left',bg="#FFE6B6")
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10), column=2)

btn5 = tk.Button(frame1, text='Exit',height=90, width=180, fg='red', command=window.quit,compound='left',image=btn5_image,bg="#FFE6B6")
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=3, padx=(20,10))

btn7 = tk.Button(frame1, text="Add", fg="green",command=capturing, compound='left', image=btn7_image, height=90, width=180,bg="#FFE6B6")
btn7['font'] = btn_font
btn7.grid(row=3, column=2, pady=(20,10))

btn8 = tk.Button(frame1, text="Test", fg="green",command=testing, compound='left', image=btn8_image, height=90, width=180,bg="#FFE6B6")
btn8['font'] = btn_font
btn8.grid(row=6, pady=(20,10), padx=(20,10))


frame1.pack()
window.mainloop()


