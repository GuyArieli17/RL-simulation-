Roadnet File Format
===================
The simulation(cityflow) use this json file to build the road map on wich the vehicle drive. 
The file compose of 2 main 'objects' wich determined it behaviour: `intersections` , `roads`.

### intersections 
object|description
------|-------------------------
`id` |uniq string.
`point`| the intersection centered coordinate `x` , `y`
`width`| the height or length of the intersection
`roads`| id's of roads connected to the intersection(max.6)
`roadLinks`| list of possible route from one road to another trhow the intersection Object <br> `type`: "turn_left" \ "turn_right" \ "go_straight", <br>`startRoad`: from road-id ,<br>`endRoad`: to road-id <br> `laneLinks`: array of lane movment inside the intersection
`trafficLight` | include `lightphases` wich determined th phase (period,and wich lanes).
`virtual` | true if it's a peripheral intersection (if it only connects to one road).
                
### roads
object|description
------|-------------------------
`id` | uniq string
`startIntersection` | id of the intersection we start from
`endIntersection` | id of the intersection we end in
`points`| array of start of the road and end point in `x`,`y` axis
`lanes` | array of lane {`width`: 4, `maxSpeed`: 16.67}
