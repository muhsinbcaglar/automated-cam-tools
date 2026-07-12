# NX 2312
# Journal created by muhsin.caglar on Thu Mar  6 22:20:04 2025 GMT Standard Time
#
import math
import NXOpen
import NXOpen.CAM
import csv




def main() : 
    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    start_point = workPart.CAMSetup.CAMOperationCollection.FindObject("NC_PROGRAM")
    objects_at_start = NXOpen.CAM.NCGroup.GetMembers(start_point)   
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
                
    csv_file_path = "S:\\CAD_Office\\Muhsin\\NXOPEN\\OPnPROGNameMassEdit\\OperationData_Extracted.csv"

# Write the operation list to CSV
   
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Operation name", "Program Name"])
        writer.writeheader()
        writer.writerows(op_data_list)  # Writing the operation data

         

if __name__ == '__main__':
    main()