import bpy
'''
Select all Fcurves and delete all keys by parameters
    In this exemple:
        Delete all Location types animations. Preserve Scale and 
'''

# ---  Var
Actions = bpy.data.actions
ParamToDelete = "Location" # change by  "Scale" or "Rotation"

# ---- Functions

def ListActions(Act):
    '''List all actions and send it to curve'''
    for i in Act:
        ListFcurve(i)

def ListFcurve(Curves):
    '''List all curves in action'''
    for i in Curves.fcurves:
        print(i.data_path.endswith)
        if i.data_path.endswith(ParamToDelete) == True:
            Curves.fcurves.remove(i)

ListActions(Actions)