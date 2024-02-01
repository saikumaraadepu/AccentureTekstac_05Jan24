select e.category,v.venue_name,v.capacity
from event_master e,venue_master v
where e.event_id=v.event_id and
capacity=(select max(v2.capacity)
from venue_master v2
where e.event_id=v2.event_id);