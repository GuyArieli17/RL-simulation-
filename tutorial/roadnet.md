Roadnet File Format
===================
The simulation(cityflow) use this json file to build the road map on witch the vehicle drive. 
The file compose of 2 main 'objects' witch determined it behaviour: `intersections` , `roads`.

### intersections 
object|description
------|-------------------------
`id` |uniq string.
`point`| the intersection centered coordinate `{"x": num1,"y":num2}`
`width`| the height or length of the intersection
`roads`| id's of roads connected to the intersection(max.6)
`roadLinks`| list of possible route from one road to another trhow the intersection<br>
             {
                `type`: ,
                `startRoad`: "road_1",
                `endRoad`: "road_2",
                `laneLinks`: [
                  {
                    `startLaneIndex`: 0, 
                    `endLaneIndex`: 1,
                    // points along the laneLink which describe the shape of laneLink
                    `points`: [
                      {
                        `x`: -10,
                        `y`: 2
                      },
                      {
                        `x`: 10,
                        `y`: -2
                      }
                    ]
                  }
                ]
             
             
             
             }



### roads
```js

  {
    "intersections": [
      {
        // traffic light plan of the intersection
        "trafficLight": {
          "lightphases": [
            {
              // default duration of the phase
              "time": 30,
              // available roadLinks of current phase, index is the no. of roadlinks defined above.
              "availableRoadLinks": [
                0,
                2
              ]
            }
          ]
        },
        // true if it's a peripheral intersection (if it only connects to one road)
        "virtual": false
      }
    ],
    "roads": [
      {
        // id of road
        "id": "road_1",
        // id of start intersection
        "startIntersection": "intersection_1",
        // id of end intersection
        "endIntersection": "intersection_2",
        // points along the road which describe the shape of the road
        "points": [
          {
            "x": -200,
            "y": 0
          },
          {
            "x": 0,
            "y": 0
          }
        ],
        // property of each lane
        "lanes": [
          {
            "width": 4,
            "maxSpeed": 16.67
          }
        ]
      }
    ]
  }
```
