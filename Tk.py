# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:48:19 2015

@author: Tosh
"""

# Simple enough, just import everything from tkinter.
from tkinter import *
import TSX
import sys

#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
# from PIL import Image, ImageTk


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Steve's Stock Selector Tool")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        scan = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        #edit.add_command(label="Show Img", command=self.showImg)
        scan.add_command(label="Show Text", command=self.showText)
        scan.add_command(label="Test Option", command=self.showTEST)
        scan.add_command(label="Run Complete TSX Scan", command=self.showTsxPicks)
        scan.add_command(label="Run NYSE Scan", command=self.showNysePicks)
        scan.add_command(label="Run TSX 500 Scan", command=self.showTsx500)
        #added "file" to our menu
        menu.add_cascade(label="Scan", menu=scan)

    #def showImg(self):
        #load = Image.open("chat.png")
        #render = ImageTk.PhotoImage(load)

        # labels can be text or images
        #img = Label(self, image=render)
        #img.image = render
        #img.place(x=0, y=0)


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()
   
    def showTEST(self):
        tsxTEST = TSX.showTEST() 
        text = Label(self, command=tsxTEST)
        text.pack()   
   
    def showTsxPicks(self):
        tsxPick = TSX.scrapeTSX() 
        text = Label(self, text = 'Full TSX Scan Here')
        text.pack()
        
    def showNysePicks(self):
        NysePick = TSX.scrapeNYSE() 
        text = Label(self, text = 'Full NYSE Scan Here')
        text.pack()
    
    def showTsx500(self):
        NysePick = TSX.scrapeTSX500() 
        text = Label(self, text = 'TSX500 Scan Here')
        text.pack()    
        
    def client_exit(self):
        exit()



'''
######################################
#incompleted Save to File Section
    saveFile = open('TSXgraham.txt','w')
    saveFile.write(text)
    saveFile.close() 

####################################

'''

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
