import bpy

print(bpy.data.collections[0].objects)

Mcol =  bpy.data.collections

for col in Mcol:
    
    Mname = str(col.name) # le nom de ma collection

    # ajoute des objets empty si il n'existent pas ----------------------------
    newObj =  bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
    bpy.context.object.name = col.name

    
    
    
    ColObj = bpy.data.collections[Mname].objects

    for obj in ColObj:

        #-------------------------------- Parente les objets au null des collections
        print(obj)
        print()  

        Mname2 = str(obj.name)
        
        a = bpy.data.objects[Mname2]
        b = bpy.data.objects[Mname]
        #-------------------------------- Methode crade
   

        bpy.ops.object.select_all(action='DESELECT') #deselect all object

        a.select_set( state = True, view_layer = None)
        b.select_set( state = True, view_layer = None) 

        #bpy.context.scene.objects.active = a    #the active object will be the parent of all selected object

        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        #bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

    
   
    
    
 
    #bpy.context.active_object.name = 'test'
    
#bpy.data.object    

    
print(bpy.data.collections["Collection"] )