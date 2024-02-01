select venue_id,venue_name,venue_cost,location
from venue_master
where capacity between 1000 and 20000
order by venue_name;