# NX 2312
# Journal created by muhsin.caglar on Thu Sep  5 11:36:29 2024 GMT Summer Time
#
import math
import NXOpen
import NXOpen.MenuBar


import math
import NXOpen
import NXOpen.CAM
import NXOpen.Display
import subprocess 


import os








def main() : 
    
    
    exe_path = "S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_Step_File_Creator\\NX_Step_File_Creator_App\\NX_STEP_File_Creator_App.exe"
    subprocess.run([exe_path], capture_output=True, text=True, check=True)

    with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_Step_File_Creator\\NX_Step_File_Creator_App\\STEPFILEDATA\\STEPFILEPATH.txt") as file:
        lines = [line.rstrip() for line in file]
        if 'USER CANCELLED' in lines:
            return
    text_file = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_Step_File_Creator\\NX_Step_File_Creator_App\\STEPFILEDATAOutput.txt", "w")
    step_file_path = str(lines)
    step_file_path = step_file_path.replace("\\\\","\\")
    step_file_path = step_file_path.replace("[","")
    step_file_path = step_file_path.replace("]","")
    step_file_path = step_file_path.replace("'","")
    
    last_index = step_file_path.rfind("\\")


    if last_index != -1:
        assembly_step_file = step_file_path[last_index + 1:]
    
    
    assembly_step_file.replace(".","_")
    text_file.write(step_file_path + "xxxxx")
    text_file.write(assembly_step_file)
    final_file_path = step_file_path.replace(assembly_step_file,"")
    
    
    
    
    text_file.write("xxxxx")
    text_file.write(final_file_path)
    
    
    
    
    
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Load Part")
    
    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(step_file_path, NXOpen.DisplayPartOption.AllowAdditional)
    
    workPart = theSession.Parts.Work # H2T5310-901-1AF-0001_stp
    displayPart = theSession.Parts.Display # H2T5310-901-1AF-0001_stp
    partLoadStatus1.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    theUI = NXOpen.UI.GetUI() #type: NXOpen.UI
    menuButton1 = theUI.MenuBarManager.GetButtonFromName("UG_PREFERENCES_3D_INPUT_DEVICES")
    
    menuButton1.ButtonSensitivity = NXOpen.MenuBar.MenuButton.SensitivityStatus.Insensitive
    
    menuButton2 = theUI.MenuBarManager.GetButtonFromName("_3DX_BUTTONEDITOR")
    
    menuButton2.ButtonSensitivity = NXOpen.MenuBar.MenuButton.SensitivityStatus.Sensitive
    
    theSession.CleanUpFacetedFacesAndEdges()


##### GET Component PRT file directories
    path = "B:\\Internal projects\\NX\\Testing\\New folder"
    
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    mylist = os.listdir(path)
    print(mylist)
    mylist = [item for item in mylist if ".prt" in item]
    mylist = [item for item in mylist if "_stp.prt" not in item]
    
    
    text_file = open("B:\\Internal projects\\NX\\Testing\\New folder\\Output.txt", "w")
    strlist = str(mylist)
    text_file.write(strlist)
    text_file.close()
    
    
    no_of_parts = len(mylist)
    
    for i in range(len(mylist)):

        theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
        workPart = theSession.Parts.Work
        displayPart = theSession.Parts.Display
        workPart.Close(NXOpen.BasePart.CloseWholeTree.TrueValue, NXOpen.BasePart.CloseModified.UseResponses, None)

        theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
        workPart = theSession.Parts.Work
        displayPart = theSession.Parts.Display
        markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Load Part")
        openfile_path = str(final_file_path + mylist[i])
        basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(openfile_path, NXOpen.DisplayPartOption.AllowAdditional)
        
        workPart = theSession.Parts.Work 
        displayPart = theSession.Parts.Display 
        partLoadStatus1.Dispose()
        theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
        theUI = NXOpen.UI.GetUI() #type: NXOpen.UI
        menuButton1 = theUI.MenuBarManager.GetButtonFromName("UG_PREFERENCES_3D_INPUT_DEVICES")
    
        menuButton1.ButtonSensitivity = NXOpen.MenuBar.MenuButton.SensitivityStatus.Insensitive
    
        menuButton2 = theUI.MenuBarManager.GetButtonFromName("_3DX_BUTTONEDITOR")
    
        menuButton2.ButtonSensitivity = NXOpen.MenuBar.MenuButton.SensitivityStatus.Sensitive
    
        theSession.CleanUpFacetedFacesAndEdges()
        
        markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
        
        
        
        
    
        stepCreator1 = theSession.DexManager.CreateStepCreator()
    
        stepCreator1.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap214
    
        stepCreator1.BsplineTol = 0.001
    
        stepCreator1.SettingsFile = "C:\\Program Files\\Siemens\\NX2312\\step214ug\\ugstep214.def"
    
        stepCreator1.ObjectTypes.Curves = True
    
        stepCreator1.ObjectTypes.Surfaces = True
    
        stepCreator1.ObjectTypes.Solids = True
    
        stepCreator1.ObjectTypes.Csys = True
    
        stepCreator1.ObjectTypes.ProductData = True
    
        stepCreator1.ObjectTypes.PmiData = True
        
        output_file_name = str(mylist[i].replace(".prt",".stp"))
    
        stepCreator1.InputFile = str(final_file_path + mylist[i])
    
        stepCreator1.OutputFile = final_file_path + output_file_name
    
        theSession.SetUndoMarkName(markId1, "Export STEP File Dialog")
    
        markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Export STEP File")
    
        theSession.DeleteUndoMark(markId2, None)
    
        markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Export STEP File")
    
        stepCreator1.OutputFile = final_file_path + output_file_name
    
        stepCreator1.FileSaveFlag = False
    
        stepCreator1.LayerMask = "1-256"
    
        stepCreator1.ProcessHoldFlag = True
    
        nXObject1 = stepCreator1.Commit()
    
        theSession.DeleteUndoMark(markId3, None)
    
        theSession.SetUndoMarkName(markId1, "Export STEP File")
    
        stepCreator1.Destroy()
    
        theSession.CleanUpFacetedFacesAndEdges()












if __name__ == '__main__':
    main()