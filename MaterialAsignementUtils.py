import bpy

# je choppe les materieux
AllMaterials = bpy.data.materials
# je les mets dans un Enum
AllMat = [(mat.name, mat.name, mat.name) for mat in AllMaterials]
# Pour remplacer celui-ci
MatToReplace = AllMat
# Par Celui ci
MatReplace = AllMat

# C'est ici que j'affiche mes variables dynamiques.
# -----------------------------------------------------------------------------
# CLASS backfacemat
#       Remplace les materials
# -----------------------------------------------------------------------------


class MaterialUtilitiesPropertyGroup(bpy.types.PropertyGroup):
    MaterialToReplace = bpy.props.EnumProperty(items=MatToReplace)
    MaterialReplace = bpy.props.EnumProperty(items=MatReplace)
    BackfaceBool = bpy.props.BoolProperty(
        name="BackfaceBool",
        description="Backface all materials",
        default=False
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

# -----------------------------------------------------------------------------
# CLASS backfacemat
#       Active/desactive les backfaces sur tout les materials
# -----------------------------------------------------------------------------


class SimpleOperator(bpy.types.Operator):

    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Remplace material"

    def execute(self, context):
        props = context.scene.MaterialUtilitiesPropertyGroup
        MATERIAL_REPLACE(props.MaterialToReplace, props.MaterialReplace)
        return {'FINISHED'}


# -----------------------------------------------------------------------------
# CLASS backfacemat
#       Active/desactive les backfaces sur tout les materials
# -----------------------------------------------------------------------------


class BackfaceMaterial(bpy.types.Operator):

    bl_idname = "object.backfacematerial_operator"
    bl_label = " Activate/desactivate backface for all Mat "

    def execute(self, context):
        props = context.scene.MaterialUtilitiesPropertyGroup
        BackfaceBoolVal = props.BackfaceBool

        print("BACK FESSE BOOL ")
        print(props.BackfaceBool)

        i = -1
        for num in bpy.data.materials:
            i = i + 1
            print(i)
            print(num)
            print(bpy.data.materials[i])
            bpy.data.materials[i].use_backface_culling = BackfaceBoolVal
            print(bpy.data.materials[i].use_backface_culling)

        return{'FINISHED'}


# -----------------------------------------------------------------------------
# CLASS  l'Interface
# -----------------------------------------------------------------------------
class MU_PT_pane(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Material Asignement Utils"
    bl_category = "Tool"

    def draw(self, context):

        layout = self.layout
        obj = context.object

        props = context.scene.MaterialUtilitiesPropertyGroup

        row = layout.row()
        layout.label(text="Material Replace")

        # --------------------------------------------------------
        # Mes 2 magnifiques boutons !
        # --------------------------------------------------------
        row = layout.row()
        row.prop(props, "MaterialReplace")

        row = layout.row()
        row.prop(props, "MaterialToReplace")

        # --------------------------------------------------------
        # Mon magnifique apply !
        # --------------------------------------------------------
        layout.label(text="Replace by this Material in all object")
        row = layout.row()
        row.operator('object.simple_operator')

        row = layout.row()
        layout.label(text="BackeFace")
        row.prop(props, "BackfaceBool")

        row = layout.row()
        layout.label(text="Apply backface to all materials")
        row.operator("object.backfacematerial_operator")


classes = [
    SimpleOperator,
    MU_PT_pane,
    MaterialUtilitiesPropertyGroup,
    BackfaceMaterial]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.MaterialUtilitiesPropertyGroup = bpy.props.PointerProperty(
        type=MaterialUtilitiesPropertyGroup)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.MyPropertyGroup

if __name__ == "__main__":
    register()
