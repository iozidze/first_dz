from zipfile import ZipFile
from collections import defaultdict
import time
from datetime import datetime
# from array import *


with ZipFile('FileSystem.zip', 'a') as myzip:
  me = 1
    # 1 - root
  pwd =''
  user = 'root'
  #n = 10 #максимальное количество уровней
  names = defaultdict(set)
  for name in myzip.namelist(): 
    words_list = name.split('/')
    words_list = list(filter(None, words_list))
    count = len(words_list)
    level = count + 1 # уровень, раз 1 - корень
    for i in range(2, 10):
      if level == i:
        names[str(i)].add(name)
  
  while True:
    # names = []

    



    if me == 1:
      command = input('$ ')
      realname = ""

  
          
      if command == 'ls':
        for i in names[str(me+1)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
          print(realname)

      if command.startswith('rmdir '):
        todelete = command[6:]
        ifprint = 0
        find_level_to_delete = todelete.split('/')
        find_level_to_delete = list(filter(None, find_level_to_delete))
        level_to_delete = len(find_level_to_delete)
        
        for i in names[str(level_to_delete+2)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1] #сейчас realname - директория, куда можно отправиться командой cd из todelete
          ifsomethingindir = []
          tocomparebeforedel = []
          tocomparebeforedel = todelete.split('/')
          ifsomethingindir = realname.split('/')
          if tocomparebeforedel[-1] == ifsomethingindir[-2]:
            ifprint = 1
          if (level_to_delete+1) <= me:
            ifprint = 2
        if ifprint == 2:
          print("В данный момент невозможно удалить эту директорию")
        if ifprint == 1:
          print("Директория не пуста!")
        if ifprint == 0:
          willbedeleted = ''
          for i in names[str(level_to_delete+1)]:
            lastsinght = ''
            realname = i
            lastsinght = lastsinght + realname[-1]
            while lastsinght == '/':
              realname = realname[:-1]
              lastsinght = realname[-1] #а здесь realname - директории, равные по уровню той, которую хотим удалить
            if todelete == realname:
              willbedeleted = i
          if willbedeleted != '':  
            names[str(level_to_delete+1)].remove(willbedeleted)  
        

        
      
      if command == 'cd ..':
          print('Вы находитесь в корне!')

      elif command.startswith('cd '):
   
        word = command[3:]
        for i in names[str(me+1)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
          if word == realname:
            menow = me
            me = me + 1
            pwd = word
          else:
            print("Такой директории не существует!")


      if command == "exit":
        exit()

      if command == "who":
        current_time = int(time.time())
        hours = (current_time // 3600 + 3)% 24
        minutes = current_time // 60 % 60
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        if len(str(minutes)) == 1:
          minutes = '0' + str(minutes)
        if len(str(hours)) == 1:
          hours = '0' + str(hours)
        time_now = str(hours) + ':' + str(minutes)
        
        print(user + "     pts/1     " + str(formatted_date) + ' ' + time_now)

    elif me == 2:
  
      if (menow < me) or flag == 1:
        command = input('$ '+ pwd + ' ')
      else:
        words = []
        words = pwd.split('/')
        pwd = ''
        lena = len(words)
        for i in range(lena-1):
          pwd = pwd + words[i] + '/'
        pwd = pwd[:-1]
        command = input('$ '+ pwd + ' ')
        flag = 1

      
          
      if command == 'ls':
        for i in names[str(me+1)]:
          
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
          words = []
          word = pwd.split('/')
          words = realname.split('/')
          if words[-2] == word[-1]:
            print(words[-1])

      if command.startswith('rmdir '):
        todelete = command[6:]
        ifprint = 0
        find_level_to_delete = todelete.split('/')
        find_level_to_delete = list(filter(None, find_level_to_delete))
        level_to_delete = len(find_level_to_delete)
        
        for i in names[str(level_to_delete+2)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1] #сейчас realname - директория, куда можно отправиться командой cd из todelete
          ifsomethingindir = []
          tocomparebeforedel = []
          tocomparebeforedel = todelete.split('/')
          ifsomethingindir = realname.split('/')
          if tocomparebeforedel[-1] == ifsomethingindir[-2]:
            ifprint = 1
          if (level_to_delete+1) <= me:
            ifprint = 2
        if ifprint == 2:
          print("В данный момент невозможно удалить эту директорию")
        if ifprint == 1:
          print("Директория не пуста!")
        if ifprint == 0:
          willbedeleted = ''
          for i in names[str(level_to_delete+1)]:
            lastsinght = ''
            realname = i
            lastsinght = lastsinght + realname[-1]
            while lastsinght == '/':
              realname = realname[:-1]
              lastsinght = realname[-1] #а здесь realname - директории, равные по уровню той, которую хотим удалить
            if todelete == realname:
              willbedeleted = i
          if willbedeleted != '':  
            names[str(level_to_delete+1)].remove(willbedeleted)  
        
          
        
      
        
            
        

      if command == 'cd ..': 
        me = me - 1
        flag = 0

      elif command.startswith('cd '):
        
        word = command[3:]
        n = 0
        for i in names[str(me+1)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
          words = []
          words = realname.split('/')
          
          if word == words[-1]:
            menow = me
            me = me + 1
            pwd = pwd + '/' + word
            n = 1
            flag = 1
        if n == 0:
          print("Такой директории не существует!")


      if command == "exit":
        exit()

      if command == "who":
        current_time = int(time.time())
        hours = (current_time // 3600 + 3)% 24
        minutes = current_time // 60 % 60
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        time_now = str(hours) + ':' + str(minutes)
        
        print("root     pts/1     " + str(formatted_date) + ' ' + time_now)

    elif me >= 3:
  
      if (menow < me) or flag == 1:
        command = input('$ '+ pwd + ' ')
      else:
        words = []
        words = pwd.split('/')
        pwd = ''
        lena = len(words)
        for i in range(lena-1):
          pwd = pwd + words[i] + '/'
        pwd = pwd[:-1]
        command = input('$ '+ pwd + ' ')
        flag = 1



      if command == 'ls':
        for i in names[str(me+1)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
          words = []
          words = realname.split('/')
          word = pwd.split('/')
          if words[-2] == word[-1]:
            print(words[-1])

      if command.startswith('rmdir '):
        todelete = command[6:]
        ifprint = 0
        find_level_to_delete = todelete.split('/')
        find_level_to_delete = list(filter(None, find_level_to_delete))
        level_to_delete = len(find_level_to_delete)
        
        for i in names[str(level_to_delete+2)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1] #сейчас realname - директория, куда можно отправиться командой cd из todelete
          ifsomethingindir = []
          tocomparebeforedel = []
          tocomparebeforedel = todelete.split('/')
          ifsomethingindir = realname.split('/')
          if tocomparebeforedel[-1] == ifsomethingindir[-2]:
            ifprint = 1
          if (level_to_delete+1) <= me:
            ifprint = 2
        if ifprint == 2:
          print("В данный момент невозможно удалить эту директорию")
        if ifprint == 1:
          print("Директория не пуста!")
        if ifprint == 0:
          willbedeleted = ''
          for i in names[str(level_to_delete+1)]:
            lastsinght = ''
            realname = i
            lastsinght = lastsinght + realname[-1]
            while lastsinght == '/':
              realname = realname[:-1]
              lastsinght = realname[-1] #а здесь realname - директории, равные по уровню той, которую хотим удалить
            if todelete == realname:
              willbedeleted = i
          if willbedeleted != '':  
            names[str(level_to_delete+1)].remove(willbedeleted)   
        
          
            
            
       
          
            
          
            
    
      if command == 'cd ..':
          me = me - 1
          flag = 0

      elif command.startswith('cd '):
        
        word = command[3:]
        n = 0
        for i in names[str(me+1)]:
          lastsinght = ''
          realname = i
          lastsinght = lastsinght + realname[-1]
          while lastsinght == '/':
            realname = realname[:-1]
            lastsinght = realname[-1]
          words = []
          words = realname.split('/')
          menow = me
          if word == words[-1]:
            menow = me
            me = me + 1
            pwd = pwd + '/' + word
            n = 1
            flag = 1
        if n == 0:
          print("Такой директории не существует!")


      

      if command == "exit":
        exit()

      if command == "who":
        current_time = int(time.time())
        hours = (current_time // 3600 + 3)% 24
        minutes = current_time // 60 % 60
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        time_now = str(hours) + ':' + str(minutes)
        
        print("root     pts/1     " + str(formatted_date) + ' ' + time_now)


