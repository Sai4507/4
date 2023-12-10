import tkinter as tk
import backend as b
import actual_crops as ac
import suggest_crops as sc

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.admin = False
        '''self.connections_dict = {}'''
        self.minsize(800, 450)
        self.title("Login page")
        self.geometry_centered(800, 450)
        self.configure(bg='#141414')

        self.title_label = tk.Label(self, text="Fill the Fields", font=("courier new", 45, "bold"), fg="#426ae3", bg="#141414")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Row 1: Labels
        self.databaseurl_label = tk.Label(self, text="Nitrogen", font=("bookman old style", 15), fg="gray", bg="#141414")
        self.databaseurl_label.grid(row=1, column=0, padx=20)
        self.username_label = tk.Label(self, text="Phosphorus", font=("bookman old style", 15), fg="gray", bg="#141414")
        self.username_label.grid(row=2, column=0, padx=20)
        self.password_label = tk.Label(self, text="Potassium", font=("bookman old style", 15), fg="gray", bg="#141414")
        self.password_label.grid(row=3, column=0, padx=20)

        # Row 1: Entry Fields
        self.databaseurl_entry = tk.Entry(self, width=50, font=("Helvetica", 11), bg="white", fg="#141414")
        self.databaseurl_entry.grid(row=1, column=1, pady=5)
        self.username_entry = tk.Entry(self, width=45, font=("gothic", 13), bg="white", fg="#141414")
        self.username_entry.grid(row=2, column=1, pady=5)
        self.password_entry = tk.Entry(self, width=45, font=("Helvetica", 12), bg="white", fg="#141414")
        self.password_entry.grid(row=3, column=1, pady=5)

        # Row 2: Start Text Input
        self.start_text_label = tk.Label(self, text="Start Month Index", font=("bookman old style", 15), fg="gray", bg="#141414")
        self.start_text_label.grid(row=4, column=0, padx=20)
        self.start_text_entry = tk.Entry(self, width=50, font=("Helvetica", 11), bg="white", fg="#141414")
        self.start_text_entry.grid(row=4, column=1, pady=5)

        # Row 3: End Text Input
        self.end_text_label = tk.Label(self, text="End Month Index", font=("bookman old style", 15), fg="gray", bg="#141414")
        self.end_text_label.grid(row=5, column=0, padx=20)
        self.end_text_entry = tk.Entry(self, width=50, font=("Helvetica", 11), bg="white", fg="#141414")
        self.end_text_entry.grid(row=5, column=1, pady=5)

        # Row 4: Submit Button
        self.submit_button = tk.Button(self, width=20, command=self.submit_press, text="Submit", font=("courier new bold", 15), bg="#426ae3", fg="black")
        self.submit_button.grid(row=6, column=1, columnspan=2, pady=30)

        # Row 5: Error Label
        self.error_label = tk.Label(self, text=None, font=("bookman old style", 12), fg="red", bg='#141414')
        self.error_label.grid(row=7, column=0, columnspan=2, pady=(10, 10))

        self.next_window = None

    def geometry_centered(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def submit_press(self):
        dburl = self.databaseurl_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        start_text = self.start_text_entry.get()
        end_text = self.end_text_entry.get()
        
        if dburl == "" or username == "" or password == "" or start_text == "" or end_text == "":
            self.update_error_label("Please fill all the fields")
        else:
            #label_values = f"Database URL: {dburl}, Username: {username}, Password: {password}, Start Text: {start_text}, End Text: {end_text}"
            #self.update_error_label(label_values)
            NPKvalue=b.suggest_crop_input(dburl,username,password,start_text,end_text)
            avgTemp=b.giveavg(dburl,username,password,start_text,end_text)
            slist,sugDict=sc.runSuggestCrops(NPKvalue)
            suitcrops=ac.runSuitableCropList(slist,sugDict,avgTemp)
            label_values="Suitable Crops are: "
            for i in suitcrops:
                label_values=label_values+i+", "
            if label_values == "Suitable Crops are: ":
                label_values = "No suitable crops found"
            self.open_next_window(label_values)

    def update_error_label(self, message):
        self.error_label.config(text=message)
    
    def open_next_window(self,label_values):
        if self.next_window is None or not self.next_window.winfo_exists():
            self.next_window=menu(label_values)
            self.next_window.protocol("WM_DELETE_WINDOW")
            self.withdraw()
            self.next_window.deiconify()

class menu(tk.Tk):
    def __init__ (self,textdisplay,*args,**kwargs):
        super().__init__(*args, **kwargs)
        textFill=textdisplay
        self.minsize(800, 450)
        self.title("Login page")
        self.geometry_centered(800, 450)
        self.configure(bg='#141414')

        self.title_label = tk.Label(self, text="Crops Recommended", font=("courier new", 45, "bold"), fg="#426ae3", bg="#141414")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.databaseurl_label = tk.Label(self, text=textFill, font=("bookman old style", 15), fg="gray", bg="#141414")
        self.databaseurl_label.grid(row=1, column=0, padx=20)
        
        
    def geometry_centered(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

if __name__ == "__main__":
    app = Login()
    app.mainloop()