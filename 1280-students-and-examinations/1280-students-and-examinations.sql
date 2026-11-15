# Write your MySQL query statement below
Select Students.student_id, Students.student_name, Subjects.subject_name, Count(Examinations.student_id) as attended_exams
From Students
Cross Join Subjects
Left Join Examinations 
On Students.student_id = Examinations.student_id and Subjects.subject_name = Examinations.subject_name
Group by Students.student_id, Students.student_name, Subjects.subject_name
Order by Students.student_id, Subjects.subject_name;