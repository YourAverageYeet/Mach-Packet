class MPacket():
  """
  A simple, self-programmed packet
  """
  def __init__(self):
    self.HEADER = "MCMP"
    self.version = 0.1
    self.blockSize = 512
    self.dataBlock = []
    self.dataCRC = None
    self.FOOTER = "V0.1"
    self.dB_Loc = 0
    pass
  def writeByte(self, byteVal = 0x00):
    """
    Write a byte to the latest location in the data block.
    """
    if(len(self.dataBlock) == self.blockSize or len(self.dataBlock) > self.blockSize):
      print("ERR: Tried to store data past limit")
      return 1
    else:
      self.dataBlock.append(byteVal)
      self.dB_Loc += 1
      return 0
    pass
  def readByte(self, byteLoc = None):
    """
    Reads a byte from the current or given location
    """
    if(byteLoc):
      bV = self.dataBlock[byteLoc]
      pass
    else:
      bV = self.dataBlock[self.dB_Loc]
      pass
    return bV
  def calcCRC(self, setCRC = False):
    """
    Calculates the internal data-checking CRC
    """
    totalVal = 0
    for v in range(0, len(self.dataBlock)):
      totalVal += self.dataBlock
      pass
    dCRC = totalVal % 256
    if(setCRC):
      self.dataCRC = dCRC
      return 0
      pass
    else:
      return dCRC
    pass
  def checkCRC(self):
    """
    Check current CRC against current data
    """
    cCRC = self.calcCRC(False)
    sCRC = self.dataCRC
    if(sCRC != cCRC):
      return -1
    else:
      return 0
    pass
  pass