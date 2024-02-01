select c.cust_id,c.c_first_name,c.city,c.phoneno
from customer_master c left join
enquiry_master e
on c.cust_id=e.cust_id
where e.venue_id is null
order by c.c_first_name;