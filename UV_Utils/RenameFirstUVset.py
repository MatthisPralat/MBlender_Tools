import bpy

NewUVName = "UVMap"

for ob in bpy.data.objects:

    if ob.type == "MESH" :
        arr = 0      
        for uv in ob.data.uv_layers:
            arr = arr + 1    
            if arr > 0 :
                print (uv.name)
                uv.name = NewUVName

