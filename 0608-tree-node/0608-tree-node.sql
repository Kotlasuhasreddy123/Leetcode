# Write your MySQL query statement below
Select id, 
Case
When p_id is null then 'Root'
When id in (Select p_id from Tree) Then 'Inner'
Else 'Leaf'
End as Type
From Tree;