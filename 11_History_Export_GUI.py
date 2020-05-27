from tkinter import *
import random
from functools import partial #To prevent unwanted windows
import re

class Convertor:
    def __init__(self,parent):
        
        #Formatting variables...
        background_colour = "light blue"
        
        #In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              #'40 degrees C is 104 degrees F',
                              #'40 degrees C is 4.4 degrees F',
                              #'12 degrees C is 53.6 degrees F',                              
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F']
        
        #self.all_calc_list = []
        
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
        
        #history Button (row 1)
        self.history_button = Button(self.converter_frame, text = "History", 
                                  font = ("Arial", "14"),
                                  padx = 10, pady = 10, 
                                  command = lambda: self.history(self.all_calc_list))
        self.history_button.grid(row = 1)
        
        if len(self.all_calc_list) == 0:
            self.history_button.config(state = DISABLED)
        
        
    
    def history(self, calc_history):
        History(self, calc_history)
        

class History:
    def __init__(self, partner, calc_history):
        
        background = "#a9ef99" #Pale green
        
        #Disable history button
        partner.history_button.config(state = DISABLED)
        
        #Sets up child window (i.e. history box)
        self.history_box = Toplevel()
        
        #If user press cross at top, closes history and 'unlocks' the history button...
        self. history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))
        
        #Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg = background)
        self.history_frame.grid()        
        
        #Set up history heading (row 0)
        self.history_heading = Label(self.history_frame, text = "Calculation History", 
                                          font = ("Arial", "19", "bold"),
                                          bg = background)
        self.history_heading.grid(row = 0)        
        
        #history text (label, row 1)
        self.history_text = Label(self.history_frame, text = "Here are your most recent "
                                  "calculations. Please use the "
                                  "export button to create a text "
                                  "file for all your calculations for "
                                  "this session", font = "arial 10 italic",
                               justify = LEFT, fg = "maroon",
                               padx = 10, pady = 10, bg = background,
                               wrap = 250)
        self.history_text.grid(row = 1)
        
        #History output goes here (row 2)
        
        #Generate string from list of calculations
        history_string = ""
        
        if len(calc_history) > 7:
            for item in range (0,7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"
        
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                
                self.history_text.config(text = "Here is your calculation "
                                         "history. You can use the "
                                         "export button to save this "
                                         "data to a text file if "
                                         "desired.")
                
        
        #Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text = history_string, bg = background, font = "arial 12", justify = LEFT)
        self.calc_label.grid(row = 2)
        
        #Export / Dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row = 3, pady = 10)
        
        #Export Button
        self.export_button = Button(self.export_dismiss_frame, text = "Export",
                                    font = "Arial 12 bold",
                                    command=lambda: self.export(calc_history)) #New addition
        self.export_button.grid(row = 0, column = 0)
        
        #Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text = "Dismiss",
                                    font = "Arial 12 bold", command = partial(self.close_history, partner))
        self.dismiss_button.grid(row = 0, column = 1)
        
        
    def close_history(self, partner):
    
        #Put history button back to normal...
        partner.history_button.config(state = NORMAL)
        self.history_box.destroy()
        
    def export(self, calc_history):
        Export(self, calc_history)
        

class Export:
    def __init__(self, partner, calc_history):
        
        print(calc_history)
        
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
        
        #Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text = "", fg = "maroon", bg = background)
        self.save_error_label.grid(row = 4)
        
        #Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row = 5, pady = 10)
        
        #Save / Cancel button (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text = "Save", command = partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row = 0, column = 0)
        
        self.cancel_button = Button(self.save_cancel_frame, text = "Cancel", command = partial(self.close_export, partner))
        self.cancel_button.grid(row = 0, column = 1)        
        
    def save_history(self, partner, calc_history):
    
        #Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error ="no"
        
        filename = self.filename_entry.get() #Can retrieve what the user had typed earlier
        print(filename)
        
        for letter in filename:
            if re.match(valid_char, letter):
                continue
            
            elif letter == " ":
                problem = "(no spaces allowed)"
                
            else:
                problem = ("(no {}'s allowed)".format(letter))
            
            has_errror = "yes"
            break
            
            
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"
        
        if has_error == "yes":
            #Disply error message
            self.save_error_label.config(text = "Invalid filename - {}".format(problem))
            #Change entry box background to pink
            self.filename_entry.config(bg = "#ffafaf")
            print()
            
        else:
            #If there are no errors, generate text file and then close dialouge
            #add .txt suffix!
            filename = filename + ".txt"
            
            #Create file to hold data 
            f = open(filename, "w+")
            
            #Add new line at the end of each item
            for item in calc_history:
                f.write(item + "\n")
            
            #close file
            f.close()
            
            #Close dialouge
            self.close_export(partner)
    
    
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