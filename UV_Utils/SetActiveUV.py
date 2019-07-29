import bpy

for ob in bpy.data.objects: 
    
    if ob.type == "MESH" :    
        obName = str(ob.name)
        myarr ={}
                
        if "LightmapUV" in ob.data.uv_layers:
            print("il existe")
            bpy.context.object.data.uv_layers["LightmapUV"].active = True
