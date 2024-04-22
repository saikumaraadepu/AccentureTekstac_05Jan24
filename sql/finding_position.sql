select c_first_name, position('m' in c_first_name) as position
from Customer_Master
where City in ('Los Angeles', 'Boston')
order by position desc, c_first_name asc;
