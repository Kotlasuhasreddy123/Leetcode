# Write your MySQL query statement below
Select 
Date_Format(trans_date, "%Y-%m") as month,
country,
Count(*) as trans_count,
Sum(if(state = "approved", 1, 0)) as approved_count,
Sum(amount) as trans_total_amount,
Sum(if(state = "approved", amount, 0)) as approved_total_amount
from Transactions
Group by month, country;