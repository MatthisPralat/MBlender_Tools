# select by mat
import bpy

bpy.ops.object.mode_set(mode='OBJECT')

obj = bpy.data.objects
matselect = "Glass"
selobj=[]

print(obj)

for i in obj:
    print(i.material_slots)
    
    for m in i.material_slots:
        print(m.name)
        if m.name == matselect:
            print("ajoute ce mesh")
            selobj.append(i)
            

print(selobj)

for tosel in selobj:
    tosel.select_set(True)
    bpy.context.view_layer.objects.active = tosel
    #print( str(tosel) )
    #bpy.context.scene.objects.active = tosel
    #tosel.select = True

bpy.ops.object.mode_set(mode='EDIT')

for msh in bpy.context.objects_in_mode:
    print(msh)

#for 