import bpy
#1-------------------------------------------------
#
#    Je créé un nouvel objet avec une nouvelle collection
#       Ce qui va me permette de foutre toute ma hierarchie dedans
#-------------------------------------------------
'''
newObj =  bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
bpy.context.object.name = "NewHierarchy"

bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name="NewHierarchy")

'''
#2-------------------------------------------------
#
# Je vais loop dans toutes mes collections pour creer des nulls avec les meme noms
#     
#-------------------------------------------------


print("---------------------------------------------------")
print("-------------------Start---------------------------")
print("---------------------------------------------------")
print( bpy.data.collections[2].objects )


# retourne toutes les collections//////////////////////////
for col in bpy.data.collections: 
        
    colName = str(col.name) # le nom de ma collection

    # c b = bpy.data.objects[Mname]reer un objet si il n'existe pas déjà---------------
    if bpy.data.objects.get(col.name) is not None:
        print("found object")
    else: 
        print("ça n'existe pas")
        newObj =  bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
        bpy.context.object.name = col.name

    # Retourne toutes les parentés de collections////////////// 
    for colChild in bpy.data.collections[colName].children :
	
        colChildName = str(colChild.name)
        
        if bpy.data.objects.get(colChild.name) is not None:
            print("found object")
        else: 
            print("ça n'existe pas")
            newObj =  bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
            bpy.context.object.name = colChild.name
       
        #Selection de mon objet """Enfant"""
        #la je deselectionne
        bpy.ops.object.select_all(action='DESELECT')
        
        a = bpy.data.objects[colName]
        b = bpy.data.objects[colChildName]
        b.parent = a

#--------------------------------------------------------------------------
# PARTIE 2 : Pour les objets
#--------------------------------------------------------------------------
for col in bpy.data.collections:
    colName2 = str(col.name)
    for obj in col.objects: 
        objName2 = str(obj.name)	
        print (obj.name)
        bpy.ops.object.select_all(action='DESELECT')
        e = bpy.data.objects[colName2]
        f = bpy.data.objects[objName2]
        f.parent = e.matrix_parent_inverse