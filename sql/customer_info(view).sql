create view customer_info as
(select c.c_first_name,c.phoneno,c.city,b.total_amount
from customer_master c,enquiry_master e,booking_master b
where c.cust_id=e.cust_id and e.enquiry_id=b.enquiry_id and
b.total_amount<60000
order by c_first_name);