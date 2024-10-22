# C167BootTool
C167 / ST10 Boostrap mode tool, R/W ext. Flash, read int Rom/Flash, R/W ext SPI/I2C EEProm

For educational purposes only!

Usage:

BootMode Tool for me(d)7 , Simos 3.x & EDC15VM/P+ Variants inspired by ArgDub , 360trev and Gremlin
***********

 type -h for this help
 Arguments in [] are optional:

-------------------- Read EEProm--------------------
    ME7BootTool  baudrate  -readeeprom -PeriphType  eepromtype Port(of chip select) Pin(of chip select) size(hex or dezimal)  [filename]
eg: ME7BootTool  9600      -readeeprom -XSSC         1         Port4                Pin7                0x100                 551Eeprom.ori
eg: ME7BootTool  28800     -readeeprom -SSC          1         Port4                Pin7                0x200                 551Eeprom.ori

eg: ME7BootTool  28800     -readeeprom -I2C          11                                                 0x200                 551Eeprom.ori
----------------------------------------------------

-------------------- Write EEProm--------------------
    ME7BootTool  baudrate  -writeeeprom -PeriphType eepromtype Port(of chip select) Pin(of chip select) filename
eg: ME7BootTool  9600      -writeeeprom -XSSC         1        Port6                Pin3                551ImmoOff.bin
eg: ME7BootTool  28800     -writeeeprom -SSC          1        Port6                Pin3                551ImmoOff.bin

eg: ME7BootTool  28800     -writeeeprom -I2C         11                                                 551ImmoOff.bin
----------------------------------------------------

-------------------- Parameters for R/W EEProm--------------------

type of eeprom is 0 for 95080 to 95320, 1 for 95040 or 95p08,
2 for 93S46 with 6bit address, 3 for 93S56 or 93S66 with 8 bit address, 4 for 93S76 or 93S86 with 10 bit address
10 for 24c02 with 8bit address, 11 for 24c04 with 9bit address

Chip select for eeprom: Port2,3,4,6,7,8 are supported, pins 0-15; ME7.5 & 7.1 P4.7; ME7.1.1 P6.3 ; SIMOS 3.2 is P6.4
 -PeriphType : -SSC for C16x or ST10, -XSSC for ST10 and XC167 (only type 0 and 1 supported),
 -PeriphType : -I2C for EDC15VM/P+ (only type 10 and 11 supported)
----------------------------------------------------

-------------------- read internal Rom or Flash (IROM, IFLASH) --------------------
     ME7BootTool  baudrate  -readInt    size(hex or dezimal)  [filename]
 eg: ME7BootTool  28800     -readInt    0x8000                551IntRom.ori
----------------------------------------------------

-------------------- read external Flash --------------------
     ME7BootTool  baudrate  -readextflash   size(hex or dezimal)  [filename]
 eg: ME7BootTool  28800     -readextflash   0x80000                551extFlash.ori
----------------------------------------------------

-------------------- write external Flash --------------------
     ME7BootTool  baudrate  -writeextflash  filename Ecu/FlashType (ME7, Simos3, EDC15)
eg:  ME7BootTool  28800     -writeextflash  551extFlash.bin         simos3
eg:  ME7BootTool  57600     -writeextflash  551extFlash.bin         me7
eg:  ME7BootTool  57600     -writeextflash  551extFlash.bin         edc15
----------------------------------------------------

-------------------- Baudrate --------------------
 standard rates: 9600, 19200, 28800, 38400, 57600, 115200 ; depending on cable 115200 or 57600 may not work
