import tkinter as tk
import hashlib
import tkinter
import tkinter.messagebox
import mysql.connector

class Manager():
    def __init__(self):
        self.main_window = tk.Tk()
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.geometry("{}x{}".format(int(screen_width), int(screen_height)))
        self.main_window.title("Pizza Billing System - Employee SignUp")

        frame_width = 500
        frame_height = 700
        self.signup_frame = tk.Frame(self.main_window, width=frame_width, height=frame_height, highlightthickness=2,
                                     highlightbackground="black")
        self.signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ## creating first name last name contact
        self.first_label = tk.Label(self.signup_frame, text="First Name:", font=("Arial", 12))
        self.first_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.first_label.grid(row=0, column=0, pady=10)
        self.first_entry.grid(row=0, column=1, pady=10)

        self.middle_label = tk.Label(self.signup_frame, text="Middle Name:", font=("Arial", 12))
        self.middle_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.middle_label.grid(row=1, column=0, pady=10)
        self.middle_entry.grid(row=1, column=1, pady=10)

        self.last_label = tk.Label(self.signup_frame, text="Last Name:", font=("Arial", 12))
        self.last_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.last_label.grid(row=2, column=0, pady=10)
        self.last_entry.grid(row=2, column=1, pady=10)

        self.contact_label = tk.Label(self.signup_frame, text="Contact Number:", font=("Arial", 12))
        self.contact_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.contact_label.grid(row=3, column=0, pady=10)
        self.contact_entry.grid(row=3, column=1, pady=10)

        # create Adress label and entry
        self.Address_label = tk.Label(self.signup_frame, text="Address:", font=("Arial", 12))
        self.Address_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.Address_label.grid(row=4, column=0, pady=10)
        self.Address_entry.grid(row=4, column=1, pady=10)

        self.State_label = tk.Label(self.signup_frame, text="State:", font=("Arial", 12))
        self.State_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.State_label.grid(row=5, column=0, pady=10)
        self.State_entry.grid(row=5, column=1, pady=10)

        self.City_label = tk.Label(self.signup_frame, text="City:", font=("Arial", 12))
        self.City_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.City_label.grid(row=6, column=0, pady=10)
        self.City_entry.grid(row=6, column=1, pady=10)

        self.Zip_label = tk.Label(self.signup_frame, text="ZipCode:", font=("Arial", 12))
        self.Zip_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.Zip_label.grid(row=7, column=0, pady=10)
        self.Zip_entry.grid(row=7, column=1, pady=10)

        self.Email_label = tk.Label(self.signup_frame, text="Email:", font=("Arial", 12))
        self.Email_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.Email_label.grid(row=8, column=0, pady=10)
        self.Email_entry.grid(row=8, column=1, pady=10)

        # create password label and entry
        self.password_label = tk.Label(self.signup_frame, text="Password:", font=("Arial", 12))
        self.password_entry = tk.Entry(self.signup_frame, show="*", font=("Arial", 12))
        self.password_label.grid(row=9, column=0, pady=10)
        self.password_entry.grid(row=9, column=1, pady=10)

        # create confirm password label and entry
        self.confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:", font=("Arial", 12))
        self.confirm_password_entry = tk.Entry(self.signup_frame, show="*", font=("Arial", 12))
        self.confirm_password_label.grid(row=10, column=0, pady=10)
        self.confirm_password_entry.grid(row=10, column=1, pady=10)

        # create signup button
        self.signup_button = tk.Button(self.signup_frame, text="Sign Up", command=self.signup, width=10, bg="White",
                                       fg="red", font=("Arial", 10, "bold"))
        self.signup_button.grid(row=11, column=1, pady=10)

        # create back button
        self.back_button = tk.Button(self.signup_frame, text="Back", command=self.back, width=10, bg="White", fg="red",
                                     font=("Arial", 10, "bold"))
        self.back_button.grid(row=11, column=0, pady=10)

        tk.mainloop()

    def signup(self):

        first = self.first_entry.get()
        middle = self.middle_entry.get()
        last = self.last_entry.get()
        fi = first[0].lower()
        uid = ' '
        num = 0
        if middle != "":
            mi = middle[0].lower()
        else:
            mi = ""

        if len(last) > 5:
            first_p = last[:5]
        else:
            first_p = last
            print(first_p)

        pattern = first_p + '%'
        # check if the username already exists in the database
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="pizza"
        )
        # Perform database operations
        cursor = mydb.cursor()
        select_stmt = "SELECT COUNT(last_name) FROM EmployeeInformation WHERE Last_Name like %s"
        cursor.execute(select_stmt, (pattern,))
        num = cursor.fetchone()[0]
        print('num: ', num)
        uid = first_p.lower() + str(num + 1) + fi + mi
        if self.password_entry.get() != self.confirm_password_entry.get():
            error_message = tk.Label(self.main_window, text="Error: Passwords do not match.")
            error_message.grid(row=4, column=0, columnspan=2)
            return
        tkinter.messagebox.showinfo("Username", uid)

        #######
        # Query the database for the highest existing Employee ID
        cursor.execute("SELECT MAX(Employee_ID) FROM EmployeeInformation")
        max_id = cursor.fetchone()[0]
        if max_id is None:
            # If there are no existing Employee, start the Employee ID sequence at 1
            max_id = 0
        else:
            # Convert the max_id value to an integer
            max_id = int(max_id.replace("EMP", ""))

        # Increment the highest Employee ID to generate a new unique Employee ID
        new_id = max_id + 1

        # Add "CUS" back to the beginning of the new Employee ID
        employee_id = f"EMP{new_id}"
        first = self.first_entry.get()
        middle = self.middle_entry.get()
        last = self.last_entry.get()
        address = self.Address_entry.get()
        city = self.City_entry.get()
        state = self.State_entry.get()
        zip_code = self.Zip_entry.get()
        phone = self.contact_entry.get()
        email = self.Email_entry.get()
        username = uid

        # hash the password
        hashed_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        # check if the contact already exists in the database
        cursor.execute("SELECT Phone_Number FROM EmployeeInformation WHERE Phone_Number = %s",
                       (self.contact_entry.get(),))
        result = cursor.fetchone()

        if result is not None:
            tkinter.messagebox.showinfo("Error", " Contact already exists.")
            return
        cursor.execute(
            "INSERT INTO EmployeeInformation (Employee_ID, First_Name, Middle_Name, Last_Name, Address, City, State, ZipCode, Phone_Number, Username, Password, Email_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (employee_id, first, middle, last, address, city, state, zip_code, phone, username, hashed_password, email)
            )

        tkinter.messagebox.showinfo("UserID", uid)
        # add the new user to the database

        mydb.commit()
        mydb.close()

        # switch to login page
        self.main_window.destroy()

    def back(self):
        # switch to login page
        self.main_window.destroy()


if __name__ == "__main__":
    mm = Manager()