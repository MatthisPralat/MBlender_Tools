import bpy

# Enum property.
# Note: the getter/setter callback must use integer identifiers!
test_items = [
    ("Exemple01", "Red", "", 1),
    ("Exemple02", "Green", "", 2),
    ("Exemple03", "Blue", "", 3),
    ("Exemple04", "Yellow", "", 4),
    ]
    
# C'est ici que j'affiche mes variables dynamiques.
class MyToolPropertyGroup( bpy.types.PropertyGroup ): #PropertyGroup pour faire ça
 
    MyEnum = bpy.props.EnumProperty( items= test_items )
    
    MyInt = bpy.props.IntProperty(  
        name= "MyInt",
        description= " Exemple of int button",
        default=1,
        min=1,
        )
    
    MyFloat =  bpy.props.FloatProperty(
        name = "MyFloat",
        description = " Exemple of float button ",
        default = 1.0
    )

    MyFloatVector = bpy.props.FloatVectorProperty(
        name = "MyFloatVector",
        description = "Exemple of float Vector" ,
        default = (1.0 , 1.0 , 1.0)
    )

    MyBool = bpy.props.BoolProperty( 
        name = "MyBool",
        description = " Exemple of Bool button ",
        default = False
    )

    MyString = bpy.props.StringProperty(
        name = "MyString",
        description = " Exemple of string button ",
        default = "Exemple String",
    )
   
   

def DO_SOMETHING(arg1, arg2):
    print("%i * %f = %f" % (arg1, arg2, (arg1*arg2)))


class MyOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.my_operator"
    bl_label = "exemple Object Operator"

    def execute(self, context):
        props = context.scene.MyPropertyGroup
        my_val = 2
        DO_SOMETHING(props.MyInt, MyFloat)
        return {'FINISHED'}


class MyPanel(bpy.types.Panel):

    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_label = "mypanel"
    bl_idname = "OBJECT_PT_MyPanel"

    def draw(self, context):
        
        layout = self.layout
        obj = context.object
        props = context.scene.MyPropertyGroup
       
        row = layout.row()
        
        layout.label(text="SimpleEnumExemple")
        row = layout.row()
        row.prop(props, "MyEnum")
       
        #layout.label(text="MyInt")
        row = layout.row()
        row.prop(props, "MyInt")
        
        #layout.label(text="MyFloat")
        row = layout.row()
        row.prop(props, "MyFloat")

        #layout.label(text="MyFloat")
        row = layout.row()
        row.prop(props, "MyFloatVector")

        #layout.label(text="MyBool")
        row = layout.row()
        row.prop(props, "MyBool")
        
        #layout.label(text="MyString!", icon='WORLD_DATA') # juste pour l'exemple qu'on peut ajouter un icone
        row = layout.row()
        row.prop(props, "MyString")
           
        row = layout.row()
        row.operator('object.my_operator')


classes = [ 
    MyOperator, 
    MyPanel, 
    MyToolPropertyGroup, 
    ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.MyPropertyGroup = bpy.props.PointerProperty(
            type=MyToolPropertyGroup)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.MyPropertyGroup

if __name__ == "__main__":
    register()