# `NetworkAnalyzer` Class

This class is separate from the `Network` class, which does most of the heavy lifting of simulating the network between all of the nodes. This instead helps to analyze the network at a certain time, calculating losses, distances, and plotting attitudes.

The main indicator of a healthy signal between any two nodes is classified in TrajVis by the receiver power between them. This means we need to use some simple radio comms link analysis to calculate the power in relation to a couple different considered losses: 

- Pointing loss: If using an antenna that is directional (non-isotropic) there will be loss the more "misaligned" the antennas are.
- Free space loss: Loss related to the inverse square law.

> Note: Within this doc, the terms "balloon" and "node" are interchangeable.

## Initialization

```py
MyNetworkAnalyzer = NetworkAnalyzer(b1, b2, b3...) # all balloons part of the network 
```

## Methods

### NetworkAnalyzer.show_pointing()

Create a 3D plot showing the direction of the antennas on all of the balloons.

### NetworkAnalyzer.rp_all(time)

Calculate the receiver power between all pairs of nodes at a given time. Will print the output.

### NetworkAnalyzer.rp(time, tx_node, rx_node)

Calculate the receiver power between a given tx and rx node (`Balloon()` type) at a given time.

## `NetworkAnalyzer` data

None.