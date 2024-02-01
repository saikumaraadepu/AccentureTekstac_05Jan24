select venue_id, venue_name, location, venue_cost
from venue_master
where wifi='Yes'and location not in ('New York','Austin')
order by venue_cost;