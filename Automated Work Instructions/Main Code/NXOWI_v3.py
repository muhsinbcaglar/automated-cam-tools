# NX 2312
# Journal created by muhsin.caglar on Thu Aug  1 14:27:33 2024 GMT Summer Time
#

import math
import NXOpen
import NXOpen.CAM
import NXOpen.Display
import subprocess
import NXOpen.Layer
import os
import time
import sys

def create_view_for_tpds() : 

    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Replace View")
    
    layout1 = workPart.Layouts.FindObject("L1")
    modelingView1 = workPart.ModelingViews.FindObject("Isometric")
    layout1.ReplaceView(workPart.ModelingViews.WorkView, modelingView1, True)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.71509032863639632
    rotMatrix1.Xy = -0.69903206070300583
    rotMatrix1.Xz = 0.0
    rotMatrix1.Yx = 0.40358634841905922
    rotMatrix1.Yy = 0.41285759373312153
    rotMatrix1.Yz = 0.81649658092772615
    rotMatrix1.Zx = -0.57075728752286692
    rotMatrix1.Zy = -0.58386880838610178
    rotMatrix1.Zz = 0.57735026918962584
    translation1 = NXOpen.Point3d(6.0268643439188425, 57.285962720666745, 81.385000682129203)
    modelingView1.SetRotationTranslationScale(rotMatrix1, translation1, 0.062198663806658408)
    modelingView1.Fit()
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    theSession.UpdateManager.ClearErrorList()
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects1 = [NXOpen.TaggedObject.Null] * 1

    
    
    try:
        modelingView1 = workPart.ModelingViews.FindObject("IsometricWI")
        objects1[0] = modelingView1
        nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
  
        id1 = theSession.NewestVisibleUndoMark
        nErrs2 = theSession.UpdateManager.DoUpdate(id1)
    except NXOpen.NXException as e:
        e = None
    
    theSession.DeleteUndoMark(markId1, None)

    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Add View")
    
    view1 = workPart.Views.SaveAsPreservingCase(workPart.ModelingViews.WorkView, "IsometricWI", True, False)




def manual_exit_module():
    exe_path1 = "S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\NX_OWI_Manual_Exit\\NXOWI_Manual_Exit\\bin\\Debug\\net8.0-windows\\NXOWI_Manual_Exit.exe"
    manual_exit = subprocess.Popen([exe_path1], shell=True, stdin=None, stdout=None, stderr=None)

def dismiss_error():
    exe_path1 = "S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\OWI_Creator_Help\\OWI_Creator_Help\\bin\\Debug\\net8.0\\OWI_Creator_Help.exe"
    subprocess.Popen([exe_path1], shell=True, stdin=None, stdout=None, stderr=None)
    
    return


### FUNCTION TO TURN PMI'S OFF
def NX_Turn_PMIs_Off():    
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    
    
    
    
    objects1 = [NXOpen.CAM.CAMObject.Null] * 1 
    theUI = NXOpen.UI.GetUI() #type: NXOpen.UI 
    ###
    lw = theSession.ListingWindow
    lw.Open()
    ###
    theParts = theSession.Parts
    theWorkPart = theParts.Work
    allPMIObjects = theWorkPart.PmiManager.Pmis
    i = 0
    for p in allPMIObjects:

        Index = p.GetDisplayInstances()[0]
        i = i + 1
        #lw.WriteLine(str(Index))
    #lw.WriteLine(str(i))
    objectArray1 = [NXOpen.DisplayableObject.Null] * i
    
    ii=0
    for p in allPMIObjects:
        Index1 = p.GetDisplayInstances()[0]
        objectArray1[ii] = Index1
        ii = ii + 1
    workPart.Layers.MoveDisplayableObjects(69, objectArray1)
    
    
    
    
    ###
    for p in allPMIObjects:

        Index = p.GetDisplayInstances()[0]
        Index2 = Index.Layer
        #lw.WriteLine(str(Index2))
    ####

    
    
    
    
    ## HIDE ALL PMI'S THAT MOVE TO LAYER 69
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Layer Settings Dialog")
    
    stateArray1 = [None] * 1 
    stateArray1[0] = NXOpen.Layer.StateInfo()
    stateArray1[0] = NXOpen.Layer.StateInfo(69, NXOpen.Layer.State.Hidden)
    workPart.Layers.ChangeStates(stateArray1, False)
    
    theSession.SetUndoMarkName(markId1, "Layer Settings")
    
    theSession.DeleteUndoMark(markId1, None)
    lw.WriteLine("TURNING PMI'S OFF FOR TOOL PATH DISPLAY SHEETS TO BE PUBLISHED")
    lw.WriteLine("CREATING TOOL PATH DISPLAY SHEETS")
    lw.Close()
    return
    
#FUNCTION TO TURN PMI'S ON  
def NX_Turn_PMIs_On():       
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    objects1 = [NXOpen.CAM.CAMObject.Null] * 1 
    theUI = NXOpen.UI.GetUI() #type: NXOpen.UI 
    ###
    lw = theSession.ListingWindow
    lw.Open()
    ###
    theParts = theSession.Parts
    theWorkPart = theParts.Work
    allPMIObjects = theWorkPart.PmiManager.Pmis
    i = 0
    for p in allPMIObjects:

        Index = p.GetDisplayInstances()[0]
        i = i + 1
        #lw.WriteLine(str(Index))
    #lw.WriteLine(str(i))
    objectArray1 = [NXOpen.DisplayableObject.Null] * i
    
    ii=0
    for p in allPMIObjects:
        Index1 = p.GetDisplayInstances()[0]
        objectArray1[ii] = Index1
        ii = ii + 1
    workPart.Layers.MoveDisplayableObjects(69, objectArray1)
    
    
    
    
    ###
    for p in allPMIObjects:

        Index = p.GetDisplayInstances()[0]
        Index2 = Index.Layer
        #lw.WriteLine(str(Index2))
    ####
    
    
    
    
    
    ## SHOW ALL PMI'S THAT MOVE TO LAYER 69
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Layer Settings Dialog")
    
    stateArray1 = [None] * 1 
    stateArray1[0] = NXOpen.Layer.StateInfo()
    stateArray1[0] = NXOpen.Layer.StateInfo(69, NXOpen.Layer.State.Selectable)
    workPart.Layers.ChangeStates(stateArray1, False)
    
    theSession.SetUndoMarkName(markId1, "Layer Settings")
    
    theSession.DeleteUndoMark(markId1, None)


    return 

###MAIN FUNCTION
def main() :
    notesreq = "YES"
    username = str(os.getlogin())
    username = username.replace(".", "")

    exe_path = "S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\NXOWI\\NXOWI\\bin\\Release\\net8.0-windows\\NXOWI.exe"
    subprocess.run([exe_path], capture_output=True, text=True, check=True)
    time.sleep(1)
    with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
        lines = [line.rstrip() for line in file]
        if 'USER CANCELLED' in lines:
            file.close()
            return
            sys.exit()
        else:
            file.close()
    #### LAUNCH ERROR CHECKER & MANUAL EXIT MODULE
    if username == "muhsincaglar":
        dismiss_error()
    time.sleep(0.5)
    
    ################# 
    exe_path11 = "S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\NX_OWI_Manual_Exit\\NXOWI_Manual_Exit\\bin\\Debug\\net8.0-windows\\NXOWI_Manual_Exit.exe"
    
    manual_exit = subprocess.Popen([exe_path11], stdin=None, stdout=None, stderr=None)
    
    
    theSession = NXOpen.Session.GetSession()
    theSession.Parts.LoadOptions.UsePartialLoading = False

    displayPart = theSession.Parts.Display
    workPart = theSession.Parts.Work
    FilePath = str(theSession.Parts.Work.FullPath)
    camSession = theSession.CreateCamSession()
    start_point = workPart.CAMSetup.CAMOperationCollection.FindObject("NC_PROGRAM")
    objects_at_start = NXOpen.CAM.NCGroup.GetMembers(start_point)
    
    #MODEL VIEW = ISOMETRIC, PMI'S ON
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Replace View")
    
    layout1 = workPart.Layouts.FindObject("L1")
    modelingView1 = workPart.ModelingViews.FindObject("Isometric")
    layout1.ReplaceView(workPart.ModelingViews.WorkView, modelingView1, True)    
    
    NX_Turn_PMIs_On()
    #


    lw = theSession.ListingWindow
    lw.Open()


    with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
        lines = [line.rstrip() for line in file]
        if 'USER CANCELLED' in lines:
            file.close()
            return
            sys.exit()
        else:
            file.close()
    WI_DATA = str(lines)
    
    WI_DATA = WI_DATA.replace("'","")
    WI_DATA = WI_DATA.replace("[","")   
    WI_DATA = WI_DATA.replace("]","")
    ##text_file1.write(WI_DATA)
    start_index = WI_DATA.rindex("-1- ")
    end_index = WI_DATA.rindex(" -1-")
    Project_Name = WI_DATA[start_index + 4: end_index]
    
    start_index = WI_DATA.rindex("-2- ")
    end_index = WI_DATA.rindex(" -2-")
    Program_Folder = WI_DATA[start_index + 4: end_index]
    
    start_index = WI_DATA.rindex("-3- ")
    end_index = WI_DATA.rindex(" -3-")
    Rev_No = WI_DATA[start_index + 4: end_index]
    
    start_index = WI_DATA.rindex("-4- ")
    end_index = WI_DATA.rindex(" -4-")
    Costumer_Name = WI_DATA[start_index + 4: end_index]

    start_index = WI_DATA.rindex("-5- ")
    end_index = WI_DATA.rindex(" -5-")
    Machine_Name = WI_DATA[start_index + 4: end_index]
    
    start_index = WI_DATA.rindex("-6- ")
    end_index = WI_DATA.rindex(" -6-")
    Instructions_Text = WI_DATA[start_index + 4: end_index]
    ##text_file1.write(Instructions_Text)
    
    Instructions_Text = Instructions_Text.replace(",","")
    Instructions_Text = Instructions_Text.replace("##",",")
    
    
    
    ##text_file.write(Instructions_Text)
    start_index = WI_DATA.rindex("-7- ")
    end_index = WI_DATA.rindex(" -7-")
    Datum_Info = WI_DATA[start_index + 4: end_index]
    Datum_Info = Datum_Info.replace(",","")
    Datum_Info = Datum_Info.replace("##",",")    
    
    
    start_index = WI_DATA.rindex("-8- ")
    end_index = WI_DATA.rindex(" -8-")
    WorkHold_Info = WI_DATA[start_index + 4: end_index]
    WorkHold_Info = WorkHold_Info.replace(",","")
    WorkHold_Info = WorkHold_Info.replace("##",",")    
    
    
    
    
    start_index = WI_DATA.rindex("-9- ")
    end_index = WI_DATA.rindex(" -9-")
    AsOpp_Info = WI_DATA[start_index + 4: end_index]
    
    start_index = WI_DATA.rindex("-10- ")
    end_index = WI_DATA.rindex(" -10-")
    Notes_Text = WI_DATA[start_index + 4: end_index]
    Notes_Text = Notes_Text.replace(",","")
    Notes_Text = Notes_Text.replace("##",",")

    start_index = WI_DATA.rindex("-11- ")
    end_index = WI_DATA.rindex(" -11-")
    TPDSheetsReq = WI_DATA[start_index + 4: end_index]
    
    
    
    #### JOB NOTES ####
    start_index = WI_DATA.rindex("-32- ")
    end_index = WI_DATA.rindex(" -32-")
    notesreq = WI_DATA[start_index + 4: end_index]
    
    
    start_index = WI_DATA.rindex("-12- ")
    end_index = WI_DATA.rindex(" -12-")
    JN_Note_1 = WI_DATA[start_index + 4: end_index]
    JN_Note_1 = JN_Note_1.replace(",","")
    JN_Note_1 = JN_Note_1.replace("##",",")
    
    start_index = WI_DATA.rindex("-13- ")
    end_index = WI_DATA.rindex(" -13-")
    JN_Note_2 = WI_DATA[start_index + 4: end_index]
    JN_Note_2 = JN_Note_2.replace(",","")
    JN_Note_2 = JN_Note_2.replace("##",",")

    start_index = WI_DATA.rindex("-14- ")
    end_index = WI_DATA.rindex(" -14-")
    JN_Note_3 = WI_DATA[start_index + 4: end_index]
    JN_Note_3 = JN_Note_3.replace(",","")
    JN_Note_3 = JN_Note_3.replace("##",",")


    start_index = WI_DATA.rindex("-15- ")
    end_index = WI_DATA.rindex(" -15-")
    JN_Note_4 = WI_DATA[start_index + 4: end_index]
    JN_Note_4 = JN_Note_4.replace(",","")
    JN_Note_4 = JN_Note_4.replace("##",",")



    start_index = WI_DATA.rindex("-16- ")
    end_index = WI_DATA.rindex(" -16-")
    JN_Note_5 = WI_DATA[start_index + 4: end_index]
    JN_Note_5 = JN_Note_5.replace(",","")
    JN_Note_5 = JN_Note_5.replace("##",",")
    
    
    start_index = WI_DATA.rindex("-17- ")
    end_index = WI_DATA.rindex(" -17-")
    JN_Note_6 = WI_DATA[start_index + 4: end_index]
    JN_Note_6 = JN_Note_6.replace(",","")
    JN_Note_6 = JN_Note_6.replace("##",",")
    
    
    
    
    start_index = WI_DATA.rindex("-18- ")
    end_index = WI_DATA.rindex(" -18-")
    JN_Note_7 = WI_DATA[start_index + 4: end_index]
    JN_Note_7 = JN_Note_7.replace(",","")
    JN_Note_7 = JN_Note_7.replace("##",",")
    
    
    
    
    start_index = WI_DATA.rindex("-19- ")
    end_index = WI_DATA.rindex(" -19-")
    JN_Note_8 = WI_DATA[start_index + 4: end_index]
    JN_Note_8 = JN_Note_8.replace(",","")
    JN_Note_8 = JN_Note_8.replace("##",",")
    
    
    
    
    
    start_index = WI_DATA.rindex("-20- ")
    end_index = WI_DATA.rindex(" -20-")
    JN_Note_9 = WI_DATA[start_index + 4: end_index]
    JN_Note_9 = JN_Note_9.replace(",","")
    JN_Note_9 = JN_Note_9.replace("##",",")


    start_index = WI_DATA.rindex("-21- ")
    end_index = WI_DATA.rindex(" -21-")
    JN_Note_10 = WI_DATA[start_index + 4: end_index]
    JN_Note_10 = JN_Note_10.replace(",","")
    JN_Note_10 = JN_Note_10.replace("##",",")    
    
    start_index = WI_DATA.rindex("-22- ")
    end_index = WI_DATA.rindex(" -22-")
    JN_Note_1_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_1_Ref = JN_Note_1_Ref.replace(",","")
    JN_Note_1_Ref = JN_Note_1_Ref.replace("##",",") 


    start_index = WI_DATA.rindex("-23- ")
    end_index = WI_DATA.rindex(" -23-")
    JN_Note_2_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_2_Ref = JN_Note_2_Ref.replace(",","")
    JN_Note_2_Ref = JN_Note_2_Ref.replace("##",",") 

    start_index = WI_DATA.rindex("-24- ")
    end_index = WI_DATA.rindex(" -24-")
    JN_Note_3_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_3_Ref = JN_Note_3_Ref.replace(",","")
    JN_Note_3_Ref = JN_Note_3_Ref.replace("##",",") 

    start_index = WI_DATA.rindex("-25- ")
    end_index = WI_DATA.rindex(" -25-")
    JN_Note_4_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_4_Ref = JN_Note_4_Ref.replace(",","")
    JN_Note_4_Ref = JN_Note_4_Ref.replace("##",",") 


    start_index = WI_DATA.rindex("-26- ")
    end_index = WI_DATA.rindex(" -26-")
    JN_Note_5_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_5_Ref = JN_Note_5_Ref.replace(",","")
    JN_Note_5_Ref = JN_Note_5_Ref.replace("##",",")

    start_index = WI_DATA.rindex("-27- ")
    end_index = WI_DATA.rindex(" -27-")
    JN_Note_6_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_6_Ref = JN_Note_6_Ref.replace(",","")
    JN_Note_6_Ref = JN_Note_6_Ref.replace("##",",")

    start_index = WI_DATA.rindex("-28- ")
    end_index = WI_DATA.rindex(" -28-")
    JN_Note_7_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_7_Ref = JN_Note_7_Ref.replace(",","")
    JN_Note_7_Ref = JN_Note_7_Ref.replace("##",",")

    start_index = WI_DATA.rindex("-29- ")
    end_index = WI_DATA.rindex(" -29-")
    JN_Note_8_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_8_Ref = JN_Note_8_Ref.replace(",","")
    JN_Note_8_Ref = JN_Note_8_Ref.replace("##",",")
    
    
    start_index = WI_DATA.rindex("-29- ")
    end_index = WI_DATA.rindex(" -29-")
    JN_Note_8_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_8_Ref = JN_Note_8_Ref.replace(",","")
    JN_Note_8_Ref = JN_Note_8_Ref.replace("##",",")

    start_index = WI_DATA.rindex("-30- ")
    end_index = WI_DATA.rindex(" -30-")
    JN_Note_9_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_9_Ref = JN_Note_9_Ref.replace(",","")
    JN_Note_9_Ref = JN_Note_9_Ref.replace("##",",")
    
    start_index = WI_DATA.rindex("-31- ")
    end_index = WI_DATA.rindex(" -31-")
    JN_Note_10_Ref = WI_DATA[start_index + 4: end_index]
    JN_Note_10_Ref = JN_Note_10_Ref.replace(",","")
    JN_Note_10_Ref = JN_Note_10_Ref.replace("##",",")    
    
    start_index = WI_DATA.rindex("-33- ")
    end_index = WI_DATA.rindex(" -33-")
    JN_PartName = WI_DATA[start_index + 4: end_index]
    JN_PartName = JN_PartName.replace(",","")
    JN_PartName = JN_PartName.replace("##",",")     
    
    
    fp_index = FilePath.rindex("\\")
    
    FilePath1 = FilePath[:fp_index+1]
    FilePath = FilePath.replace("\\","\\\\")
    
 
    pdfdirectory = str(FilePath1 + "Work Instructions\\")
    pdfdirectory2 = str(pdfdirectory + "Tool Path Display Sheets\\")
    pdfpath = str(pdfdirectory + Program_Folder + " - Work Instructions.pdf")
    
    

    if not os.path.exists(pdfdirectory):
        os.makedirs(pdfdirectory)
    if not os.path.exists(pdfdirectory2):
        os.makedirs(pdfdirectory2)    
    
    
    
    

    #text_file.close()
    
    
    
    

    group_list = []
    checked_list = []
    operation_list = []
    def get_group_objects(group_name,workPart):
        find_it = workPart.CAMSetup.CAMOperationCollection.FindObject(group_name)
        new_objects = NXOpen.CAM.NCGroup.GetMembers(find_it)
        return new_objects
    def _get_op_data(obj):
        op_data = {}
        op_data['Operation name'] = obj.Name
        program_name = obj.GetParent(NXOpen.CAM.CAMSetup.View.ProgramOrder)
        op_data['Program Name'] =  program_name.Name
        obj.Print()
        return op_data
    
    op_data_list = []
    for each_object in objects_at_start:
        if workPart.CAMSetup.IsGroup(each_object) == True:
            group_list.append(each_object.Name)
        elif workPart.CAMSetup.IsOperation(each_object) == True:
            op_data = _get_op_data(each_object)
            op_data_list.append(op_data)
 
    while group_list != checked_list:
        for each_object in group_list:
            if each_object not in checked_list:
                temp_objects = get_group_objects(each_object,workPart)
                for sub_object in temp_objects:
                    if workPart.CAMSetup.IsGroup(sub_object) == True:
                        group_list.append(sub_object.Name)
                    elif workPart.CAMSetup.IsOperation(sub_object) == True:
                        op_data = _get_op_data(sub_object)
                        op_data_list.append(op_data)
                checked_list.append(each_object)
    text_file = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\Output.txt", "w")
    text_file1 = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\Output1.txt", "w")
    text_file3 = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\Output3.txt", "w")
    text_file5 = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\Output5.txt", "w")
    op_data_list_programs = [str(item) for item in op_data_list]
    text_file3.write(str(TPDSheetsReq))
    ##op_data_list1 = [item for item in op_data_list if "Operation name" not in item]
    op_data_list1 = [str(item) for item in op_data_list]
    op_data_list1 = [item.replace('}', '') for item in op_data_list1]
    op_data_list1 = [item.replace('{', '') for item in op_data_list1]
    op_data_list1 = [item.replace(',', '') for item in op_data_list1]
    substring1 = "Program Name': "
    op_data_list1 = [item[item.find(substring1) + len(substring1):] if substring1 in item else item for item in op_data_list1]
    op_data_list1 = [item.replace(str("'"), '') for item in op_data_list1]
    op_data_list2 = []
    for item in op_data_list1:
        if item not in op_data_list2:
            op_data_list2.append(item)
    op_data_list2 = [item for item in op_data_list2 if len(item) <= 15]
    op_data_list2 = [item for item in op_data_list2 if Program_Folder in item]
    op_data_list2 = [item for item in op_data_list2 if item != 'NONE']
    
    ##s1 = str(op_data_list2[0])
    s1 = str(op_data_list2)
    s = str(op_data_list)
    text_file3.write(pdfdirectory2)
    #text_file1.write(s1)
    op_data_list_programs = [item for item in op_data_list_programs if Program_Folder in item]
    op_data_list_programs = [item.replace(',', '') for item in op_data_list_programs]
    op_data_list_programs = [item.replace('}', '') for item in op_data_list_programs]
    op_data_list_programs = [item.replace('{', '') for item in op_data_list_programs]
    op_data_list_programs = [item.replace(str("'"), '') for item in op_data_list_programs]
    op_data_list_programs = [item.split('Operation name: ')[1].split(' Program Name:')[0] for item in op_data_list_programs]
    text_file3.write(str(op_data_list_programs))
    
    text_file5.write(s1)
    s = s.replace("[","")
    s = s.replace("{","")
    s = s.replace("}","")
    s = s.replace("]","")
    s = s.replace(",","\n")
    s_index1 = s.rindex("'Operation name':")
    s = s[s_index1:]
    s_index2 = s.rindex("'Program Name':")
    s = s[:s_index2]
    s = s.replace("'Operation name': '","")
    s = s.replace("'","")
    s= s.strip()
    s = str(op_data_list_programs[len(op_data_list_programs) - 1])
    Selected_Op = s
    
    text_file5.write(Selected_Op)
    
    

    

    #######################################################  
    ### TOOL PATH DISPLAY SHEET LOOP
   
    time.sleep(2)
    if TPDSheetsReq == " Tool Path Display Required":
        NX_Turn_PMIs_Off()
        create_view_for_tpds()
        no_of_ops = len(op_data_list_programs)
    
        for ix in range(len(op_data_list_programs)):
            ##GET VIEW RIGHT
            theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
            workPart = theSession.Parts.Work
            displayPart = theSession.Parts.Display
            markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Replace View")
    
            layout1 = workPart.Layouts.FindObject("L1")
            modelingView1 = workPart.ModelingViews.FindObject("IsometricWI")
            layout1.ReplaceView(workPart.ModelingViews.WorkView, modelingView1, True)
            
            theSession.CAMSession.PathDisplay.DisplayToolPath = True

            planarMilling1 = workPart.CAMSetup.CAMOperationCollection.FindObject(str(op_data_list_programs[ix]))
            theSession.CAMSession.PathDisplay.ShowToolPath(planarMilling1)
            
            inTaskEnv1 = theSession.IsBatch
            
            theSession.CAMSession.PathDisplay.StepDisplay(True)
            
            objects1 = [NXOpen.CAM.CAMObject.Null] * 1 
            objects1[0] = planarMilling1
            workPart.CAMSetup.DeleteWorkInstructions(objects1)
            
            objectWorkInstructionBuilder1 = workPart.CAMSetup.CreateObjectWorkInstructionBuilder(planarMilling1)
            
            markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
            
            theSession.SetUndoMarkName(markId2, "Author Work Instructions Dialog")
            
            objectWorkInstructionBuilder1.Work.SheetNumber = 1
            
            sheettitle1 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.SheetTitle = str("EVTEC Superlight - " + Program_Folder +" - "+ op_data_list_programs[ix] + " - Tool Path Display Sheet")
            
            sheetnum1 = objectWorkInstructionBuilder1.Work.AddSheet()
            
            sheettitle2 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.TemplateName = "Tool Path Display Sheet [Trial 1]"
            
            objectWorkInstructionBuilder1.Work.CommitMaster()
            
            itemnames1 = [None] * 7 
            itemnames1[0] = "OWI_TEXT_1"
            itemnames1[1] = "OWI_TEXT_2"
            itemnames1[2] = "OWI_PATH_VIEW_2"
            itemnames1[3] = "OWI_PATH_VIEW_1"
            itemnames1[4] = "OWI_PATH_VIEW_3"
            itemnames1[5] = "OWI_PATH_VIEW_4"
            itemnames1[6] = "OWI_TEXT_3"
            objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames1)
            
            camera1 = workPart.Cameras.FindObject("NXOWI_CACHE_CURRENT_VIEW")
            cameraBuilder1 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera1)
            
            nXObject1 = cameraBuilder1.Commit()
            
            cameraBuilder1.Destroy()
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_1"
            
            multilinetext1 = []
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext1)
            
            sheettitle3 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.SheetTitle = str("EVTEC Superlight - " + Program_Folder +" - "+ op_data_list_programs[ix] + " - Tool Path Display Sheet")
            
            multilinetext2 = [None] * 1 
            multilinetext2[0] = Project_Name
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext2)
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            camera2 = nXObject1
            cameraBuilder2 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera2)
            
            nXObject2 = cameraBuilder2.Commit()
            
            cameraBuilder2.Destroy()
            
            objectWorkInstructionBuilder1.Work.FontSize = 16
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            camera3 = nXObject2
            cameraBuilder3 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera3)
            
            nXObject3 = cameraBuilder3.Commit()
            
            cameraBuilder3.Destroy()
            
            multilinetext3 = [None] * 1 
            multilinetext3[0] = Project_Name
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext3)
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_2"
            
            multilinetext4 = []
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext4)
            
            camera4 = nXObject3
            cameraBuilder4 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera4)
            
            nXObject4 = cameraBuilder4.Commit()
            
            cameraBuilder4.Destroy()
            
            sheettitle4 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            camera5 = nXObject4
            cameraBuilder5 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera5)
            
            nXObject5 = cameraBuilder5.Commit()
            
            cameraBuilder5.Destroy()
            
            objectWorkInstructionBuilder1.Work.FontSize = 16
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            camera6 = nXObject5
            cameraBuilder6 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera6)
            
            nXObject6 = cameraBuilder6.Commit()
            
            cameraBuilder6.Destroy()
            
            multilinetext5 = [None] * 1 
            multilinetext5[0] = Machine_Name
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext5)
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_PATH_VIEW_1"
            
            camera7 = nXObject6
            cameraBuilder7 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera7)
            
            nXObject7 = cameraBuilder7.Commit()
            
            cameraBuilder7.Destroy()
            
            camera8 = nXObject7
            cameraBuilder8 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera8)
            
            nXObject8 = cameraBuilder8.Commit()
            
            cameraBuilder8.Destroy()
            
            sheettitle5 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.ViewTool = True
            
            objectWorkInstructionBuilder1.Work.SetToolDisplayMotion(0, 0)
            
            cameraBuilder9 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, NXOpen.Display.Camera.Null)
            
            nXObject9 = cameraBuilder9.Commit()
            
            cameraBuilder9.Destroy()
            
            objectWorkInstructionBuilder1.Work.CaptureCurrentView()
            
            objectWorkInstructionBuilder1.Work.CameraName = "NXOWI_CACHE_CURRENT_VIEW"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            camera9 = nXObject8
            cameraBuilder10 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera9)
            
            nXObject10 = cameraBuilder10.Commit()
            
            cameraBuilder10.Destroy()
            
            layout1.ReplaceView(modelingView1, modelingView1, False)
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_PATH_VIEW_2"
            
            camera10 = nXObject10
            cameraBuilder11 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera10)
            
            nXObject11 = cameraBuilder11.Commit()
            
            cameraBuilder11.Destroy()
            
            sheettitle6 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.ViewTool = True
            
            objectWorkInstructionBuilder1.Work.CameraName = "Top"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_PATH_VIEW_3"
            
            camera11 = nXObject11
            cameraBuilder12 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera11)
            
            nXObject12 = cameraBuilder12.Commit()
            
            cameraBuilder12.Destroy()
            
            sheettitle7 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.ViewTool = True
            
            objectWorkInstructionBuilder1.Work.CameraName = "Front"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_PATH_VIEW_4"
            
            camera12 = nXObject12
            cameraBuilder13 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera12)
            
            nXObject13 = cameraBuilder13.Commit()
            
            cameraBuilder13.Destroy()
            
            sheettitle8 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            objectWorkInstructionBuilder1.Work.CameraName = "Back"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_3"
            
            multilinetext6 = []
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext6)
            
            sheettitle9 = objectWorkInstructionBuilder1.Work.SheetTitle
            
            multilinetext7 = [None] * 1 
            multilinetext7[0] = ""
            objectWorkInstructionBuilder1.Work.SetRichText(multilinetext7)
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            objectWorkInstructionBuilder1.Work.FontSize = 16
            
            objectWorkInstructionBuilder1.Work.CommitItem()
            
            markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Author Work Instructions")
            
            theSession.DeleteUndoMark(markId3, None)
            
            markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Author Work Instructions")
            
            theSession.DeleteUndoMark(markId4, None)
            
            theSession.SetUndoMarkName(markId2, "Author Work Instructions")
            
            theSession.DeleteUndoMark(markId2, None)
            
            nXObject14 = objectWorkInstructionBuilder1.Commit()
            
            objectWorkInstructionBuilder1.Destroy()
            
            markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
            
            workInstructionOutputBuilder1 = workPart.CAMSetup.CreateWorkInstructionOutputBuilder()
            
            workInstructionOutputBuilder1.PageSize = NXOpen.CAM.WorkInstructionOutputBuilder.PageSizeType.Letter
            
            workInstructionOutputBuilder1.ScaleFactor = 1.0
            
            workInstructionOutputBuilder1.OutputFormat = NXOpen.CAM.WorkInstructionOutputBuilder.OutputFormatType.Pdf
            
            workInstructionOutputBuilder1.OutputFile = str(pdfdirectory2 + str(ix + 1) +"- "+ str(op_data_list_programs[ix]) + " - Tool Path Display Sheet.pdf")
            
            theSession.SetUndoMarkName(markId5, "Publish Work Instructions Dialog")
            with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
                lines = [line.rstrip() for line in file]
                if 'USER CANCELLED' in lines:
                    file.close()
                    return
                    sys.exit()
                else:
                    file.close()             
            
            # ----------------------------------------------
            #   Dialog Begin Publish Work Instructions
            # ----------------------------------------------
            markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Publish Work Instructions")
            
            theSession.DeleteUndoMark(markId6, None)
            
            markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Publish Work Instructions")
            
            camera13 = nXObject13
            cameraBuilder14 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera13)
            
            nXObject15 = cameraBuilder14.Commit()
            
            cameraBuilder14.Destroy()
            
            objects2 = [NXOpen.CAM.CAMObject.Null] * 1 
            objects2[0] = planarMilling1
            modelingView1.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
            
            layout1.ReplaceView(modelingView1, modelingView1, False)
            
            modelingView1.Orient(NXOpen.View.Canned.Front, NXOpen.View.ScaleAdjustment.Fit)
            
            modelingView1.Orient(NXOpen.View.Canned.Back, NXOpen.View.ScaleAdjustment.Fit)
            
            workInstructionOutputBuilder1.Publish(objects2, planarMilling1, 0)
            
            camera14 = nXObject15
            camera14.ApplyToView(modelingView1)
            
            theSession.DeleteUndoMark(markId7, None)
            
            theSession.SetUndoMarkName(markId5, "Publish Work Instructions")
            
            workInstructionOutputBuilder1.Destroy()
            with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
                lines = [line.rstrip() for line in file]
                if 'USER CANCELLED' in lines:
                    file.close()
                    return
                    sys.exit()
                else:
                    file.close()             
        
        
        markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Replace View")
    
        layout1 = workPart.Layouts.FindObject("L1")
        modelingView1 = workPart.ModelingViews.FindObject("Isometric")
        layout1.ReplaceView(workPart.ModelingViews.WorkView, modelingView1, True)
        NX_Turn_PMIs_On()
        lw.WriteLine("TOOL PATH DISPLAY SHEETS COMPLETED")
        lw.WriteLine("TURNING ON PMI'S TO CONTINUE PUBLISHING WORK INSTRUCTIONS")
    #######################################################          








    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theUI = NXOpen.UI.GetUI() #type: NXOpen.UI
    theSession.CAMSession.PathDisplay.DisplayToolPath = False
    
    surfaceContour1 = workPart.CAMSetup.CAMOperationCollection.FindObject(Selected_Op)

    objects2 = [NXOpen.CAM.CAMObject.Null] * 1 
    objects2[0] = surfaceContour1
    
    workPart.CAMSetup.DeleteWorkInstructions(objects2)
    theSession.CAMSession.PathDisplay.HideToolPath(surfaceContour1)
    if theUI.SelectionManager.GetSelectedTaggedObject(0) != None:
        theSession.CAMSession.PathDisplay.HideToolPath(theUI.SelectionManager.GetSelectedTaggedObject(0))
    theSession.CAMSession.PathDisplay.SetToolDisplayType(NXOpen.CAM.PathDisplay.ToolDisplayType.Point)
    holeDrilling1 = workPart.CAMSetup.CAMOperationCollection.FindObject(Selected_Op)
    objectWorkInstructionBuilder1 = workPart.CAMSetup.CreateObjectWorkInstructionBuilder(holeDrilling1)




    
    #objectWorkInstructionBuilder1 = workPart.CAMSetup.CreateObjectWorkInstructionBuilder(theUI.SelectionManager.GetSelectedTaggedObject(0))
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Author Work Instructions Dialog")
    
    objectWorkInstructionBuilder1.Work.SheetNumber = 1
    
    sheettitle1 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.SheetTitle =  str("EVTEC Superlight - " + Program_Folder + " - Job Information Sheet")
    
    sheetnum1 = objectWorkInstructionBuilder1.Work.AddSheet()
    
    sheettitle2 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.TemplateName = "Job Information Sheet [Trial 1]"
    
    objectWorkInstructionBuilder1.Work.CommitMaster()
    
    itemnames1 = [None] * 11 
    itemnames1[0] = "OWI_TEXT_1"
    itemnames1[1] = "OWI_TEXT_4"
    itemnames1[2] = "OWI_TEXT_5"
    itemnames1[3] = "OWI_TEXT_6"
    itemnames1[4] = "OWI_TEXT_3"
    itemnames1[5] = "OWI_TEXT_2"
    itemnames1[6] = "OWI_PROD_VIEW_1"
    itemnames1[7] = "OWI_TEXT_7"
    itemnames1[8] = "OWI_TEXT_8"
    itemnames1[9] = "OWI_TEXT_9"
    itemnames1[10] = "OWI_TEXT_10"
    objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames1)
    
    layout1 = workPart.Layouts.FindObject("L1")
    camera1 = workPart.Cameras.FindObject("NXOWI_CACHE_CURRENT_VIEW")
    cameraBuilder1 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera1)
    
    nXObject1 = cameraBuilder1.Commit()
    
    cameraBuilder1.Destroy()
    
    
    #### ADD NOTES PAGE IF REQURIED
    
    if notesreq == "YES":
        objectWorkInstructionBuilder1.Work.SheetNumber = 2
        
        sheettitle1 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        objectWorkInstructionBuilder1.Work.SheetTitle = "EVTEC Superlight - " + Program_Folder + " - Job Notes"
        
        sheetnum1 = objectWorkInstructionBuilder1.Work.AddSheet()
        
        sheettitle2 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        objectWorkInstructionBuilder1.Work.TemplateName = "Job Notes [Evtec]"
        
        objectWorkInstructionBuilder1.Work.CommitMaster()
        
        itemnames1 = [None] * 23 
        itemnames1[0] = "OWI_PROD_VIEW_2"
        itemnames1[1] = "OWI_TEXT_1"
        itemnames1[2] = "OWI_TEXT_2"
        itemnames1[3] = "OWI_TEXT_3"
        itemnames1[4] = "OWI_TEXT_13"
        itemnames1[5] = "OWI_TEXT_4"
        itemnames1[6] = "OWI_TEXT_14"
        itemnames1[7] = "OWI_TEXT_5"
        itemnames1[8] = "OWI_TEXT_15"
        itemnames1[9] = "OWI_TEXT_6"
        itemnames1[10] = "OWI_TEXT_16"
        itemnames1[11] = "OWI_TEXT_7"
        itemnames1[12] = "OWI_TEXT_17"
        itemnames1[13] = "OWI_TEXT_8"
        itemnames1[14] = "OWI_TEXT_18"
        itemnames1[15] = "OWI_TEXT_9"
        itemnames1[16] = "OWI_TEXT_19"
        itemnames1[17] = "OWI_TEXT_10"
        itemnames1[18] = "OWI_TEXT_20"
        itemnames1[19] = "OWI_TEXT_11"
        itemnames1[20] = "OWI_TEXT_21"
        itemnames1[21] = "OWI_TEXT_12"
        itemnames1[22] = "OWI_TEXT_22"
        objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames1)
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_2"
        
        layout1 = workPart.Layouts.FindObject("L1")
        camera1 = workPart.Cameras.FindObject("NXOWI_CACHE_CURRENT_VIEW")
        cameraBuilder1 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera1)
        
        nXObject1 = cameraBuilder1.Commit()
        
        cameraBuilder1.Destroy()
        
        sheettitle3 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        objectWorkInstructionBuilder1.Work.CameraName = "Isometric"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_1"
        
        multilinetext1 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext1)
        
        sheettitle4 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext2 = [None] * 1 
        multilinetext2[0] = JN_PartName
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext2)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext3 = [None] * 1 
        multilinetext3[0] = JN_PartName
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext3)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_2"
        
        multilinetext4 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext4)
        
        sheettitle5 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext5 = [None] * 1 
        multilinetext5[0] = Rev_No
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext5)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext6 = [None] * 1 
        multilinetext6[0] = Rev_No
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext6)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_3"
        
        multilinetext7 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext7)
        
        sheettitle6 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext8 = [None] * 1 
        multilinetext8[0] = JN_Note_1
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext8)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext9 = [None] * 1 
        multilinetext9[0] = JN_Note_1
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext9)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_13"
        
        multilinetext10 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext10)
        
        sheettitle7 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext11 = [None] * 1 
        multilinetext11[0] = JN_Note_1_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext11)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext12 = [None] * 1 
        multilinetext12[0] = JN_Note_1_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext12)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_4"
        
        multilinetext13 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext13)
        
        sheettitle8 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext14 = [None] * 1 
        multilinetext14[0] = JN_Note_2
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext14)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext15 = [None] * 1 
        multilinetext15[0] = JN_Note_2
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext15)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_14"
        
        multilinetext16 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext16)
        
        sheettitle9 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext17 = [None] * 1 
        multilinetext17[0] = JN_Note_2_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext17)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Cambria"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext18 = [None] * 1 
        multilinetext18[0] = JN_Note_2_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext18)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_5"
        
        multilinetext19 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext19)
        
        sheettitle10 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext20 = [None] * 1 
        multilinetext20[0] = JN_Note_3
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext20)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext21 = [None] * 1 
        multilinetext21[0] = JN_Note_3
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext21)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_15"
        
        multilinetext22 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext22)
        
        sheettitle11 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext23 = [None] * 1 
        multilinetext23[0] = JN_Note_3_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext23)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext24 = [None] * 1 
        multilinetext24[0] = JN_Note_3_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext24)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_6"
        
        multilinetext25 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext25)
        
        sheettitle12 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext26 = [None] * 1 
        multilinetext26[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext26)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 28
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext27 = [None] * 1 
        multilinetext27[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext27)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_16"
        
        multilinetext28 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext28)
        
        sheettitle13 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext29 = [None] * 1 
        multilinetext29[0] = JN_Note_4_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext29)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_6"
        
        multilinetext30 = [None] * 1 
        multilinetext30[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext30)
        
        sheettitle14 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext31 = [None] * 1 
        multilinetext31[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext31)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext32 = [None] * 1 
        multilinetext32[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext32)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_15"
        
        multilinetext33 = [None] * 1 
        multilinetext33[0] = JN_Note_3_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext33)
        
        sheettitle15 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext34 = [None] * 1 
        multilinetext34[0] = JN_Note_3_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext34)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_6"
        
        multilinetext35 = [None] * 1 
        multilinetext35[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext35)
        
        sheettitle16 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext36 = [None] * 1 
        multilinetext36[0] = JN_Note_4
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext36)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_16"
        
        multilinetext37 = [None] * 1 
        multilinetext37[0] = JN_Note_4_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext37)
        
        sheettitle17 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext38 = [None] * 1 
        multilinetext38[0] = JN_Note_4_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext38)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_7"
        
        multilinetext39 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext39)
        
        sheettitle18 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext40 = [None] * 1 
        multilinetext40[0] = JN_Note_5
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext40)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 14
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext41 = [None] * 1 
        multilinetext41[0] = JN_Note_5
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext41)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_17"
        
        multilinetext42 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext42)
        
        sheettitle19 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext43 = [None] * 1 
        multilinetext43[0] = JN_Note_5_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext43)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()

        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext44 = [None] * 1 
        multilinetext44[0] = JN_Note_5_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext44)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_8"
        
        multilinetext45 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext45)
        
        sheettitle20 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext46 = [None] * 1 
        multilinetext46[0] = JN_Note_6
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext46)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext47 = [None] * 1 
        multilinetext47[0] = JN_Note_6
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext47)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_18"
        
        multilinetext48 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext48)
        
        sheettitle21 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext49 = [None] * 1 
        multilinetext49[0] = JN_Note_6_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext49)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext50 = [None] * 1 
        multilinetext50[0] = JN_Note_6_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext50)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_9"
        
        multilinetext51 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext51)
        
        sheettitle22 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext52 = [None] * 1 
        multilinetext52[0] = JN_Note_7
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext52)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext53 = [None] * 1 
        multilinetext53[0] = JN_Note_7
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext53)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_19"
        
        multilinetext54 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext54)
        
        sheettitle23 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext55 = [None] * 1 
        multilinetext55[0] = JN_Note_7_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext55)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext56 = [None] * 1 
        multilinetext56[0] = JN_Note_7_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext56)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_10"
        
        multilinetext57 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext57)
        
        sheettitle24 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext58 = [None] * 1 
        multilinetext58[0] = JN_Note_8
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext58)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext59 = [None] * 1 
        multilinetext59[0] = JN_Note_8
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext59)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_20"
        
        multilinetext60 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext60)
        
        sheettitle25 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext61 = [None] * 1 
        multilinetext61[0] = JN_Note_8_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext61)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext62 = [None] * 1 
        multilinetext62[0] = JN_Note_8_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext62)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_11"
        
        multilinetext63 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext63)
        
        sheettitle26 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext64 = [None] * 1 
        multilinetext64[0] = JN_Note_9
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext64)
        
        objectWorkInstructionBuilder1.Work.CommitItem()

        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext65 = [None] * 1 
        multilinetext65[0] = JN_Note_9
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext65)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_21"
        
        multilinetext66 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext66)
        
        sheettitle27 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext67 = [None] * 1 
        multilinetext67[0] = JN_Note_9_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext67)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext68 = [None] * 1 
        multilinetext68[0] = JN_Note_9_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext68)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_12"
        
        multilinetext69 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext69)
        
        sheettitle28 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext70 = [None] * 1 
        multilinetext70[0] = JN_Note_10
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext70)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 16
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext71 = [None] * 1 
        multilinetext71[0] = JN_Note_10
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext71)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_22"
        
        multilinetext72 = []
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext72)
        
        sheettitle29 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        multilinetext73 = [None] * 1 
        multilinetext73[0] = JN_Note_10_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext73)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        

        
        objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.FontSize = 30
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        multilinetext74 = [None] * 1 
        multilinetext74[0] = JN_Note_10_Ref
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext74)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.SheetNumber = 2
        
        itemnames2 = [None] * 23 
        itemnames2[0] = "OWI_PROD_VIEW_2"
        itemnames2[1] = "OWI_TEXT_1"
        itemnames2[2] = "OWI_TEXT_2"
        itemnames2[3] = "OWI_TEXT_3"
        itemnames2[4] = "OWI_TEXT_13"
        itemnames2[5] = "OWI_TEXT_4"
        itemnames2[6] = "OWI_TEXT_14"
        itemnames2[7] = "OWI_TEXT_5"
        itemnames2[8] = "OWI_TEXT_15"
        itemnames2[9] = "OWI_TEXT_6"
        itemnames2[10] = "OWI_TEXT_16"
        itemnames2[11] = "OWI_TEXT_7"
        itemnames2[12] = "OWI_TEXT_17"
        itemnames2[13] = "OWI_TEXT_8"
        itemnames2[14] = "OWI_TEXT_18"
        itemnames2[15] = "OWI_TEXT_9"
        itemnames2[16] = "OWI_TEXT_19"
        itemnames2[17] = "OWI_TEXT_10"
        itemnames2[18] = "OWI_TEXT_20"
        itemnames2[19] = "OWI_TEXT_11"
        itemnames2[20] = "OWI_TEXT_21"
        itemnames2[21] = "OWI_TEXT_12"
        itemnames2[22] = "OWI_TEXT_22"
        objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames2)
        
        sheettitle30 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        objectWorkInstructionBuilder1.Work.SheetTitle = sheettitle2
        
        objectWorkInstructionBuilder1.Work.SheetTitle = "EVTEC Superlight - " + Program_Folder + " - Job Notes"

        objectWorkInstructionBuilder1.Work.CommitMaster()
        
        multilinetext75 = [None] * 1 
        multilinetext75[0] = "A43"
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext75)
        
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_2"
        
        multilinetext76 = [None] * 1 
        multilinetext76[0] = "rev"
        objectWorkInstructionBuilder1.Work.SetRichText(multilinetext76)
        
        sheettitle31 = objectWorkInstructionBuilder1.Work.SheetTitle
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    sheetnum2 = objectWorkInstructionBuilder1.Work.AddSheet()
    
    sheettitle3 = objectWorkInstructionBuilder1.Work.SheetTitle
    if notesreq == "YES":
        x = 3
    else:
        x = 2
    objectWorkInstructionBuilder1.Work.SheetNumber = x
    
    sheettitle4 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.SheetTitle = str("EVTEC Superlight - " + Program_Folder + " - Tool List")
    
    objectWorkInstructionBuilder1.Work.TemplateName = "Tool Sheet [Trial 1]"
    
    objectWorkInstructionBuilder1.Work.CommitMaster()
    
    itemnames2 = [None] * 2 
    itemnames2[0] = "OWI_PROD_VIEW_2"
    itemnames2[1] = "OWI_TOOL_LIST_1"
    objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames2)
    
    camera2 = nXObject1
    cameraBuilder2 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera2)
    
    nXObject2 = cameraBuilder2.Commit()
    
    cameraBuilder2.Destroy()
    
    sheetnum3 = objectWorkInstructionBuilder1.Work.AddSheet()
    
    sheettitle5 = objectWorkInstructionBuilder1.Work.SheetTitle
    if notesreq =="YES":
        x = 4
    else:
        x = 3
    objectWorkInstructionBuilder1.Work.SheetNumber = x
    
    sheettitle6 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.SheetTitle = str("EVTEC Superlight - " + Program_Folder + "- Job Views")
    
    objectWorkInstructionBuilder1.Work.TemplateName = "Job View [Trial 1]"
    
    objectWorkInstructionBuilder1.Work.CommitMaster()
    
    itemnames3 = [None] * 5 
    itemnames3[0] = "OWI_PROD_VIEW_5"
    itemnames3[1] = "OWI_PROD_VIEW_1"
    itemnames3[2] = "OWI_PROD_VIEW_2"
    itemnames3[3] = "OWI_PROD_VIEW_3"
    itemnames3[4] = "OWI_IMAGE_1"
    objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames3)
    
    camera3 = nXObject2
    cameraBuilder3 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera3)
    
    nXObject3 = cameraBuilder3.Commit()
    
    cameraBuilder3.Destroy()
    
    
    
    
    
    
    
    # Add Path Summary Sheets Loop
    no_of_programs = len(op_data_list2)
    
    for i in range(len(op_data_list2)):
        sheetnum4 = objectWorkInstructionBuilder1.Work.AddSheet()
    
        sheettitle7 = objectWorkInstructionBuilder1.Work.SheetTitle
        if notesreq == "YES":
            x = 5
        else:
            x = 4
        objectWorkInstructionBuilder1.Work.SheetNumber = x + i
    
        sheettitle8 = objectWorkInstructionBuilder1.Work.SheetTitle
    
        objectWorkInstructionBuilder1.Work.SheetTitle = str("EVTEC Superlight - " + Program_Folder + " - Tool Path Summary - " + str(op_data_list2[i]))
    
        objectWorkInstructionBuilder1.Work.TemplateName = "Tool Path Summary [Trial 1]"
    
        objectWorkInstructionBuilder1.Work.CommitMaster()
    
        itemnames4 = [None] * 2 
        itemnames4[0] = "OWI_PROD_VIEW_2"
        itemnames4[1] = "OWI_OPER_LIST_1"
        objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames4)
        
        camera4 = nXObject3
        cameraBuilder4 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera4) 
        nXObject4 = cameraBuilder4.Commit()
    
        cameraBuilder4.Destroy()
        
        with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
            lines = [line.rstrip() for line in file]
            if 'USER CANCELLED' in lines:
                file.close()
                return
                sys.exit()
            else:
                file.close() 
    
    
    #### Add Path Summary Sheets Loop End
    
    
    
    ### EDIT SHEET ONE - JOB INFORMATION SHEET
    objectWorkInstructionBuilder1.Work.SheetNumber = 1
    
    itemnames5 = [None] * 11 
    itemnames5[0] = "OWI_TEXT_1"
    itemnames5[1] = "OWI_TEXT_4"
    itemnames5[2] = "OWI_TEXT_5"
    itemnames5[3] = "OWI_TEXT_6"
    itemnames5[4] = "OWI_TEXT_3"
    itemnames5[5] = "OWI_TEXT_2"
    itemnames5[6] = "OWI_PROD_VIEW_1"
    itemnames5[7] = "OWI_TEXT_7"
    itemnames5[8] = "OWI_TEXT_8"
    itemnames5[9] = "OWI_TEXT_9"
    itemnames5[10] = "OWI_TEXT_10"
    objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames5)
    
    camera5 = nXObject4
    cameraBuilder5 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera5)
    
    nXObject5 = cameraBuilder5.Commit()
    
    cameraBuilder5.Destroy()
    
    sheettitle9 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.SheetTitle = sheettitle2
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_1"
    
    multilinetext1 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext1)
    
    sheettitle10 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext2 = [None] * 1 
    multilinetext2[0] = Rev_No
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext2)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
   
    objectWorkInstructionBuilder1.Work.FontSize = 16
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_4"
    
    multilinetext3 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext3)
    
    camera6 = nXObject5
    cameraBuilder6 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera6)
    
    nXObject6 = cameraBuilder6.Commit()
    
    cameraBuilder6.Destroy()
    
    sheettitle11 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext4 = [None] * 1 
    multilinetext4[0] = Costumer_Name
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext4)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 16
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_5"
    
    multilinetext5 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext5)
    
    camera7 = nXObject6
    cameraBuilder7 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera7)
    
    nXObject7 = cameraBuilder7.Commit()
    
    cameraBuilder7.Destroy()
    
    sheettitle12 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext6 = [None] * 1 
    multilinetext6[0] = Project_Name
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext6)
    
    objectWorkInstructionBuilder1.Work.CommitItem()

    objectWorkInstructionBuilder1.Work.FontSize = 16
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_6"
    
    multilinetext7 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext7)
    
    camera8 = nXObject7
    cameraBuilder8 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera8)
    
    nXObject8 = cameraBuilder8.Commit()
    
    cameraBuilder8.Destroy()
    
    sheettitle13 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext8 = [None] * 1 
    multilinetext8[0] = Machine_Name
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext8)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 16
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_3"
    
    multilinetext9 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext9)
    
    camera9 = nXObject8
    cameraBuilder9 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera9)
    
    nXObject9 = cameraBuilder9.Commit()
    
    cameraBuilder9.Destroy()
    
    sheettitle14 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext10 = [None] * 1 
    multilinetext10[0] = Program_Folder
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext10)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 18
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    

    textcolor2 = [None] * 3 
    textcolor2[0] = 0.0
    textcolor2[1] = 0.50196078431372548
    textcolor2[2] = 0.070588235294117646
    
    objectWorkInstructionBuilder1.Work.SetTextColor(textcolor2)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_2"
    
    multilinetext11 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext11)
    
    camera10 = nXObject9
    cameraBuilder10 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera10)
    
    nXObject10 = cameraBuilder10.Commit()
    
    cameraBuilder10.Destroy()
    
    sheettitle15 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext12 = [None] * 1 
    multilinetext12[0] = Instructions_Text
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext12)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 12
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_1"
    
    camera11 = nXObject10
    cameraBuilder11 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera11)
    
    nXObject11 = cameraBuilder11.Commit()
    
    cameraBuilder11.Destroy()
    
    camera12 = nXObject11
    cameraBuilder12 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera12)
    
    nXObject12 = cameraBuilder12.Commit()
    
    cameraBuilder12.Destroy()
    
    sheettitle16 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    part1 = theSession.Parts.Display
    
    view1 = workPart.Views.WorkView
    
    modelingView1 = view1
    modelingView1.Fit()
    
    # ----------------------------------------------
    #   Menu: Orient View->Isometric
    # ----------------------------------------------
    modelingView1.Orient(NXOpen.View.Canned.Isometric, NXOpen.View.ScaleAdjustment.Fit)
    
    multilinetext13 = [None] * 1 
    multilinetext13[0] = Instructions_Text
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext13)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    cameraBuilder13 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, NXOpen.Display.Camera.Null)
    
    nXObject13 = cameraBuilder13.Commit()
    
    cameraBuilder13.Destroy()
    
    objectWorkInstructionBuilder1.Work.CaptureCurrentView()
    
    objectWorkInstructionBuilder1.Work.CameraName = "Isometric"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera13 = nXObject12
    cameraBuilder14 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera13)
    
    nXObject14 = cameraBuilder14.Commit()
    
    cameraBuilder14.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_7"
    
    multilinetext14 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext14)
    
    sheettitle17 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext15 = [None] * 1 
    multilinetext15[0] = Datum_Info
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext15)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 12
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_8"
    
    multilinetext16 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext16)
    
    camera14 = nXObject14
    cameraBuilder15 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera14)
    
    nXObject15 = cameraBuilder15.Commit()
    
    cameraBuilder15.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    sheettitle18 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext17 = [None] * 1 
    multilinetext17[0] = WorkHold_Info
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext17)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 12
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_9"
    
    multilinetext18 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext18)
    
    camera15 = nXObject15
    cameraBuilder16 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera15)
    
    nXObject16 = cameraBuilder16.Commit()
    
    cameraBuilder16.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    sheettitle19 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext19 = [None] * 1 
    multilinetext19[0] = AsOpp_Info
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext19)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 12
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TEXT_10"
    
    multilinetext20 = []
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext20)
    
    camera16 = nXObject16
    cameraBuilder17 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera16)
    
    nXObject17 = cameraBuilder17.Commit()
    
    cameraBuilder17.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    sheettitle20 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    multilinetext21 = [None] * 1 
    multilinetext21[0] = Notes_Text
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext21)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontSize = 10
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    objectWorkInstructionBuilder1.Work.FontFace = "Calibri"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    
    
    
    
    ### EDIT TOOL LIST
    if notesreq == "YES":
        x = 3
    else:
        x = 2
    objectWorkInstructionBuilder1.Work.SheetNumber = x
    
    itemnames6 = [None] * 2 
    itemnames6[0] = "OWI_PROD_VIEW_2"
    itemnames6[1] = "OWI_TOOL_LIST_1"
    objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames6)
    
    camera17 = nXObject17
    cameraBuilder18 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera17)
    
    nXObject18 = cameraBuilder18.Commit()
    
    cameraBuilder18.Destroy()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_2"
    
    camera18 = nXObject18
    cameraBuilder19 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera18)
    
    nXObject19 = cameraBuilder19.Commit()
    
    cameraBuilder19.Destroy()
    
    camera19 = nXObject19
    cameraBuilder20 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera19)
    
    nXObject20 = cameraBuilder20.Commit()
    
    cameraBuilder20.Destroy()
    
    sheettitle21 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.SheetTitle = sheettitle5
    
    multilinetext22 = [None] * 1 
    multilinetext22[0] = Notes_Text
    objectWorkInstructionBuilder1.Work.SetRichText(multilinetext22)
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    cameraBuilder21 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, NXOpen.Display.Camera.Null)
    
    nXObject21 = cameraBuilder21.Commit()
    
    cameraBuilder21.Destroy()
    
    objectWorkInstructionBuilder1.Work.CaptureCurrentView()
    
    objectWorkInstructionBuilder1.Work.CameraName = "Isometric"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera20 = nXObject20
    cameraBuilder22 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera20)
    
    nXObject22 = cameraBuilder22.Commit()
    
    cameraBuilder22.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_TOOL_LIST_1"
    
    sheettitle22 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.ToolListProgramGroup = Program_Folder
    
    objectWorkInstructionBuilder1.Work.ToolListProgramGroup = Program_Folder
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera21 = nXObject22
    cameraBuilder23 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera21)
    
    nXObject23 = cameraBuilder23.Commit()
    
    cameraBuilder23.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    #### EDIT JOB VIEWS SHEET
    if notesreq == "YES":
        x = 4
    else:
        x = 3
    objectWorkInstructionBuilder1.Work.SheetNumber = x
    
    itemnames7 = [None] * 5 
    itemnames7[0] = "OWI_PROD_VIEW_5"
    itemnames7[1] = "OWI_PROD_VIEW_1"
    itemnames7[2] = "OWI_PROD_VIEW_2"
    itemnames7[3] = "OWI_PROD_VIEW_3"
    itemnames7[4] = "OWI_PROD_VIEW_4"
    objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames7)
    
    camera22 = nXObject23
    cameraBuilder24 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera22)
    
    nXObject24 = cameraBuilder24.Commit()
    
    cameraBuilder24.Destroy()
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_5"
    
    camera23 = nXObject24
    cameraBuilder25 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera23)
    
    nXObject25 = cameraBuilder25.Commit()
    
    cameraBuilder25.Destroy()
    
    sheettitle23 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.SheetTitle = sheettitle7
    
    cameraBuilder26 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, NXOpen.Display.Camera.Null)
    
    nXObject26 = cameraBuilder26.Commit()
    
    cameraBuilder26.Destroy()
    
    objectWorkInstructionBuilder1.Work.CaptureCurrentView()
    
    objectWorkInstructionBuilder1.Work.CameraName = "Isometric"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera24 = nXObject25
    cameraBuilder27 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera24)
    
    nXObject27 = cameraBuilder27.Commit()
    
    cameraBuilder27.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_1"
    
    camera25 = nXObject27
    cameraBuilder28 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera25)
    
    nXObject28 = cameraBuilder28.Commit()
    
    cameraBuilder28.Destroy()
    
    sheettitle24 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    cameraBuilder29 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, NXOpen.Display.Camera.Null)
    
    nXObject29 = cameraBuilder29.Commit()
    
    cameraBuilder29.Destroy()
    
    objectWorkInstructionBuilder1.Work.CaptureCurrentView()
    
    objectWorkInstructionBuilder1.Work.CameraName = "Isometric"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera26 = nXObject28
    cameraBuilder30 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera26)
    
    nXObject30 = cameraBuilder30.Commit()
    
    cameraBuilder30.Destroy()
    ####
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_4"
    
    camera279 = nXObject30
    cameraBuilder319 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera279)
    
    nXObject319 = cameraBuilder319.Commit()
    
    cameraBuilder319.Destroy()
    
    sheettitle25 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.CameraName = "Right"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera289 = nXObject319
    cameraBuilder329 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera289)
    
    nXObject329 = cameraBuilder329.Commit()
    
    cameraBuilder329.Destroy()

    ####
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_2"
    
    camera27 = nXObject30
    cameraBuilder31 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera27)
    
    nXObject31 = cameraBuilder31.Commit()
    
    cameraBuilder31.Destroy()
    
    sheettitle25 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.CameraName = "Top"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera28 = nXObject31
    cameraBuilder32 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera28)
    
    nXObject32 = cameraBuilder32.Commit()
    
    cameraBuilder32.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    modelingView1.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
    
    objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_3"
    
    camera29 = nXObject32
    cameraBuilder33 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera29)
    
    nXObject33 = cameraBuilder33.Commit()
    
    cameraBuilder33.Destroy()
    
    sheettitle26 = objectWorkInstructionBuilder1.Work.SheetTitle
    
    objectWorkInstructionBuilder1.Work.CameraName = "Front"
    
    objectWorkInstructionBuilder1.Work.CommitItem()
    
    camera30 = nXObject33
    cameraBuilder34 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera30)
    
    nXObject34 = cameraBuilder34.Commit()
    
    cameraBuilder34.Destroy()
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    modelingView1.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
    
    modelingView1.Orient(NXOpen.View.Canned.Front, NXOpen.View.ScaleAdjustment.Fit)
    
    
    #### Edit Path Summary Sheets Loop
    
    for ix in range(len(op_data_list2)):
        ##text_file1.write(str(ix))
        if notesreq == "YES":
            x = 5
        else:
            x = 4
        objectWorkInstructionBuilder1.Work.SheetNumber = x + ix
    
        itemnames8 = [None] * 2 
        itemnames8[0] = "OWI_PROD_VIEW_2"
        itemnames8[1] = "OWI_OPER_LIST_1"
        objectWorkInstructionBuilder1.Work.UpdateItemsInCurrentSheet(itemnames8)
        
        camera31 = nXObject34
        cameraBuilder35 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera31)
    
        nXObject35 = cameraBuilder35.Commit()
    
        cameraBuilder35.Destroy()
    
        sheettitle27 = objectWorkInstructionBuilder1.Work.SheetTitle
    
        objectWorkInstructionBuilder1.Work.SheetTitle = str(Program_Folder + "- Sheet " + str(op_data_list2[ix]))
    
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_PROD_VIEW_2"
    
        camera32 = nXObject35
        cameraBuilder36 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera32)
    
        nXObject36 = cameraBuilder36.Commit()
    
        cameraBuilder36.Destroy()
    
        sheettitle28 = objectWorkInstructionBuilder1.Work.SheetTitle
        
        cameraBuilder37 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, NXOpen.Display.Camera.Null)
    
        nXObject37 = cameraBuilder37.Commit()
    
        cameraBuilder37.Destroy()
    
        objectWorkInstructionBuilder1.Work.CaptureCurrentView()
    
        objectWorkInstructionBuilder1.Work.CameraName = "Isometric"
    
        objectWorkInstructionBuilder1.Work.CommitItem()
        
        camera33 = nXObject36
        cameraBuilder38 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera33)
        
        nXObject38 = cameraBuilder38.Commit()
    
        cameraBuilder38.Destroy()
        
        layout1.ReplaceView(modelingView1, modelingView1, False)
    
        objectWorkInstructionBuilder1.Work.ItemName = "OWI_OPER_LIST_1"
    
        sheettitle29 = objectWorkInstructionBuilder1.Work.SheetTitle
    
        objectWorkInstructionBuilder1.Work.OperListProgramGroup = op_data_list2[ix]
    
        objectWorkInstructionBuilder1.Work.OperListProgramGroup = op_data_list2[ix]
    
        objectWorkInstructionBuilder1.Work.CommitItem()

        camera34 = nXObject38
        cameraBuilder39 = workPart.Cameras.CreateCameraBuilder(modelingView1, layout1, camera34)
    
        nXObject39 = cameraBuilder39.Commit()
        
        cameraBuilder39.Destroy()
        with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
            lines = [line.rstrip() for line in file]
            if 'USER CANCELLED' in lines:
                file.close()
                return
                sys.exit()
            else:
                file.close()         
    ## End Edit Path Summary Loop
    
    layout1.ReplaceView(modelingView1, modelingView1, False)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Author Work Instructions")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Author Work Instructions")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Author Work Instructions")
    
    theSession.DeleteUndoMark(markId1, None)
    
    nXObject40 = objectWorkInstructionBuilder1.Commit()
    
    objectWorkInstructionBuilder1.Destroy()
    
    with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt") as file:
        lines = [line.rstrip() for line in file]
        if 'USER CANCELLED' in lines:
            file.close()
            return
            sys.exit()
        else:
            file.close()   




    
    # PUBLISHHHHH
    
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    holeDrilling1 = workPart.CAMSetup.CAMOperationCollection.FindObject(Selected_Op)

    
    inTaskEnv1 = theSession.IsBatch
    
    theSession.CAMSession.PathDisplay.StepDisplay(True)
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    workInstructionOutputBuilder1 = workPart.CAMSetup.CreateWorkInstructionOutputBuilder()
    
    workInstructionOutputBuilder1.PageSize = NXOpen.CAM.WorkInstructionOutputBuilder.PageSizeType.Letter
    
    workInstructionOutputBuilder1.ScaleFactor = 1.0
    
    workInstructionOutputBuilder1.OutputFormat = NXOpen.CAM.WorkInstructionOutputBuilder.OutputFormatType.Pdf
    
    workInstructionOutputBuilder1.OutputFile = pdfpath
    
    workInstructionOutputBuilder1.OpenFile = True
    
    workInstructionOutputBuilder1.PageSize = NXOpen.CAM.WorkInstructionOutputBuilder.PageSizeType.A4
    
    theSession.SetUndoMarkName(markId1, "Publish Work Instructions Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Publish Work Instructions
    # ----------------------------------------------
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Publish Work Instructions")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Publish Work Instructions")
    
    layout1 = workPart.Layouts.FindObject("L1")
    camera1 = workPart.Cameras.FindObject("NXOWI_CACHE_CURRENT_VIEW")
    cameraBuilder1 = workPart.Cameras.CreateCameraBuilder(workPart.ModelingViews.WorkView, layout1, camera1)
    
    nXObject1 = cameraBuilder1.Commit()
    
    cameraBuilder1.Destroy()
    
    objects1 = [NXOpen.CAM.CAMObject.Null] * 1 
    objects1[0] = holeDrilling1

    layout1.ReplaceView(workPart.ModelingViews.WorkView, workPart.ModelingViews.WorkView, False)
    

    layout1.ReplaceView(workPart.ModelingViews.WorkView, workPart.ModelingViews.WorkView, False)
    

    layout1.ReplaceView(workPart.ModelingViews.WorkView, workPart.ModelingViews.WorkView, False)

    layout1.ReplaceView(workPart.ModelingViews.WorkView, workPart.ModelingViews.WorkView, False)
    
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
    
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Front, NXOpen.View.ScaleAdjustment.Fit)
    
    layout1.ReplaceView(workPart.ModelingViews.WorkView, workPart.ModelingViews.WorkView, False)
    
    workInstructionOutputBuilder1.Publish(objects1, holeDrilling1, 0)
    
    camera2 = nXObject1
    camera2.ApplyToView(workPart.ModelingViews.WorkView)
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Publish Work Instructions")
    
    workInstructionOutputBuilder1.Destroy()
    
    
    theSession.CAMSession.PathDisplay.SetToolDisplayType(NXOpen.CAM.PathDisplay.ToolDisplayType.SolidWithHolder)

    manual_exit.kill()
    f = open("S:\\CAD_Office\\Muhsin\\NXOPEN\\NX_OWI_Automation\\WI_DATA\\WorkInstructionsData-" + username + ".txt", "w")
    f.write("Work Instructions Complete.") 
    f.close()

    
    

if __name__ == '__main__':
    main()