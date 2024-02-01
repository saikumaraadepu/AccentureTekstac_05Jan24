select venue_name, venue_cost,
case 
when venue_cost between 50000 and 200000 then 'Medium Cost'
when venue_cost < 50000 then 'Low Cost'
when venue_cost > 200000 then 'High Cost'
end as cost_category
from venue_master
order by capacity desc;