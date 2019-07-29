import bpy


class MonPanel(bpy.types.Panel):
    # creer un pannel dans la view 3D 
    bl_label = "Pannel dans la vue 3D"
    bl_idname = "PANNEL_PT_VIEW3D"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Ma Categorie <3 "

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        row = layout.row()
        row.operator("mesh.primitive_monkey_add")
        #row.prop(props, "MyString")
        

class MyOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.my_operator"
    bl_label = "exemple Object Operator"

    def execute(self, context):

        props = context.scene.MyPropertyGroup
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(props.MyFloat, props.MyFloat, 0))
        DO_SOMETHING(props.MyInt, props.MyFloat)
        return {'FINISHED'}


classes = [ 
    MyOperator, 
    MonPanel
    ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
