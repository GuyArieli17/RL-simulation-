.. _roadnet:

Roadnet File Format
===================

Roadnet file defines the roadnet structure. CityFlow's roadnet mainly consists of intersections and roads (see them as nodes and edges of a graph). 

- *Road* represents a directional road from one *intersection* to another *intersection* with road-specific properties. A *road* may contain multiple *lanes*. 
- *Intersection* is where roads intersects. An *intersection* contains several *roadlinks*. Each *roadlink* connects two roads of the intersection and can be controlled by traffic signals. 
- A *roadlink* may contain several *lanelinks*. Each lanelink represents a specific path from one lane of incoming road to one lane of outgoing road. 

Now let's see a sample roadnet file and we'll explain the meaning of each components. Relax, the definition of field is quite straight forward, if you are familiar with modern road networks. For the following json file, ``[]`` means this field is an array, but we will only show one object for demonstration. 

```javascript
{ "some": "json" }
```

 bla bla blas


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


.. figure:: https://github.com/cityflow-project/data/raw/master/docs/images/roadnet.jpg
    :align: center

    Illustration of a 1x2 grid roadnet.


You can convert SUMO roadnet files into CityFlow format using tools/Converter/converter.py

For example, the following code converts a sumo roadnet file, atlanta.net.xml, to CityFlow format.

.. code-block:: shell

    python converter.py --sumonet atlanta_sumo.net.xml --cityflownet atlanta_cityflow.json
