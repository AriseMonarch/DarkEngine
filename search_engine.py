import Sort
import os

#txt search-------------------------------------------------------
def txt(search, catchIT):
  
 count = 0
 match = 0
 path = 'C:\\'

 score = {}

 for root, folder, files in os.walk(path):

  for i in files:
      

    path_file = os.path.join(root, i)

    if os.path.isfile(path_file) and i.endswith('.txt'):

      try:
        file = open(path_file, 'r', encoding= 'UTF-8')
        text = file.read()
        match = 0
      except UnicodeDecodeError:
       continue
      except PermissionError:
        continue

      for word in search.split():
          match = match + text.lower().count(word)
        

      if match > 0:
          count = count + 1
          score[path_file] = match 
          
  
 gui_print = sorted(score.items(), key= Sort.key, reverse=True)

 catchIT.put(gui_print)

 return('\nNumber Of Results:',count, gui_print, '\n')
#-------------------------------------------------------------------

#pdf search---------------------------------------------------------
def pdf(search, catchIT3):

 count = 0
 match = 0
 path = 'C:\\'

 score = {}

 for root, folder, files in os.walk(path):

  for i in files:

     match = 0
     path_file = os.path.join(root, i)

     if os.path.isfile(path_file) and i.endswith('.pdf'):  

      for word in search.split():
         match = match + path_file.lower().count(word)

      if  match > 0:
         score[path_file] = match 
       
  
 gui_print = sorted(score.items(), key= Sort.key, reverse=True)

 catchIT3.put(gui_print)


 return('\nNumber Of Results:',count, gui_print, '\n')
#-------------------------------------------------------------------



#folder search FAIL VERSION KEEP THIS AS A LEARNING EXPERIENCE--------------------
def directoriesFAIL(search):

  count = 0
  match = 0
  path = 'C:\\'

  score = {}

  for root, folder, files in os.walk(path):

   for i in files:
      
    path_file = os.path.join(root, i)

    if os.path.isfile(path_file):

      try:
        file = open(path_file, 'r', encoding= 'UTF-8')
        text = file.read()
        match = 0
      except UnicodeDecodeError:
       continue
      except PermissionError:
        continue
      
      for word in search.split():
       match = match + text.lower().count(word)


      if match > 0:
          count = count + 1

          if root in score:
               score[root] = score[root] + match 
          else:
               score[root] = match

      
        
    
  gui_print = sorted(score.items(), key= Sort.key, reverse=True)

  return('\nNumber Of Results:',count, gui_print, '\n')
#-----------------------------------------------------------------------

#WORKING FOLDER SEARCH(NOT EVERYTHING NEEDS TO BE COMPLICATED)-----------
def directories(search, catchIT2):

 count = 0
 match = 0
 path = 'C:\\'

 score = {}

 for root, folder, files in os.walk(path):

  for i in folder:

    match = 0
    path_folder = os.path.join(root, i)
      
    for word in search.split():
       match = match + path_folder.lower().count(word)

    if match > 0:
        score[path_folder] = match 
   
        if path_folder in score:
         score[path_folder] = score[path_folder] + match 
        else:
         score[path_folder] = match
       
  
 gui_print = sorted(score.items(), key= Sort.key, reverse=True)

 catchIT2.put(gui_print)


 return('\nNumber Of Results:',count, gui_print, '\n')
#-------------------------------------------------------------------

#powerpoint search---------------------------------------------------------
def powerpoint(search, catchIT4):

 count = 0
 match = 0
 path = 'C:\\'

 score = {}

 for root, folder, files in os.walk(path):

  for i in files:

     match = 0
     path_file = os.path.join(root, i)

     if os.path.isfile(path_file) and i.endswith('.pptx'):  

      for word in search.split():
         match = match + path_file.lower().count(word)

      if  match > 0:
         score[path_file] = match 
       
  
 gui_print = sorted(score.items(), key= Sort.key, reverse=True)

 catchIT4.put(gui_print)


 return('\nNumber Of Results:',count, gui_print, '\n')
#-------------------------------------------------------------------

