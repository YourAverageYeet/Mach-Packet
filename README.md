#  Mach Packet

### Usage:
> `python main.py file0.txt [file1.txt [...]]`

A simple Python "toy packet" class I made after learing how actual packets work.

The packets *do* have nearly all internal information, like a header, footer, and CRC, but are still a little incomplete.

Current planned additions are:
+ Add a counter inside the packet for track which one it is in a series
+ Create a command line option for writing to a file (currently does so by default)
+ Create dedicated storage and retrieveal functions for hardcopy storage

(C<-) YourAverageYeet
