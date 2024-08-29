from components.networkanalyzer import Antenna, RadioType

CSSlot = Antenna(name="CubeSat Slot (#F)",
                    gain=4.98,
                    freq=5030,
                    hpbw=90,
                    radio_type=RadioType.TwoWay,
                    tpwr=30,
                    sensitivity=-115)

VHF = Antenna(name="Dual Band VHF/UHF Antenna (#G)",
                    gain=2.06,
                    freq=146,
                    hpbw=80,
                    radio_type=RadioType.TwoWay,
                    tpwr=22,
                    sensitivity=-104)

CPXband = Antenna(name="Circularly Polarized X-band Antenna",
                    gain=20.03,
                    freq=8020,
                    hpbw=40,
                    radio_type=RadioType.TwoWay,
                    tpwr=40,
                    sensitivity=-100)

TpCBand = Antenna(name="Transparent C-Band",
                    gain=5.9,
                    freq=5100,
                    hpbw=45,
                    radio_type=RadioType.TwoWay,
                    tpwr=30,
                    sensitivity=-115)

PrintedDipole = Antenna(name="Printed Dipole",
                    gain=3.49,
                    freq=2450,
                    hpbw=50,
                    radio_type=RadioType.TwoWay,
                    tpwr=30,
                    sensitivity=-108)

LoadedDipole = Antenna(name="Loaded Dipole",
                    gain=3.91,
                    freq=435,
                    hpbw=10000,
                    radio_type=RadioType.TwoWay,
                    tpwr=10,
                    sensitivity=-118)