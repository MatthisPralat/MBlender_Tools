
import bpy

Arr = {}

for ob in bpy.data.objects:
#    print("hello")

    if ob.type == "MESH" :
        print(ob.data.uv_layers)

        arr = 0    
         
        for uv in ob.data.uv_layers:
            arr = arr + 1    
            if arr > 0 :
                #print(uv.name)
                print (ob.name)
                if uv.name != "UVSet0":
                    print(uv.name)
                    UvName = str(uv.name)
                    meshName = str(ob.name)

                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.data.objects[meshName].select_set(True)
                    bpy.context.view_layer.objects.active = bpy.data.objects[meshName]
                    bpy.context.object.data.uv_layers[UvName].active_render = True
                    bpy.ops.mesh.uv_texture_remove()

 
#                bpy.ops.object.select_all(action='DESELECT')
#                meshName = str(ob.name)
#                bpy.data.objects[meshName].select_set(True)
#                bpy.context.object.data.active_index[arr] = True
#                print( bpy.context.object.data.active_index )

          


#           print(uv.activ_index)
#            if uv.name == "Orco":
#                uv.name = "UVSet0"
#                
#            if uv.name == "UvSet0":
#                uv.name = "UVSet0"
#                
#            if uv.name == "UVMap.001'":
#                uv.name = "UVSet0"
#                
#            if uv.name == "UVMap":
#                uv.name = "UVSet0"
#                
#            if uv.name == "UVMap.002":
#                uv.name = "UVSet0"
#                
#            if uv.name == "UVMap.001":
#                uv.name = "UVSet0"
#                
#            Arr.update({uv.name:"uv"})
#            print(uv)

print(Arr)


