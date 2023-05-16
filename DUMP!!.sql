
SET FOREIGN_KEY_CHECKS = 0;
INSERT INTO Orders (Order_ID, Customer_ID, Order_Date, Order_Total, Order_Qty, Order_Ratings)
VALUES (17, 'CUS1', '2023-03-16 09:30:00', 37.97, 3, 3),
(18, 'CUS2', '2023-03-16 12:45:00', 49.98, 4, 4),
(19, 'CUS3', '2023-03-16 14:15:00', 23.95, 2, 5),
(20, 'CUS4', '2023-03-16 15:30:00', 41.97, 3, 0),
(21, 'CUS5', '2023-02-18 17:00:00', 27.96, 2, 0),
(22, 'CUS6', '2023-02-18 18:30:00', 19.97, 1, 0),
(23, 'CUS7', '2023-02-18 20:00:00', 59.96, 5, 0),
(24, 'CUS8', '2023-02-18 21:15:00', 15.95, 1, 0);

-- Insert into Order_Items table
INSERT INTO Order_Item (Order_ID, item_ID, item_Quantity)
VALUES (17, 3006, 1),
(17, 101, 1),
(17, 203, 1),
(18, 4009, 1),
(18, 3008, 1),
(18, 204, 2),
(18, 103, 1),
(19, 201, 1),
(19, 202, 1),
(20, 4004, 1),
(20, 100, 2),
(21, 3001, 1),
(21, 102, 1),
(22, 204, 1),
(23, 4001, 1),
(23, 4005, 2),
(23, 202, 1),
(23, 103, 1),
(23, 104, 2),
(24, 203, 1);

-- Insert into Payment table
INSERT INTO Payment (Invoice_Num, MOP, Order_ID, Customer_ID, Order_Date, Amount_Paid)
VALUES ('2023031609300017', 'Card', 17, 'CUS1', '2023-03-16', 37.97),
('2023031612450018', 'Cash', 18, 'CUS2', '2023-03-16', 49.98),
('2023031614150019', 'Card', 19, 'CUS3', '2023-03-16', 23.95),
('2023031615300020', 'Cash', 20, 'CUS4', '2023-03-16', 41.97),
('2023021817000021', 'Card', 21, 'CUS5', '2023-02-18', 27.96),
('2023021818300022', 'Cash', 22, 'CUS6', '2023-02-18', 19.97),
('2023021820000023', 'Card', 23, 'CUS7', '2023-02-18', 59.96),
('2023021821150024', 'Cash', 24, 'CUS8', '2023-02-18', 15.95);

-- Insert into Order_Status table
INSERT INTO Order_Status (Order_ID, Order_Status)
VALUES (17, 'Ready'),
(18, 'Preparing'),
(19, 'Ready'),
(20, 'Ready'),
(21, 'Ready'),
(22, 'Ready'),
(23, 'Ready'),
(24, 'Ready');


SET FOREIGN_KEY_CHECKS = 1;