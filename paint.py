from tkinter import *
import tkinter.ttk as ttk #provide access to tk themed widget
from tkinter import colorchooser
from tkinter import filedialog #for creating file directory
from PIL import Image,ImageDraw,ImageGrab,ImageTk
import PIL #used for saving many different images file formats (image editing capablilities)
from tkinter import messagebox

root=Tk()
root.title("Paint program")
root.geometry("600x600")

brush_color="black"

def paint(event):  
	#Brush parameters
	brush_width="%0.0f"% float(my_slider.get())
	#brush_color="purple"
	#Brush type:BUTT,ROUND,PROJECTING
	brush_type2=brush_type.get()

	#starting position
	x1=event.x-1#event.x means take event to position x
	y1=event.y-1
	#endong position
	x2=event.x+1
	y2=event.y+1  
	#draw on the canvas
	my_canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_width,capstyle=brush_type2,smooth="true")

def change_brush_size(thing):
	slider_label.config(text="%0.0f"% float(my_slider.get()))

#change brush color
def change_brush_color():
	global brush_color
	brush_color="black"
	brush_color=colorchooser.askcolor(color=brush_color)[1]

def change_canvas_color():
	global bgcolor
	bg_color="black"
	bg_color=colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)

#clear screen
def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg="white")

#save image
def save_as_png():
	result= filedialog.asksaveasfilename(initialdir='c:/paint/Images/',filetypes=(("png files","*.png"),("all files","*.*")))

	if result.endswith(".png"):	
		pass
	else:
		result=result+".png"

	if result:
		x=root.winfo_rootx()+my_canvas.winfo_rootx()
		y=root.winfo_rooty()+my_canvas.winfo_rooty()
		x1=x+my_canvas.winfo_width()
		y1=y+my_canvas.winfo_height()
		ImageGrab.grab().crop((x,y,x1,y1)).save(result)

		#pop up success message
		messagebox.showinfo("Image saved","Your image has been saved!")

my_canvas=Canvas(root,width=400,height=300,bg="black")
my_canvas.pack(pady=20)

#my_canvas.create_line(0,100,300,100,fill="red")
#my_canvas.create_line(150,0,150,200,fill="red")

my_canvas.bind("<B1-Motion>",paint)#motion is moving the mouse and by paint we can track the mouse where the mouse is
#we can use B1 as left mouse side and B3 is right mouse side 

#create brush options frame
brush_options_frame=Frame(root)
brush_options_frame.pack(pady=20)

#Brush size
brush_size_frame=LabelFrame(brush_options_frame,text="Brush Size")
brush_size_frame.grid(row=0,column=0,padx=50)#feature things correctly
#Brush Slider
my_slider=ttk.Scale(brush_size_frame,from_=1,to=100,command=change_brush_size,orient=VERTICAL,value=10)#orient to move up and down or left or right
my_slider.pack(pady=10,padx=10)

#Brush slider label
slider_label=Label(brush_size_frame,text=my_slider.get())
slider_label.pack(pady=5)
#brush type
brush_type_frame=LabelFrame(brush_options_frame,text="Brush Type",height=400)
brush_type_frame.grid(row=0,column=1,padx=50)

brush_type=StringVar()
brush_type.set("round")

#create radio buttons for brush type
brush_type_radio1=Radiobutton(brush_type_frame,text="Round",variable=brush_type,value="round")
brush_type_radio2=Radiobutton(brush_type_frame,text="Slash",variable=brush_type,value="butt")
brush_type_radio3=Radiobutton(brush_type_frame,text="Diamond",variable=brush_type,value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

#change colors
change_colors_frame=LabelFrame(brush_options_frame,text="Change colors")
change_colors_frame.grid(row=0,column=2,)

#change brush color button
brush_color_button=Button(change_colors_frame,text="Brush Color",command=change_brush_color)
brush_color_button.pack(pady=10,padx=10)

#change canvas background color
canvas_color_button=Button(change_colors_frame,text="Canvas Color",command=change_canvas_color)
canvas_color_button.pack(pady=10,padx=10)

#Program options frame
options_frame=LabelFrame(brush_options_frame,text="Progarm options")
options_frame.grid(row=0,column=3,padx=50)#for save and clear screen option

#clear screen button
clear_button=Button(options_frame,text="Clear screen",command=clear_screen)
clear_button.pack(padx=10,pady=10)
#save image
save_image_button=Button(options_frame,text="Save to PNG",command=save_as_png)
save_image_button.pack(pady=10,padx=10)

root.mainloop()