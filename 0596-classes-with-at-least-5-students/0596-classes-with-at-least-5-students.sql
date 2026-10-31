# Write your MySQL query statement below
Select class from Courses
Group by class
Having count(class) >= 5;