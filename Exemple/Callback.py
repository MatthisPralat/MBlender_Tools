import bpy

def my_handler(scene):
    print(len(bpy.data.materials))

bpy.app.handlers.depsgraph_update_pre.append(my_handler)

