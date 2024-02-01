select c1.c_first_name,c2.c_first_name,c1.city,e1.venue_id
from customer_master c1,customer_master c2, enquiry_master e1,enquiry_master e2
where c1.city=c2.city and c1.cust_id!=c2.cust_id and c2.cust_id!=c1.cust_id and
c1.cust_id=e1.cust_id and c2.cust_id=e2.cust_id and 
e1.venue_id=e2.venue_id;