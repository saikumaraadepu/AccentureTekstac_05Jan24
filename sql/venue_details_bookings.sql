select v.venue_id,v.venue_name,v.location,em.category
from venue_master v,event_master em
where v.event_id=em.event_id and 
(select count(*) from booking_master b1,
enquiry_master eq1
where b1.enquiry_id=eq1.enquiry_id and 
eq1.venue_id=v.venue_id)=(select count(*)
from booking_master b2,
enquiry_master eq2
where b2.enquiry_id=eq2.enquiry_id and
eq2.venue_id='V10') and v.venue_id!='V10'
order by v.venue_name desc;