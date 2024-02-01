select c.c_first_name, sum(b.total_amount)as total_booking_amount
from customer_master c,enquiry_master e,booking_master b
where c.cust_id=e.cust_id and e.enquiry_id=b.enquiry_id
group by c.c_first_name
having sum(b.total_amount)>=all(select avg(b.total_amount)
from enquiry_master e, booking_master b
where e.enquiry_id=b.enquiry_id
group by e.cust_id)
order by c.c_first_name;