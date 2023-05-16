# LOGIN PAGE
class LoginPage:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.attributes('-fullscreen', True)
        self.main_window.title("Pizza Billing System - Login")

        img222 = Image.open("LOGIN.jpg")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        img222 = img222.resize((screen_width, screen_height))
        self.BGG = ImageTk.PhotoImage(img222)
        self.imageL = tk.Label(self.main_window, image=self.BGG)
        self.imageL.place(x=0, y=0)
######## Main Label
        self.store_label = tk.Label(self.main_window, text="The Charcoal Pizza Store", font=("Times New Roman", 54, "bold"),bg="grey")
        self.store_label.place(relx=0.25,rely=0.01)

        self.top_frame = tk.Frame(self.main_window, highlightthickness=2, highlightbackground="black",bg="grey")
        self.middle_frame = tk.Frame(self.main_window, highlightthickness=2, highlightbackground="black",bg="grey")
        self.bottom_frame = tk.Frame(self.main_window, highlightthickness=2, highlightbackground="black",bg="grey")
        self.BBottom_frame = tk.Frame(self.main_window, highlightthickness=2, highlightbackground="black",bg="grey")
        # create username label and entry
        self.username_label = tk.Label(self.top_frame, text="Username:", font=("Arial", 15, "bold"),bg="grey")
        self.username_label.pack(side="left", pady=10)
        self.username_entry = tk.Entry(self.top_frame, font=("Arial", 15, "bold"))
        self.username_entry.pack(side="left", pady=10)
        # create password label and entry
        self.password_label = tk.Label(self.middle_frame, text="Password:", font=("Arial", 15, "bold"),bg="grey")
        self.password_label.pack(side="left", pady=10)
        self.password_entry = tk.Entry(self.middle_frame, show="*", font=("Arial", 15, "bold"))
        self.password_entry.pack(side="left", pady=10)
        ##Admin
        self.admin_button = tk.Button(self.BBottom_frame, text="AdminLogin", height=2, width=20, bg="grey",
                                      font=("Arial", 15, "bold"), command=self.adminlogin)
        self.admin_button.pack()
        # create login button
        self.login_button = tk.Button(self.bottom_frame, text="Login", height=2, width=20, bg="grey",
                                      font=("Arial", 15, "bold"), command=self.login)
        self.login_button.grid(row=0, column=0, padx=(0, 0))  # add extra padding to the right
        # create signup button
        self.signup_button = tk.Button(self.bottom_frame, text="Sign Up", height=2, width=20, bg="grey",
                                       font=("Arial", 15, "bold"), command=self.signup)
        self.signup_button.grid(row=0, column=1, padx=(0, 0))  # add extra padding to the left
        ## Packing the frmes
        self.top_frame.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.middle_frame.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.bottom_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.BBottom_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        ##close BUtton
        self.close_button = tk.Button(self.main_window, text="Close", command=self.close, width=10, fg="white",
                                     font=("Arial", 15, "bold"),bg="red")
        self.close_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

        tk.mainloop()

    def close(self):  ## closing the application
        self.main_window.destroy()

    def adminlogin(self):
        # check if username and password match with stored credentials
        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()

        # fetch stored credentials from the database
        cursor.execute("SELECT Username, Password FROM EmployeeInformation")
        stored_credentials = cursor.fetchall()

        entered_username = self.username_entry.get()
        entered_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        for username, password in stored_credentials:
            if username == entered_username and password == entered_password:
                cursor.execute(
                    "SELECT employee_id,(Last_Name || ', ' || First_Name || ' ' || Middle_Name)AS full_name FROM EmployeeInformation WHERE Username=?",
                    (username,))
                result = cursor.fetchone()
                employee_id = result[0]
                full_name = result[1]
                # if username and password match, go to main menu
                self.main_window.destroy()
                EmpMenu(employee_id, full_name)
                return
        # if username and password do not match, show error message
        error_message = tk.Label(self.main_window, text="Error: Invalid username or password.")
        error_message.pack()

        conn.close()

    def login(self):
        # check if username and password match with stored credentials
        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()

        # fetch stored credentials from the database
        cursor.execute("SELECT Username, Password FROM CustomersInformation")
        stored_credentials = cursor.fetchall()

        entered_username = self.username_entry.get()
        entered_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        for username, password in stored_credentials:
            if username == entered_username and password == entered_password:
                cursor.execute(
                    "SELECT Customer_ID,(Last_Name || ', ' || First_Name || ' ' || Middle_Name)AS full_name FROM CustomersInformation WHERE Username=?",
                    (username,))
                result = cursor.fetchone()
                customer_id = result[0]
                full_name = result[1]
                # if username and password match, go to main menu
                self.main_window.destroy()
                MainMenu(customer_id, full_name)
                return
        # if username and password do not match, show error message
        error_message = tk.Label(self.main_window, text="Error: Invalid username or password.")
        error_message.pack()

        conn.close()

    def signup(self):
        self.main_window.destroy()
        SignUpPage()


class SignUpPage:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Pizza Billing System - Sign Up")
        self.main_window.attributes('-fullscreen', True)

        img222 = Image.open("LOGIN.jpg")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        img222 = img222.resize((screen_width, screen_height))
        self.BGG = ImageTk.PhotoImage(img222)
        self.imageL = tk.Label(self.main_window, image=self.BGG)
        self.imageL.place(x=0, y=0)

        frame_width = 500
        frame_height = 700
        self.signup_frame = tk.Frame(self.main_window, width=frame_width, height=frame_height, highlightthickness=2,
                                     highlightbackground="black",bg="grey")
        self.signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        self.store_label = tk.Label(self.main_window, text="Registration", font=("Times New Roman", 64, "bold"),
                                    bg="grey")
        self.store_label.place(relx=0.35,rely=0.01)
        ## creating first name last name contact
        self.first_label = tk.Label(self.signup_frame, text="First Name:", font=("Arial", 12,"bold"),bg="grey")
        self.first_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.first_label.grid(row=0, column=0, pady=10)
        self.first_entry.grid(row=0, column=1, pady=10)

        self.middle_label = tk.Label(self.signup_frame, text="Middle Name:", font=("Arial", 12,"bold"),bg="grey")
        self.middle_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.middle_label.grid(row=1, column=0, pady=10)
        self.middle_entry.grid(row=1, column=1, pady=10)

        self.last_label = tk.Label(self.signup_frame, text="Last Name:", font=("Arial", 12,"bold"),bg="grey")
        self.last_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.last_label.grid(row=2, column=0, pady=10)
        self.last_entry.grid(row=2, column=1, pady=10)

        self.contact_label = tk.Label(self.signup_frame, text="Contact Number:", font=("Arial", 12,"bold"),bg="grey")
        self.contact_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.contact_label.grid(row=3, column=0, pady=10)
        self.contact_entry.grid(row=3, column=1, pady=10)

        # create Adress label and entry
        self.Address_label = tk.Label(self.signup_frame, text="Address:", font=("Arial", 12,"bold"),bg="grey")
        self.Address_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.Address_label.grid(row=4, column=0, pady=10)
        self.Address_entry.grid(row=4, column=1, pady=10)

        self.State_label = tk.Label(self.signup_frame, text="State:", font=("Arial", 12,"bold"),bg="grey")
        self.State_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.State_label.grid(row=5, column=0, pady=10)
        self.State_entry.grid(row=5, column=1, pady=10)

        self.City_label = tk.Label(self.signup_frame, text="City:", font=("Arial", 12,"bold"),bg="grey")
        self.City_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.City_label.grid(row=6, column=0, pady=10)
        self.City_entry.grid(row=6, column=1, pady=10)

        self.Zip_label = tk.Label(self.signup_frame, text="ZipCode:", font=("Arial", 12,"bold"),bg="grey")
        self.Zip_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.Zip_label.grid(row=7, column=0, pady=10)
        self.Zip_entry.grid(row=7, column=1, pady=10)

        self.Email_label = tk.Label(self.signup_frame, text="Email:", font=("Arial", 12,"bold"),bg="grey")
        self.Email_entry = tk.Entry(self.signup_frame, font=("Arial", 12))
        self.Email_label.grid(row=8, column=0, pady=10)
        self.Email_entry.grid(row=8, column=1, pady=10)

        # create password label and entry
        self.password_label = tk.Label(self.signup_frame, text="Password:", font=("Arial", 12,"bold"),bg="grey")
        self.password_entry = tk.Entry(self.signup_frame, show="*", font=("Arial", 12))
        self.password_label.grid(row=9, column=0, pady=10)
        self.password_entry.grid(row=9, column=1, pady=10)

        # create confirm password label and entry
        self.confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:", font=("Arial", 12,"bold"),bg="grey")
        self.confirm_password_entry = tk.Entry(self.signup_frame, show="*", font=("Arial", 12))
        self.confirm_password_label.grid(row=10, column=0, pady=10)
        self.confirm_password_entry.grid(row=10, column=1, pady=10)

        # create signup button
        self.signup_button = tk.Button(self.signup_frame, text="Sign Up", command=self.signup, width=10,
                                       fg="black", font=("Arial", 15, "bold"),bg="grey")
        self.signup_button.grid(row=11, column=0, columnspan=2, pady=10)

        # create back button
        self.back_button = tk.Button(self.main_window, text="Back", command=self.back, width=10, fg="white",
                                     font=("Arial", 15, "bold"),bg="red")
        self.back_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)



        tk.mainloop()

    #         self.main_window.mainloop()

    def signup(self):

        first = self.first_entry.get().lower()
        middle = self.middle_entry.get().lower()
        last = self.last_entry.get().lower()
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
        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()
        select_stmt = "SELECT COUNT(last_name) FROM customersinformation WHERE Last_Name like ?"
        cursor.execute(select_stmt, (pattern,))
        num = cursor.fetchone()[0]
        print('num: ', num)
        uid = first_p.lower() + str(num + 1) + fi + mi
        if self.password_entry.get() != self.confirm_password_entry.get():
            error_message = tk.Label(self.main_window, text="Error: Passwords do not match.")
            error_message.grid(row=4, column=0, columnspan=2)
            return

        #######
        # Query the database for the highest existing customer ID
        cursor.execute("SELECT MAX(Customer_ID) FROM CustomersInformation")
        max_id = cursor.fetchone()[0]
        if max_id is None:
            # If there are no existing customers, start the customer ID sequence at 1
            max_id = 0
        else:
            # Convert the max_id value to an integer
            max_id = int(max_id.replace("CUS", ""))

        # Increment the highest customer ID to generate a new unique customer ID
        new_id = max_id + 1

        # Add "CUS" back to the beginning of the new customer ID
        customer_id = f"CUS{new_id}"
        first = self.first_entry.get().lower()
        middle = self.middle_entry.get().lower()
        last = self.last_entry.get().lower()
        address = self.Address_entry.get().lower()
        city = self.City_entry.get().lower()
        state = self.State_entry.get().lower()
        zip_code = self.Zip_entry.get().lower()
        phone = self.contact_entry.get().lower()
        email = self.Email_entry.get().lower()
        username = uid

        # hash the password
        hashed_password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

        # check if the contact already exists in the database
        cursor.execute("SELECT Phone_Number FROM CustomersInformation WHERE Phone_Number = ?",
                       (self.contact_entry.get(),))
        result = cursor.fetchone()
        if result is not None:
            tkinter.messagebox.showinfo("Error", " Contact already exists.")
            return
        # check if the Email already exists in the database
        cursor.execute("SELECT Email_ID FROM CustomersInformation WHERE Email_ID = ?",
                       (self.Email_entry.get().lower(),))
        result1 = cursor.fetchone()
        if result1 is not None:
            tkinter.messagebox.showinfo("Error", " E-mail already exists.")
            return

        cursor.execute(
            "INSERT INTO CustomersInformation (Customer_ID, First_Name, Middle_Name, Last_Name, Address, City, State, ZipCode, Phone_Number, Username, Password, Email_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (customer_id, first, middle, last, address, city, state, zip_code, phone, username, hashed_password, email)
        )
        ### Sending confirmation E-mail
        # send confirmation email to user
        sender_email = "friendscmu2022@gmail.com"
        receiver_email = self.Email_entry.get()
        password = "oznhefehqurvpmjz"
        message = f"Thank you for signing up! Your details:\n\nName: {first} {middle} {last} \nContact Number: {phone}\nAddress:{address}\n{city}\n{zip_code}\n{state}\n\nCustomer-ID: {customer_id}\nUserName: {username} \n Password: {self.password_entry.get()}"
        msg = MIMEText(message)
        msg['Subject'] = 'Confirmation of Sign Up'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        # add the new user to the database

        conn.commit()
        conn.close()

        # Showing a top up message of details using showmessage function
        title = "Registered Successfully"
        message = (
            f"You account has been created successfully and Your login details are mailed to: {self.Email_entry.get()}\n\n"
            f"Thank you for registering with Pizza Restaurant! We are excited to have you as part of our family.\n"
            f"We look forward to serving you soon!"

        )

        font = ("Arial", 12, "bold")
        self.show_custom_messagebox(title, message, font)

    def show_custom_messagebox(self, title, message, font):
        custom_box = tk.Toplevel()
        custom_box.title(title)

        # create label widget to display message
        message_label = tk.Label(custom_box, text=message, font=font)
        message_label.pack(padx=20, pady=20)

        # create ok button to close message box
        ok_button = tk.Button(custom_box, text="OK",
                              command=lambda: [custom_box.destroy(), self.main_window.destroy(), LoginPage()])
        ok_button.pack(padx=10, pady=10)

        custom_box.mainloop()

    def back(self):
        # switch to login page
        self.main_window.destroy()
        LoginPage()


#########VEG
#########VEG#########VEG#########VEG
#########VEG#########VEG#########VEG#########VEG
#########VEG#########VEG#########VEG#########VEG#########VEG
#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG
#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG
#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG
#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG#########VEG
class VegMenu:
    def __init__(self, parent, pizzasV, pizzasVL, Cart, id, name):
        self.parent = parent
        self.main_window = tk.Toplevel(self.parent)

        self.pizzasV = pizzasV
        self.pizzasVL = pizzasVL
        self.id = id
        self.name = name

        self.main_window.attributes('-fullscreen', True)
        self.main_window.title("Pizza Billing System - Vegetarian Pizzas")
        self.cart = Cart
        ## BacgGround Image
        img222 = Image.open("PIZZA.jpeg")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        img222 = img222.resize((screen_width, screen_height))
        self.BGG = ImageTk.PhotoImage(img222)
        self.imageL = tk.Label(self.main_window, image=self.BGG)
        self.imageL.place(x=0, y=0)

        ## Creting Frames and Main Label to load the pizza data
        # Adding Heading with Animation from left to middle top of screen
        self.veg_label = tk.Label(self.main_window, text="Vegetarian Pizzas Menu", font=("Arial", 32, "bold"),bg="#3e4c4f")
        self.veg_label.place(x=-500, y=-200)

        # Animate the veg label to slide in from the left to the center of the window
        def slide_in():
            x = self.veg_label.winfo_x()
            if x < (screen_width / 2) - 250:
                self.veg_label.place(x=x + 10, y=0.9)
                self.main_window.after(10, slide_in)

        slide_in()

        self.regular_frame = tk.LabelFrame(self.main_window, text="Vegetarian Pizzas", font=("Arial", 20, "bold"),
                                           relief='flat',bg="#3e4c4f")
        self.regular_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

###LOADING IMAGES PIZZA
        images = []  # create an empty list to store the images

        cheese = Image.open("cheesepizza.png")
        cheese = cheese.resize((200, 200))  # fix the size argument to a tuple
        cheese_image = ImageTk.PhotoImage(cheese)
        images.append(cheese_image)

        spa = Image.open("spa.jpeg")
        spa = spa.resize((200, 200))  # fix the size argument to a tuple
        spa_image = ImageTk.PhotoImage(spa)
        images.append(spa_image)

        mrrom = Image.open("mrrom.png")
        mrrom = mrrom.resize((200, 200))  # fix the size argument to a tuple
        mrrom_image = ImageTk.PhotoImage(mrrom)
        images.append(mrrom_image)

        grillv = Image.open("grillv.png")
        grillv = grillv.resize((200, 200))  # fix the size argument to a tuple
        grillv_image = ImageTk.PhotoImage(grillv)
        images.append(grillv_image)

        # Create pizza frames for each pizza
        for pizza,image,pizza1 in zip(self.pizzasV,images,self.pizzasVL):
            self.create_pizza_reg_frame(pizza,image,pizza1)
        self.cart_button = tk.Button(self.main_window, text="View Cart", command=lambda: self.view_cart(), width=10,
                                     bg="green", fg="white", font=("Arial", 15, "bold"))
        self.cart_button.place(relx=0.85, rely=0.92, anchor=tk.E)
        self.add_more_button = tk.Button(self.main_window, text="Add More", command=self.add_more, width=10, bg="green",
                                         fg="white", font=("Arial", 15, "bold"))
        self.add_more_button.place(relx=0.95, rely=0.92, anchor=tk.E)

        tk.mainloop()

    def add_more(self):
        self.main_window.destroy()

    def create_pizza_reg_frame(self, pizza,image,pizza1):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.regular_frame, highlightthickness=5,
                               highlightbackground="black",bg="#3e4c4f",relief='sunken')
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20)
        ## Loading Images
        img_lbl=tk.Label(pizza_frame,image=image)
        img_lbl.pack()
        # Add the pizza name label
        pizza_name_label = tk.Label(pizza_frame, text=pizza.name, font=("Ariel", 18, "bold"), background="#2e8b57")
        pizza_name_label.pack()
        pizza1_frame = tk.Frame(pizza_frame,bg="#3e4c4f",relief='sunken')
        pizza1_frame.pack(side="left",padx=10,pady=10,ipadx=10,anchor="center")
        pizza2_frame = tk.Frame(pizza_frame,bg="#3e4c4f",relief='sunken')
        pizza2_frame.pack(side="right",padx=10,pady=10,ipadx=10,anchor="center")
        # Add the pizza price label
        pizza_price_label = tk.Label(pizza1_frame, text="${:.2f}".format(pizza.price),font=("Ariel", 14, "bold"),bg="#3e4c4f")
        pizza_price_label.pack(side="top")
        # # Add the pizza price label
        pizza1_price_label = tk.Label(pizza2_frame, text="${:.2f}".format(pizza1.price), font=("Ariel", 14, "bold"),
                                     bg="#3e4c4f")
        pizza1_price_label.pack(side="top")
        # Add the "Add to Cart" button

        add_to_cart_button = tk.Button(pizza1_frame, text="Regular", command=lambda: self.add_to_cart(pizza),
                                       font=("Ariel", 15, "bold"),bg="#2e8b57",fg="white",relief="flat")
        add_to_cart_button.pack(side="bottom",anchor="center")

        add1_to_cart_button = tk.Button(pizza2_frame, text="Large", command=lambda: self.add_to_cart(pizza1),
                                       font=("Ariel", 15, "bold"), bg="#2e8b57", fg="white", relief="flat")
        add1_to_cart_button.pack(side="bottom",anchor="center")


    # def create_pizza_large_frame(self, pizza,image):
    #     # Create a frame for the pizza
    #     pizza_frame = tk.Frame(self.large_frame, width=300, height=200, highlightthickness=2,
    #                            highlightbackground="black",bg="#3e4c4f")
    #     pizza_frame.pack(side=tk.LEFT, padx=20, pady=20)
    #     img_lbl = tk.Label(pizza_frame, image=image)
    #     img_lbl.pack()
    #     # Add the pizza name label
    #     pizza_name_label = tk.Label(pizza_frame, text=pizza.name, font=("Ariel", 20, "bold"), background="#2e8b57")
    #     pizza_name_label.pack()
    #     # Add the pizza price label
    #     pizza_price_label = tk.Label(pizza_frame, text="${:.2f}".format(pizza.price), font=("Ariel", 14, "bold"),
    #                                  bg="#3e4c4f")
    #     pizza_price_label.pack()
    #     # Add the pizza quantity options
    #
    #     # Add the "Add to Cart" button
    #     add_to_cart_button = tk.Button(pizza_frame, text="Add to Cart", command=lambda: self.add_to_cart(pizza),
    #                                    font=("Ariel", 14, "bold"), bg="#2e8b57",fg="white",relief="flat")
    #     add_to_cart_button.pack()

    def add_to_cart(self, pizza):
        pizza_price = pizza.price
        # Create a new Pizza object with the selected size and price
        selected_pizza = Pizza(pizza.id, pizza.name, pizza_price, pizza.type, pizza.size)
        selected_pizza.quantity.set(pizza.quantity.get())
        # Check if the pizza already exists in the cart
        for item in self.cart.items:
            if item.id == selected_pizza.id:
                # Update the quantity of the existing pizza item
                item.quantity.set(item.quantity.get() + selected_pizza.quantity.get())
                break
        else:
            # Add the pizza copy to the cart
            self.cart.add_item(selected_pizza)

    def view_cart(self):
        # Create a new window for the cart
        self.cart_window = tk.Toplevel(self.main_window)
        self.cart_window.title("View Cart")
        frame = tk.Frame(self.cart_window).place(relx=0.00, rely=0.00)
        # Add a label for the cart items
        cart_items_label = tk.Label(self.cart_window, text="Cart Items", font=("default", 16, "bold"))
        cart_items_label.pack()

        # Add a frame for the cart items
        cart_items_frame = tk.Frame(self.cart_window)
        cart_items_frame.pack()
        self.cart_items_frame = cart_items_frame

        # Add a label for the cart total
        self.cart_total_label = tk.Label(self.cart_window, text="Total: ${:.2f}".format(self.get_cart_total()),
                                         font=("default", 16))
        self.cart_total_label.pack()

        # Add a "Checkout" button
        checkout_button = tk.Button(self.cart_window, text="Checkout", command=self.checkout, width=10, bg="green",
                                    fg="white", font=("Arial", 10, "bold"))
        checkout_button.pack(pady=10)

        # Add a label and Spinbox for each pizza item in the cart
        for i, pizza in enumerate(self.cart.get_items()):
            # Create a frame to hold the product label and Spinbox
            product_frame = tk.Frame(cart_items_frame,bg="white")
            product_frame.grid(row=i, column=0, sticky='w',pady=10)

            product_frame1 = tk.Frame(cart_items_frame,bg="white")
            product_frame1.grid(row=i, column=2, sticky='w',pady=10)

            pizza.product_frame = product_frame
            pizza.product_frame1 = product_frame1

            # Add a label for the product name, type, and size
            product_label = tk.Label(product_frame, text="{} ({} {})".format(pizza.name, pizza.type, pizza.size),
                                     font=('Ariel', 15, "bold"),bg="white")
            product_label.grid(row=0, column=0, sticky='w')

            # Add a Spinbox for the product quantity
            quantity_spinbox = tk.Spinbox(product_frame1, from_=1, to=10, width=5, textvariable=pizza.quantity,
                                          command=lambda: self.update_cart_total(), font=('Ariel', 15, "bold"))
            quantity_spinbox.grid(row=0, column=7, padx=(10, 0))

            # Add a label for the product price
            price_label = tk.Label(product_frame, text="${:.2f}".format(pizza.price * int(pizza.quantity.get())),
                                   font=('Ariel', 15, "bold"),bg="white")
            price_label.grid(row=0, column=8, padx=(10, 0))

            # Add a "Remove" button for the pizza item
            remove_button = tk.Button(product_frame1, text="Remove",
                                      command=lambda pizza_item=pizza: self.remove_from_cart(pizza_item),
                                      font=('Ariel', 15, "bold"))
            remove_button.grid(row=0, column=9, padx=(10, 0))

            # Add the price label to the pizza item for later use
            pizza.price_label = price_label


    def update_cart_total(self):
        # Update the price labels for each pizza item in the cart
        for pizza in self.cart.get_items():
            pizza.price_label.config(text="${:.2f}".format(pizza.price * int(pizza.quantity.get())))

        # Update the cart total label with the new total
        self.cart_total_label.config(text="Total: ${:.2f}".format(self.get_cart_total()))

    def remove_from_cart(self, pizza_item):
        # Check if the pizza item is in the items list
        if pizza_item in self.cart.items:
            # Remove the pizza item from the cart's items list
            self.cart.items.remove(pizza_item)
            # Update the cart items and total labels
            self.update_cart_total()
            # Destroy the product frames associated with the pizza item
            pizza_item.product_frame.destroy()
            pizza_item.product_frame1.destroy()

    def get_cart_total(self):
        return self.cart.get_total()

    def checkout(self):
        checkout_window = Checkout(self.main_window, self.cart, self.id)


### NON VEG
### NON VEG### NON VEG### NON VEG
### NON VEG### NON VEG### NON VEG### NON VEG
### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG
### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG
### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG### NON VEG
### NON VEG
class NonVegMenu:
    def __init__(self, parent, pizzasNV, pizzasNVL, Cart, id, name):
        self.parent = parent
        self.main_window = tk.Toplevel(self.parent)

        self.pizzasNV = pizzasNV
        self.pizzasNVL = pizzasNVL
        self.id = id
        self.name = name

        self.main_window.attributes('-fullscreen', True)
        self.main_window.title("Pizza Billing System - Non-Vegetarian Pizzas")
        self.cart = Cart
        ## BacgGround Image
        img222 = Image.open("PIZZA.jpeg")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        img222 = img222.resize((screen_width, screen_height))
        self.BGG = ImageTk.PhotoImage(img222)
        self.imageL = tk.Label(self.main_window, image=self.BGG)
        self.imageL.place(x=0, y=0)

        ## Creting Frames and Main Label to load the pizza data
        # Adding Heading with Animation from left to middle top of screen
        self.veg_label = tk.Label(self.main_window, text="Non-Vegetarian Pizzas Menu", font=("Arial", 32, "bold"),bg="#3e4c4f")
        self.veg_label.place(x=-500, y=-200)

        # Animate the veg label to slide in from the left to the center of the window
        def slide_in():
            x = self.veg_label.winfo_x()
            if x < (screen_width / 2) - 250:
                self.veg_label.place(x=x + 10, y=0.1)
                self.main_window.after(10, slide_in)

        slide_in()

        self.regular_frame = tk.LabelFrame(self.main_window, text="Regular Pizzas", font=("Arial", 25, "bold"),
                                           relief='flat',bg="#3e4c4f")
        self.regular_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.large_frame = tk.LabelFrame(self.main_window, text="Large Pizzas", font=("Arial", 25, "bold"),
                                         relief='flat',bg="#3e4c4f")
        self.large_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Create pizza frames for each pizza
        for pizza in self.pizzasNV:
            self.create_pizza_reg_frame(pizza)

        for pizza in self.pizzasNVL:
            self.create_pizza_large_frame(pizza)
        # Add a "View Cart" button at the bottom of the window
        self.cart_button = tk.Button(self.main_window, text="View Cart", command=lambda: self.view_cart(), width=10,
                                     bg="green", fg="white", font=("Arial", 15, "bold"))
        self.cart_button.place(relx=0.85, rely=0.92, anchor=tk.E)
        self.add_more_button = tk.Button(self.main_window, text="Add More", command=self.add_more, width=10, bg="green",
                                         fg="white", font=("Arial", 15, "bold"))
        self.add_more_button.place(relx=0.95, rely=0.92, anchor=tk.E)

        tk.mainloop()

    def add_more(self):
        self.main_window.destroy()

    def create_pizza_reg_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.regular_frame, width=300, height=200, highlightthickness=2,
                               highlightbackground="black",bg="#3e4c4f")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20)
        # Add the pizza name label
        pizza_name_label = tk.Label(pizza_frame, text=pizza.name, font=("default", 20, "bold"), background="#b22222")
        pizza_name_label.pack()
        # Add the pizza price label
        pizza_price_label = tk.Label(pizza_frame, text="${:.2f}".format(pizza.price), font=("Ariel", 16, "bold"),bg="#3e4c4f")
        pizza_price_label.pack()
        # Add the pizza quantity options
        quantity_label = tk.Label(pizza_frame, text="Quantity:",font=("Ariel", 16, "bold"),bg="#3e4c4f")
        quantity_label.pack()
        quantity_spinbox = tk.Spinbox(pizza_frame, from_=1, to=10, width=3, textvariable=pizza.quantity,font=("Ariel", 16, "bold"))
        quantity_spinbox.pack()
        # Add the "Add to Cart" button
        add_to_cart_button = tk.Button(pizza_frame, text="Add to Cart", command=lambda: self.add_to_cart(pizza),
                                       font=("Ariel", 16, "bold"), bg="#b22222", fg="white", relief="flat")
        add_to_cart_button.pack()

    def create_pizza_large_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.large_frame, width=300, height=200, highlightthickness=2,
                               highlightbackground="black",bg="#3e4c4f")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20)
        # Add the pizza name label
        pizza_name_label = tk.Label(pizza_frame, text=pizza.name, font=("default", 20, "bold"), background="#b22222")
        pizza_name_label.pack()

        # Add the pizza price label
        pizza_price_label = tk.Label(pizza_frame, text="${:.2f}".format(pizza.price), font=("Ariel", 16, "bold"),bg="#3e4c4f")
        pizza_price_label.pack()
        # Add the pizza quantity options
        quantity_label = tk.Label(pizza_frame, text="Quantity:",font=("Ariel", 16, "bold"),bg="#3e4c4f")
        quantity_label.pack()
        quantity_spinbox = tk.Spinbox(pizza_frame, from_=1, to=10, width=3, textvariable=pizza.quantity,font=("Ariel", 16, "bold"))
        quantity_spinbox.pack()
        # Add the "Add to Cart" button
        add_to_cart_button = tk.Button(pizza_frame, text="Add to Cart", command=lambda: self.add_to_cart(pizza),
                                       font=("Ariel", 16, "bold"), bg="#b22222", fg="white", relief="flat")
        add_to_cart_button.pack()

    def add_to_cart(self, pizza):
        pizza_price = pizza.price
        # Create a new Pizza object with the selected size and price
        selected_pizza = Pizza(pizza.id, pizza.name, pizza_price, pizza.type, pizza.size)
        selected_pizza.quantity.set(pizza.quantity.get())
        # Check if the pizza already exists in the cart
        for item in self.cart.items:
            if item.id == selected_pizza.id:
                # Update the quantity of the existing pizza item
                item.quantity.set(item.quantity.get() + selected_pizza.quantity.get())
                break
        else:
            # Add the pizza copy to the cart
            self.cart.add_item(selected_pizza)

    def view_cart(self):
        # Create a new window for the cart
        self.cart_window = tk.Toplevel(self.main_window)
        self.cart_window.title("View Cart")
        frame = tk.Frame(self.cart_window).place(relx=0.00, rely=0.00)
        # Add a label for the cart items
        cart_items_label = tk.Label(self.cart_window, text="Cart Items", font=("default", 16, "bold"))
        cart_items_label.pack()

        # Add a frame for the cart items
        cart_items_frame = tk.Frame(self.cart_window)
        cart_items_frame.pack()
        self.cart_items_frame = cart_items_frame

        # Add a label for the cart total
        self.cart_total_label = tk.Label(self.cart_window, text="Total: ${:.2f}".format(self.get_cart_total()),
                                         font=("default", 16))
        self.cart_total_label.pack()

        # Add a "Checkout" button
        checkout_button = tk.Button(self.cart_window, text="Checkout", command=self.checkout, width=10, bg="green",
                                    fg="white", font=("Arial", 10, "bold"))
        checkout_button.pack(pady=10)

        # Add a label and Spinbox for each pizza item in the cart
        for i, pizza in enumerate(self.cart.get_items()):
            # Create a frame to hold the product label and Spinbox
            product_frame = tk.Frame(cart_items_frame, bg="white")
            product_frame.grid(row=i, column=0, sticky='w', pady=10)

            product_frame1 = tk.Frame(cart_items_frame, bg="white")
            product_frame1.grid(row=i, column=2, sticky='w', pady=10)

            pizza.product_frame = product_frame
            pizza.product_frame1 = product_frame1

            # Add a label for the product name, type, and size
            product_label = tk.Label(product_frame, text="{} ({} {})".format(pizza.name, pizza.type, pizza.size),
                                     font=('Ariel', 15, "bold"), bg="white")
            product_label.grid(row=0, column=0, sticky='w')

            # Add a Spinbox for the product quantity
            quantity_spinbox = tk.Spinbox(product_frame1, from_=1, to=10, width=5, textvariable=pizza.quantity,
                                          command=lambda: self.update_cart_total(), font=('Ariel', 15, "bold"))
            quantity_spinbox.grid(row=0, column=7, padx=(10, 0))

            # Add a label for the product price
            price_label = tk.Label(product_frame, text="${:.2f}".format(pizza.price * int(pizza.quantity.get())),
                                   font=('Ariel', 15, "bold"), bg="white")
            price_label.grid(row=0, column=8, padx=(10, 0))

            # Add a "Remove" button for the pizza item
            remove_button = tk.Button(product_frame1, text="Remove",
                                      command=lambda pizza_item=pizza: self.remove_from_cart(pizza_item),
                                      font=('Ariel', 15, "bold"))
            remove_button.grid(row=0, column=9, padx=(10, 0))

            # Add the price label to the pizza item for later use
            pizza.price_label = price_label

    def update_cart_total(self):
        # Update the price labels for each pizza item in the cart
        for pizza in self.cart.get_items():
            pizza.price_label.config(text="${:.2f}".format(pizza.price * int(pizza.quantity.get())))

        # Update the cart total label with the new total
        self.cart_total_label.config(text="Total: ${:.2f}".format(self.get_cart_total()))

    def remove_from_cart(self, pizza_item):
        # Check if the pizza item is in the items list
        if pizza_item in self.cart.items:
            # Remove the pizza item from the cart's items list
            self.cart.items.remove(pizza_item)
            # Update the cart items and total labels
            self.update_cart_total()
            # Destroy the product frames associated with the pizza item
            pizza_item.product_frame.destroy()
            pizza_item.product_frame1.destroy()

    def get_cart_total(self):
        return self.cart.get_total()

    def checkout(self):
        checkout_window = Checkout(self.main_window, self.cart, self.id)


## BEV Sides
## BEV Sides## BEV Sides## BEV Sides
## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides
## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides
## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides## BEV Sides
## BEV Sides
class BevSideMenu:
    def __init__(self, parent, bev, sides, Cart, id, name):
        self.parent = parent
        self.main_window = tk.Toplevel(self.parent)

        self.bev = bev
        self.sides = sides
        self.id = id
        self.name = name
        self.main_window.attributes('-fullscreen',True)

        self.main_window.title("Pizza Billing System - Beverages & Sides")
        self.cart = Cart

        ## BacgGround Image
        img222 = Image.open("PIZZA.jpeg")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        img222 = img222.resize((screen_width, screen_height))
        self.BGG = ImageTk.PhotoImage(img222)
        self.imageL = tk.Label(self.main_window, image=self.BGG)
        self.imageL.place(x=0, y=0)

        ## Creting Frames and Main Label to load the pizza data
        # Adding Heading with Animation from left to middle top of screen
        self.veg_label = tk.Label(self.main_window, text="Beverages & Sides Menu", font=("Arial", 32, "bold"),bg="#3e4c4f")
        self.veg_label.place(x=-500, y=-200)

        # Animate the veg label to slide in from the left to the center of the window
        def slide_in():
            x = self.veg_label.winfo_x()
            if x < (screen_width / 2) - 250:
                self.veg_label.place(x=x + 10, y=0.1)
                self.main_window.after(10, slide_in)

        slide_in()

        self.bev_frame = tk.LabelFrame(self.main_window, text="Beverages", font=("Arial", 25, "bold"),
                                           relief='flat',bg="#3e4c4f")
        self.bev_frame.place(relx=0.55, rely=0.3, anchor=tk.CENTER)

        self.sides_frame = tk.LabelFrame(self.main_window, text="Sides", font=("Arial", 25, "bold"), relief='flat',bg="#3e4c4f")
        self.sides_frame.place(relx=0.54, rely=0.7, anchor=tk.CENTER)

        # Create pizza frames for each pizza
        for pizza in self.bev:
            self.create_bev_frame(pizza)

        colors = ["#2e8b57", "#2e8b57", "#b22222", "#612D08"]
        for pizza, color in zip(self.sides, colors):
            self.create_sides_frame(pizza, color)
        # Add a "View Cart" button at the bottom of the window
        self.cart_button = tk.Button(self.main_window, text="View Cart", command=lambda: self.view_cart(), width=10,
                                     bg="green", fg="white", font=("Arial", 15, "bold"))
        self.cart_button.place(relx=0.85, rely=0.92, anchor=tk.E)
        self.add_more_button = tk.Button(self.main_window, text="Add More", command=self.add_more, width=10, bg="green",
                                         fg="white", font=("Arial", 15, "bold"))
        self.add_more_button.place(relx=0.95, rely=0.92, anchor=tk.E)

        tk.mainloop()

    def add_more(self):
        self.main_window.destroy()

    def create_bev_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.bev_frame, width=300, height=200, highlightthickness=2,
                               highlightbackground="black",bg="#3e4c4f")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20)
        # Add the pizza name label
        pizza_name_label = tk.Label(pizza_frame, text=pizza.name, font=("Ariel", 20, "bold"), background="#71a6d2")
        pizza_name_label.pack()
        # Add the pizza price label
        pizza_price_label = tk.Label(pizza_frame, text="${:.2f}".format(pizza.price), font=("Ariel", 14, "bold"),bg="#3e4c4f")
        pizza_price_label.pack()
        # Add the pizza quantity options
        quantity_label = tk.Label(pizza_frame, text="Quantity:",font=("Ariel", 14, "bold"), bg="#3e4c4f")
        quantity_label.pack()
        quantity_spinbox = tk.Spinbox(pizza_frame, from_=1, to=10, width=3, textvariable=pizza.quantity,font=("Ariel", 14, "bold"))
        quantity_spinbox.pack()
        # Add the "Add to Cart" button
        add_to_cart_button = tk.Button(pizza_frame, text="Add to Cart", command=lambda: self.add_to_cart(pizza),
                                       font=("Ariel", 14, "bold"),bg="#71a6d2",fg="white",relief="flat")
        add_to_cart_button.pack()

    def create_sides_frame(self, pizza, color):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.sides_frame, width=300, height=200, highlightthickness=2,
                               highlightbackground="black",bg="#3e4c4f")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20)
        # Add the pizza name label
        pizza_name_label = tk.Label(pizza_frame, text=pizza.name, font=("Ariel", 20, "bold"), background=color)
        pizza_name_label.pack()

        # Add the pizza price label
        pizza_price_label = tk.Label(pizza_frame, text="${:.2f}".format(pizza.price), font=("Ariel", 14, "bold"),bg="#3e4c4f")
        pizza_price_label.pack()
        # Add the pizza quantity options
        quantity_label = tk.Label(pizza_frame, text="Quantity:",font=("Ariel", 14, "bold"),bg="#3e4c4f")
        quantity_label.pack()
        quantity_spinbox = tk.Spinbox(pizza_frame, from_=1, to=10, width=3, textvariable=pizza.quantity,font=("Ariel", 14, "bold"))
        quantity_spinbox.pack()
        # Add the "Add to Cart" button
        add_to_cart_button = tk.Button(pizza_frame, text="Add to Cart", command=lambda: self.add_to_cart(pizza),
                                       font=("Ariel", 14, "bold"), bg=color, fg="white", relief="flat")
        add_to_cart_button.pack()

    def add_to_cart(self, pizza):
        pizza_price = pizza.price
        # Create a new Pizza object with the selected size and price
        selected_pizza = Pizza(pizza.id, pizza.name, pizza_price, pizza.type, pizza.size)
        selected_pizza.quantity.set(pizza.quantity.get())
        # Check if the pizza already exists in the cart
        for item in self.cart.items:
            if item.id == selected_pizza.id:
                # Update the quantity of the existing pizza item
                item.quantity.set(item.quantity.get() + selected_pizza.quantity.get())
                break
        else:
            # Add the pizza copy to the cart
            self.cart.add_item(selected_pizza)

    def view_cart(self):
        # Create a new window for the cart
        self.cart_window = tk.Toplevel(self.main_window)
        self.cart_window.title("View Cart")
        frame = tk.Frame(self.cart_window).place(relx=0.00, rely=0.00)
        # Add a label for the cart items
        cart_items_label = tk.Label(self.cart_window, text="Cart Items", font=("default", 16, "bold"))
        cart_items_label.pack()

        # Add a frame for the cart items
        cart_items_frame = tk.Frame(self.cart_window)
        cart_items_frame.pack()
        self.cart_items_frame = cart_items_frame

        # Add a label for the cart total
        self.cart_total_label = tk.Label(self.cart_window, text="Total: ${:.2f}".format(self.get_cart_total()),
                                         font=("default", 16))
        self.cart_total_label.pack()

        # Add a "Checkout" button
        checkout_button = tk.Button(self.cart_window, text="Checkout", command=self.checkout, width=10, bg="green",
                                    fg="white", font=("Arial", 10, "bold"))
        checkout_button.pack(pady=10)

        # Add a label and Spinbox for each pizza item in the cart
        for i, pizza in enumerate(self.cart.get_items()):
            # Create a frame to hold the product label and Spinbox
            product_frame = tk.Frame(cart_items_frame, bg="white")
            product_frame.grid(row=i, column=0, sticky='w', pady=10)

            product_frame1 = tk.Frame(cart_items_frame, bg="white")
            product_frame1.grid(row=i, column=2, sticky='w', pady=10)

            pizza.product_frame = product_frame
            pizza.product_frame1 = product_frame1

            # Add a label for the product name, type, and size
            product_label = tk.Label(product_frame, text="{} ({} {})".format(pizza.name, pizza.type, pizza.size),
                                     font=('Ariel', 15, "bold"), bg="white")
            product_label.grid(row=0, column=0, sticky='w')

            # Add a Spinbox for the product quantity
            quantity_spinbox = tk.Spinbox(product_frame1, from_=1, to=10, width=5, textvariable=pizza.quantity,
                                          command=lambda: self.update_cart_total(), font=('Ariel', 15, "bold"))
            quantity_spinbox.grid(row=0, column=7, padx=(10, 0))

            # Add a label for the product price
            price_label = tk.Label(product_frame, text="${:.2f}".format(pizza.price * int(pizza.quantity.get())),
                                   font=('Ariel', 15, "bold"), bg="white")
            price_label.grid(row=0, column=8, padx=(10, 0))

            # Add a "Remove" button for the pizza item
            remove_button = tk.Button(product_frame1, text="Remove",
                                      command=lambda pizza_item=pizza: self.remove_from_cart(pizza_item),
                                      font=('Ariel', 15, "bold"))
            remove_button.grid(row=0, column=9, padx=(10, 0))

            # Add the price label to the pizza item for later use
            pizza.price_label = price_label

    def update_cart_total(self):
        # Update the price labels for each pizza item in the cart
        for pizza in self.cart.get_items():
            pizza.price_label.config(text="${:.2f}".format(pizza.price * int(pizza.quantity.get())))

        # Update the cart total label with the new total
        self.cart_total_label.config(text="Total: ${:.2f}".format(self.get_cart_total()))

    def remove_from_cart(self, pizza_item):
        # Check if the pizza item is in the items list
        if pizza_item in self.cart.items:
            # Remove the pizza item from the cart's items list
            self.cart.items.remove(pizza_item)
            # Update the cart items and total labels
            self.update_cart_total()
            # Destroy the product frames associated with the pizza item
            pizza_item.product_frame.destroy()
            pizza_item.product_frame1.destroy()

    def get_cart_total(self):
        return self.cart.get_total()

    def checkout(self,parent):
        self.parent1=parent
        self.parent1.destroy()
        checkout_window = Checkout(self.main_window, self.cart, self.id)


# MainMenu ## Cart ## Pizza # Receipt
# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt
# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt
# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt
# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt# MainMenu ## Cart ## Pizza # Receipt


## Pizza CLass
class Pizza:
    def __init__(self, id, name, price, type, size):
        self.id = id
        self.name = name
        self.price = price
        self.type = type
        self.size = size
        self.quantity = tk.IntVar()
        self.quantity.set(1)


## Cart class
class Cart:
    def __init__(self):
        self.items = []

        self.cart_items_label = None

    def add_item(self, item):
        self.items.append(item)

        self.update_cart_items_label()

    def remove_item(self, item):
        self.items.remove(item)
        self.update_cart_items_label()

    def update_cart_items_label(self):
        if self.cart_items_label:
            self.cart_items_label.configure(text="Cart Items: {}".format(len(self.items)))

    def get_items(self):
        return self.items

    def get_total_quantity(self):
        total_quantity = 0
        for item in self.items:
            total_quantity += item.quantity.get()
        return total_quantity

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity.get()
        return total


### CUSTOMER CHECKOUT AND RECEIPT
### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT
### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT
### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT
### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT### CUSTOMER CHECKOUT AND RECEIPT
class Checkout:
    def __init__(self, parent, cart, id):
        self.parent = parent
        self.cart = cart
        self.id = id
        self.payment_method = ""  # To store the payment method option
        self.window = tk.Toplevel(self.parent)
        self.window.title("Checkout")
        self.window.geometry("400x250")

        # Add a label for the checkout total
        total_label = tk.Label(self.window, text="Total: ${:.2f}".format(self.cart.get_total()), font=("default", 16))
        total_label.pack()

        # Add the payment method options
        payment_label = tk.Label(self.window, text="Select Payment Method:", font=("default", 12))
        payment_label.pack(pady=5)
        # Add the "Cash" button
        cash_button = tk.Button(self.window, text="Cash", command=self.select_cash, width=10, bg="green",
                                fg="white", font=("Arial", 10, "bold"))
        cash_button.pack(pady=10)

        # Add the "Card" button
        card_button = tk.Button(self.window, text="Card", command=self.select_card, width=10, bg="green",
                                fg="white", font=("Arial", 10, "bold"))
        card_button.pack(pady=10)

    #         # Add the "Checkout" button
    #         checkout_button = tk.Button(self.window, text="Checkout", command=self.checkout, width=10, bg="green",
    #                                     fg="white", font=("Arial", 10, "bold"))
    #         checkout_button.pack(pady=10)

    def select_cash(self):
        self.payment_method = "Cash"
        self.checkout()

    def select_card(self):
        self.payment_method = "Card"
        self.checkout()

    def checkout(self):
        payment_method = self.payment_method
        totalitems = self.cart.get_total_quantity()
        total = self.cart.get_total()
        if total == 0:
            tk.messagebox.showerror("Error", "Your cart is empty.")
        else:
            # Connect to the database and get the highest order ID
            conn = sqlite3.connect("pizza2.db")
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(Order_ID) FROM Orders")
            result = cursor.fetchone()
            order_id = result[0] + 1 if result[0] else 1  # Increment the highest ID by one or start at 1 if the table is empty

            # Generate an invoice code based on the current time and date
            invoice_code = time.strftime("%Y%m%d%H%M%S") + str(order_id)


            tk.messagebox.showinfo("Checkout",
                                   "Thank you for your order! Your total is ${:.2f}. Your order will be ready soon.\n\nInvoice Code: {}. Your order ID is {}.".format(
                                       total, invoice_code, order_id))
            # Update the Order_Status table
            cursor.execute("INSERT INTO Order_Status (Order_ID, Order_Status) VALUES (?, ?)", (order_id, 'Pending'))

            # Insert the order into the database
            cursor.execute(
                "INSERT INTO Orders (Order_ID,Customer_ID,Order_Date,Order_Total,Order_Qty) VALUES (?, ?, ?, ?, ?)",
                (order_id, self.id, time.strftime('%Y-%m-%d %H:%M:%S'), '{:.2f}'.format(total), totalitems))

            for item in self.cart.items:
                cursor.execute("INSERT INTO Order_Item (Order_ID, item_ID, item_quantity) VALUES (?, ?, ?)",
                               (order_id, item.id, item.quantity.get()))

            cursor.execute(
                "INSERT INTO Payment (Invoice_Num,MOP,Order_ID,Customer_ID,Order_Date,Amount_Paid) VALUES(?, ?, ?, ?, ?, ?)",
                (invoice_code, payment_method, order_id, self.id, time.strftime('%Y-%m-%d'), '{:.2f}'.format(total)))

            conn.commit()
            cursor.close()
            conn.close()
            # Create a copy of the cart items list
            cart_items_copy = self.cart.items.copy()

            # Create the receipt using the copy of the cart items
            receipt = Receipt(cart_items_copy, total, dt.datetime.now(), invoice_code, payment_method, order_id,
                              parent=self.parent)

            # Clear the cart after checkout
            self.cart.items.clear()

            # Close the window
            self.window.destroy()


### EMPLOYEE CHECKOUT AND RECEIPT
### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT
### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT
### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT### EMPLOYEE CHECKOUT AND RECEIPT
class EmpCheckout:
    def __init__(self, parent, cart, id, empid):
        self.parent = parent
        self.cart = cart
        self.id = id
        self.empid = empid
        self.payment_method = ""  # To store the payment method option
        self.window = tk.Toplevel(self.parent)
        self.window.title("Checkout")
        self.window.geometry("400x250")

        # Add a label for the checkout total
        total_label = tk.Label(self.window, text="Total: ${:.2f}".format(self.cart.get_total()), font=("default", 16))
        total_label.pack()

        # Add the payment method options
        payment_label = tk.Label(self.window, text="Select Payment Method:", font=("default", 12))
        payment_label.pack(pady=5)
        # Add the "Cash" button
        cash_button = tk.Button(self.window, text="Cash", command=self.select_cash, width=10, bg="green",
                                fg="white", font=("Arial", 10, "bold"))
        cash_button.pack(pady=10)

        # Add the "Card" button
        card_button = tk.Button(self.window, text="Card", command=self.select_card, width=10, bg="green",
                                fg="white", font=("Arial", 10, "bold"))
        card_button.pack(pady=10)

    def select_cash(self):
        self.payment_method = "Cash"
        self.checkout()

    def select_card(self):
        self.payment_method = "Card"
        self.checkout()

    def checkout(self):
        payment_method = self.payment_method
        totalitems = self.cart.get_total_quantity()
        total = self.cart.get_total()
        if total == 0:
            tk.messagebox.showerror("Error", "Your cart is empty.")
        else:
            # Connect to the database and get the highest order ID
            conn = sqlite3.connect("pizza2.db")
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(Order_ID) FROM Orders")
            result = cursor.fetchone()
            order_id = result[0] + 1 if result[
                0] else 1  # Increment the highest ID by one or start at 1 if the table is empty

            # Generate an invoice code based on the current time and date
            invoice_code = time.strftime("%Y%m%d%H%M%S") + str(order_id)

            tk.messagebox.showinfo("Checkout",
                                   "Thank you for your order! Your total is ${:.2f}. Your order will be ready soon.\n\nInvoice Code: {}. Your order ID is {}.".format(
                                       total, invoice_code, order_id))
            # Update the Order_Status table
            cursor.execute("INSERT INTO Order_Status (Order_ID, Order_Status) VALUES (?, ?)", (order_id, 'Pending'))

            # Insert the order into the database
            cursor.execute(
                "INSERT INTO Orders (Order_ID,Customer_ID,Employee_ID,Order_Date,Order_Total,Order_Qty) VALUES (?, ?, ?, ?, ?, ?)",
                (order_id, self.id, self.empid, time.strftime('%Y-%m-%d %H:%M:%S'), '{:.2f}'.format(total), totalitems))

            for item in self.cart.items:
                cursor.execute("INSERT INTO Order_Item (Order_ID, item_ID, item_quantity) VALUES (?, ?, ?)",
                               (order_id, item.id, item.quantity.get()))

            cursor.execute(
                "INSERT INTO Payment (Invoice_Num,MOP,Order_ID,Customer_ID,Order_Date,Amount_Paid) VALUES(?, ?, ?, ?, ?, ?)",
                (invoice_code, payment_method, order_id, self.id, time.strftime('%Y-%m-%d'), '{:.2f}'.format(total)))

            conn.commit()
            cursor.close()
            conn.close()
            # Create a copy of the cart items list
            cart_items_copy = self.cart.items.copy()

            # Create the receipt using the copy of the cart items
            receipt = EmpReceipt(cart_items_copy, total, dt.datetime.now(), invoice_code, payment_method, order_id,
                                 parent=self.parent)

            # Clear the cart after checkout
            self.cart.items.clear()

            # Close the window
            self.window.destroy()


class Receipt:
    def __init__(self, items, total, date_time, invoice_code, payment_mode, order_id, parent=None):
        self.items = items
        self.total = total
        self.date_time = date_time
        self.invoice_code = invoice_code
        self.payment_mode = payment_mode
        self.order_id = order_id
        self.parent = parent
        # create the receipt window
        self.receipt_window = tk.Toplevel(self.parent)
        self.receipt_window.title("Receipt")
        #         self.receipt_window.geometry("400x500")
        # Add a label for the receipt items
        receipt_items_label = tk.Label(self.receipt_window, text="Receipt Items", font=("Ariel", 16, "bold"))
        receipt_items_label.pack(anchor=tk.CENTER)
        # Add a label for the invoice code
        invoice_label = tk.Label(self.receipt_window, text="Invoice Code: {}".format(self.invoice_code),font=("Ariel", 14, "bold"))
        invoice_label.pack(anchor=tk.W)
        # Add a label for the date and time
        date_time_label = tk.Label(self.receipt_window, text="Date and Time: {}".format(self.date_time),font=("Ariel", 14, "bold"))
        date_time_label.pack(anchor=tk.W)
        # Add a label for the payment mode
        MOP_label = tk.Label(self.receipt_window, text="Mode of Payment: {}".format(self.payment_mode),font=("Ariel", 14, "bold"))
        MOP_label.pack(anchor=tk.W)
        # Add a horizontal line
        line_label = tk.Label(self.receipt_window, text="---------------------------------------------------------------------------------------------------------------------------")
        line_label.pack(anchor=tk.W)
        # Add a label for each pizza item in the cart
        for pizza in self.items:
            pizza_label = tk.Label(self.receipt_window, font=("Ariel", 15),
                                   text="{} ({} {}), Quantity: {}, Price: ${:.2f}".format(pizza.name, pizza.type,
                                                                                          pizza.size,
                                                                                          pizza.quantity.get(),
                                                                                          pizza.price * int(
                                                                                              pizza.quantity.get())))
            pizza_label.pack(anchor=tk.W,pady=10)
        # Add a horizontal line
        line_label2 = tk.Label(self.receipt_window, text="---------------------------------------------------------------------------------------------------------------------------")
        line_label2.pack(anchor=tk.W)
        # Add a label for the cart total
        total_label = tk.Label(self.receipt_window, text="Total: ${:.2f}".format(self.total), font=("Ariel", 16))
        total_label.pack()
        # Add a "Print" button
        print_button = tk.Button(self.receipt_window, text="Print", command=lambda :self.print_receipt(self.receipt_window), width=10, bg="blue",
                                 fg="white", font=("Arial", 10, "bold"))
        print_button.pack(pady=10)

        # add a label for rating input
        rating_label = tk.Label(self.receipt_window, text="Please rate your order from 1 to 5:",font=("Ariel",15,'bold'))
        rating_label.pack(pady=10)

        # add a rating scale
        rating_scale = tk.Scale(self.receipt_window, from_=0, to=5, orient=tk.HORIZONTAL)
        rating_scale.pack(pady=10)

        # add a submit button
        submit_button = tk.Button(self.receipt_window, text="Submit",
                                  command=lambda: self.update_order_rating(rating_scale.get()))
        submit_button.pack()

    def update_order_rating(self, rating):
        # update the order rating in the database
        try:
            conn = sqlite3.connect("pizza2.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE Orders SET Order_Ratings = ? WHERE Order_ID = ?", (rating, self.order_id))
            conn.commit()
            tk.messagebox.showinfo("Success", "Order rating has been updated successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", "An error occurred while updating order rating: {}".format(str(e)))
        finally:
            cursor.close()
            conn.close()
            self.receipt_window.destroy()

    #             self.parent.destroy()

    def print_receipt(self,parent):
        self.parent=parent
        # Print the receipt
        print("Invoice Code: {}".format(self.invoice_code))
        print("Date and Time: {}".format(self.date_time))
        print("Mode of Payment: {}".format(self.payment_mode))
        print("--------------------------------------------------")
        for pizza in self.items:
            print("{} ({} {}), Quantity: {}, Price: ${:.2f}".format(pizza.name, pizza.type, pizza.size,
                                                                    pizza.quantity.get(),
                                                                    pizza.price * int(pizza.quantity.get())))
        print("--------------------------------------------------")
        print("Total: ${:.2f}".format(self.total))
        self.parent.destroy()


class EmpReceipt:
    def __init__(self, items, total, date_time, invoice_code, payment_mode, order_id, parent=None):
        self.items = items
        self.total = total
        self.date_time = date_time
        self.invoice_code = invoice_code
        self.payment_mode = payment_mode
        self.order_id = order_id
        self.parent = parent
        # create the receipt window
        self.receipt_window = tk.Toplevel(self.parent)
        self.receipt_window.title("Receipt")
        #         self.receipt_window.geometry("400x500")
        # Add a label for the receipt items
        receipt_items_label = tk.Label(self.receipt_window, text="Receipt Items", font=("default", 16, "bold"))
        receipt_items_label.pack()
        # Add a label for the invoice code
        invoice_label = tk.Label(self.receipt_window, text="Invoice Code: {}".format(self.invoice_code))
        invoice_label.pack()
        # Add a label for the date and time
        date_time_label = tk.Label(self.receipt_window, text="Date and Time: {}".format(self.date_time))
        date_time_label.pack()
        # Add a label for the payment mode
        MOP_label = tk.Label(self.receipt_window, text="Mode of Payment: {}".format(self.payment_mode))
        MOP_label.pack()
        # Add a horizontal line
        line_label = tk.Label(self.receipt_window, text="--------------------------------------------------")
        line_label.pack()
        # Add a label for each pizza item in the cart
        for pizza in self.items:
            pizza_label = tk.Label(self.receipt_window, font=("default", 15, "bold"),
                                   text="{} ({} {}), Quantity: {}, Price: ${:.2f}".format(pizza.name, pizza.type,
                                                                                          pizza.size,
                                                                                          pizza.quantity.get(),
                                                                                          pizza.price * int(
                                                                                              pizza.quantity.get())))
            pizza_label.pack(anchor=tk.W)
        # Add a horizontal line
        line_label2 = tk.Label(self.receipt_window, text="--------------------------------------------------")
        line_label2.pack()
        # Add a label for the cart total
        total_label = tk.Label(self.receipt_window, text="Total: ${:.2f}".format(self.total), font=("default", 16))
        total_label.pack()
        # Add a "Print" button
        print_button = tk.Button(self.receipt_window, text="Print", command=self.print_receipt, width=10, bg="blue",
                                 fg="white", font=("Arial", 10, "bold"))
        print_button.pack(pady=10)

        # add a label for rating input
        rating_label = tk.Label(self.receipt_window, text="Please rate your order from 1 to 5:")
        rating_label.pack(pady=10)

        # add a rating scale
        rating_scale = tk.Scale(self.receipt_window, from_=0, to=5, orient=tk.HORIZONTAL)
        rating_scale.pack(pady=10)

        # add a submit button
        submit_button = tk.Button(self.receipt_window, text="Submit",
                                  command=lambda: self.update_order_rating(rating_scale.get()))
        submit_button.pack()

    def update_order_rating(self, rating):
        # update the order rating in the database
        try:
            conn = sqlite3.connect("pizza2.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE Orders SET Order_Ratings = ? WHERE Order_ID = ?", (rating, self.order_id))
            conn.commit()
            tk.messagebox.showinfo("Success", "Order rating has been updated successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", "An error occurred while updating order rating: {}".format(str(e)))
        finally:
            cursor.close()
            conn.close()
            self.receipt_window.destroy()
            self.parent.destroy()

    def print_receipt(self):
        # Print the receipt
        print("Invoice Code: {}".format(self.invoice_code))
        print("Date and Time: {}".format(self.date_time))
        print("Mode of Payment: {}".format(self.payment_mode))
        print("--------------------------------------------------")
        for pizza in self.items:
            print("{} ({} {}), Quantity: {}, Price: ${:.2f}".format(pizza.name, pizza.type, pizza.size,
                                                                    pizza.quantity.get(),
                                                                    pizza.price * int(pizza.quantity.get())))
        print("--------------------------------------------------")
        print("Total: ${:.2f}".format(self.total))

    ## Customer MainMenu


class MainMenu:
    def __init__(self, id, name):
        ## Customer Name And ID
        self.id = id
        self.name = name

        ### It creates the main window that will contain all of the other graphical elements
        # Main window screen
        self.main_window = tk.Tk()
        self.main_window.attributes('-fullscreen', True)
        self.main_window.title("Employee Main Menu")
        ## Creating an instances of Cart class to store items added to carts.
        self.cart = Cart()

        ## BacgGround Image
        img222 = Image.open("PIZZA.jpeg")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        img222 = img222.resize((screen_width, screen_height))
        self.BGG = ImageTk.PhotoImage(img222)
        self.imageL = tk.Label(self.main_window, image=self.BGG)
        self.imageL.place(x=0, y=0)

        self.store_label = tk.Label(self.main_window, text="Welcome To The Charcoal Pizza Store!!", font=("Times New Roman", 30, "bold"),
                                    bg="grey")
        self.store_label.place(relx=0.00, rely=0.00)

        self.firstframe = tk.Frame(self.main_window)
        self.firstframe.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        self.secondframe = tk.Frame(self.main_window)
        self.secondframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.thirdframe = tk.Frame(self.main_window)
        self.thirdframe.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

        cart_image = Image.open(
            "Cart.jpg")  ## adding th image
        resized_cart_image = cart_image.resize((50, 50))  # resizeing the image
        cart_photo = ImageTk.PhotoImage(resized_cart_image)


        self.cart_items_Button = tk.Button(self.main_window, image=cart_photo
                                           , command=lambda: self.view_cart(), height=36, width=50,
                                           bg="black")
        self.cart_items_Button.place(relx=0.95, rely=0.05, anchor=tk.E)

        ## Loading Pizza data & Beverages Sides
        # Loading Pizza data in pizza class and storing the instances in the below lists
        self.pizzasV = []  # loading veg regular
        self.pizzasVL = []  # loading veg large
        self.pizzasNV = []  # loading non veg regular
        self.pizzasNVL = []  # loading non veg large
        self.bev = []  # loading bev
        self.sides = []  # loading sides
        self.load_pizza_data()

        self.pizza_button = tk.Button(self.firstframe, text="Vegetarian Menu",
                                      command=lambda: self.open_veg_menu(self.main_window, self.pizzasV, self.pizzasVL,
                                                                         self.cart, self.id, self.name), width=18,
                                      height=3, bg="green", fg="white", font=("Arial", 20, "bold")).pack()
        self.pizza_button = tk.Button(self.secondframe, text="Non-Vegetarian Menu",
                                      command=lambda: self.open_non_veg_menu(self.main_window, self.pizzasNV,
                                                                             self.pizzasNVL, self.cart, self.id,
                                                                             self.name), width=18, height=3, bg="green",
                                      fg="white", font=("Arial", 20, "bold")).pack()
        self.pizza_button = tk.Button(self.thirdframe, text="Beverages & Sides",
                                      command=lambda: self.open_bevsides_menu(self.main_window, self.bev, self.sides,
                                                                              self.cart, self.id, self.name), width=18,
                                      height=3, bg="green", fg="white", font=("Arial", 20, "bold")).pack()

        self.idlabel = tk.Label(self.main_window, text=f"Customer-ID      : {self.id}\n   Customer Name: {self.name}",
                                font=("Arial", 10, "bold"),bg="grey")
        self.idlabel.place(rely=0.07, relx=0.00)
        ##LogOUT BUtton
        self.logout_button = tk.Button(self.main_window, text="LogOut", command=self.logout, width=8, bg="red",
                                       fg="white", font=("Arial", 15, "bold"))
        self.logout_button.place(relx=0.85, rely=0.05, anchor=tk.CENTER)

        ##close BUtton
        self.close_button = tk.Button(self.main_window, text="Close", command=self.close, width=8, bg="red", fg="white",
                                      font=("Arial", 15, "bold"))
        self.close_button.place(relx=0.76, rely=0.05, anchor=tk.CENTER)

        # Add a button to show the order history
        history_button = tk.Button(self.main_window, text="Order History", command=self.show_order_history, bg="red",
                                   fg="white", font=("Arial", 15, "bold"))
        history_button.place(relx=0.65, rely=0.05, anchor=tk.CENTER)
        tk.mainloop()

    def show_order_history(self):
        # Connect to the database and retrieve all the orders
        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT Orders.Order_ID, Orders.Order_Date, Orders.Order_Total, Order_Status.Order_Status FROM Orders INNER JOIN Order_Status ON Orders.Order_ID = Order_Status.Order_ID WHERE Orders.Customer_ID = ?",
            (self.id,))
        orders = cursor.fetchall()

        # Create a new window to display the orders
        window = tk.Toplevel(self.main_window)
        window.title("Order History")
        window.geometry("1000x700")
        window.configure(background="#7e4b1c")
        # Add a label for the order history
        label = tk.Label(window, text="Order History", font=("default", 16))
        label.pack(pady=10)
        s = ttk.Style()
        s.theme_use('classic')
        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#ff8c00", font=("Ariel", 15, "bold"))
        s.configure('Treeview', font=('Arial', 12))

        # Add a treeview to display the orders
        columns = ("Order ID", "Order Date", "Order Total", "Order Status")
        tree = ttk.Treeview(window, columns=columns, show="headings", height=20)

        tree.column("Order Date", width=300)
        for col in columns:
            tree.heading(col, text=col)
            if col in ["Order ID", "Order Total", "Order Status"]:
                tree.column(col, anchor="center")
        tree.pack()

        # Define the tags for each status
        tree.tag_configure("pending", background="yellow")
        tree.tag_configure("preparing", background="orange")
        tree.tag_configure("ready", background="green")

        # Add the orders to the treeview
        for order in orders:
            order_id, order_date, order_total, order_status = order
            order_total_formatted = f"{order_total:.2f}"
            order_item_id = f"{order_id}_item"
            tree.insert("", "end", values=(order_id, order_date, order_total_formatted, order_status), iid=order_id,
                        tags=(order_status.lower(),))

            # Retrieve the order items for the current order
            cursor.execute(
                "SELECT (Items.item_name || ' ' || Items.item_size) AS name, Order_Item.item_Quantity,(Order_Item.item_Quantity * Items.item_price) AS price FROM Items INNER JOIN Order_Item ON Items.item_ID = Order_Item.item_ID WHERE Order_Item.Order_ID = ?",
                (order_id,))
            order_items = cursor.fetchall()

            # Add the order items to the treeview as sub-items
            for index, order_item in enumerate(order_items, 1):
                name, item_quantity, price = order_item
                item_id = f"{order_item_id}_{index}"

                tree.insert(order_id, "end", values=("", f"{name} ({item_quantity})", "{:.2f}".format(price)), iid=item_id)

        def clear_selection(event):
            selected_items = event.widget.selection()
            for item in selected_items:
                event.widget.selection_remove(item)

        # Bind the TreeviewSelect event to clear_selection
        tree.bind("<<TreeviewSelect>>", clear_selection)

        cursor.close()
        conn.close()

        close_button = tk.Button(window, text="Close", font=("Ariel", 20, "bold"), background="#ffebcd",
                                 command=window.destroy)
        close_button.pack(side="right")



    def close(self):  ## closing the application
        self.main_window.destroy()

    def logout(self):
        # switch to login page
        self.main_window.destroy()
        LoginPage()

    ## Veg NonVeg BevSides - calling the class
    def open_veg_menu(self, parent, pizzasV, pizzasVL, Cart, id, name):
        self.veg_menu = VegMenu(parent, pizzasV, pizzasVL, Cart, id, name)

    def open_non_veg_menu(self, parent, pizzasNV, pizzasNVL, Cart, id, name):
        self.non_veg_menu = NonVegMenu(parent, pizzasNV, pizzasNVL, Cart, id, name)

    def open_bevsides_menu(self, parent, bev, sides, Cart, id, name):
        self.bevsides_menu = BevSideMenu(parent, bev, sides, Cart, id, name)

    def get_cart_total(self):
        return self.cart.get_total()

    def checkout(self):
        checkout_window = Checkout(self.main_window, self.cart, self.id)

    ## Loading the data of the menu itesm from the database
    def load_pizza_data(self):
        # Connect to the database
        conn = sqlite3.connect('pizza2.db')
        c = conn.cursor()
        # Retrieve the pizza data from the database Vege-R
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("Vegetarian", "Regular"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasV.append(pizza)

        # Retrieve the pizza data from the database Veg-L
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("Vegetarian", "Large"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasVL.append(pizza)

        # Retrieve the pizza data from the database NON Veg-R
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("NonVegetarian", "Regular"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasNV.append(pizza)

        # Retrieve the pizza data from the database NON Veg-L
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("NonVegetarian", "Large"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasNVL.append(pizza)

        # Retrieve the pizza data from the database BevSide
        c.execute("SELECT * FROM Items WHERE item_type = ?", ("Beverages",))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            bev = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.bev.append(bev)

        # Retrieve the pizza data from the database Side
        c.execute("SELECT * FROM Items WHERE item_type = ?", ("Sides",))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            print(row[4])
            side = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.sides.append(side)
        # Close the database connection
        conn.close()

    def view_cart(self):
        # Create a new window for the cart
        self.cart_window = tk.Toplevel(self.main_window)
        self.cart_window.title("View Cart")
        frame = tk.Frame(self.cart_window).place(relx=0.00, rely=0.00)
        # Add a label for the cart items
        cart_items_label = tk.Label(self.cart_window, text="Cart Items", font=("default", 16, "bold"))
        cart_items_label.pack()

        # Add a frame for the cart items
        cart_items_frame = tk.Frame(self.cart_window)
        cart_items_frame.pack()
        self.cart_items_frame = cart_items_frame

        # Add a label for the cart total
        self.cart_total_label = tk.Label(self.cart_window, text="Total: ${:.2f}".format(self.get_cart_total()),
                                         font=("default", 16))
        self.cart_total_label.pack()

        # Add a "Checkout" button
        checkout_button = tk.Button(self.cart_window, text="Checkout", command=self.checkout, width=10, bg="green",
                                    fg="white", font=("Arial", 10, "bold"))
        checkout_button.pack(pady=10)

        # Add a label and Spinbox for each pizza item in the cart
        for i, pizza in enumerate(self.cart.get_items()):
            # Create a frame to hold the product label and Spinbox
            product_frame = tk.Frame(cart_items_frame, bg="white")
            product_frame.grid(row=i, column=0, sticky='w', pady=10)

            product_frame1 = tk.Frame(cart_items_frame, bg="white")
            product_frame1.grid(row=i, column=2, sticky='w', pady=10)

            pizza.product_frame = product_frame
            pizza.product_frame1 = product_frame1

            # Add a label for the product name, type, and size
            product_label = tk.Label(product_frame, text="{} ({} {})".format(pizza.name, pizza.type, pizza.size),
                                     font=('Ariel', 15, "bold"), bg="white")
            product_label.grid(row=0, column=0, sticky='w')

            # Add a Spinbox for the product quantity
            quantity_spinbox = tk.Spinbox(product_frame1, from_=1, to=10, width=5, textvariable=pizza.quantity,
                                          command=lambda: self.update_cart_total(), font=('Ariel', 15, "bold"))
            quantity_spinbox.grid(row=0, column=7, padx=(10, 0))

            # Add a label for the product price
            price_label = tk.Label(product_frame, text="${:.2f}".format(pizza.price * int(pizza.quantity.get())),
                                   font=('Ariel', 15, "bold"), bg="white")
            price_label.grid(row=0, column=8, padx=(10, 0))

            # Add a "Remove" button for the pizza item
            remove_button = tk.Button(product_frame1, text="Remove",
                                      command=lambda pizza_item=pizza: self.remove_from_cart(pizza_item),
                                      font=('Ariel', 15, "bold"))
            remove_button.grid(row=0, column=9, padx=(10, 0))

            # Add the price label to the pizza item for later use
            pizza.price_label = price_label

    def update_cart_total(self):
        # Update the price labels for each pizza item in the cart
        for pizza in self.cart.get_items():
            pizza.price_label.config(text="${:.2f}".format(pizza.price * int(pizza.quantity.get())))

        # Update the cart total label with the new total
        self.cart_total_label.config(text="Total: ${:.2f}".format(self.get_cart_total()))

    def remove_from_cart(self, pizza_item):
        # Check if the pizza item is in the items list
        if pizza_item in self.cart.items:
            # Remove the pizza item from the cart's items list
            self.cart.items.remove(pizza_item)
            # Update the cart items and total labels
            self.update_cart_total()
            # Destroy the product frames associated with the pizza item
            pizza_item.product_frame.destroy()
            pizza_item.product_frame1.destroy()
# Notes:
##The self.cart_items_frame instance variable is necessary to keep track of the frame holding the pizza items in the cart.
##When the view_cart method is called, it creates a cart_items_frame frame and adds the pizza items to it.
## When the remove_from_cart method is called to remove a pizza item,
## it needs to access the cart_items_frame frame to search for and remove the appropriate pizza item widget.

## If we did not use self.cart_items_frame and just used cart_items_frame as a local variable in view_cart,
## it would not be accessible in the remove_from_cart method because it would not be defined in that method's scope.
## By assigning cart_items_frame to self.cart_items_frame,
##we make it an instance variable that is accessible throughout the class, including in the remove_from_cart method.

## So, using self.cart_items_frame as an instance variable is necessary to keep track of the
##cart items frame and access it from other methods in the class.

# if __name__ == "__main__":
# #     ee= EmpMenu("EMP1","AG")
#     MJ = MainMenu("CUS1","AnuragG")
# #     lg = LoginPage()


from tkcalendar import Calendar
import csv
import pandas as pd
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import hashlib
import sqlite3
import time
import tkinter.messagebox
from PIL import Image, ImageTk

import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import datetime as dt

### Employee admin### Employee admin
### Employee admin### Employee admin### Employee admin### Employee admin
### Employee admin### Employee admin### Employee admin### Employee admin### Employee admin
### Employee admin### Employee admin### Employee admin### Employee admin### Employee admin### Employee admin
### Employee admin### Employee admin### Employee admin### Employee admin### Employee admin### Employee admin### Employee admin
class EmpMenu():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.main_window = tk.Tk()
        self.main_window.title("Admin-Menu")
        self.main_window.attributes("-fullscreen",True)
        self.main_window.configure(background="#7e4b1c")

        # Create the frame and center it
        self.firstframe = tk.Frame(self.main_window)
        self.firstframe.place(relx=0.1, rely=0.4)
        self.secondframe = tk.Frame(self.main_window)
        self.secondframe.place(relx=0.4, rely=0.4)
        self.thirdframe = tk.Frame(self.main_window)
        self.thirdframe.place(relx=0.7, rely=0.4)

        # Create the buttons
        tk.orderButton = tk.Button(self.firstframe, text="New-Order", width=14, relief='raised',
                                   font=("default", 20, "bold"), bg="green", fg="yellow", command=self.new_order)
        tk.orderButton.pack(ipady=10, ipadx=10)
        pending_button = tk.Button(self.secondframe, text="Pending Orders", command=lambda: self.show_orders("Pending"),
                                   width=14, relief='raised', font=("default", 20, "bold"), bg="#f01e00").pack()
        preparing_button = tk.Button(self.secondframe, text="Preparing Orders",
                                     command=lambda: self.show_orders("Preparing"), width=14, relief='raised',
                                     font=("default", 20, "bold"), bg="#fcf75e").pack()
        ready_button = tk.Button(self.secondframe, text="Ready Orders", command=lambda: self.show_orders("Ready"),
                                 width=14, relief='raised', font=("default", 20, "bold"), bg="#32cd32").pack()

        tk.ReportsButton = tk.Button(self.thirdframe, text="Reports", width=14, relief='raised',
                                     font=("default", 20, "bold"), bg="#ffebcd", command=self.show_reports)
        tk.ReportsButton.pack(ipady=10, ipadx=10)

        self.close_button = tk.Button(self.main_window, text="Close", command=self.main_window.destroy, width=10, fg="white",
                                      font=("Arial", 15, "bold"), bg="red")
        self.close_button.place(relx=0.76, rely=0.9, anchor=tk.CENTER)

        # Start the main loop
        self.main_window.mainloop()

####### Start Reports
    ####### Start Reports####### Start Reports####### Start Reports
    ####### Start Reports####### Start Reports####### Start Reports####### Start Reports####### Start Reports
    def show_reports(self):
        # Create a new window to display the reports
        window = tk.Toplevel(self.main_window)
        self.show_reports_window = window
        window.title("Reports")
        window.configure(background="#7e4b1c")
        # Create buttons for different types of reports
        customer_reports_button = tk.Button(self.show_reports_window, text="Customer Reports",
                                            command= self.show_customer_reports
                                            , font=("Ariel", 15, "bold"), background="#ffebcd")
        sales_reports_button = tk.Button(self.show_reports_window, text="Sales Reports",
                                         command=self.show_sales_reports
                                         , font=("Ariel", 15, "bold"), background="#ffebcd")

        sales_reports1_button = tk.Button(self.show_reports_window, text="Customer Ratings",
                                          command=self.view_sales_reports
                                          , font=("Ariel", 15, "bold"), background="#ffebcd")
        sales_visual_button = tk.Button(self.show_reports_window, text="Sales-Most Sold Items- Visuals",
                                        command=self.view_sales_reports
                                        , font=("Ariel", 15, "bold"), background="#ffebcd")

        # Add the buttons to the window
        customer_reports_button.pack(pady=10)
        sales_reports_button.pack(pady=10)
        sales_reports1_button.pack(pady=10)
        sales_visual_button.pack(pady=10)


        close_button = tk.Button(window, text="Close", font=("Ariel", 15, "bold"), background="#ffebcd",
                                 command=self.show_reports_window.destroy)
        close_button.pack(side="bottom")
    def show_customer_reports(self):
        # Connect to the database
        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()

        # Execute the SQL query to retrieve customer reports
        cursor.execute("SELECT * FROM CustomersInformation")
        customer_data = cursor.fetchall()

        # Close the database connection
        conn.close()

        s = ttk.Style()
        s.theme_use('classic')
        font1 = ['Times', 15, 'bold']
        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#ff8c00", font=("Ariel",15,"bold"))
        s.configure('Treeview', font=('Arial', 12))

        # Create a new window to display the customer reports
        window = tk.Toplevel(self.show_reports_window)
        window.title("Customer Reports")
        window.configure(background="#7e4b1c")
        # Create a Treeview widget to display the customer data
        tree = ttk.Treeview(window, columns=(
        "Customer ID", "First Name", "Middle Name", "Last Name", "Phone Number",
        "Username", "Email ID"))
        tree.heading("#0", text="Index")
        tree.heading("Customer ID", text="Customer ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Name", text="Middle Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Phone Number", text="Phone Number")
        tree.heading("Username", text="Username")
        tree.heading("Email ID", text="Email ID")
        tree.column("#0", width=65, minwidth=50, anchor=tk.CENTER)
        tree.column("Customer ID", width=140, minwidth=100, anchor=tk.CENTER)
        tree.column("First Name", width=140, minwidth=100, anchor=tk.CENTER)
        tree.column("Middle Name", width=160, minwidth=100, anchor=tk.CENTER)
        tree.column("Last Name", width=140, minwidth=100, anchor=tk.CENTER)
        tree.column("Phone Number", width=170, minwidth=120, anchor=tk.CENTER)
        tree.column("Username", width=120, minwidth=100, anchor=tk.CENTER)
        tree.column("Email ID", width=250, minwidth=200, anchor=tk.CENTER)

        # Define tags for alternate row colors
        tree.tag_configure('evenrow', background='#addfad')
        tree.tag_configure('oddrow', background='white')

        # Insert the customer data into the Treeview widget
        for i, customer in enumerate(customer_data):
            if i % 2 == 0:
                tree.insert(parent="", index="end", iid=i, text=i, values=(
                    customer[0], customer[1], customer[2], customer[3], customer[8], customer[9], customer[11]),
                            tags=('evenrow',))
            else:
                tree.insert(parent="", index="end", iid=i, text=i, values=(
                    customer[0], customer[1], customer[2], customer[3], customer[8], customer[9], customer[11]),
                            tags=('oddrow',))

        tree.pack(fill=tk.BOTH, expand=1)



        # Create a button to export the data to an Excel file
        def export_to_excel():
            # Ask the user to choose a file location to save the Excel file
            filepath = filedialog.asksaveasfilename(defaultextension='.xlsx')
            if filepath:
                # Create a CSV file with the customer data
                with open('customer_data.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Customer ID', 'First Name', 'Middle Name', 'Last Name', 'Phone Number', 'Username','Email ID'])
                    for customer in customer_data:
                        print(customer)
                        writer.writerow((customer[0], customer[1], customer[2], customer[3], customer[8], customer[9], customer[11]))
                df = pd.read_csv('customer_data.csv')
                df.to_excel(filepath, index=False)

            window.destroy()
            self.show_reports_window.destroy()
            self.show_reports()


        export_button = tk.Button(window, text="Export to Excel", font=("Ariel", 15, "bold"), background="#ffebcd",
                                  command=export_to_excel)
        export_button.pack(side="bottom",anchor=tk.E)
        close_button = tk.Button(window, text="Close", font=("Ariel", 15, "bold"), background="#ffebcd",
                                     command=window.destroy)
        close_button.pack(side="bottom")
        date = dt.datetime.now()

        date_label = tk.Label(window, text=f"{date:%A, %B %d, %Y}", font="Ariel, 25", anchor='e')
        date_label.pack(side="bottom",anchor=tk.E) # r=1, column = 0
    def show_sales_reports(self):

        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()

        # Execute the SQL query to retrieve sales reports
        cursor.execute(
            "SELECT date(Order_Date) as Date,ROUND(SUM(Order_Total), 2) as Total_Sales FROM Orders GROUP BY Date")
        total_sales = cursor.fetchall()

        # Close the database connection
        conn.close()

        s = ttk.Style()
        s.theme_use('classic')
        font1 = ['Times', 15, 'bold']
        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#ff8c00", font=("Ariel", 15, "bold"))
        s.configure('Treeview', font=('Arial', 12))
        # Connect to the database

        # Create a new window to display the customer reports
        window = tk.Toplevel(self.show_reports_window)
        window.title("Customer Reports")
        window.configure(background="#7e4b1c")

        # Create a Treeview widget to display the customer data
        tree = ttk.Treeview(window, columns=("Order_Date","Total_Sales"))
        tree.heading("#0", text="Index")
        tree.heading("Order_Date", text="Order Date")
        tree.heading("Total_Sales", text="Total Sales")
        tree.column("#0", width=65, minwidth=50, anchor=tk.CENTER)
        tree.column("Order_Date", width=140, minwidth=100, anchor=tk.CENTER)
        tree.column("Total_Sales", width=140, minwidth=100, anchor=tk.CENTER)
        # Define tags for alternate row colors
        tree.tag_configure('evenrow', background='#addfad')
        tree.tag_configure('oddrow', background='white')

        # Insert the customer data into the Treeview widget
        for i, sales in enumerate(total_sales):
            if i % 2 == 0:
                tree.insert(parent="", index="end", iid=i, text=i, values=(
                    sales[0], sales[1]),
                            tags=('evenrow',))
            else:
                tree.insert(parent="", index="end", iid=i, text=i, values=(
                    sales[0], sales[1]),
                            tags=('oddrow',))

        tree.pack(fill=tk.BOTH, expand=1)
        def export_to_excel():
            # Ask the user to choose a file location to save the Excel file
            filepath = filedialog.asksaveasfilename(defaultextension='.xlsx')
            if filepath:
                # Create a CSV file with the customer data
                with open('sales_data.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Order Date","Total Sales"])
                    for sales in total_sales:
                        writer.writerow((sales[0], sales[1]))


                df = pd.read_csv('customer_data.csv')
                df.to_excel(filepath, index=False)
            window.destroy()
            self.show_reports_window.destroy()
            self.show_reports()

        date = dt.datetime.now()
        date_label = tk.Label(window, text=f"{date:%A, %B %d, %Y}", font="Ariel, 25", anchor='e')
        date_label.pack(side="left", anchor=tk.E)  # r=1, column = 0

        export_button = tk.Button(window, text="Export to Excel", font=("Ariel", 15, "bold"), background="#ffebcd",
                                  command=export_to_excel)
        export_button.pack(side="left")
        close_button = tk.Button(window, text="Close", font=("Ariel", 15, "bold"), background="#ffebcd",
                                     command=window.destroy)
        close_button.pack(side="left")
    def view_sales_reports(self):
        # create a new Toplevel window
        window = tk.Toplevel(self.show_reports_window)
        window.attributes("-fullscreen",True)
        frame1 = tk.Frame(window)
        frame1.pack(fill="both", expand=True)
        frame2 = tk.Frame(window,bg="white")
        frame2.pack(fill="both", expand=True)
        frame3=tk.Frame(frame2,bg="white")
        frame3.pack(side="right")


        # Connect to the database
        conn = sqlite3.connect("pizza2.db")
        c = conn.cursor()

        ## Fetching Total orders and Total Revenue earned from database
        c.execute("SELECT COUNT(*) as Total_Orders,SUM(Order_Total) as total FROM Orders")
        text_query=c.fetchall()
        for values in text_query:
            Total_Orders=values[0]
            Total_sales=values[1]

        ## Fetching Average Customer Ratings
        c.execute("SELECT AVG(Order_Ratings) as ratings FROM Orders WHERE Order_Ratings>=1")
        Average_Ratings = c.fetchone()[0]

        ## Fetching Mode Of Payment total
        c.execute("SELECT SUM(Amount_Paid) FROM Payment WHERE MOP = 'Cash'")
        cash_MOP= c.fetchone()[0]
        print(cash_MOP)
        c.execute("SELECT SUM(Amount_Paid) FROM Payment WHERE MOP = 'Card'")
        card_MOP= c.fetchone()[0]
        print(card_MOP)

        ## Assigning the Above value to lables for dashboard display
        total_orders=tk.Label(frame3,text=f'Total Orders: {Total_Orders}',font=("Ariel",20,"bold"),bg="white")
        total_orders.pack()
        total_sales = tk.Label(frame3, text=f'Total Sales: ${Total_sales:.2f}', font=("Ariel", 20, "bold"),bg="white")
        total_sales.pack()
        cash_sales = tk.Label(frame3, text=f'Cash Total: ${cash_MOP:.2f}', font=("Ariel", 20, "bold"), bg="white")
        cash_sales.pack()
        card_sales = tk.Label(frame3, text=f'Card Total: ${card_MOP:.2f}', font=("Ariel", 20, "bold"), bg="white")
        card_sales.pack()
        average_ratings = tk.Label(frame3, text=f'Average Ratings: {Average_Ratings:.2f}/5', font=("Ariel", 20, "bold"),bg="white")
        average_ratings.pack()






###### MOst Sold Items
        items_query = "SELECT item_name, SUM(item_Quantity) as Total_Quantity_Sold FROM Order_Item oi INNER JOIN Items i ON oi.item_ID = i.item_ID GROUP BY item_name ORDER BY Total_Quantity_Sold DESC LIMIT 5"

        items_query = pd.read_sql_query(items_query, conn)
        fig1, ax = plt.subplots()
        items_query.plot(kind='barh', x="item_name", y="Total_Quantity_Sold", ax=ax)
        ax.set_title("Items Report")

        for i, v in enumerate(items_query["Total_Quantity_Sold"].values):
            ax.text(v + 0.5, i, str(v), color='black', fontsize=10)

        # embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig1, master=frame1)
        canvas.draw()
        canvas.get_tk_widget().pack(side="right", fill=tk.BOTH, expand=True,anchor="e")
### Sales History By Date
        # Sales report over changing dates
        sales_query = "SELECT date(Order_Date) as Date, SUM(Order_Total) as Total_Sales FROM Orders GROUP BY Date"
        sales_df = pd.read_sql_query(sales_query, conn)
        sales_df = sales_df.rename(columns={"Date": "Order_Date"})
        fig, ax = plt.subplots()
        sales_df.plot(x="Order_Date", y="Total_Sales", ax=ax)
        ax.set_title("Sales Report")
        for i, v in enumerate(sales_df["Total_Sales"]):
            plt.text(i, v, str(round(v)), color='blue', fontweight='bold')
        # Set the x-axis labels to display vertically
        plt.xticks(rotation=15)
        # embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=True)

        # add a close button to the plot window
        # Sales report over changing dates


##### Order ratings
        star_query = "SELECT Order_Ratings as ratings, COUNT(*) as Num_Of_Orders FROM Orders GROUP BY Order_Ratings"

        star_query = pd.read_sql_query(star_query, conn)
        fig2, ax = plt.subplots()
        star_query.plot(kind='barh', x="ratings", y="Num_Of_Orders", ax=ax)
        ax.set_title("Order Ratings")
        # embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig2, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=True)



        # add a close button to the plot window
        close_button = tk.Button(frame3, text="Close", command=window.destroy,width=10,bg="red",fg="white",font=("Ariel",20,"bold"))
        close_button.pack(side="bottom")


        conn.close()



### Order History

    def show_orders(self, status):
        # Create a new window to display the orders
        window = tk.Toplevel(self.main_window)
        window.title("Order History")
        window.geometry("1000x700")
        window.configure(background="#7e4b1c")
        # Add a label for the order history
        label = tk.Label(window, text="Order History", font=("Ariel", 25),bg="#7e4b1c")
        label.pack(pady=10)
        date = dt.datetime.now()
        date_label = tk.Label(window, text=f"{date:%A, %B %d, %Y}", font="Ariel, 20", anchor='e')
        date_label.pack(pady=10,anchor=tk.CENTER)

        s = ttk.Style()
        s.theme_use('clam')
        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#ff8c00", font=("Ariel", 15, "bold"))
        s.configure('Treeview', font=('Arial', 12))



        # Add a treeview to display the orders
        columns = ("Order ID", "Order Date", "Order Total", "Order Status")
        tree = ttk.Treeview(window, columns=columns, show="headings", height=20)

        tree.column("Order Date", width=300)
        for col in columns:
            tree.heading(col, text=col)
            if col in ["Order ID", "Order Total", "Order Status"]:
                tree.column(col, anchor="center")
        tree.pack()

        # Define the tags for each status
        tree.tag_configure("pending", background="yellow")
        tree.tag_configure("preparing", background="orange")
        tree.tag_configure("ready", background="green")

        # Set the default date to today's date
        default_date = dt.date.today().strftime('%Y-%m-%d')

        # Show orders for today's date by default
        self.show_orders_by_date(tree, default_date, status)

        # Add a button to select a date
        date_button = tk.Button(window, text="Select Date", font=("Arial", 20, "bold"),
                                command=lambda: self.select_date(tree, status),bg="grey")
        date_button.pack(side="left")

        # Create buttons to update order status
        prepare_button = tk.Button(window, text="Preparing", font=("Arial", 20, "bold"),
                                   command=lambda: self.update_order_status(tree, "Preparing"), bg="orange")
        prepare_button.pack(side="left")

        ready_button = tk.Button(window, text="Ready", font=("Arial", 20, "bold"),
                                 command=lambda: self.update_order_status(tree, "Ready"), bg="green")
        ready_button.pack(side="left", anchor=tk.CENTER)

        close_button = tk.Button(window, text="Close", font=("Ariel", 20, "bold"), background="#ffebcd",
                                 command=window.destroy)
        close_button.pack(side="right")
          # r=1, column = 0

    def select_date(self, tree,status):
        def select():
            selected_date = cal.selection_get().strftime('%Y-%m-%d')
            self.show_orders_by_date(tree, selected_date,status)
            top.destroy()

        top = tk.Toplevel(self.main_window)
        top.geometry("400x300")

        # Set the default date to today's date
        default_date = dt.datetime.today().date()

        # Pass the default date to the Calendar widget
        cal = Calendar(top, selectmode='day', year=default_date.year, month=default_date.month, day=default_date.day)
        cal.pack(pady=10)

        button = tk.Button(top, text="Select", command=select)
        button.pack(pady=10)

    def show_orders_by_date(self, tree, selected_date,status):
        conn = sqlite3.connect("pizza2.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT Orders.Order_ID, Orders.Order_Date, Orders.Order_Total, Order_Status.Order_Status FROM Orders INNER JOIN Order_Status ON Orders.Order_ID = Order_Status.Order_ID WHERE date(Orders.Order_Date) = ? AND Order_Status.Order_Status =?",
            (selected_date, status))

        orders = cursor.fetchall()
        cursor.close()
        conn.close()
        self.display_orders(tree, orders)

    def display_orders(self, tree, orders):
        tree.delete(*tree.get_children())
        for order in orders:
            order_id, order_date, order_total, order_status = order
            order_total_formatted = f"{order_total:.2f}"
            order_item_id = f"{order_id}_item"
            tree.insert("", "end", values=(order_id, order_date, order_total_formatted, order_status), iid=order_id,
                        tags=(order_status.lower(),))
            conn = sqlite3.connect("pizza2.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT (Items.item_name || ' ' || Items.item_size) AS name, Order_Item.item_Quantity,(Order_Item.item_Quantity * Items.item_price) AS price FROM Items INNER JOIN Order_Item ON Items.item_ID = Order_Item.item_ID WHERE Order_Item.Order_ID = ?",
                (order_id,))
            order_items = cursor.fetchall()
            cursor.close()
            for index, order_item in enumerate(order_items, 1):
                name, item_quantity, price = order_item
                item_id = f"{order_item_id}_{index}"
                tree.insert(order_id, "end", values=("", f"{name} ({item_quantity})", "{:.2f}".format(price)), iid=item_id)


    def update_order_status(self, order_tree, status):
        # Get the selected order from the Treeview
        selected_order = order_tree.focus()
        print(selected_order)

        # Extract the order ID from the selected order
        order_id = selected_order

        # Update the order status in the database
        conn = sqlite3.connect("pizza2.db")
        conn.execute(f"UPDATE Order_Status SET Order_Status = '{status}' WHERE Order_ID = {order_id}")

        # Commit the changes to the database
        conn.commit()

        # Remove the selected order from the Treeview
        order_tree.delete(selected_order)
### New Orders
    def new_order(self):
        # Create a new window
        order_window = tk.Toplevel()
        order_window.title("New Order")
        order_window.configure(background="#7e4b1c")


        no_ff_Frame = tk.Frame(order_window,bg="#7e4b1c")
        no_ff_Frame.pack(side="left")

        no_ff11_Frame = tk.Frame(order_window)
        no_ff11_Frame.pack(side="left")

        # Create the labels and entry boxes for customer information
        tk.Label(no_ff_Frame, text="First Name: ",font=("Ariel", 15, "bold"),bg="#7e4b1c").pack(anchor=tk.W)
        first_name_entry = tk.Entry(no_ff11_Frame,font=("Ariel", 15, "bold"))
        first_name_entry.pack()

        tk.Label(no_ff_Frame, text="Middle Name: ",font=("Ariel", 15, "bold"),bg="#7e4b1c").pack(anchor=tk.W)
        middle_name_entry = tk.Entry(no_ff11_Frame,font=("Ariel", 15, "bold"))
        middle_name_entry.pack()

        tk.Label(no_ff_Frame, text="Last Name: ",font=("Ariel", 15, "bold"),bg="#7e4b1c").pack(anchor=tk.W)
        last_name_entry = tk.Entry(no_ff11_Frame,font=("Ariel", 15, "bold"))
        last_name_entry.pack()

        tk.Label(no_ff_Frame, text="Email: ",font=("Ariel", 15, "bold"),bg="#7e4b1c").pack(anchor=tk.W)
        email_entry = tk.Entry(no_ff11_Frame,font=("Ariel", 15, "bold"))
        email_entry.pack()

        tk.Label(no_ff_Frame, text="Contact Number: ",font=("Ariel", 15, "bold"),bg="#7e4b1c").pack(anchor=tk.W)
        contact_entry = tk.Entry(no_ff11_Frame,font=("Ariel", 15, "bold"))
        contact_entry.pack()

        ##Close Button
        close_button = tk.Button(order_window, text="Close", font=("Ariel", 15, "bold"), background="#ffebcd",
                                 command=order_window.destroy)
        close_button.pack(side="bottom")

        # Create a button to submit the customer information
        submit_button = tk.Button(order_window, text="Submit",font=("Trebuchet MS", 15, "bold"),bg="green",fg="white",
                                  command=lambda: self.submit_order(order_window, first_name_entry.get().lower(),
                                                                    middle_name_entry.get().lower(), last_name_entry.get().lower(),
                                                                    email_entry.get().lower(), contact_entry.get().lower()))
        submit_button.pack()


### Submitting order
### ADD Constraints CHeck
    def submit_order(self, order_window, first_name, middle_name, last_name, email, contact):
        # Check if customer already exists in the database
        conn = sqlite3.connect('pizza2.db')
        c = conn.cursor()
        c.execute(
            "SELECT Customer_ID, (Last_Name || ', ' || First_Name || ' ' || Middle_Name) AS full_name FROM CustomersInformation WHERE (Email_ID = ? OR Email_ID IS NULL OR Phone_Number = ? OR Phone_Number IS NULL)",
            (email, contact))

        row = c.fetchone()
        print(row)

        if row:
            # Customer already exists, retrieve customer id
            customer_id = row[0]
            full_name = row[1]

        else:
            # Query the database for the highest existing customer ID
            # Retrieve the last customer ID, sorting by numeric part
            c.execute("SELECT Customer_ID FROM CustomersInformation ORDER BY CAST(substr(Customer_ID, 4) AS INTEGER) DESC LIMIT 1")
            max_id = c.fetchone()[0]
            print(max_id)
            if max_id is None:
                # If there are no existing customers, start the customer ID sequence at 1
                max_id = 0
            else:
                # Convert the max_id value to an integer
                max_id = int(max_id.replace("CUS", ""))
                print(max_id)

            # Increment the highest customer ID to generate a new unique customer ID
            new_id = max_id + 1
            print(new_id)

            # Add "CUS" back to the beginning of the new customer ID
            customer_id = f"CUS{new_id}"
            print(customer_id)
            c.execute(
                "INSERT INTO CustomersInformation (Customer_ID,First_Name,Middle_Name,Last_Name,Email_ID,Phone_Number) VALUES (?,?, ?, ?, ?, ?)",
                (customer_id,first_name, middle_name, last_name, email, contact))
            full_name = f"{last_name},{first_name} {middle_name} ".strip()

        # Close the database connection
        conn.commit()
        conn.close()

        # Open the main menu with the customer id and full name
        order_window.destroy()
        self.parent = self.main_window
        self.mainmenu(customer_id, full_name, self.id)
### Calling the MainMenu class
    def mainmenu(self, customer_id, full_name, empid):
        mainmenu = EmpMainMenu(self.parent, customer_id, full_name, empid)


class EmpMainMenu:
    def __init__(self, parent, id, name, empid):
        self.parent = parent
        self.main_window = tk.Toplevel(self.parent)
        self.main_window.attributes("-fullscreen",True)
        ## Customer Name And ID
        self.id = id
        self.name = name
        self.empid = empid
        print(self.empid)
        self.main_window.title("Employee Main Menu")
        ## Creating an instances of Cart class to store items added to carts.
        self.cart = Cart()
## Printing ID and Name on screen
        self.id_label=tk.Label(self.main_window,text=f'Customer ID={self.id}\n Customer Name:{self.name}\n Employee ID: {self.empid}',font=("Ariel",15,"bold"))
        self.id_label.grid(row=0,column=0)

        ## Creating Three Frames
        ### Adding Frames
        self.frame = tk.Frame(self.main_window, relief='flat')
        self.frame.place(relx=0.9, rely=0.7, anchor=tk.CENTER)

        self.firstframe = tk.LabelFrame(self.main_window, text="Beverages", font=("Arial", 14, "bold"), relief='flat')
        self.firstframe.place(relx=0.1, rely=0.72, anchor=tk.W)
        self.secondframe = tk.LabelFrame(self.main_window, text="Veg Regular", font=("Arial", 14, "bold"),
                                         relief='flat')
        self.secondframe.place(relx=0.1, rely=0.2, anchor=tk.W)
        self.thirdframe = tk.LabelFrame(self.main_window, text="Veg Large", font=("Arial", 14, "bold"), relief='flat')
        self.thirdframe.place(relx=0.1, rely=0.33, anchor=tk.W)
        self.forthframe = tk.LabelFrame(self.main_window, text="NonVeg Regular", font=("Arial", 14, "bold"),
                                        relief='flat')
        self.forthframe.place(relx=0.1, rely=0.46, anchor=tk.W)
        self.fifthframe = tk.LabelFrame(self.main_window, text="NonVeg Large", font=("Arial", 14, "bold"),
                                        relief='flat')
        self.fifthframe.place(relx=0.1, rely=0.59, anchor=tk.W)
        self.fffirstframe = tk.LabelFrame(self.main_window, text="Sides", font=("Arial", 14, "bold"), relief='flat')
        self.fffirstframe.place(relx=0.1, rely=0.85, anchor=tk.W)

        #         Creating a cart button with image
        self.cart_items_Button = tk.Button(self.frame, text="Cart"
                                           , command=lambda: self.view_cart(), font=("default", 18, "bold"), background="#ffebcd")
        self.cart_items_Button.pack()
        ##Close Button
        close_button = tk.Button(self.frame, text="Close", font=("Ariel", 15, "bold"), background="#ffebcd",
                                 command=self.main_window.destroy)
        close_button.pack()

        ## Loading Pizza data & Beverages Sides
        # Loading Pizza data in pizza and bevsides class and storing the instances in the below lists
        self.pizzasV = []  # loading veg regular
        self.pizzasVL = []  # loading veg large
        self.pizzasNV = []  # loading non veg regular
        self.pizzasNVL = []  # loading non veg large
        self.bev = []  # loading bev
        self.sides = []  # loading sides
        self.load_pizza_data()

        # Create pizza frames for each pizza
        for pizza in self.bev:
            self.create_bev_frame(pizza)

        colors = ["#2e8b57", "#2e8b57", "#b22222", "#612D08"]
        for pizza, color in zip(self.sides, colors):
            self.create_sides_frame(pizza, color)

        for pizza in self.pizzasV:
            self.create_pizzasV_frame(pizza)

        for pizza in self.pizzasVL:
            self.create_pizzasVL_frame(pizza)
        for pizza in self.pizzasNV:
            self.create_pizzasNV_frame(pizza)

        for pizza in self.pizzasNVL:
            self.create_pizzasNVL_frame(pizza)



        tk.mainloop()

    def create_bev_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.firstframe, width=300, height=200, highlightthickness=2,
                               highlightbackground="black")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor=tk.W)
        add_to_cart_button = tk.Button(pizza_frame, text=f"{pizza.name} {pizza.size}",
                                       command=lambda: self.add_to_cart(pizza), font=("Arial", 15, "bold"),
                                       bg="#9bddff")
        add_to_cart_button.pack(anchor=tk.W)

    def create_sides_frame(self, pizza, color):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.fffirstframe, width=300, height=200, highlightthickness=2,
                               highlightbackground="black")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor=tk.W)
        add_to_cart_button = tk.Button(pizza_frame, text=f"{pizza.name} {pizza.size}",
                                       command=lambda: self.add_to_cart(pizza), font=("Arial", 15, "bold"), bg=color)
        add_to_cart_button.pack(anchor=tk.W)

    def create_pizzasV_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.secondframe, width=300, height=200, highlightthickness=2,
                               highlightbackground="black")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor=tk.W)
        add_to_cart_button = tk.Button(pizza_frame, text=f"{pizza.name} {pizza.size}",
                                       command=lambda: self.add_to_cart(pizza), font=("Arial", 15, "bold"),
                                       bg="#2e8b57")
        add_to_cart_button.pack(anchor=tk.W)

    def create_pizzasVL_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.thirdframe, width=300, height=200, highlightthickness=2,
                               highlightbackground="black")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor=tk.W)
        add_to_cart_button = tk.Button(pizza_frame, text=f"{pizza.name} {pizza.size}",
                                       command=lambda: self.add_to_cart(pizza), font=("Arial", 15, "bold"),
                                       bg="#2e8b57")
        add_to_cart_button.pack(anchor=tk.W)

    def create_pizzasNV_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.forthframe, width=300, height=200, highlightthickness=2,
                               highlightbackground="black")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor=tk.W)
        add_to_cart_button = tk.Button(pizza_frame, text=f"{pizza.name} {pizza.size}",
                                       command=lambda: self.add_to_cart(pizza), font=("Arial", 15, "bold"),
                                       bg="#b22222")
        add_to_cart_button.pack(anchor=tk.W)

    def create_pizzasNVL_frame(self, pizza):
        # Create a frame for the pizza
        pizza_frame = tk.Frame(self.fifthframe, width=300, height=200, highlightthickness=2,
                               highlightbackground="black")
        pizza_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor=tk.W)
        add_to_cart_button = tk.Button(pizza_frame, text=f"{pizza.name} {pizza.size}",
                                       command=lambda: self.add_to_cart(pizza), font=("Arial", 15, "bold"),
                                       bg="#b22222")
        add_to_cart_button.pack(anchor=tk.W)

    def add_to_cart(self, pizza):
        pizza_price = pizza.price
        # Create a new Pizza object with the selected size and price
        selected_pizza = Pizza(pizza.id, pizza.name, pizza_price, pizza.type, pizza.size)
        selected_pizza.quantity.set(pizza.quantity.get())
        # Check if the pizza already exists in the cart
        for item in self.cart.items:
            if item.id == selected_pizza.id:
                # Update the quantity of the existing pizza item
                item.quantity.set(item.quantity.get() + selected_pizza.quantity.get())
                break
        else:
            # Add the pizza copy to the cart
            self.cart.add_item(selected_pizza)

    def get_cart_total(self):
        return self.cart.get_total()

    def checkout(self):
        checkout_window = EmpCheckout(self.main_window, self.cart, self.id, self.empid)

    ## Loading the data of the menu itesm from the database
    def load_pizza_data(self):
        # Connect to the database
        conn = sqlite3.connect('pizza2.db')
        c = conn.cursor()
        # Retrieve the pizza data from the database Vege-R
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("Vegetarian", "Regular"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasV.append(pizza)

        # Retrieve the pizza data from the database Veg-L
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("Vegetarian", "Large"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasVL.append(pizza)

        # Retrieve the pizza data from the database NON Veg-R
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("NonVegetarian", "Regular"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasNV.append(pizza)

        # Retrieve the pizza data from the database NON Veg-L
        c.execute("SELECT * FROM Items WHERE item_type = ? AND item_size = ?", ("NonVegetarian", "Large"))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.pizzasNVL.append(pizza)

        # Retrieve the pizza data from the database BevSide
        c.execute("SELECT * FROM Items WHERE item_type = ?", ("Beverages",))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            bev = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.bev.append(bev)

        # Retrieve the pizza data from the database Side
        c.execute("SELECT * FROM Items WHERE item_type = ?", ("Sides",))
        rows = c.fetchall()
        # Create Pizza objects for each row in the database
        for row in rows:
            print(row[4])
            side = Pizza(row[0], row[1], row[2], row[3], row[4])
            self.sides.append(side)
        # Close the database connection
        conn.close()

    def view_cart(self):
        # Create a new window for the cart
        self.cart_window = tk.Toplevel(self.main_window)
        self.cart_window.title("View Cart")
        frame = tk.Frame(self.cart_window).place(relx=0.00, rely=0.00)
        # Add a label for the cart items
        cart_items_label = tk.Label(self.cart_window, text="Cart Items", font=("default", 16, "bold"))
        cart_items_label.pack()

        # Add a frame for the cart items
        cart_items_frame = tk.Frame(self.cart_window)
        cart_items_frame.pack()
        self.cart_items_frame = cart_items_frame

        # Add a label for the cart total
        self.cart_total_label = tk.Label(self.cart_window, text="Total: ${:.2f}".format(self.get_cart_total()),
                                         font=("default", 16))
        self.cart_total_label.pack()

        # Add a "Checkout" button
        checkout_button = tk.Button(self.cart_window, text="Checkout", command=self.checkout, width=10, bg="green",
                                    fg="white", font=("Arial", 10, "bold"))
        checkout_button.pack(pady=10)

        # Add a label and Spinbox for each pizza item in the cart
        for i, pizza in enumerate(self.cart.get_items()):
            # Create a frame to hold the product label and Spinbox
            product_frame = tk.Frame(cart_items_frame, bg="white")
            product_frame.grid(row=i, column=0, sticky='w', pady=10)

            product_frame1 = tk.Frame(cart_items_frame, bg="white")
            product_frame1.grid(row=i, column=2, sticky='w', pady=10)

            pizza.product_frame = product_frame
            pizza.product_frame1 = product_frame1

            # Add a label for the product name, type, and size
            product_label = tk.Label(product_frame, text="{} ({} {})".format(pizza.name, pizza.type, pizza.size),
                                     font=('Ariel', 15, "bold"), bg="white")
            product_label.grid(row=0, column=0, sticky='w')

            # Add a Spinbox for the product quantity
            quantity_spinbox = tk.Spinbox(product_frame1, from_=1, to=10, width=5, textvariable=pizza.quantity,
                                          command=lambda: self.update_cart_total(), font=('Ariel', 15, "bold"))
            quantity_spinbox.grid(row=0, column=7, padx=(10, 0))

            # Add a label for the product price
            price_label = tk.Label(product_frame, text="${:.2f}".format(pizza.price * int(pizza.quantity.get())),
                                   font=('Ariel', 15, "bold"), bg="white")
            price_label.grid(row=0, column=8, padx=(10, 0))

            # Add a "Remove" button for the pizza item
            remove_button = tk.Button(product_frame1, text="Remove",
                                      command=lambda pizza_item=pizza: self.remove_from_cart(pizza_item),
                                      font=('Ariel', 15, "bold"))
            remove_button.grid(row=0, column=9, padx=(10, 0))

            # Add the price label to the pizza item for later use
            pizza.price_label = price_label

    def update_cart_total(self):
        # Update the price labels for each pizza item in the cart
        for pizza in self.cart.get_items():
            pizza.price_label.config(text="${:.2f}".format(pizza.price * int(pizza.quantity.get())))

        # Update the cart total label with the new total
        self.cart_total_label.config(text="Total: ${:.2f}".format(self.get_cart_total()))

    def remove_from_cart(self, pizza_item):
        # Check if the pizza item is in the items list
        if pizza_item in self.cart.items:
            # Remove the pizza item from the cart's items list
            self.cart.items.remove(pizza_item)
            # Update the cart items and total labels
            self.update_cart_total()
            # Destroy the product frames associated with the pizza item
            pizza_item.product_frame.destroy()
            pizza_item.product_frame1.destroy()


if __name__ == "__main__":
    # lg = LoginPage()
    # mm = MainMenu("CUS1","Anurag")
    eee = EmpMenu("EMP1","AG")

