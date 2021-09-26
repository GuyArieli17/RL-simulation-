Roadnet File
======

.. code-block:: js
"intersections": [
        {
            // eatch intersection has to have id 
          
            "id": "intersection_0_0",
            // where is intersection on y x axis
            "point": {
                "x": 0,
                "y": 0
              },
            // the with (size\length) of the intersection
            "width": 10,
            // roads that connected to the intersections
            "roads": [
                "road_0_0_0",
                "road_0_0_1",
                "road_1_0_0",
                "road_1_0_1"
              ],
            // what route u can take trhow this intersection
            "roadLinks": [
                {
                    "type": "go_straight", // can be left\right\strgth
                    "startRoad": "road_0_0_0",// from 
                    "endRoad": "road_1_0_1",// to
                    // from witch lane to witch lane u can go
                    "laneLinks": [
                        {
                            "startLaneIndex": 0, from lane 
                            "endLaneIndex": 0, to lane
                            "points": [
                                {
                                    "x": 2,
                                    "y": -5
                                },
                                {
                                    "x": 2,
                                    "y": 5
                                }
                            ]
                        }
                    ]
                }
            ],
            // trafic light in the intersection
            "trafficLight": {
                the pases of the trafic light
                "lightphases": [
                    {
                        "time": 30,
                        "availableRoadLinks": [
                            0
                        ]
                    },
                    {
                        "time": 5,
                        "availableRoadLinks": [
                            
                        ]
                    }
                ]
            },
            // if has then one road connected so false
            "virtual": false
        },

That was my JSON code block.
