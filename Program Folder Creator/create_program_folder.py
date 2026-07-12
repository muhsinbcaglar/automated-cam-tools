# NX 2312
# Journal created by muhsin.caglar on Thu Mar  6 21:28:59 2025 GMT Standard Time
#
import math
import NXOpen
import NXOpen.CAM
import csv
def main() : 
    

    with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\ProgramFolderCreator\\ProgramFolderCreator.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
    
        # Get the header (first row) to find the column index
        header = next(reader)
        column_index = header.index("ProgramFolderName")  # Change to your column name
    
        # Iterate through the rows and print each value in the column
        for row in reader:
            try:
                theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
                workPart = theSession.Parts.Work
                displayPart = theSession.Parts.Display
                markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Program")
                
                nCGroup1 = workPart.CAMSetup.CAMGroupCollection.FindObject("NONE")
                nCGroup2 = workPart.CAMSetup.CAMGroupCollection.CreateProgram(nCGroup1, "mill_planar", "PROGRAM", NXOpen.CAM.NCGroupCollection.UseDefaultName.FalseValue, row[column_index])
                
                markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
                
                programOrderGroupBuilder1 = workPart.CAMSetup.CAMGroupCollection.CreateProgramOrderGroupBuilder(nCGroup2)
                
                theSession.SetUndoMarkName(markId2, "Program Dialog")
                
                taggedObject1 = programOrderGroupBuilder1.StartUdeSet.UdeList.FindItem(0)
                
                # ----------------------------------------------
                #   Dialog Begin Program
                # ----------------------------------------------
                markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Program")
                
                theSession.DeleteUndoMark(markId3, None)
                
                markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Program")
                
                nXObject1 = programOrderGroupBuilder1.Commit()
                
                theSession.DeleteUndoMark(markId4, None)
                
                theSession.SetUndoMarkName(markId2, "Program")
                
                programOrderGroupBuilder1.Destroy()
                
                theSession.DeleteUndoMark(markId2, None)
                
                theSession.CAMSession.Utils.SetInspectionIntent(False)
                
                theSession.CleanUpFacetedFacesAndEdges()
                
                # ----------------------------------------------
                #   Menu: Tools->Automation->Journal->Stop Recording
                # ----------------------------------------------
            except Exception as e: 
                continue  # Skip to the next row if an error occurs
if __name__ == '__main__':
    main()