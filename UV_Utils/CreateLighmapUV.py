import bpy

for ob in bpy.data.objects: 
    
    if ob.type == "MESH" :    
        obName = str(ob.name)
        myarr ={}
                
        if "LightmapUV" in ob.data.uv_layers:
            print("il existe")
        else : 
            #Set active
            bpy.context.view_layer.objects.active = bpy.data.objects[obName]
            #bpy.ops.mesh.uv_texture_add()
            bpy.context.object.data.uv_layers[1].active = True
            bpy.context.object.data.uv_layers[1].name = "LightmapUV"
            print("Il faut en creer un")
