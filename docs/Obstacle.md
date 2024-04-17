# `Obstacle` class

Provides the ability to add obstacles in the network, accounting for situations or losses that could occur that aren't strictly modeled by TrajVis. Obstacles are dependent on chance; for example, if "Node B is unreachable 40% of the time", that can be modeled using this class.

Currently, two types of obstacles are supported:

1. `ReceiverPower`: on some chance, the receiver power of a given node is modified. This is useful for any other types of losses one would like to introduce into the system, or the degradation of the comms system on one of the nodes.

2. `DeadNode`: on some chance, a node can be marked as "dead" for either transmission, receiving packets, or both. 

## Initialization

```py
# for ReceiverPower obstacle
config = {
    'modifier': # float, in dB
    'appliesTo': # [Balloon().name, Balloon().name,...]
    'chance': # float, 0-1
}

# for DeadNode obstacle
config = {
    'node': # Balloon()
    'type': # "tx", "rx", or "both"
    'chance': # float, 0-1
}

MyObstacle = Obstacle(ObstacleType, config) # ObstacleType is an enum representing all possible obstacles
```

## Utilization

Obstacles are added at the Network stage.

```py
MyNetwork.add_obstacle(Obstacle)
```