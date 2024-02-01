select v.venue_id,v.venue_name,v.location,m.maximumcost,m.minimumcost
from venue_master v join (
select venue_id, max(venue_cost)as maximumcost, min(venue_cost)as minimumcost
from venue_master
group by venue_id) m
where v.venue_id=m.venue_id
order by venue_cost;