### Main Program Script File

import mpacket, pickle
from sys import argv
from os import SEEK_END, path, makedirs
from math import ceil

def main():
  if(len(argv) == 1):
    print("Usage: main.py file1.ext [file2.ext [...]]")
    return 0
    pass
  else:
    rawList = []
    sucList = []
    for i in range(1, len(argv)):
      rawList.append(argv[i])
      pass
    for file in rawList:
      try:
        sucess = open(file, "r")
        sucList.append(sucess)
        pass
      except FileNotFoundError:
        print("\n\"" + str(file) + "\" is not a file, skipping.")
        pass
      pass
    del rawList
    for fStream in sucList:
      pacList = []
      fStream.seek(0, SEEK_END)
      fSize = fStream.tell()
      pCount = ceil(fSize / 512)
      fStream.seek(0)
      for p in range(pCount):
        packet = mpacket.MPacket()
        for line in fStream:
          for byte in line:
            if(packet.dB_Loc >= (packet.blockSize - 1)):
              pacList.append(packet)
              pass
            else:
              packet.writeByte(byte)
              pass
            pass
          pass
        fileNameStr = "Packet" + str(p) + ".mpk.pkl"
        folderNameStr = "./Pickle-Files/File" + str(sucList.index(fStream)) + "/"
        fullPath = folderNameStr + fileNameStr
        if(not path.exists(folderNameStr)):
          makedirs(folderNameStr)
          pass
        pFile = open(fullPath, "wb")
        pickle.dump(packet.dataBlock, pFile)
        pass
      pass
    return 0
    pass
  pass

if __name__ == "__main__":
  main()
  pass
