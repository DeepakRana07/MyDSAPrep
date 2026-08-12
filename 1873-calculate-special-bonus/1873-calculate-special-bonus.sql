# Write your MySQL query statement below


select employee_id , 

case  
when mod(employee_id,2) != 0 
and 
lower(substr(name,1,1))!='m' then salary
else 0

end as bonus from employees order by employee_id;
