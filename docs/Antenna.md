# `Antenna` class

This class acts primarily as a data structure. It does not have any methods besides initialization.

The `Antenna` class is a bit of a misnomer, as it initializes with data that is both related to a selected antenna, and a selected radio. For simplicity, this single class was kept instead of making two separate classes.

This class is added to each balloon (node), so that a proper comms link can be calculated between the nodes.

## Initialization

```py
# example from http://www.saturnpcb.com/wp-content/datasheets/SPCBD-S102-07_Datasheet.pdf
# and Xbee Pro SX module
SaturnPatch = Antenna(name="Saturn Patch Antenna",
                      gain=3.3,
                      freq=915,
                      hpbw=70,
                      radio_type=RadioType.TwoWay, # from RadioType enum
                      tpwr=13,
                      sensitivity=-113)
```

## Methods

None.

## `Antenna` data

- `name`: Name of the antenna/radio system
- `gain`: Antenna's rated gain in dB
- `freq`: Frequency of communication
- `hpbw`: The half-power beam width of the antenna (see [this link](https://www.exfo.com/en/resources/glossary/hpbw/))
- `radio_type`: Type of the radio. Can it accept messages, or only transmit?
- `tpwr`: Transmitter power
- `sensitivity`: Radio sensitivity (minimum power to receive)