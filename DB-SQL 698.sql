-- create database pizza;

USE  pizza;





-- Create CustomersInformation table
CREATE TABLE CustomersInformation (
  Customer_ID VARCHAR(20) PRIMARY KEY,
  First_Name TEXT NOT NULL,
  Middle_Name TEXT,
  Last_Name TEXT NOT NULL,
  Address VARCHAR(100),
  City TEXT,
  State TEXT,
  ZipCode VARCHAR(10),
  Phone_Number VARCHAR(20) NOT NULL,
  Username VARCHAR(50),
  Password VARCHAR(150),
  Email_ID VARCHAR(50) NOT NULL,
  constraint CHECK_PHONE CHECK(CHAR_LENGTH(Phone_Number) = 10),
  CONSTRAINT check_email_format CHECK (Email_ID REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')  
);

-- Create EmployeeInformation table
CREATE TABLE EmployeeInformation (
  Employee_ID VARCHAR(20) PRIMARY KEY,
  First_Name TEXT NOT NULL,
  Middle_Name TEXT,
  Last_Name TEXT NOT NULL,
  Address VARCHAR(100),
  City TEXT,
  State TEXT,
  ZipCode VARCHAR(10),
  Phone_Number VARCHAR(20) NOT NULL,
  Username VARCHAR(50),
  Password VARCHAR(150) NOT NULL,
  Email_ID VARCHAR(50) NOT NULL,
  constraint CHECKEMP_PHONE CHECK(CHAR_LENGTH(Phone_Number) <= 10),
  CONSTRAINT checkEMP_email_format CHECK (Email_ID REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$') 
);






-- Create Orders table
CREATE TABLE Orders (
  Order_ID INT PRIMARY KEY ,
  Customer_ID VARCHAR(20),
  Employee_ID VARCHAR(20),
  Order_Date DATETIME NOT NULL,
  Order_Total DECIMAL(10,2) NOT NULL,
  Order_Qty INT NOT NULL,
  Order_Ratings INT DEFAULT 0 CHECK(Order_Ratings >= 0 AND Order_Ratings <= 5),
  FOREIGN KEY(Customer_ID) REFERENCES CustomersInformation(Customer_ID),
  FOREIGN KEY(Employee_ID) REFERENCES EmployeeInformation(Employee_ID)
);

-- Create Items table
CREATE TABLE Items (
  item_ID INT PRIMARY KEY,
  item_name TEXT NOT NULL,
  item_price DECIMAL(10,2) NOT NULL,
  item_type TEXT NOT NULL,
  item_size TEXT
);
-- Create Order_Item table
CREATE TABLE Order_Item (
  Order_ID INT,
  item_ID INT,
  item_Quantity INT NOT NULL,
  PRIMARY KEY (Order_ID, item_ID),
  FOREIGN KEY(Order_ID) REFERENCES Orders(Order_ID),
  FOREIGN KEY(item_ID) REFERENCES Items(item_ID)
);

-- Create Order_Status table
CREATE TABLE Order_Status (
  Order_ID INT PRIMARY KEY,
  Order_Status TEXT NOT NULL,
  FOREIGN KEY(Order_ID) REFERENCES Orders(Order_ID),
  CONSTRAINT chk_Order_Status CHECK(Order_Status IN ('Pending', 'Preparing', 'Ready', 'Cancelled'))
);



-- Create Payment table
CREATE TABLE Payment (
  Invoice_Num varchar(50),
  MOP TEXT NOT NULL CHECK(MOP IN ("Cash","Card")),
  Order_ID INT NOT NULL, 
  Customer_ID VARCHAR(20),
  Order_Date DATE NOT NULL,
  Amount_Paid DECIMAL(10,2) NOT NULL,
  FOREIGN KEY(Customer_ID) REFERENCES CustomersInformation(Customer_ID),
  FOREIGN KEY(Order_ID) REFERENCES Orders(Order_ID)
);




INSERT INTO Items (item_id, item_name, item_price, item_type, item_size) 
VALUES (3001, 'Cheese Pizza', 8.99, 'Vegetarian', 'Regular'),
       (3002, 'Cheese Pizza', 13.99, 'Vegetarian', 'Large'),
       (3003, 'Margherita', 10.99, 'Vegetarian', 'Regular'),
       (3004, 'Margherita', 15.99, 'Vegetarian', 'Large'),
       (3005, 'Mushroom', 9.99, 'Vegetarian', 'Regular'),
       (3006, 'Mushroom', 14.99, 'Vegetarian', 'Large'),
       (3007, 'Grilled Vegetables', 11.99, 'Vegetarian', 'Regular'),
       (3008, 'Grilled Vegetables', 16.99, 'Vegetarian', 'Large'),
       (4000, 'Chicken Tandoori', 12.99, 'NonVegetarian', 'Regular'),
       (4001, 'Chicken Tandoori', 17.99, 'NonVegetarian', 'Large'),
       (4002, 'Pepperoni', 10.99, 'NonVegetarian', 'Regular'),
       (4003, 'Pepperoni ', 15.99, 'NonVegetarian', 'Large'),
       (4004, 'Grilled Chicken', 11.99, 'NonVegetarian', 'Regular'),
       (4005, 'Grilled Chicken', 16.99, 'NonVegetarian', 'Large'),
       (4008, 'Hawaiian', 12.99, 'NonVegetarian', 'Regular'),
       (4009, 'Hawaiian ', 17.99, 'NonVegetarian', 'Large');
       
INSERT INTO Items (item_id, item_name, item_price, item_type) 
VALUES (100, 'Dite Coke', 1.99, 'Beverages'),
       (101, 'Coke', 1.99, 'Beverages'),
       (102, 'Mountain Dew', 1.99, 'Beverages'),
       (104, 'Dr.Pepper', 2.99, 'Beverages'),
       (201, 'Garlic Bread', 6.99, 'Sides'),
       (202, 'Potato Wedges', 5.99, 'Sides'),
       (203, 'Chicken Wings', 12.00, 'Sides'),
       (204, 'Choco Lava', 3.99, 'Sides');




SELECT * FROM Customersinformation;
SELECT * FROM Employeeinformation;
select * from Orders;
select * from Order_Item;
select * from items;
select * from Order_Item;
select * from payment;
select * from order_status;










