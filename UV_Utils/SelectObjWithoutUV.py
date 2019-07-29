import bpy 
    
bpy.ops.object.select_all(action='DESELECT')

for ob in bpy.data.objects:

        obName = str(ob.name)
        if ob.type == "MESH" :    
        # selectionne les mesh sans uvs
                if str(ob.data.uv_layers) == "<bpy_collection[0], UVLoopLayers>" :
                        bpy.data.objects[obName].select_set(True)
                        print(ob.name)
                
        #for uv in ob.data.uv_layers: