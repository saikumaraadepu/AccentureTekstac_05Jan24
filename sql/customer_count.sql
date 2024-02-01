select count(cust_id)as ENQUIRY_COUNT
from enquiry_master
group by cust_id 
having ENQUIRY_COUNT>1
order by ENQUIRY_COUNT desc;