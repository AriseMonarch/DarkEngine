import tkinter as tk
from search_engine import txt
from search_engine import directories
from search_engine import pdf
from search_engine import powerpoint
from PIL import Image, ImageDraw , ImageTk
import math
import threading
import queue


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








#tkinter window---------------------------
root = tk.Tk()
root.config(bg = '#290040' )
root.geometry('1920x1080')
canvas = tk.Canvas(root, bg= "#000000" , width= 1929, height=1081)
#-----------------------------------------

#this is the library to return the result of the function
catchIT = queue.Queue()
catchIT2 = queue.Queue()
catchIT3 = queue.Queue()
catchIT4 = queue.Queue()
#--------------------------------------------------------

search = tk.Entry(root)
canvas.place(x=-5, y=0)
search.place(x=430, y=0)
glow = Image.new("RGBA",(200,200),(91, 0, 128, 0))
draw = ImageDraw.Draw(glow)


for x in range(200):
 for y in range(200):
  horizontal = (x - 100) ** 2 
  vertical = (y - 100) ** 2
  distance = (horizontal + vertical)
  squere_root = math.sqrt(distance)
  away_center = squere_root / 100 
  if squere_root <= 100:
   real_distance = 1 - away_center
   alpha = int(real_distance * 255)
   draw.point((x,y), fill=(91 ,0 ,128 ,alpha ))

real_glow = ImageTk.PhotoImage(glow)
glow_image = canvas.create_image(500,300, image= real_glow)

def mouse_animated(position):
 canvas.coords(glow_image,position.x, position.y)

canvas.bind('<Motion>',mouse_animated)



#Instruction text------------------------------------------------------------------------------------------------------------------------------------------------
tk.Label(root, text = 'INSTUCTION: write what you want to search for and wait until it responds',  bg = '#290040', fg = '#FFFFFF' ).place(x=600, y=0)

tk.Label(root, text = 'SEARCH HERE ---->', bg = '#290040', fg = '#FFFFFF').place(x=320,y=0)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#BUTTONS----------------------------------------------------------------------------------------------------------------------
tk.Button(root, text ='Search txt', bg = '#290040', fg = '#FFFFFF', command = search_txt).place(x=400, y=25)

tk.Button(root, text ='Search folder', bg = '#290040', fg = '#FFFFFF', command = search_folder).place(x=460, y=25)

tk.Button(root, text ='Search PDF', bg = '#290040', fg =  '#FFFFFF' , command = search_PDF).place(x=538, y=25)

tk.Button(root, text ='Search Powerpoint', bg ='#290040', fg = '#FFFFfF', command = search_powerpoint).place(x=607,y=25)
#-----------------------------------------------------------------------------------------------------------------------------


#Black box that prints like a terminal--------------------------------------------------------
information = tk.Text(root, bg = '#000000', fg = '#FFFFFF', width = 240, height = 30  )

information.place(x=0, y=600)
#---------------------------------------------------------------------------------------------
































root.mainloop()