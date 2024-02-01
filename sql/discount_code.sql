select distinct c.c_first_name,
concat(substr(c.c_first_name,1,3), substr(c.phoneno,1,3))as Discount_Code
from customer_master c,enquiry_master e,booking_master b
where c.cust_id=e.cust_id and e.enquiry_id=b.enquiry_id
and c.city in('Los Angeles','Boston') and 
b.total_amount>50000
order by c_first_name;