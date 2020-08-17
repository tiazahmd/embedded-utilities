## Bit Band Address Generator
This program takes in a GPIO port and a pin then applies bit band formula to derive to a bit banded address for that port and pin.

## Compatibility
This program has been tested with with Nucleo F411RE board, which uses ARM Cortex M4 processor. A snapshot of its memory map can be found below for reference.

## Formula:
Alias Base Region = The very base where the alias region starts for that particular GPIO

Bit Band Region Base = The base address where the bit band region starts

Bit number = Pin number
``` 
Region Base Offset = SF Register Base - Bit Band Region Base
Bit Band Address = Alias Region Base + (Region Base Offset x 32) + (Bit number x 4)
```

![Memory Map and Bit Banding Regions](https://i.imgur.com/yF5sylK.png)

![GPIO Memory Addresses](https://i.imgur.com/kqq4rPK.png)