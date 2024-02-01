select distinct c.cust_id, c_first_name, phoneno, email
from customer_master c join enquiry_master e join booking_master b
where c.cust_id=e.cust_id and e.enquiry_id=b.enquiry_id and 
b.mode_of_pay='Online'
order by c.cust_id;