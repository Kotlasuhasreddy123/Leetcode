# Write your MySQL query statement below
Select customer_number 
From Orders
Group by customer_number
Order by count(order_number) desc
limit 1;