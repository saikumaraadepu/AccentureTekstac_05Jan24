select c_first_name,c_last_name,street,city
from customer_master
where c_first_name like '_m%'
order by c_first_name;