Roadnet File Format
===================
The simulation(cityflow) use this json file to build the road map on witch the vehicle drive. \n
The file compose of 3 main 'objects':
  * dsfgfg
  * dssfsdf
the rest
```js

  {
    "intersections": [
      {
        // id of the intersection
        "id": "intersection_1_0",
        // coordinate of center of intersection
        "point": { 
          "x": 0,
          "y": 0
        },
        // width of the intersection
        "width": 10,
        // roads connected to the intersection
        "roads": [
          "road_1",
          "road_2"
        ],
        // roadLinks of the intersection
        "roadLinks": [
          {
            // 'turn_left', 'turn_right', 'go_straight'
            "type": "go_straight",
            // id of starting road
            "startRoad": "road_1",
            // id of ending road
            "endRoad": "road_2",
            // lanelinks of roadlink
            "laneLinks": [ 
              {
                // from startRoad's startLaneIndex lane to endRoad's endLaneIndex lane
                "startLaneIndex": 0, 
                "endLaneIndex": 1,
                // points along the laneLink which describe the shape of laneLink
                "points": [
                  {
                    "x": -10,
                    "y": 2
                  },
                  {
                    "x": 10,
                    "y": -2
                  }
                ]
              }
            ]
          }
        ],
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
