import bpy

AllMaterials = bpy.data.materials   # je choppe les materieux
AllMat = [ (mat.name, mat.name, mat.name) for mat in AllMaterials ] # je les mets dans un Enum
MatToReplace = AllMat   # Pour remplacer celui-ci
MatReplace = AllMat     # Par Celui ci 

# C'est ici que j'affiche mes variables dynamiques.
#---------------------------------------------------------------------------------------------------
# CLASS backfacemat 
#       Remplace les materials
#---------------------------------------------------------------------------------------------------

for mat in MatReplace:
    print (mat[0])


'''
class MaterialUtilitiesPropertyGroup( bpy.types.PropertyGroup ):

    MaterialToReplace = bpy.props.EnumProperty( items= MatToReplace )
    MaterialReplace = bpy.props.EnumProperty( items= MatReplace )

    BackfaceBool = bpy.props.BoolProperty( 
        name = "BackfaceBool",
        description = " Backface all materials",
        default = False
    )
   
def MATERIAL_REPLACE(mtr, mr):

    objects = bpy.context.scene.objects
    
    for obj in objects:
        if obj.type == "MESH":
            i = -1
            for mat in obj.data.materials: 
                i = i + 1
                if mat.name == str(mtr):
                    obj.data.materials[i] = bpy.data.materials[str(mr)]
                    
'''
#---------------------------------------------------------------------------------------------------
# CLASS backfacemat 
#       Active/desactive les backfaces sur tout les materials
#---------------------------------------------------------------------------------------------------
'''
class SimpleOperator(bpy.types.Operator):
 
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Remplace material"

    def execute(self, context):
        
        props = context.scene.MaterialUtilitiesPropertyGroup  
        MATERIAL_REPLACE( props.MaterialToReplace, props.MaterialReplace )
        return {'FINISHED'}

'''
