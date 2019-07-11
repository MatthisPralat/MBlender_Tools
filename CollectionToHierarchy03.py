# 1

# Loop dans les collections

# Creer un Null si la collection n'existe pas

#   Loop dans les Child Collections --------------------
#   Trouver les childs de collections
#   Creer un Null si le Null n'existe pas
#   Parenter le Null du child Collection au Null Parent Collection
#   
#   Loop pour trouver les objects de la collection actuelle
#   Parenter les objects de la collections actuelle au null qui correspont a la Collections --------------------


import bpy

for col in bpy.data.collections:
    
    colName = str(col.name)
    
    
    if bpy.data.objects.get(colName) is None:
        newObj = bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
        bpy.context.object.name = col.name
    
    myParent = bpy.data.objects[colName]
    #myChildren = myParent; #initialisation de la variable

    print(col)

    for colChild in col.children:
        
        colChildName = str(colChild.name)

        if bpy.data.objects.get(colChildName) is None:
            newObj = bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
            bpy.context.object.name = colChildName
    
    myChildren = bpy.data.objects[colChildName]
    myChildren.parent = myParent
    myChildren.matrix_parent_inverse = myChildren.matrix_world.inverted() 
        
'''
    for obj in col.objects:
        objName = str(obj.name)

        if len(obj.children) > 0 :
            bpy.ops.object.select_all(action='DESELECT')
            
            bpy.data.objects["Cube.001"].select_set(True)
            bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')

            myChildren = bpy.context.selected_objects
            print(myChildren)

        myChildren.parent = myParent
        myChildren.matrix_parent_inverse = myChildren.matrix_world.inverted() 
        print(obj)
'''