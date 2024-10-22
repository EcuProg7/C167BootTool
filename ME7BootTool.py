
import os;
import serial;
import serial.tools;
import serial.tools.list_ports;
import time;
import sys;
import traceback

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def ResetAdapter(ser):
    ser.setDTR(1);
    time.sleep(0.1);
    ser.setDTR(0);
    time.sleep(0.1);

def SetAdapterKKL(ser):
    ser.setDTR(0);
    ser.setRTS(0);
    time.sleep(0.1);


def SendCharwEcho(ser, data):
    #time.sleep(self.sleeptime);
##    now = time.time()
##    while( time.time() < now + self.sleeptime):
##        pass
    ret = True;
    ser.write(data);
    #time.sleep(self.sleeptime);
    echo = ser.read(1)
    if(len(echo) != 0):
        if(echo[0] != data[0]):
            print("echo error sent: ", hex(data[0])," received: ", hex(echo[0]))
            ret = False;
    else:
        print("got no echo")
    return ret;

def SendDatawEcho(ser, data):
##    for d in data:
##        #print("sendDatawEcho char: ", hex(d))
##        SendCharwEcho(ser,[d]);
    ser.write(data);
    echo = ser.read(len(data))

    if(len(echo) != len(data)):
        print("got wrong echo length")
        return False;

    counter = 0
    while counter < len(data):
        if(data[counter] != echo[counter]):
            print("echo error sent: ", hex(data[counter])," received: ", hex(echo[counter]), "at data pos : ", hex(counter))
            ret = False;
        counter += 1

    return True;



def GetAddressAsLittleEndian(address):
    add = [ (address)&0xff, (address>>8)&0xff, (address>>16)&0xff,];
    return add;

def GetWordAsLittleEndian(data):
    add = [ (data)&0xff, (data>>8)&0xff];
    return add;

I_LOADER_STARTED	        = 0x01	#// Loader successfully launched
I_APPLICATION_LOADED	= 0x02	#// Application succ. loaded
I_APPLICATION_STARTED	= 0x03	#// Application succ. launched
I_AUTOBAUD_ACKNOWLEDGE      = 0x04  #// Autobaud detection acknowledge

A_ACK1			    =0xAA  	#// 1st Acknowledge to function code
A_ACK2			    =0xEA	#// 2nd Acknowledge (last byte)
A_ASC1_CON_INIT		    =0xCA	#// ASC1 Init OK
A_ASC1_CON_OK		    =0xD5	#// ASC1 Connection OK

C_WRITE_BLOCK		    =0x84 #// Write memory block to target mem
C_READ_BLOCK		    =0x85 #// Read memory block from target mem
C_EINIT			    =0x31 #// Execute Einit Command
C_SWRESET		   	    =0x32 #// Execute Software Reset
C_GO			    =0x41 #// Jump to user program
C_GETCHECKSUM    	            =0x33 #// get checksum of previous sent block
C_TEST_COMM		   	    =0x93 #// Test communication
C_CALL_FUNCTION		    =0x9F#	// Mon. extension interface: call driver
C_WRITE_WORD		    =0x82 #// write word to memory/register
C_MON_EXT		            =0x9F#	// call driver routine
C_ASC1_CON		      	    =0xCC #// Connection over ASC1
C_READ_WORD	  	      	    =0xCD #// Read Word from memory/register
C_WRITE_WORD_SEQUENCE           =0xCE #// Write Word Sequence
C_CALL_MEMTOOL_DRIVER           =0xCF #// Call memtool driver routine
C_AUTOBAUD		      	    =0xD0 #// Call autobaud routine
C_SETPROTECTION  	            =0xD1 #// Call security function

T_95080                         = 0#
T_95040                         = 1#
T_M93S46_6BIT                   = 2#
T_M93S56_8BIT                   = 3#
T_M93S76_10BIT                  = 4#
T_24C02_8BIT                    = 10#
T_24C04_9BIT                    = 11#
T_29FX00B                       = 20#
T_29FX00B_Simos3                = 21#
T_29FX00BT_EDC15                = 22#

########## C167
# Port Register Addresses:
Port2Address = 0xFFC0;
Port3Address = 0xFFC4;
Port4Address = 0xFFC8;
#Port5Address = 0xFFA2;
Port6Address = 0xFFCC;
Port7Address = 0xFFD0;
Port8Address = 0xFFD4;

Port2Address8bit = 0xE0;
Port3Address8bit = 0xE2;
Port4Address8bit = 0xE4;
#Port5Address8bit = 0xD1;
Port6Address8bit = 0xE6;
Port7Address8bit = 0xE8;
Port8Address8bit = 0xEA;

DirectionPort0LAddress = 0xF100;
DirectionPort0HAddress = 0xF102;
DirectionPort1LAddress = 0xF104;
DirectionPort1HAddress = 0xF106;
DirectionPort2Address = 0xFFC2;
DirectionPort3Address = 0xFFC6;
DirectionPort4Address = 0xFFCA;
#CDirectionPort5Address = 0xFF;
DirectionPort6Address = 0xFFCE;
DirectionPort7Address = 0xFFD2;
DirectionPort8Address = 0xFFD6;

DirectionPort0LData = 0x00FF; # all output
DirectionPort0HData = 0x00FF; # all output
DirectionPort1LData = 0x00FF; # all output
DirectionPort1HData = 0x00FF; # all output
DirectionPort4Data = 0x0F; # all output

DirectionPort2Address8bit = 0xE1;
DirectionPort3Address8bit = 0xE3;
DirectionPort4Address8bit = 0xE5;
#DirectionPort5Address8bit = 0xFF;
DirectionPort6Address8bit = 0xE7;
DirectionPort7Address8bit = 0xE9;
DirectionPort8Address8bit = 0xEB;

SSCTB_Address       = 0xF0B0;       #; SSC transmit register
SSCRB_Address       = 0xF0B2;       #; SSC receive register
SSCBR_Address       = 0xF0B4;       #; SSC baudrate
SSCRIC_Address      = 0xFF74;       #; SSC receive interrupt control reg
SSCRIC_Address8bit  = 0xBA;         #; SSC receive interrupt control reg
SSCCON_Address      = 0xFFB2;       #; SSC config reg

SSCRIR_Bit          = 7;            #; exchange completion flag in SSCRIC

SSCBR_Data          = 0x000B;       #; baudrate speed in the ECU firmware
SSCCON_Data         = 0xC037;       #; configuration


XSSCTB_Address       = 0xE806;       #; XSSC transmit register
XSSCRB_Address       = 0xE808;       #; XSSC receive register

XSSCBR_Address       = 0xE80A;       #; XSSC baudrate
XSSCBR_Data         = 0x000B            #; baudrate speed in the ECU firmware



XSSCCON_Address      = 0xE800;       #; XSSC  config reg
XSSCCON_Data        = 0xC037        #; configuration enable module

SSCRIR_Bit          = 7;            #; exchange completion flag in XSSCRIC


#XSSC_MTSR	equ		P6.6			; Master transmit / slave receive
#XSSC_MRST	equ		P6.7			; Master receive / slave transmit
#XSSC_SCLK	equ		P6.5			; Clock out/ in

#SSC_MTSR	equ		P3.9			; Master transmit / slave receive
#SSC_MRST	equ		P3.8			; Master receive / slave transmit
#SSC_SCLK	equ		P3.13			; Clock out/ in

SSC_PortAddress                 = Port3Address;
SSC_PortDirectionAddress        = DirectionPort3Address;

SSC_MTSR_Pinnum                 = 9;
SSC_MRST_Pinnum                 = 8;
SSC_SCLK_Pinnum                 = 13;

XSSC_PortAddress                 = Port6Address;
XSSC_PortDirectionAddress        = DirectionPort6Address;

XSSC_MTSR_Pinnum                 = 6;
XSSC_MRST_Pinnum                 = 7;
XSSC_SCLK_Pinnum                 = 5;

########## C167 end

# C16x variants
variantByteC166         = 0x55
variantByteC167Old      = 0xA5
variantByteC165         = 0xB5
variantByteC167         = 0xC5
variantByteC167WithID   = 0xD5

# ST10 variants
variantByteST10 = 0x55

DEV_ID_F400BB     = 0x22ab;
DEV_ID_F800BB     = 0x2258;
DEV_ID_F400BT     = 0x2223;
DEV_ID_F800BT     = 0x22D6;


def SendCommand(ser, data):
    SendCharwEcho(ser, data)
    echo = ser.read(1)
    if(len(echo) != 1):
        print("got no command ackn")
        return False;
    if(echo[0] != A_ACK1):
        print("got different response than ackn1: ", hex(echo[0]))
        return False;
    return True;

def SendData(ser, data):
    SendDatawEcho(ser, data)
    echo = ser.read(1)
    if(len(echo) != 1):
        print("got no send data ackn")
        return False;
    if(echo[0] != A_ACK2):
        print("got different response than ackn2: ", hex(echo[0]))
        return False;
    return True;

def GetData(ser, data):
    SendDatawEcho(ser, data)
    echo = ser.read(3)
    if(len(echo) != 3):
        print("got no get data ackn")
        return False, [];
    if(echo[2] != A_ACK2):
        print("got different response than ackn2: ", hex(echo[0]))
        return False, [];
    return True, [echo[0] | echo[1]<<8];

def TestComm(ser):
    print("test comm")
    SendDatawEcho(ser, [C_TEST_COMM])

    data = ser.read(2);
    if(len(data) != 2):
        print("\n no response from ecu after test comm")
        return -1;
    if(data[0] != A_ACK1) | (data[1] != A_ACK2):
        print("\n wrong response from ecu after sending test comm", hex(data[0]),hex(data[1]))
        return -1;

    print(" got core akn :", hex(A_ACK1), hex(A_ACK2))

def SetWordAtAddress(ser, addr, data):
    ret = SendCommand(ser, [C_WRITE_WORD])
    ret &= SendData(ser, GetAddressAsLittleEndian(addr)+GetWordAsLittleEndian(data))
    ret &= SendCommand(ser, [C_READ_WORD])
    ret , readData = GetData(ser, GetAddressAsLittleEndian(addr))
    if(ret == False):
        print("set Data not successfull");
        return False;
    if(readData[0] != data):
        print("set Data not successfull; set: ",data, "readback: ", readData[0]);
        return False;
    print("set Data at: ", hex(addr)," success:", ret)
    return True;

# simos 3 flash funcs

def GetCrossedWord(inputData):
    out =   (inputData & 0x0001) << 15
    out +=  (inputData & 0x0002) << 12
    out +=  (inputData & 0x0004) << 9
    out +=  (inputData & 0x0008) << 6
    out +=  (inputData & 0x0010) << 3
    out +=  (inputData & 0x0020) >> 0
    out +=  (inputData & 0x0040) >> 3
    out +=  (inputData & 0x0080) >> 6
    out +=  (inputData & 0x0100) << 6
    out +=  (inputData & 0x0200) << 3
    out +=  (inputData & 0x0400) << 0
    out +=  (inputData & 0x0800) >> 3
    out +=  (inputData & 0x1000) >> 6
    out +=  (inputData & 0x2000) >> 9
    out +=  (inputData & 0x4000) >> 12
    out +=  (inputData & 0x8000) >> 15
    return out

def GetBackCrossedWord(inputData):
    out =   (inputData & 0x8000) >> 15
    out +=  (inputData & 0x2000) >> 12
    out +=  (inputData & 0x0800) >> 9
    out +=  (inputData & 0x0200) >> 6
    out +=  (inputData & 0x0080) >> 3
    out +=  (inputData & 0x0020) << 0
    out +=  (inputData & 0x0008) << 3
    out +=  (inputData & 0x0002) << 6
    out +=  (inputData & 0x4000) >> 6
    out +=  (inputData & 0x1000) >> 3
    out +=  (inputData & 0x0400) >> 0
    out +=  (inputData & 0x0100) << 3
    out +=  (inputData & 0x0040) << 6
    out +=  (inputData & 0x0010) << 9
    out +=  (inputData & 0x0004) << 12
    out +=  (inputData & 0x0001) << 15
    return out



def GetBlockChecksum(ser):
    SendCharwEcho(ser, [C_GETCHECKSUM])
    echo = ser.read(3)
    if(len(echo) != 3):
        print("got no command ackn")
        return False,[];
    if(echo[2] != A_ACK2):
        print("got different response than ackn2: ", hex(echo[2]))
        return False,[];
    return True,[echo[1]];

def CalcBlockChecksum(data):
    checksum = 0;

    for d in data:
        checksum = (checksum ^ (d))&0xFF

    return checksum

def SetBlockAtAddress(ser, addr, data):
    ret = SendCommand(ser, [C_WRITE_BLOCK])
    ret &= SendData(ser, GetAddressAsLittleEndian(addr)+GetWordAsLittleEndian(len(data))+data)

    ret , checksum = GetBlockChecksum(ser);
    calcChecksum = CalcBlockChecksum(data);
    if(ret == False):
        print("set Block not successfull");
        return False;
    if(calcChecksum != checksum[0]):
        print("get Block at: ", hex(addr),"Wrong Checksum:", ret, " got checksum: ", hex(checksum[0]),
          " is calculated CalcChecksum", hex(calcChecksum) )
        return False,[];
    return True;

def GetBlockAtAddress(ser, addr, size):
    ret = SendCommand(ser, [C_READ_BLOCK])
    SendDatawEcho(ser,  GetAddressAsLittleEndian(addr)+GetWordAsLittleEndian(size))
    echo = ser.read(size+1)
    if(len(echo) != size+1):
        print("GetBlockAtAddress got no ackn: ",echo)
        return False, [];
    if(echo[size] != A_ACK2):
        print("GetBlockAtAddress got different response than ackn2: ", hex(echo[size]))
        return False, [];

    ret , checksum = GetBlockChecksum(ser);
    calcChecksum = CalcBlockChecksum(echo[:size]);
    if(ret == False):
        print("Get Block not successfull, got no checksum ");
        return False,[];
    if(calcChecksum != checksum[0]):
        print("get Block at: ", hex(addr),"Wrong Checksum:", ret, " got checksum: ", hex(checksum[0]),
          " is calculated CalcChecksum", hex(calcChecksum) )
        return False,[];
    return True, echo[:size];

def CallAtAddress(ser, addr, register):     ## 8 register words assumed r8-r15
    ret = SendCommand(ser, [C_CALL_FUNCTION])
    regdata =[]
    for r in register:
        regdata += GetWordAsLittleEndian(r)

    SendDatawEcho(ser, GetAddressAsLittleEndian(addr)+regdata)
    echo = ser.read(17)
    if(len(echo) != 17):
        print("CallAtAddress got no ackn: ",echo)
        return False, [];
    if(echo[16] != A_ACK2):
        print("CallAtAddress got different response than ackn2: ", hex(echo[16]))
        return False, [];

    returnreg = [echo[0] | echo[1]<<8, echo[2] | echo[3]<<8, echo[4] | echo[5]<<8, echo[6] | echo[7]<<8,
                 echo[8] | echo[9]<<8, echo[10] | echo[11]<<8, echo[12] | echo[13]<<8, echo[14] | echo[15]<<8];

##    print(" CallAtAddress at: ", hex(addr)," successfull");#, register after call: ")
##    for r in returnreg:
##        print(hex(r));
    return True, returnreg;

def RunFunc(exitt, ser, file, job, startAddr, size, eetype, portAddr8, directionPortAddress8, pinnum, sscType):
    
    ResetAdapter(ser);
    SetAdapterKKL(ser);
    
    ser.reset_input_buffer();
    char = b'';

    SYSCON_Addr         = 0x00ff12;
    SYSCON_Data_ext     = 0xe204        # from 15 -0: 3b stksz, 1b ROMS1, 1b SGTDIS, 1b ROMEN, 1b BYTDIS, 1b CLKEN, 1b WRCFG, 1b CSCFG, 1b reserved, 
                                    #               1b OWDDIS, 1b BDRSTEN, 1b XPEN, 1b VISIBLE, 1b SPER-SHARE
                                    # e -> rom mapped at >0x0 0000 and a Stacksize = ???, 2 -> Romen = 0 & BytDis = 1

    SYSCON_Data_int     = 0xf604        # from 15 -0: 3b stksz, 1b ROMS1, 1b SGTDIS, 1b ROMEN, 1b BYTDIS, 1b CLKEN, 1b WRCFG, 1b CSCFG, 1b reserved, 
                                #               1b OWDDIS, 1b BDRSTEN, 1b XPEN, 1b VISIBLE, 1b SPER-SHARE
                                # f -> rom mapped at >0x01 0000 and a Stacksize = ???, 6 -> Romen = 1 & BytDis = 1
                                    
    
    BUSCON0_Addr    = 0x00ff0c;
    #BUSCON0_Data    = 0xc4ae;       # e = 1 memory cycle wait state, a = 16bit demultiplexed bus - no tristate wait state - 1 read/write delay, 4= external bus active
    BUSCON0_Data    = 0x04ad;       # d = 2 memory cycle wait state, a = 16bit demultiplexed bus - no tristate wait state - 1 read/write delay,
                                    # 4= external bus active, c chipSelect read/write enable

    BUSCON0_WriteData    = 0x04ad;       # d = 2 memory cycle wait state, a = 16bit demultiplexed bus - no tristate wait state - 1 read/write delay,
                                    # 4= external bus active, c chipSelect read/write enable
    BUSCON0_Simos3_Data    = 0x44be;       # d = 2 memory cycle wait state, a = 16bit demultiplexed bus - no tristate wait state - 1 read/write delay,
                                    # 4= external bus active, c chipSelect read/write enable    
##Simos3
##BUSCON0 : 45BF
##BUSCON1 : 858E

    ADDRSEL1_Addr   = 0x00fe18;
    ADDRSEL1_Data = 0x3803          # 32kByte window starting at 0x38 0000 ??
    
    ADDRSEL1_Simos3_Data = 0x4008          # 1024kByte window starting at 0x40 0000 ??
    
    ADDRSEL2_Addr = 0x00fe1a;
    ADDRSEL2_Data = 0x2008          # 1024kByte window starting at 0x20 0000 ??
    
    ADDRSEL3_Addr = 0x00fe1c;       ## not used
    ADDRSEL3_Data = 0x0
    ADDRSEL3_EDC15_Data = 0x4008          # 1024kByte window starting at 0x40 0000 ??
    
    ADDRSEL4_Addr = 0x00fe1e;       ## not used
    ADDRSEL4_Data = 0x0000
    
    BUSCON1_Addr = 0x00ff14;
    BUSCON1_Data = 0x040d           #  d = 2 memory cycle wait state, 0 = 8bit demultiplexed bus - 1 tristate wait state - 1 read/write delay, 0= external bus inactive

    BUSCON1_Simos3_Data = 0x848e           #  d = 2 memory cycle wait state, 0 = 8bit demultiplexed bus - 1 tristate wait state - 1 read/write delay, 0= external bus inactive


    BUSCON2_Addr = 0x00ff16;
    BUSCON2_Data = 0x04ad           #  d = 2 memory cycle wait state, a = 16bit demultiplexed bus - no tristate wait state - 1 read/write delay,
                                    #  4= external bus active,
    
    BUSCON3_Addr = 0x00ff18;       ## not used
    BUSCON3_Data = 0x0000
    BUSCON3_EDC15_Data = 0x848e           #  d = 2 memory cycle wait state, 0 = 8bit demultiplexed bus - 1 tristate wait state - 1 read/write delay, 0= external bus inactive
        
    BUSCON4_Addr = 0x00ff1a;       ## not used
    BUSCON4_Data = 0x0000

    BUSCON4_Addr = 0x00ff1a;       ## not used
    BUSCON4_Data = 0x0000

    XPERCON_Addr = 0x00f024;       ## for XSSC in ST10
#    XPERCON_Data = 0x032C;          # XRAM1&2 en, XFlash en, XSSC en, misc_en
    XPERCON_Data = 0x0500;          # XSSC en, misc_en


    driverAddress = 0x00F600;
    DriverEntryPoint = 0x00F640;

    FlashDriverEntryPoint = 0x00F640;
    
    driverSetCsDirAddress = 0xF600;
    driverClearCsDirAddress = 0xF604;
    driverSetCsAddress = 0xF60C;
    driverClearCsAddress = 0xF608;
    opCodeBset = 0xF;
    opCodeBCLR = 0xE;

    #driver commands
    C_GETSTATE = 0x0093;
    C_READSPI = 0x0036;
    C_WRITESPI = 0x0037;

    #flash driver commands
    FC_PROG			=	0x00	; #Program Flash
    FC_ERASE		        =	0x01	; #Erase Flash
    FC_SETTIMING		=	0x03	; #Set Timing
    FC_GETSTATE		        =	0x06	; #Get State
    FC_GETSTATE_ADDR_MANUFID    =       0x00;
    FC_GETSTATE_ADDR_DEVICEID   =       0x01;
    FC_LOCK			=	0x10	; #Lock Flash bank
    FC_UNLOCK		        =	0x11	; #Unlock Flash bank
    FC_PROTECT		        =	0x20	; #Protect entire Flash
    FC_UNPROTECT		=	0x21	; #Unprotect Flash
    FC_BLANKCHECK		=	0x34	; #OTP/ Flash blankcheck
#    FC_GETID		        =	0x35	; #Get Manufacturer ID/ Device ID ->not implemented


#    ;--------------------- Error Values -----------------------------

    E_NOERROR		        =	0x00	; #No error
    E_UNKNOWN_FC		=	0x01	; #Unknown function code

    E_PROG_NO_VPP		=	0x10	; #No VPP while programming
    E_PROG_FAILED		=	0x11	; #Programming failed
    E_PROG_VPP_NOT_CONST	=	0x12	; #VPP not constant while programming

    E_INVALID_BLOCKSIZE	        =	0x1B	; #Invalid blocksize
    E_INVALID_DEST_ADDR	        =	0x1C	; #Invalid destination address

    E_ERASE_NO_VPP		=	0x30	; #No VPP while erasing
    E_ERASE_FAILED		=	0x31	; #Erasing failed
    E_ERASE_VPP_NOT_CONST	=	0x32	; #VPP not constant while erasing

    E_INVALID_SECTOR	        =	0x33	; #Invalid sector number
    E_Sector_LOCKED		=	0x34	; #Sector locked
    E_FLASH_PROTECTED	        =	0x35	; #Flash protected
    
    IntRomAddress = 0x010000;
##    IntRomAddress = 0x000000;

    ExtFlashAddress             = 0x800000;
    ExtFlashWriteAddressMe7     = 0x800000;
    ExtFlashWriteAddressECD15   = 0x400000;
    ExtFlashWriteAddressSimos3   = 0x400000;

    DriverCopyAddress = 0xFC00;
    BlockLength = 0x200;
    if(size< BlockLength):
        BlockLength = size;


## upload core
    
    SendDatawEcho(ser,[0])  #say hello
    byte = ser.read(1);
    if(len(byte) != 1):
        print("\n no response from ecu, Set device into bootmode", byte)
        return -1;
    if(byte[0] != 0xaa):

            
        print(" got cpu version :", hex(byte[0]))
        
        if(byte[0] == variantByteC166):
            print("variantByteC166")
        elif(byte[0] == variantByteC167Old):
            print("variantByteC167Old")
        elif(byte[0] == variantByteC165):
            print("variantByteC165")
        elif(byte[0] == variantByteC167):
            print("variantByteC167")
        elif(byte[0] == variantByteC167WithID):
            print("variantByteC167WithID Or ST10")
        else:
            print("no C16x Variant, ST10 selected");

        print("sending loader")

        path = resource_path("Minimon/LOADK.bin");
        
        loaderfile = open(path, 'rb')
        loader = loaderfile.read();
        loaderfile.close()

        SendDatawEcho(ser,loader);
        byte = ser.read(1);
        if(len(byte) != 1):
            print("\n no response from ecu after sending loader")
            return -1;
        if(byte[0] != I_LOADER_STARTED):
            print("\n wrong response from ecu after sending loader, got :", hex(byte[0])," instead of 0x01")
            return -1;

        print("\n got loader akn :", I_LOADER_STARTED)

        print("sending core")

        path = resource_path("Minimon/MINIMONK.bin");
        
        corefile = open(path, 'rb')
        core = corefile.read();
        corefile.close()

        SendDatawEcho(ser,core);
        byte = ser.read(1);
        if(len(byte) != 1):
            print("\n no response from ecu after sending loader")
            return -1;
        if(byte[0] != I_APPLICATION_STARTED):
            print("\n wrong response from ecu after sending loader, got :", hex(byte[0])," instead of 0x01")
            return -1;

        print("\n got core akn :", I_APPLICATION_STARTED)

    else:
        print(" core already running\n")

    TestComm(ser);


    


    if(job == jobReadEeprom) | (job == jobWriteEeprom):

        if(eetype == T_95080) | (eetype == T_95040):         
            if(sscType == sscTypeX):
                SetWordAtAddress(ser, XPERCON_Addr, XPERCON_Data);
                SYSCON_Data     = 0xe204 # enable xper on
                SetWordAtAddress(ser, SYSCON_Addr, SYSCON_Data);

                path = resource_path("Drivers/ST10XDriver.bin");
                
                eepromDriverFile = open(path, 'rb')
                eepromDriver = list(eepromDriverFile.read());
                eepromDriverFile.close()
            else:
                path = resource_path("Drivers/gremlindriver.bin");
                eepromDriverFile = open(path, 'rb')
                eepromDriver = list(eepromDriverFile.read());
                eepromDriverFile.close()
        elif(eetype == T_M93S46_6BIT) | (eetype == T_M93S56_8BIT) | (eetype == T_M93S76_10BIT):
            path = resource_path("Drivers/SSC_93_Driver.bin");
            eepromDriverFile = open(path, 'rb')
            eepromDriver = list(eepromDriverFile.read());
            eepromDriverFile.close()
        elif(eetype == T_24C02_8BIT) | (eetype == T_24C04_9BIT) :
            path = resource_path("Drivers/24C0xDriver.bin");
            eepromDriverFile = open(path, 'rb')
            eepromDriver = list(eepromDriverFile.read());
            eepromDriverFile.close()
        else:
            print("wrong type in run func")
            return -1;
    
        print("sending eeprom driver")
        SetBlockAtAddress(ser,driverAddress, eepromDriver)

        csSearch = True;
        portCounter = 0;
        pinCounter = 0;
        cyclecounter = 0;
        
        while(csSearch == True):
            if(cyclecounter == 1):
                char = input(" type 1 and enter for brute force search of CS pin : ")
                try:
                    char = int(char)
                except:
                    return -1;
                if(char != 1):
                    return -1;


            if(cyclecounter > 0):
                print("\n next used port pin:")
                if(portCounter == 0):
                    print("port 2")
                    portAddr8 = Port2Address8bit;
                    directionPortAddress8 = DirectionPort2Address8bit;
                if(portCounter == 1):
                    print("port 3")
                    portAddr8 = Port3Address8bit;
                    directionPortAddress8 = DirectionPort3Address8bit;
                if(portCounter == 2):
                    print("port 4")
                    portAddr8 = Port4Address8bit;
                    directionPortAddress8 = DirectionPort4Address8bit;
                if(portCounter == 3):
                    print("port 6")
                    portAddr8 = Port6Address8bit;
                    directionPortAddress8 = DirectionPort6Address8bit;
                if(portCounter == 4):
                    print("port 7")
                    portAddr8 = Port7Address8bit;
                    directionPortAddress8 = DirectionPort7Address8bit;
                if(portCounter == 5):
                    print("port 8")
                    portAddr8 = Port8Address8bit;
                    directionPortAddress8 = DirectionPort8Address8bit;

                pinnum = pinCounter;
                pinCounter +=1;
                if(portCounter == 1) & (pinCounter == 10):
                    pinCounter +=1;
                print("pin : ", pinnum)
                if(pinCounter >15):
                    if(portCounter > 4):
                        print("CS not found")
                        return -1;
                    portCounter += 1;
                    pinCounter = 0

        # patch driver Chip select functions

            cyclecounter += 1;

            if(eetype != T_24C02_8BIT) | (eetype != T_24C04_9BIT):
                SetWordAtAddress(ser, driverSetCsDirAddress, ((pinnum << 4) | opCodeBset) | (directionPortAddress8<<8));
                SetWordAtAddress(ser, driverClearCsDirAddress, ((pinnum << 4) | opCodeBCLR) | (directionPortAddress8<<8));
                SetWordAtAddress(ser, driverSetCsAddress, ((pinnum << 4) | opCodeBset) | (portAddr8<<8));
                SetWordAtAddress(ser, driverClearCsAddress, ((pinnum << 4) | opCodeBCLR) | (portAddr8<<8));


            print("\n");

            if(eetype == T_M93S46_6BIT) | (eetype == T_M93S56_8BIT) | (eetype == T_M93S76_10BIT) | (eetype == T_24C02_8BIT) | (eetype == T_24C04_9BIT):
                csSearch = False;   # break of while loop; no status on 93cxx
                
            else:
        ##        for d in eepromDriver[0:0x10]:
        ##            print(hex(d));

                #end patch

        ##    print("Call C_GETSTATE comm")

                register = [C_GETSTATE, 0x0000, 0x0000, 0x0000, 0x000, 0x0000, 0x0000, 0x0001]

                success , retRegister = CallAtAddress(ser, DriverEntryPoint,register)
                if(success == False):
                    print(" Call C_GETSTATE failed")
                    return -1;
                print("Call C_GETSTATE successfull: ", (retRegister[1]== 0xF0) | (retRegister[1] == 0x80),"state is ",hex(retRegister[1]) )
                if(retRegister[1]== 0xF0) | (retRegister[1] == 0x80):       
                    csSearch = False;   # break of while loop

                             
    
    if(job == jobReadEeprom):
        print("\n *************  start read  *************\n ")
        
        offset = 0x00;

        while (offset < size):

            register = [C_READSPI, BlockLength, offset, eetype, 0x0000, DriverCopyAddress, 0x0000, 0x0009]
            success , retRegister = CallAtAddress(ser, DriverEntryPoint,register)
            
            if(success == False)| (retRegister[7]!= 0x0):
                print(" Call C_READ failed")
                for d in retRegister:
                    print(hex(d))
                return -1;
            
            print("Call C_READ successfull: ", retRegister[7]== 0x0, )

            success, blockData = GetBlockAtAddress(ser, DriverCopyAddress, BlockLength)
            

            if(success == True):
                file.write(bytes(blockData));
            else:
                print(" read not successfull!!");

            offset += BlockLength;




        print(" \n********** read END!! ***********\n");
        return 1;


    elif(job == jobWriteEeprom):
        print("\n *************  start write  *************\n ")
        
        offset = 0x0;
        writeData = file.read();
        size = len(writeData);

        if((eetype == T_24C02_8BIT) | (eetype == T_24C04_9BIT)):
            BlockLength = 0x40

        while (offset < size):
            writeSize = BlockLength;
            if(writeSize > (size - offset)):
                writeSize = (size - offset);

            success = SetBlockAtAddress(ser, DriverCopyAddress, list(writeData[offset:(offset+BlockLength)]))
            

            if(success != True):
                print(" write not successfull!!");
                return -1;

            register = [C_WRITESPI, writeSize, offset, eetype, 0x0000, DriverCopyAddress, 0x0000, 0x0009]
            success , retRegister = CallAtAddress(ser, DriverEntryPoint,register)
            
            if(success == False)| (retRegister[7]!= 0x0):
                for d in retRegister:
                    print(hex(d))
                print(" Call C_WRITESPI failed")
                return -1;
            
            print("Call C_WRITESPI at:" , hex(offset)," successfull: ", retRegister[7]== 0x0, )



            offset += BlockLength;

        print(" \n********** write END!! ***********\n");

        print("\n *************  start verify  *************\n ")
        
        offset = 0x0;
        verifyData = [];

        while (offset < size):

            register = [C_READSPI, BlockLength, offset, eetype, 0x0000, DriverCopyAddress, 0x0000, 0x0009]
            success , retRegister = CallAtAddress(ser, DriverEntryPoint,register)
            
            if(success == False):
                print(" Call C_READSPI failed")
                return -1;
            
            print("Call C_READSPI  at:" , hex(offset)," successfull: ", retRegister[7]== 0x0, )

            success, blockData = GetBlockAtAddress(ser, DriverCopyAddress, BlockLength)
            

            if(success == True):
                verifyData += blockData
            else:
                print(" verify not successfull!!");

            offset += BlockLength;

        offset = 0x0;
        writeData = list(writeData)
        while (offset < size):
            if(writeData[offset] != verifyData[offset]):
                print("write data not equal verify data at pos: ", hex(offset))

            offset += 1;

        print(" \n********** verify END!! ***********\n");

        
        return 1;
        
       
    if(job == jobReadIntRom):
        print("\n *************  start read IntRom  *************\n ")

        SetWordAtAddress(ser, SYSCON_Addr, SYSCON_Data_int);
        SetWordAtAddress(ser, BUSCON0_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL1_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL2_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL3_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL4_Addr, 0);
        SetWordAtAddress(ser, BUSCON1_Addr, 0);
        SetWordAtAddress(ser, BUSCON2_Addr, 0);
        SetWordAtAddress(ser, BUSCON3_Addr, 0);
        SetWordAtAddress(ser, BUSCON4_Addr, 0);

        offset = 0x0;
        readsize = BlockLength;

        while (offset < size):
            if((size - offset) < BlockLength):
                readsize = (size - offset);
            success, blockData = GetBlockAtAddress(ser, IntRomAddress+offset, readsize)
            if(success == True):
                file.write(bytes(blockData));
            else:
                print(" read IntRom not successfull!!");
                return 1;

            offset += readsize;
            sys.stdout.write("\r  read at "+ str(hex(offset)) +" ; finished " + str(int(offset *100 / size)) +" % ")

    if(job == jobWriteExtFlash):
        writeAddressBase = ExtFlashWriteAddressMe7
        
        SetWordAtAddress(ser, SYSCON_Addr, SYSCON_Data_ext);
        
        SetWordAtAddress(ser, ADDRSEL1_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL2_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL3_Addr, 0);
        SetWordAtAddress(ser, ADDRSEL4_Addr, 0);
        SetWordAtAddress(ser, BUSCON1_Addr, 0);
        SetWordAtAddress(ser, BUSCON2_Addr, 0);
        SetWordAtAddress(ser, BUSCON3_Addr, 0);
        SetWordAtAddress(ser, BUSCON4_Addr, 0);

        botBootSector = True;
        
        #T_29FX00B
        if(eetype == T_29FX00B_Simos3):
            path = resource_path("Drivers/FX00B_Simos3Driver.bin");
            eepromDriverFile = open(path, 'rb')
            SetWordAtAddress(ser, ADDRSEL1_Addr, ADDRSEL1_Simos3_Data);
            SetWordAtAddress(ser, BUSCON1_Addr, BUSCON1_Simos3_Data);
            
            SetWordAtAddress(ser, BUSCON0_Addr, BUSCON0_Simos3_Data);
            print("\nSimos3 Flash driver")
            writeAddressBase = ExtFlashWriteAddressSimos3
            botBootSector = True;

        elif(eetype == T_29FX00B):
            path = resource_path("Drivers/FX00Bx_Driver.bin");
            eepromDriverFile = open(path, 'rb')
            SetWordAtAddress(ser, ADDRSEL1_Addr, 0);
            SetWordAtAddress(ser, BUSCON1_Addr, 0);
            SetWordAtAddress(ser, BUSCON0_Addr, BUSCON0_WriteData);
            print("\nMe7 variant Flash driver")
            writeAddressBase = ExtFlashWriteAddressMe7
            botBootSector = True;

        elif(eetype == T_29FX00BT_EDC15):
            path = resource_path("Drivers/FX00Bx_Driver.bin");
            eepromDriverFile = open(path, 'rb')
            SetWordAtAddress(ser, ADDRSEL3_Addr, ADDRSEL3_EDC15_Data);
            SetWordAtAddress(ser, BUSCON3_Addr, BUSCON3_EDC15_Data);
            SetWordAtAddress(ser, BUSCON0_Addr, BUSCON0_Data);
            print("\nEDC15 variant Flash driver")
            writeAddressBase = ExtFlashWriteAddressECD15
            botBootSector = False;
        else:
            print(" wrong Flash/Ecu Type in runFunc")
            return -1;
        eepromDriver = list(eepromDriverFile.read());
        eepromDriverFile.close()
                
        print("sending ext flash driver")
        SetBlockAtAddress(ser,driverAddress, eepromDriver)
        
        print("\n *************  start write extFlash  *************\n ")



##        print("\n *************  write reset to read (f0)  *************\n ")
##        SetWordAtAddress(ser, 0x400000, 0xf0);

##        GetFlashManufacturerID(ser);
        
#************* get IDS *********
        writeAddressHigh = ((writeAddressBase ) >>16) & 0xFFFF;
        readAddressHigh = ((ExtFlashAddress ) >>16) & 0xFFFF;
        
        register = [FC_GETSTATE, 0x0000, writeAddressHigh, readAddressHigh, 0x000, 0x000 , FC_GETSTATE_ADDR_MANUFID, 0x0001]

        success , retRegister = CallAtAddress(ser, FlashDriverEntryPoint,register)
        if(success == False):
            print(" Call FC_GETSTATE failed")
            return -1;
        if(eetype == T_29FX00B_Simos3):
            manId = hex(GetBackCrossedWord(retRegister[1]));
        else:
            manId = hex(retRegister[1]);
        print("Call FC_GETSTATE Manufacturer ID successfull: ", retRegister[7]== 0x0,"Manuf ID is " ,manId )

        register = [FC_GETSTATE, 0x0000, writeAddressHigh, readAddressHigh, 0x000, 0x000, FC_GETSTATE_ADDR_DEVICEID, 0x0001]

        success , retRegister = CallAtAddress(ser, FlashDriverEntryPoint,register)
        if(success == False | (retRegister[7] != 0x0)):
            print(" Call FC_GETSTATE failed")
            return -1;
        if(eetype == T_29FX00B_Simos3):
            devId = GetBackCrossedWord(retRegister[1]);
        else:
            devId = retRegister[1];
        print("Call FC_GETSTATE Device ID successfull: ", retRegister[7]== 0x0,"Dev ID is " ,hex(devId) )

        flashSize = 0

        if(devId == DEV_ID_F800BB):
            print("F800BB Flash 1024kBit found");
            flashSize = (1<<20)
        elif(devId == DEV_ID_F400BB):
            print("F400BB Flash 512kBit found");
            flashSize = (1<<19)
        elif(devId == DEV_ID_F800BT):
            print("F800BT Flash 1024kBit found");
            botBootSector = False;
            flashSize = (1<<20)
        elif(devId == DEV_ID_F400BT):
            print("F400BT Flash 512kBit found");
            botBootSector = False;
            flashSize = (1<<19)
        else:
            input("no F400Bx or F800Bx AMD id, press STRG + C to end or ENTER to continue\n")
            flashSize = size

        if(size < flashSize):
           print("filesize: ", size/1024," kB is smaller than flash size: ", flashSize/1024," kB (should be no problem) !!!!!\n")
        if(size > flashSize):
           input("filesize: ", size/1024," kB is bigger than flash size: ", flashSize/1024," kB !!!!!, press STRG + C to end or ENTER to continue\n")
        
        offset = 0x0;

        # read data to know size
        writeData = file.read();
        size = len(writeData);

#************* Erase*********
        sector = 0;
        sectorSize = 0;
        while (offset < size):
            if(botBootSector == False): # Top boot sector
                if(flashSize ==  (1<<20)): #size f800 1024kB
                    if(sector == 18):
                        sectorSize = 0x4000;
                    elif(sector == 17) | (sector == 16):
                        sectorSize = 0x2000;
                    elif(sector == 15):
                        sectorSize = 0x8000;
                    else:
                        sectorSize = 0x10000;

                else: ##size f8400 512kB
                    if(sector == 10):
                        sectorSize = 0x4000;
                    elif(sector == 9) | (sector == 8):
                        sectorSize = 0x2000;
                    elif(sector == 7):
                        sectorSize = 0x8000;
                    else:
                        sectorSize = 0x10000;

            else:#(eetype == T_29FX00B)|(eetype == T_29FX00B_Simos3):  # BOT boot sector
                if(sector == 0):
                    sectorSize = 0x4000;
                elif(sector == 1) | (sector == 2):
                    sectorSize = 0x2000;
                elif(sector == 3):
                    sectorSize = 0x8000;
                else:
                    sectorSize = 0x10000;


            
            writeAddressHigh = ((writeAddressBase + offset) >>16) & 0xFFFF;
            writeAddressLow = (writeAddressBase + offset) & 0xFFFF;
            readAddressHigh = ((ExtFlashAddress + offset) >>16) & 0xFFFF;

            lastWordAddress = (ExtFlashAddress + offset + sectorSize -2) & 0xFFFF;
            
                    
            register = [FC_ERASE, writeAddressLow, writeAddressHigh, readAddressHigh, lastWordAddress, 0x000, sector, 0x0001]

            success , retRegister = CallAtAddress(ser, FlashDriverEntryPoint,register)
            if(success == False) | (retRegister[7] != 0x0):
                print(" Call FC_ERASE failed\n")
                for r in retRegister:
                    print(hex(r))
                print("\n")
                return -1;
            sys.stdout.write("\rCall FC_ERASE Sector "+ str(sector) +" successfull: "  + str(retRegister[7]== 0x0))
##            print("Call FC_ERASE Sector "+ str(sector) +" successfull: "  + str(retRegister[7]== 0x0), " return sector address: ", hex(retRegister[5]), " timoutcounter: ", hex(retRegister[6]))


            offset += sectorSize;
            sector += 1;

#************* Write*********
        print("\n")
        offset = 0x0;
        
        writesize = BlockLength;

        while (offset < size):
            if((size - offset) < BlockLength):
                writesize = (size - offset);
            blockData = writeData[offset:(offset+writesize)];
            write = False;
            for e in blockData:
                if(e != 0xff):
                    write = True;
            if (write == True):
                success = SetBlockAtAddress(ser, DriverCopyAddress, list(writeData[offset:(offset+writesize)]))

                if(success != True):
                    print("write not successfull!!");
                    return -1;

                writeAddress = writeAddressBase + offset;
                writeAddressHigh = writeAddress >>16;
                writeAddressLow = writeAddress & 0xFFFF;
                
                readAddressHigh = ((ExtFlashAddress + offset) >>16) & 0xFFFF;
                
                register = [FC_PROG, writesize, DriverCopyAddress, 0x0000, readAddressHigh, writeAddressLow, writeAddressHigh, 0x0001]

    ##            for i in register:
    ##                print(hex(i))
    ##            print("\n")
                success , retRegister = CallAtAddress(ser, FlashDriverEntryPoint,register)
                if(success == False) | (retRegister[7] != 0x0):
                    print("Call FC_PORGRAMM failed")
                    return -1;
                
                offset += writesize;
                sys.stdout.write("\rCall FC_PORGRAMM BLOCK "+ str(hex(offset)) +" successfull: "  + str(retRegister[7]== 0x0)+" ; finished " + str(int(offset *100 / size)) +" % ")
            else:
                offset += writesize;
                sys.stdout.write("\r only 0xff in block -> nothing to write "+" ; finished " + str(int(offset *100 / size)) +" % ")
             

        print(" \n********** write extFlash successfull!! ***********\n");
        return 1;

    if(job == jobReadExtFlash):
        print("\n *************  start read extFlash  *************\n\n")

        SetWordAtAddress(ser, SYSCON_Addr, SYSCON_Data_ext);
        SetWordAtAddress(ser, BUSCON0_Addr, BUSCON0_Data);
        SetWordAtAddress(ser, ADDRSEL1_Addr, ADDRSEL1_Data);
        SetWordAtAddress(ser, ADDRSEL2_Addr, ADDRSEL2_Data);
        SetWordAtAddress(ser, ADDRSEL3_Addr, ADDRSEL3_Data);
        SetWordAtAddress(ser, ADDRSEL4_Addr, ADDRSEL4_Data);
        SetWordAtAddress(ser, BUSCON1_Addr, BUSCON1_Data);
        SetWordAtAddress(ser, BUSCON2_Addr, BUSCON2_Data);
        SetWordAtAddress(ser, BUSCON3_Addr, BUSCON3_Data);
        SetWordAtAddress(ser, BUSCON4_Addr, BUSCON4_Data);
        
        offset = 0x0;
        readsize = BlockLength;

        while (offset < size):
            if((size - offset) < BlockLength):
                readsize = (size - offset);
            success, blockData = GetBlockAtAddress(ser, ExtFlashAddress+offset, readsize)
            

            if(success == True):
                file.write(bytes(blockData));
            else:
                print(" read extFlash not successfull!!");
                return 1;
            
            offset += readsize;
            sys.stdout.write("\r  read at "+ str(hex(offset)) +" ; finished " + str(int(offset *100 / size)) +" % ")


        print(" \n********** read extFlash successfull!! ***********\n");
        return 1;

    return 1;   # != 0 ... exit

def PrintUsage():
    print(" type -h for this help\n Arguments in [] are optional:\n"+
          
          "\n-------------------- Read EEProm--------------------\n"+
          "    ME7BootTool  baudrate  -readeeprom -PeriphType  eepromtype Port(of chip select) Pin(of chip select) size(hex or dezimal)  [filename]    \n"+
          "eg: ME7BootTool  9600      -readeeprom -XSSC         1         Port4                Pin7                0x100                 551Eeprom.ori\n"+
          "eg: ME7BootTool  28800     -readeeprom -SSC          1         Port4                Pin7                0x200                 551Eeprom.ori\n\n"+
          "eg: ME7BootTool  28800     -readeeprom -I2C          11                                                 0x200                 551Eeprom.ori\n"+
          "----------------------------------------------------\n"+

          "\n-------------------- Write EEProm--------------------\n"+
          "    ME7BootTool  baudrate  -writeeeprom -PeriphType eepromtype Port(of chip select) Pin(of chip select) filename                           \n"+
          "eg: ME7BootTool  9600      -writeeeprom -XSSC         1        Port6                Pin3                551ImmoOff.bin\n"+
          "eg: ME7BootTool  28800     -writeeeprom -SSC          1        Port6                Pin3                551ImmoOff.bin\n\n"+
          "eg: ME7BootTool  28800     -writeeeprom -I2C         11                                                 551ImmoOff.bin\n"+
          "----------------------------------------------------\n"+
          
          "\n-------------------- Parameters for R/W EEProm--------------------\n"+
                  "\ntype of eeprom is 0 for 95080 to 95320, 1 for 95040 or 95p08,\n"+
          "2 for 93S46 with 6bit address, 3 for 93S56 or 93S66 with 8 bit address, 4 for 93S76 or 93S86 with 10 bit address\n"+
          "10 for 24c02 with 8bit address, 11 for 24c04 with 9bit address \n\n"+
          "Chip select for eeprom: Port2,3,4,6,7,8 are supported, pins 0-15; ME7.5 & 7.1 P4.7; ME7.1.1 P6.3 ; SIMOS 3.2 is P6.4 \n"+
          " -PeriphType : -SSC for C16x or ST10, -XSSC for ST10 and XC167 (only type 0 and 1 supported),\n"+
          " -PeriphType : -I2C for EDC15VM/P+ (only type 10 and 11 supported)\n"+
          "----------------------------------------------------\n"+
          
          "\n-------------------- read internal Rom or Flash (IROM, IFLASH) --------------------\n"+
          "     ME7BootTool  baudrate  -readInt    size(hex or dezimal)  [filename]       \n"+
          " eg: ME7BootTool  28800     -readInt    0x8000                551IntRom.ori\n"+
          "----------------------------------------------------\n"+
          
          "\n-------------------- read external Flash --------------------\n"+
          "     ME7BootTool  baudrate  -readextflash   size(hex or dezimal)  [filename]  \n"+
          " eg: ME7BootTool  28800     -readextflash   0x80000                551extFlash.ori\n"+
          "----------------------------------------------------\n"+
          
          "\n-------------------- write external Flash --------------------\n"+
          "     ME7BootTool  baudrate  -writeextflash  filename Ecu/FlashType (ME7, Simos3, EDC15)  \n"+
          "eg:  ME7BootTool  28800     -writeextflash  551extFlash.bin         simos3\n"+
          "eg:  ME7BootTool  57600     -writeextflash  551extFlash.bin         me7\n"+
          "eg:  ME7BootTool  57600     -writeextflash  551extFlash.bin         edc15\n"+
          "----------------------------------------------------\n"+
          
          "\n-------------------- Baudrate --------------------\n"+
          " standard rates: 9600, 19200, 28800, 38400, 57600, 115200 ; depending on cable 115200 or 57600 may not work");

def GetPort(argPort , argPin):
    portAddr8 = Port4Address8bit;
    directionPortAddress8 = DirectionPort4Address8bit;
    pinnum = 7;

    if(argPort.lower().find("port2") != -1):
        portAddr8 = Port2Address8bit;
        directionPortAddress8 = DirectionPort2Address8bit;
    elif(argPort.lower().find("port3") != -1):
        portAddr8 = Port3Address8bit;
        directionPortAddress8 = DirectionPort3Address8bit;
    elif(argPort.lower().find("port4") != -1):
        portAddr8 = Port4Address8bit;
        directionPortAddress8 = DirectionPort4Address8bit;
    elif(argPort.lower().find("port6") != -1):
        portAddr8 = Port6Address8bit;
        directionPortAddress8 = DirectionPort6Address8bit;
    elif(argPort.lower().find("port7") != -1):
        portAddr8 = Port7Address8bit;
        directionPortAddress8 = DirectionPort7Address8bit;
    elif(argPort.lower().find("port8") != -1):
        portAddr8 = Port8Address8bit;
        directionPortAddress8 = DirectionPort8Address8bit;


    if(argPin.lower().find("pin0") != -1):
        pinnum = 0;
    elif(argPin.lower().find("pin1") != -1):
        pinnum = 1;
    elif(argPin.lower().find("pin2") != -1):
        pinnum = 2;
    elif(argPin.lower().find("pin3") != -1):
        pinnum = 3;
    elif(argPin.lower().find("pin4") != -1):
        pinnum = 4;
    elif(argPin.lower().find("pin5") != -1):
        pinnum = 5;
    elif(argPin.lower().find("pin6") != -1):
        pinnum = 6;
    elif(argPin.lower().find("pin7") != -1):
        pinnum = 7;
    elif(argPin.lower().find("pin8") != -1):
        pinnum = 8;
    elif(argPin.lower().find("pin9") != -1):
        pinnum = 9;
    elif(argPin.lower().find("pin10") != -1):
        pinnum = 10;
    elif(argPin.lower().find("pin11") != -1):
        pinnum = 11;
    elif(argPin.lower().find("pin12") != -1):
        pinnum = 12;
    elif(argPin.lower().find("pin13") != -1):
        pinnum = 13;
    elif(argPin.lower().find("pin14") != -1):
        pinnum = 14;
    elif(argPin.lower().find("pin15") != -1):
        pinnum = 15;
    else:
        return False, portAddr8, directionPortAddress8, pinnum;
        
    return True , portAddr8, directionPortAddress8, pinnum;
    


exitt = 0;
usbthere = 0;
state = 0;
printwait = 0;
ports = [];
filename = "eeprom.bin";
file = [];
job = 0;
jobReadEeprom = 1;
jobWriteEeprom = 3;
jobReadIntRom = 4;
jobReadExtFlash = 5;
jobWriteExtFlash = 6;
size = 0x200;

baud = 9600;
startAddr = -1;

portAddr8 = Port4Address8bit;
directionPortAddress8 = DirectionPort4Address8bit;
pinnum = 7;

eetype = 0;
sscTypeX = 1;
i2cType = 2;
sscType = 0;

def  ParsePeriphType(typeString, x_sscArgLength, i2cArgLength):

    expectedArgSize = x_sscArgLength
    if(sys.argv[3].lower().find("-xssc") != -1):
        sscType = sscTypeX;
        print("XC16x & ST10 XSSC is used")
    elif(sys.argv[3].lower().find("-ssc") != -1):
        sscType = 0;
        print("C16x SSC is used")
    elif(sys.argv[3].lower().find("-i2c") != -1):
        sscType = i2cType;
        print("Sw I2C is used")
        expectedArgSize = i2cArgLength
    else:
        return False, expectedArgSize, sscType
    return True, expectedArgSize, sscType

def  ParseEEType(eetypeArg, sscType):
    #type
    try:
        eetype = int(eetypeArg);
    except:
        try:
            eetype = int(eetypeArg,16);
        except:
            return False, 0

    if(eetype == T_95080):
        print(" eeprom type is 95080 to 95320");
    elif(eetype == T_95040):
        print(" eeprom type is 95040 or 5P08C3");
    elif(eetype == T_M93S46_6BIT):
        print(" eeprom type is M93S46 6BIT address");
    elif(eetype == T_M93S56_8BIT):
        print(" eeprom type is M93S56 or M93S66 8BIT address");
    elif(eetype == T_M93S76_10BIT):
        print(" eeprom type is M93S76 or M93S86 10BIT address");
    elif(eetype == T_24C02_8BIT):
        print(" eeprom type is 24C02");
    elif(eetype == T_24C04_9BIT):
        print(" eeprom type is 24c04");
    else:
        return False, 0

    if(sscType == i2cType):
        if((eetype != T_24C02_8BIT) & (eetype != T_24C04_9BIT)):
            print("i2c only with eetype 10 and 11 supported")
            return False, 0
    else:
        if((eetype == T_24C02_8BIT) | (eetype == T_24C04_9BIT)):
            print("ssc or xssc not with eetype 10 and 11 supported")
            return False, 0
    return True, eetype

print("\nBootMode Tool for me(d)7 , Simos 3.x & EDC15VM/P+ Variants inspired by ArgDub , 360trev and Gremlin \n***********\n")
while(exitt==0):
    try:
        if state == 0:
            if(len(sys.argv) <3):
                PrintUsage();
                break;

            try:
                baud = int(sys.argv[1]);
                opt1 = str(sys.argv[2])

                print(opt1," baudrate: ", baud)

                if(opt1.lower().find("readint") != -1):     ################################### READ INT ROM/ FLASH
                    if(len(sys.argv) <4):
                        print("no size given!!!!\n");
                        PrintUsage();
                        break;
                    
                    if(len(sys.argv) <5):
                        filename = "bins/intRom.bin";
                        print("no filename given, bins/intRom.bin is used\n");
                    else:
                        filename = str(sys.argv[4])
                    try:
                        size = int(sys.argv[3]);
                    except:
                        try:
                            size = int(sys.argv[3],16);
                        except:
                            print("wrong argument for size")
                            PrintUsage();
                            break;

                    print(" size: ", int(size / 1024), " kB")
                    

                    job = jobReadIntRom;
                    state = 10;
                    file = open(filename,'wb');

                
                elif(opt1.lower().find("readextflash") != -1):     ################################### READ ext FLASH
                    if(len(sys.argv) <4):
                        print("no size given!!!!\n");
                        PrintUsage();
                        break;
                    
                    if(len(sys.argv) <5):
                        filename = "bins/extFlash.bin";
                        print("no filename given, bins/extFlash.bin is used\n");
                    else:
                        filename = str(sys.argv[4])
                    try:
                        size = int(sys.argv[3]);
                    except:
                        try:
                            size = int(sys.argv[3],16);
                        except:
                            print("wrong argument for size")
                            PrintUsage();
                            break;

                    print(" size: ", int(size / 1024), " kB")
                    

                    job = jobReadExtFlash;
                    state = 10;
                    file = open(filename,'wb');

                elif(opt1.lower().find("writeextflash") != -1):     ################################### Write ExtFlash
                    if(len(sys.argv) <4):
                        print("no  filename and Flash /ECU type given !!!!\n");
                        PrintUsage();
                        break;
                    
                    if(len(sys.argv) <5):
                        print("no flash/ECU type given !!\n");
                        PrintUsage();
                        break;
                    else:
                        filename = str(sys.argv[3])
                    try:
                        file_stats = os.stat(filename);
                    except:
                        print("wrong filename or not existent ?!? \n");
                        PrintUsage();
                        break;

                    #type
                    if( sys.argv[4].lower().find("me7") != -1):
                        eetype = T_29FX00B;
                        print("\n Flash/Ecu Type is ME7.x.x variant\n");
                    elif( sys.argv[4].lower().find("simos3") != -1):
                        eetype = T_29FX00B_Simos3;
                        print("\n Flash/Ecu Type is Simos 3.x variant\n");
                    elif( sys.argv[4].lower().find("edc15") != -1):
                        eetype = T_29FX00BT_EDC15;
                        print("\n Flash/Ecu Type 29fxxxBT(Top boot) is EDC15 variant\n");

                        

                    else:
                        print("wrong argument for type")
                        PrintUsage();
                        break;

                    size = file_stats.st_size;


                    print(" size: ", int(size / 1024), " kB")
                    

                    job = jobWriteExtFlash;
                    state = 10;
                    file = open(filename,'rb');
                    
                    
                elif(opt1.lower().find("readeeprom") != -1):     ################################### READ eeprom
                    if(len(sys.argv) <6):
                        print("too few arguments .. !!!!\n");
                        PrintUsage();
                        break;
                    expectedArgSize = 9
                    
                    success, expectedArgSize, sscType = ParsePeriphType(sys.argv[3].lower(), 9, 7);

                    if(success == False):
                        print("wrong argument for peripheral type")
                        PrintUsage();
                        break;
                        
                    #type
                    success, eetype = ParseEEType(sys.argv[4], sscType);
                    if(success == False):
                        print("wrong argument for type")
                        PrintUsage();
                        break;


                    

                    if(sscType == i2cType):
                        inputPort = "Port4"     #not used in i2c
                        inputPin = "pin7"     #not used in i2c
                    else:
                        inputPort = sys.argv[5]
                        inputPin = sys.argv[6]

                    #parse chip slect for spi devices
                    success , portAddr8, directionPortAddress8, pinnum = GetPort(inputPort,inputPin)
                    if(success == False):
                        print("port or pin wrong parsed \n")
                        PrintUsage();
                        break;
                    
                    if(len(sys.argv) <expectedArgSize):
                        filename = "bins/eeprom.bin";
                        print("no filename given, bins/eeprom.bin is used\n");
                    else:
                        filename = str(sys.argv[expectedArgSize-1])

                    #size argument
                    try:
                        size = int(sys.argv[expectedArgSize-2]);
                    except:
                        try:
                            size = int(sys.argv[expectedArgSize-2],16);
                        except:
                            print("wrong argument for size")
                            PrintUsage();
                            break;
                        
                    print("read size: ", hex(size))

                    job = jobReadEeprom;
                    state = 10;
                    file = open(filename,'wb');


                elif(opt1.lower().find("writeeeprom") != -1) :     ################################### write eeprom
                    
                    if(len(sys.argv) <5):
                        print("too few arguments .. !!!!\n");
                        PrintUsage();
                        break;
                    expectedArgSize = 8

                    success, expectedArgSize, sscType = ParsePeriphType(sys.argv[3].lower(), 8, 6);

                    if(success == False):
                        print("wrong argument for peripheral type")
                        PrintUsage();
                        break;
                        
                    #type
                    success, eetype = ParseEEType(sys.argv[4], sscType);
                    if(success == False):
                        print("wrong argument for type")
                        PrintUsage();
                        break;
                    
                    if(len(sys.argv) <expectedArgSize):
                        print("no filename given\n");
                        PrintUsage();
                        break;
                    else:
                        filename = str(sys.argv[expectedArgSize-1])

                    # check if file is existent and print size
                    try:
                        file_stats = os.stat(filename);
                    except:
                        print("wrong filename or not existent ?!? \n");
                        PrintUsage();
                        break;
                    
                    size = file_stats.st_size;
                    print(" file size: ", size, " B")

                    if(sscType == i2cType):
                        inputPort = "Port4"
                        inputPin = "pin7"
                    else:
                        inputPort = sys.argv[5]
                        inputPin = sys.argv[6]
                        
                    success , portAddr8, directionPortAddress8, pinnum = GetPort(inputPort,inputPin)
                    if(success == False):
                        print("port or pin wrong parsed \n")
                        PrintUsage();
                        break;

                    job = jobWriteEeprom;
                    state = 10;
                    file = open(filename,'rb');
                else:
                    print("wrong main command parsed (writeeeprom, readextflash ....) ")
                    PrintUsage();
                    exitt = 1;
            except:
                print("wrong arguments for baudrate or main command(writeeeprom, readextflash ....)")
                traceback.print_exc()
                PrintUsage();
                exitt = 1;
        
        elif state == 10:
            if printwait == 0:
                print("Waiting for K+Can or KKL Adapter (plug in USB if not done!!)");
                printwait = 1;
            while (usbthere == 0):
                
                time.sleep(1);
                usbPort = serial.tools.list_ports.grep("USB Serial Port");
                
                for port in usbPort:
                    ports += [port];
                    #print(port);
                    usbthere = 1;
                    state = 11;
                    printwait = 0;
                    
        elif state == 11:
            comcounter = 0;
        
            if(len(ports) > 1):
                
                while(comcounter < len(ports)):
                    print("num: ",comcounter," : ", ports[comcounter]);
                    comcounter +=1;
                num = input("type com to use ( pos number)");
                try:
                    comcounter = int(num);
                    if( comcounter > len(ports)) | (comcounter < 0):
                        print("wrong input");
                        usbthere = 0;
                        state = 10;
                        ports = [];
                except:
                    print("wrong input");
                    usbthere = 0;
                    state = 10;
                    ports = [];
            if(usbthere == 1):
                print("using ", ports[comcounter].device,"\n");
                ser=serial.Serial(ports[comcounter].device, baud,timeout=3)
                ser.reset_input_buffer();
                state = 20;

        elif state == 20:
            try:
                exitt = RunFunc(exitt, ser, file, job, startAddr, size, eetype, portAddr8, directionPortAddress8, pinnum, sscType);
            except:
                exitt = -1;
                traceback.print_exc()
                print("kb-hit or exception exit")
            
    except :
        exitt = 1;
        traceback.print_exc()
        print("kb-hit or exception exit")
try:
    ser.close();
    file.close();
except:
    pass


