select c_first_name,phoneno,gender
from customer_master
where c_last_name is null or c_middle_name is null
order by phoneno;