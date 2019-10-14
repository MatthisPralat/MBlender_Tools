# Ouvrir chemin de dossier
# Regarder tout les fichier dedans
# pour tout les .src importer le modele
# enregistrer en .blend avec le nom + packagé
# ouvrir le prochain


# premierement on vas faire une popup qui nous de mande de selectionner un dossier
import bpy
import os

# -------------------------------------------------------------
# VARIABLES
# -------------------------------------------------------------

files = []  # list all my files in my dir
currentFile = r''
dir = r''


# path =''

# -------------------------------------------------------------
# OPERATOR
# -------------------------------------------------------------
class SelectFolder(bpy.types.Operator):
    """Select your folder where your files are"""

    bl_idname = "batch_src.select_folder"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "batch_src.select_folder"

    # Define this to tell 'fileselect_add' that we want a directoy
    directory = bpy.props.StringProperty(
        name="Outdir Path",
        description="Where I will save my stuff"
        # subtype='DIR_PATH' is not needed to specify the selection mode.
        # But this will be anyway a directory path.
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


# -------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------


def files_in_path(path):
    '''if file in this folder print files'''
    for i in os.listdir(path):
        print(i)
        if i.endswith(".fspy"):
            print("it's a fspy")
            global currentFile
            currentFile = i
            importfspy()


def importfspy():
    print(dir + currentFile)
    escaped_path = dir.replace("\\", "\\\\")
    entire_path = escaped_path + currentFile
    print(entire_path)
    bpy.ops.fspy_blender.import_project(filepath=entire_path)
    # bpy.ops.import_scene.fbx( filepath=entire_path)
    # save_file()



def reset_blend():
    for obj in bpy.data.objects:
        obj.select_set(True)
        # if obj.type == ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER']:
        # obj.select_set(True)

    bpy.ops.object.delete()

    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)

    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)

    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)

    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)


# -------------------------------------------------------------
# REGISTER // INITIALISATION
# -------------------------------------------------------------

# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(ImportSomeData.bl_idname, text="Text Import Operator")


classes = [
    SelectFolder,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # bpy.utils.register_class(ImportSomeData)
    # bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # bpy.utils.unregister_class(ImportSomeData)
    # bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()
    bpy.ops.batch_src.select_folder('INVOKE_DEFAULT')

