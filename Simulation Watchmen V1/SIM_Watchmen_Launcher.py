# NX 2312
# Journal created by muhsin.caglar on Wed Oct 16 15:03:30 2024 GMT Daylight Time
#
import math
import NXOpen
import os
import subprocess
import sys
def main() : 
    username = str(os.getlogin())
    username = username.replace(".", "")
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    FileName = str(theSession.Parts.Work.FullPath)
    FilePath = str(theSession.Parts.Work.FullPath)
    FilePath = FilePath.replace("\\","\\\\")
    FileName = FileName.rsplit("\\", 1)[-1].rsplit(".", 1)[0]
    FilePath = FilePath.rsplit("\\", 2)[0]
    
    File = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\DATA\FILEPATH-" + username +".txt", "w")
    File.write(FilePath)
    #File.write(FileName)
    File.close    
    
    exe_path = "S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\SIM_Watchmen_UI\\SIM_Watchmen_UI\\bin\\Release\\net8.0-windows\\SIM_Watchmen_UI.exe"
    proc = subprocess.Popen([exe_path], shell=True, stdin=None, stdout=None, stderr=None)
    
    
    #subprocess.run([exe_path], capture_output=False, text=False, check=False)

    return
    sys.exit()
    
if __name__ == '__main__':
    main()