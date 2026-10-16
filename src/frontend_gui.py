import tkinter as tk
from search_engine import txt
from search_engine import directories
from search_engine import pdf
from search_engine import powerpoint
from PIL import Image, ImageDraw , ImageTk, ImageDraw, ImageFont, ImageText , ImageFilter
import math
import threading
import queue
from pathlib import Path

font = r'C:\Windows\Fonts\Micross.ttf.'


#takes catchIT from Threading and prints the results, if its empty it retries
def search_results1():

 if catchIT.empty():

  root.after(100,search_results1)
  
 else:
  catched = catchIT.get()

  for i in catched:
    information.insert(tk.END , i )
    information.insert(tk.END , '\n\n')
#------------------------------------------------------------------------------

#takes catchIT from Threading and prints the results, if its empty it retries
def search_results2():

 if catchIT2.empty():

  root.after(100,search_results2)
  
 else:
  catched2 = catchIT2.get()

  for i in catched2:
    information.insert(tk.END , i )
    information.insert(tk.END , '\n\n')
#------------------------------------------------------------------------------

#takes catchIT from Threading and prints the results, if its empty it retries
def search_results3():

 if catchIT3.empty():

  root.after(100,search_results3)
  
 else:
  catched3 = catchIT3.get()

  for i in catched3:
    information.insert(tk.END , i )
    information.insert(tk.END , '\n\n')
#------------------------------------------------------------------------------

#takes catchIT from Threading and prints the results, if its empty it retries
def search_results4():

 if catchIT4.empty():

  root.after(100,search_results4)
  
 else:
  catched4 = catchIT4.get()

  for i in catched4:
    information.insert(tk.END , i )
    information.insert(tk.END , '\n\n')
#------------------------------------------------------------------------------

#backend function for txt search-----------------
def search_txt():

 information.delete(1.0, tk.END)
 result = search.get()
 thread_search = threading.Thread( target=txt,
                 args=(result, catchIT)
)
 thread_search.start()
 search_results1()
#-------------------------------------------------

#backend function directory search----------------------
def search_folder():

 information.delete(1.0, tk.END)
 result = search.get()
 thread_search = threading.Thread( target=directories,
                 args=(result, catchIT2)
)
 thread_search.start()
 search_results2()
#--------------------------------------------------------

#backend function for PDF Search-------------------
def search_PDF():

 information.delete(1.0, tk.END)
 result = search.get()
 thread_search = threading.Thread( target=pdf,
                 args=(result, catchIT3)
)
 thread_search.start()
 search_results3()
#-------------------------------------------------

#backend function for powerpoint Search-----------------
def search_powerpoint():

 information.delete(1.0, tk.END)
 result = search.get()
 thread_search = threading.Thread( target=powerpoint,
                 args=(result, catchIT4)
)
 thread_search.start()
 search_results4()
#-------------------------------------------------------

#Pulse animation----------------------------------------
def pulse_animation(pulse, direction):  

    if direction == 1:
      pulse = pulse + 1
    
    if direction == -1:
       pulse = pulse - 1

    if pulse == 25:
       direction = -1
    
    if pulse == 0:
       direction = 1
 
    canvas.itemconfig(glow_image, image=glows[pulse])
    root.after(25 , pulse_animation,pulse, direction) 
#---------------------------------------------------------

#tkinter window------------------------------------------------------
root = tk.Tk()
root.config(bg = '#290040' )
root.geometry('1920x1080')
canvas = tk.Canvas(root, bg= "#161616" , width= 1925, height=1080)
#--------------------------------------------------------------------

#Glow Blur on DarkEngine----------------------------------------------------------------------------------
DarkEngine_neon_text_BLUR = ImageText.Text('DarkEngine', ImageFont.truetype(font, 71)) 
DarkEngine_neon_text_glow_BLUR = Image.new('RGBA',(1000,1000),(91, 0, 128, 0))
DarkEngine_draw_text_BLUR = ImageDraw.Draw(DarkEngine_neon_text_glow_BLUR)
DarkEngine_draw_text_BLUR.text((500, 500) , text= (DarkEngine_neon_text_BLUR) , fill= "#9E00FA" )
DarkEngine_Blur = ImageFilter.GaussianBlur(8)
DarkEngine_real_BLUR = DarkEngine_neon_text_glow_BLUR.filter(DarkEngine_Blur)
DarkEngine_Finished_BLUR = ImageTk.PhotoImage(DarkEngine_real_BLUR)
tkinter_DarkEngine_BLUR = canvas.create_image(795,107, image= DarkEngine_Finished_BLUR) 

DarkEngine_neon_text_BLUR2 = ImageText.Text('DarkEngine', ImageFont.truetype(font, 71)) 
DarkEngine_neon_text_glow_BLUR2 = Image.new('RGBA',(1000,1000),(91, 0, 128, 0))
DarkEngine_draw_text_BLUR2 = ImageDraw.Draw(DarkEngine_neon_text_glow_BLUR2)
DarkEngine_draw_text_BLUR2.text((500, 500) , text= (DarkEngine_neon_text_BLUR2) , fill= "#9E00FA" )
DarkEngine_Blur2 = ImageFilter.GaussianBlur(8)
DarkEngine_real_BLUR2 = DarkEngine_neon_text_glow_BLUR.filter(DarkEngine_Blur2)
DarkEngine_Finished_BLUR2 = ImageTk.PhotoImage(DarkEngine_real_BLUR2)
tkinter_DarkEngine_BLUR2 = canvas.create_image(795,107, image= DarkEngine_Finished_BLUR2) 

DarkEngine_neon_text_BLUR3 = ImageText.Text('DarkEngine', ImageFont.truetype(font, 71)) 
DarkEngine_neon_text_glow_BLUR3 = Image.new('RGBA',(1000,1000),(91, 0, 128, 0))
DarkEngine_draw_text_BLUR3 = ImageDraw.Draw(DarkEngine_neon_text_glow_BLUR3)
DarkEngine_draw_text_BLUR3.text((500, 500) , text= (DarkEngine_neon_text_BLUR3) , fill= "#9E00FA" )
DarkEngine_Blur3 = ImageFilter.GaussianBlur(8)
DarkEngine_real_BLUR3 = DarkEngine_neon_text_glow_BLUR3.filter(DarkEngine_Blur3)
DarkEngine_Finished_BLUR3 = ImageTk.PhotoImage(DarkEngine_real_BLUR3)
tkinter_DarkEngine_BLUR3 = canvas.create_image(795,107, image= DarkEngine_Finished_BLUR3) 
#---------------------------------------------------------------------------------------------------------

#DarkEngine Text-------------------------------------------------------------------------------------------
canvas.create_text(980,150, fill= "white", font=('Microsoft-Sans-Serif', 50, 'bold'), text= 'DarkEngine')
search = tk.Entry(root, font=('Microsoft-Sans-Serif'))
#----------------------------------------------------------------------------------------------------------

#this is the library to return the result of the function
catchIT = queue.Queue()
catchIT2 = queue.Queue()
catchIT3 = queue.Queue()
catchIT4 = queue.Queue()
#--------------------------------------------------------

#basic widgets--------------------------------------
canvas.place(x=-5, y=0)
search.place(width=220, height= 30, x=855, y=400)
glow = Image.new("RGBA",(200,200),(91, 0, 128, 0))
draw = ImageDraw.Draw(glow)
pulse = 0
direction = 1
glows = []
#---------------------------------------------------

#creates 25 images so that it wont lag and stores them into glows list
for i in range(26):

      
 pulse_strength = i / 20
 glow = Image.new("RGBA", (200, 200), (91, 0, 128, 0))
 draw = ImageDraw.Draw(glow)

 for x in range(200):
  for y in range(200):
    horizontal = (x - 100) ** 2 
    vertical = (y - 100) ** 2
    distance = (horizontal + vertical)
    squere_root = math.sqrt(distance)
    away_center = squere_root / 100 
    if squere_root <= 100:
      real_distance = (1 - away_center) * pulse_strength
      alpha = int(real_distance * 255)
      draw.point((x,y), fill=(91, 0, 128, alpha))
 real_glow = ImageTk.PhotoImage(glow)
 glows.append(real_glow)
#-------------------------------------------------------------------




#creates an image on the canvas and takes the glow from the list
glow_image = canvas.create_image(500,300)
#----------------------------------------------------------------


BASE_DIR = Path(__file__).resolve().parent

#Custom images for the buttons--------------------------------------------
search_folder_image = Image.open(BASE_DIR / 'search_folder.png')
search_folder_image_size = search_folder_image.resize((100,60))
search_folder_image_real = ImageTk.PhotoImage(search_folder_image_size)

search_pdf_image = Image.open(BASE_DIR / 'search_pdf.png')
search_pdf_image_size = search_pdf_image.resize((100,60))
search_pdf_image_real = ImageTk.PhotoImage(search_pdf_image_size)

search_pptx_image = Image.open(BASE_DIR / 'search_pptx.png')
search_pptx_image_size = search_pptx_image.resize((100,60))
search_pptx_image_real = ImageTk.PhotoImage(search_pptx_image_size)

search_txt_image = Image.open(BASE_DIR / 'search_txt.png')
search_txt_image_size = search_txt_image.resize((100,60))
search_txt_image_real = ImageTk.PhotoImage(search_txt_image_size)

tk_txt = canvas.create_image(800 , 560, image= search_txt_image_real)

tk_folder = canvas.create_image(910, 560, image = search_folder_image_real)

tk_pdf = canvas.create_image(1020, 560, image = search_pdf_image_real)

tk_pptx = canvas.create_image(1130, 560, image= search_pptx_image_real)
#----------------------------------------------------------------------------



pulse_animation(pulse, direction)

def mouse_animated(position):
 canvas.coords(glow_image,position.x, position.y)

#Helpers-------------------------
def search_txt_helper(event):
  search_txt()

def search_folder_helper(event):
  search_folder()

def search_PDF_helper(event):
  search_PDF()

def search_pptx_helper(event):
  search_powerpoint()
#--------------------------------

#--------------------------------
def txt_description(event):
  print(x, y)

def folder_description(event):
  print(x,y)

def PDF_description(event):
  print(x,y)

def pptx_description(event):
  print(x,y)
#-------------------------------

#when the mouse moves the glow follows
canvas.bind('<Motion>',mouse_animated)
#-------------------------------------

#Makes the image a button and assigns it with the help of the helper function
canvas.tag_bind(tk_txt, '<Button-1>',search_txt_helper)          
canvas.tag_bind(tk_txt, '<Enter>', txt_description)

canvas.tag_bind(tk_folder, '<Button-1>', search_folder_helper)
canvas.tag_bind(tk_txt, '<Enter>', folder_description)

canvas.tag_bind(tk_folder, '<Button-1>', search_PDF_helper)
canvas.tag_bind(tk_txt, '<Enter>', PDF_description)

canvas.tag_bind(tk_folder, '<Button-1>', search_pptx_helper)
canvas.tag_bind(tk_txt, '<Enter>', pptx_description)



#----------------------------------------------------------------------------


#Instruction text-----------------------------------------------------------------------------------------------------------------------------------------
tk.Label(root, text = 'INSTUCTION: write what you want to search for and wait until it responds',  bg = '#290040', fg = '#FFFFFF' ).place(x=600, y=0)

tk.Label(root, text = 'SEARCH HERE ---->', bg = '#290040', fg = '#FFFFFF').place(x=700,y=405)
#---------------------------------------------------------------------------------------------------------------------------------------------------------


#Black box that prints like a terminal--------------------------------------------------------
information = tk.Text(root, bg = "#161616", fg = '#FFFFFF', width = 240, height = 30  )
information.insert(tk.INSERT, 'Results:')
information.place(x=0, y=600)
#---------------------------------------------------------------------------------------------
































root.mainloop()