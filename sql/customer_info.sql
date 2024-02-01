select concat(c_first_name,' lives in ',city,
' and ',case when gender='Male' then 'his' when gender='Female' then 'her' end,
' phone number is ',phoneno)as customer_Info
from customer_master
order by c_first_name desc;