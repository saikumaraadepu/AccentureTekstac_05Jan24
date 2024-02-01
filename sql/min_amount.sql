select mode_of_pay, min(total_amount)as minimum_total_amount
from booking_master
where mode_of_pay in('Cash','Online')
group by mode_of_pay
order by minimum_total_amount;