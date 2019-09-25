import bpy
'''
Select all Fcurves and delete all keys by parameters
    In this exemple:
        Delete all Location types animations. Preserve Scale and 
'''
# ---------------------------------
#               VARIABLES
# ---------------------------------


# --- Anim curves variables
Actions = bpy.data.actions
ParamToDelete = "location" # change by  "Scale" or "Rotation"

# --- Directory and Files var
files = []# list all my files in my dir
currentFile = r''
dir = r''
#entire_path = r"E:\Users\user\Desktop\TestFbx\M_STAND_CONTRACTION_IDLE_ARM-SeparatedHands-TO-TEL-InFront-4.fbx"

#-------------------------------------------------------------
# OPERATOR
#-------------------------------------------------------------


class SelectFolder(bpy.types.Operator):     # batch folder for and do operations
    """Select your folder where your files are"""

    bl_idname = "batch_fbx.select_folder"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "batch_fbx.select_folder"

    directory = bpy.props.StringProperty(
        name="Outdir Path",
        description="Batch all fbx files in folder"
        )

    def execute(self, context):

        print("Selected dir: '" + self.directory + "'")
        global dir
        dir = self.directory
        files_in_path(dir)

        return {'FINISHED'}

    def invoke(self, context, event):
        # Open browser, take reference to 'self' read the path to selected
        # file, put path in predetermined self fields.
        # See: https://docs.blender.org/api/current/bpy.types.WindowManager.html#bpy.types.WindowManager.fileselect_add
        context.window_manager.fileselect_add(self)
        # Tells Blender to hang on for the slow user input
        return {'RUNNING_MODAL'}

# ---------------------------------
#              Functions
# ---------------------------------


def reset_blend():  # Cleaning all Data

    for obj in bpy.data.objects:
        obj.select_set(True)

    bpy.ops.object.delete()
    # Can reduce that funct
    # delete actions
    for block in bpy.data.actions:
        if block.users == 0:
            print(block)
            bpy.data.actions.remove(block)
    # delete meshes
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    # delete materials
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    # delete textures
    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)
    # delete images
    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)


def files_in_path(path):
    '''Return all files in directory'''
    for i in os.listdir(path):
        print(i)
        if i.endswith(".fbx"):
            print("it's a fbx")
            global currentFile
            currentFile = i
            #import_and_save()

# ---- Fbx ops -----------------------
def impFbxMaya():
    '''Import fbx made with maya'''
    bpy.ops.import_scene.fbx(
        filepath=entire_path,
        axis_forward='X',
        axis_up='Y',
        directory="",
        filter_glob="*.fbx",
        ui_tab='MAIN',
        use_manual_orientation=False,
        global_scale=1.0,
        bake_space_transform=False,
        use_custom_normals=True,
        use_image_search=True,
        use_alpha_decals=False,
        decal_offset=0.0,
        use_anim=True,
        anim_offset=1.0,
        use_custom_props=True,
        use_custom_props_enum_as_string=True,
        ignore_leaf_bones=False,
        force_connect_children=False,
        automatic_bone_orientation=False,
        primary_bone_axis='X',
        secondary_bone_axis='Z',
        use_prepost_rot=True
    )


def expFbxMaya():
    '''Export fbx for maya'''
    bpy.ops.export_scene.fbx(
        filepath= entire_path,
        check_existing=False,
        axis_forward='-Z',
        axis_up='Y',
        filter_glob="*.fbx",
        use_selection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        bake_space_transform=False,
        object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'},
        use_mesh_modifiers=True,
        mesh_smooth_type='OFF',
        use_mesh_edges=False,
        use_tspace=False,
        use_custom_props=False,
        add_leaf_bones=True,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_armature_deform_only=False,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        use_anim=True,
        use_anim_action_all=True,
        use_default_take=True,
        use_anim_optimize=True,
        anim_optimize_precision=6.0,
        path_mode='AUTO',
        embed_textures=False,
        batch_mode='OFF',
        use_batch_own_dir=True,
        use_metadata=True)




# ---- Delete specific Anim curve -----------------------
def ListActions(Act):
    '''List all actions and send it to curve'''
    for i in Act:
        ListFcurve(i)

def ListFcurve(Curves):
    '''List all curves in action'''
    for i in Curves.fcurves:
        print(i.data_path.endswith)
        if i.data_path.endswith(ParamToDelete) == True:
            Curves.fcurves.remove(i)

# ListActions(Actions) Execute
#
# ---------------------------------
#              REGISTER
# ---------------------------------

classes = [
    SelectFolder,
    ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    #bpy.utils.register_class(ImportSomeData)
    #bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    #bpy.utils.unregister_class(ImportSomeData)
    #bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()
    #impFbxMaya()
    bpy.ops.batch_src.select_folder('INVOKE_DEFAULT')

