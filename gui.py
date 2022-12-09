from tkinter import *
import customtkinter
import csv
from tkinter import messagebox as m_box

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        '''This first section sets up the window for the GUI'''
        self.geometry("500x300")
        self.title("Project Part 1")
        self.resizable(height=False, width=False)


        '''This section establishes the first frame for the name entry box'''
        self.Frame1 = customtkinter.CTkFrame(master=self, width=180,)
        self.Label1 = customtkinter.CTkLabel(master=self.Frame1, text="Name")
        self.Entry1 = customtkinter.CTkEntry(self.Frame1)
        self.Label1.pack(padx=5, side='left')
        self.Entry1.pack(padx=5, side='left')
        self.Frame1.pack(anchor='w', pady=10)

        '''This section establishes the second frame for the age entry box'''
        self.frame_age = customtkinter.CTkFrame(master=self, width=180)  # Age Frame
        self.label_age = customtkinter.CTkLabel(master=self.frame_age, text='Age')
        self.entry_age = customtkinter.CTkEntry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=5, side='left')
        self.frame_age.pack(anchor='w')

        '''This section sets up the dropdown menu for the status choices'''
        self.frame_status = customtkinter.CTkComboBox(master=self, values = ['Student','Staff','Both'], state='readonly', text_color='#000000',fg_color = '#000000')
        self.label_status = customtkinter.CTkLabel(master=self.frame_status)
        self.frame_status.pack(padx=15,pady=15)

        '''This section sets up the Save button'''
        self.frame_button = customtkinter.CTkButton(master=self,text='SAVE', command=self.clicked)
        self.frame_button.place(relx=0.36, rely=0.425)

    '''This function grabs the entries from the the 3 different frames and also includes exception handling for incorrect inputs'''
    def clicked(self):
        name = self.Entry1.get()
        age = (self.entry_age.get())
        if name == '' or age == '':
            m_box.showerror('Error', 'Please fill both name and age, age must be greater than 0')
        else:
            try:
                age = int(age)
            except ValueError:
                m_box.showerror('title','Only numbers allowed for this field')
        status = self.frame_status.get()
        person = [name, age, status]
        m_box.showinfo('title','Information Saved!')

        '''This writes the information of the inputs onto a csv file'''
        with open("records.csv", 'a', newline='') as records:
            writer = csv.writer(records)
            writer.writerow(person)
            records.close()
            self.Entry1.delete(0,END)
            self.entry_age.delete(0,END)




if __name__ == '__main__':
    app = App()
    app.mainloop()









