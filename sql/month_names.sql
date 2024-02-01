select enquiry_id,cust_id,
date_format(start_date,'%M,%Y')as Event_Date
from enquiry_master
where year(start_date)>2015
order by Event_Date asc,cust_id asc;