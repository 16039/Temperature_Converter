from tkinter import *
import random
from functools import partial #To prevent unwanted windows

class Convertor:
    def __init__(self,parent):
        
        #Formatting variables...
        background_colour = "light blue"
        
        #Converter Main Screen GUI...
        self.converter_frame = Frame(width = 300, height = 300, bg = background_colour,
                                     pady = 10)
        self.converter_frame.grid()
        
        #Termperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text = "Temperature Converter", 
                                          font = ("Arial", "16", "bold"),
                                          bg = background_colour,
                                          padx = 10, pady = 10)
        self.temp_converter_label.grid(row = 0)
        
        #Help Button (row 1)
        self.help_button = Button(self.converter_frame, text = "Help", 
                                  font = ("Arial", "14"),
                                  padx = 10, pady = 10, command = self.help)
        self.help_button.grid(row = 1)
        
    
    def help(self):
        print("You asked for help.")
        get_help = Help(self)
        get_help.help_text.configure(text = "Help text goes here")
        

class Help:
    def __init__(self, partner):
        
        background = "orange"
        
        #Disable help button
        partner.help_button.config(state = DISABLED)
        
        #Sets up child window (i.e. help box)
        self.help_box = Toplevel()
        
        #If user press cross at top, closes help and 'unlocks' the help button...
        self. help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        
        #Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg = background)
        self.help_frame.grid()        
        
        #Set up Help heading (row 0
        self.help_heading = Label(self.help_frame, text = "Help/Instructions", 
                                          font = ("Arial", "10", "bold"),
                                          bg = background)
        self.help_heading.grid(row = 0)        
        
        #Help text (label, row 1)
        self.help_text = Label(self.help_frame, text = "", 
                               justify = LEFT, 
                               width = 40, bg = background,
                               wrap = 250)
        self.help_text.grid(row = 1)
        
        #Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, text = "Dismiss", width = 10,
                                     bg = background, font = ("Arial", "10", "bold"),
                                     command = partial(self.close_help, partner))
        self.dismiss_button.grid(row = 2, pady = 10)
        
    def close_help(self, partner):
    
        #Put help button back to normal...
        partner.help_button.config(state = NORMAL)
        self.help_box.destroy()
        

#Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()