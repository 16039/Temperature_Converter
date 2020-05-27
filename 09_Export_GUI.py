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
        
        #Export Button (row 1)
        self.export_button = Button(self.converter_frame, text = "Export", 
                                  font = ("Arial", "14"),
                                  padx = 10, pady = 10, command = self.export)
        self.export_button.grid(row = 1)
        
    
    def export(self):
        print("You asked for export.")
        get_export = Export(self)
        get_export.export_text.configure(text = "Export text goes here")
        

class Export:
    def __init__(self, partner):
        
        background = "orange"
        
        #Disable export button
        partner.export_button.config(state = DISABLED)
        
        #Sets up child window (i.e. export box)
        self.export_box = Toplevel()
        
        #If user press cross at top, closes export and 'unlocks' the export button...
        self. export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))
        
        #Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg = background)
        self.export_frame.grid()        
        
        #Set up Export heading (row 0
        self.export_heading = Label(self.export_frame, text = "Export/Instructions", 
                                          font = ("Arial", "14", "bold"),
                                          bg = background)
        self.export_heading.grid(row = 0)        
        
        #Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text = "Enter a filename "
                                 "in the box below "
                                 "and press the save "
                                 "button to save your "
                                 "calculation history "
                                 "to a text file", 
                               justify = LEFT, 
                               width = 40, bg = background,
                               wrap = 250)
        self.export_text.grid(row = 1)
        
        #Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text = "If the filename "
                                 "you enter below "
                                 "already exists, "
                                 "its contents will "
                                 "be replaced with "
                                 "your calculation "
                                 "history",
                                 justify = LEFT, 
                               fg = "maroon", bg = "#ffafaf",
                               wrap = 225, padx = 10, font = "Arial 10 italic", pady = 10)
        self.export_text.grid(row = 2, pady = 10)
        
        #Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width = 20, font = "Arial 14 bold", justify = CENTER)
        self.filename_entry.grid(row = 3, pady = 10)
        
        #Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row = 5, pady = 10)
        
        #Save / Cancel button (row 2)
        self.save_button = Button(self.save_cancel_frame, text = "Cancel", command = partial(self.close_export, partner))
        self.save_button.grid(row = 0, column = 1)
        
    def close_export(self, partner):
    
        #Put export button back to normal...
        partner.export_button.config(state = NORMAL)
        self.export_box.destroy()
        

#Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()