import bpy

#bpy.ops.wm.console_toggle(True, False) Ouvre la console, mais foire sur cette version
#Clean -----------------------------------------------------------------------

#1 Creer Un objet par collection
for col in bpy.data.collections:
    colName = str(col.name)  
    if bpy.data.objects.get(colName) is None:
        newObj = bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
        bpy.context.object.name = col.name

#2 De-parente tout les "Collections" Objets
for col in bpy.data.collections:
    colName = str(col.name)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[colName].select_set(True)
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

#3 Virre tout les objets des "Collections" Objets  de leur parentés
for col in bpy.data.collections:
    colName = str(col.name)
    for child in bpy.data.objects[colName].children:
        childName = str(child.name)
        print(childName)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[childName].select_set(True)
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

#La cuisine -----------------------------------------------------------------------

#4 Parrentes les "Collections" Objets  entre eux

for col in bpy.data.collections:
    colName = str(col.name)
    # Ici je choppe les objets
    for ObjChild in col.children:

        ObjChildChildName = str(ObjChild.name)
        
        myParent = bpy.data.objects[colName]
        myChildren = bpy.data.objects[ObjChildChildName]
        
        myChildren.parent = myParent
        myChildren.matrix_parent_inverse = myParent.matrix_world.inverted() 

#4 je parente mon objet si il n'as pas

for col in bpy.data.collections:
    colName = str(col.name)
    bpy.ops.object.select_all(action='DESELECT')
 
    for ObjChild in col.objects:
        ObjChildName = str(ObjChild.name)
        print(ObjChild.name)

        if bpy.data.collections.get(ObjChildName) is None:
            bpy.ops.object.select_all(action='DESELECT')
            print("found object")
            if bpy.data.objects[ObjChildName].parent is None:
                bpy.ops.object.select_all(action='DESELECT')    
                print('HELLO')
                colName = str(col.name)
                myParent = bpy.data.objects[colName]
                myChildren = bpy.data.objects[ObjChildName]
                myChildren.parent = myParent
                myChildren.matrix_parent_inverse = myParent.matrix_world.inverted() 