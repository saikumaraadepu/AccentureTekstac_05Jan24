select e.cust_id,b.booking_id,datediff(end_date,start_date)+1 as Days
from enquiry_master e,booking_master b
where e.enquiry_id=b.enquiry_id and datediff(end_date,start_date)+1 >3
order by e.cust_id desc;