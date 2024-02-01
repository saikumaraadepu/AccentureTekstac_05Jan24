select enquiry_id,cust_id,venue_id,
monthname(start_date)as month_name,
datediff(end_date,start_date)+1 as no_of_days
from enquiry_master
where monthname(start_date)='December'
order by no_of_days desc;