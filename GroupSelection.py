import bpy

SelObj = bpy.context.selected_objects  # get my selection
X, Y, Z = 0.000000, 0.000000, 0.000000  # Pseudo Vector 3
i = 0  # number of objects
Null = 0


def Location():
    ''' Add the Location of each selected objects'''

    global X, Y, Z
    global i

    for obj in SelObj:
        i = i + 1
        X, Y, Z = X + obj.matrix_world.to_translation().x, Y + obj.matrix_world.to_translation().y, Z + obj.matrix_world.to_translation().z
        print("Adition")
        print(X, Y, Z)


def average():
    '''Divide Location by the number of object'''
    global X, Y, Z
    X, Y, Z = X / i, Y / i, Z / i
    print(X, Y, Z)


def CreateNull():
    global null
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(X, Y, Z))
    null = bpy.context.active_object


def ParentToNull():
    for obj in SelObj:
        print(obj)
        obj.parent = null
        obj.matrix_parent_inverse = null.matrix_world.inverted()


Location()
average()
CreateNull()
ParentToNull()

bpy.data.window_managers[0].keyconfigs.active.keymaps['Mesh'].keymap_items.new('op.idname', value='PRESS', type='A',
                                                                               ctrl=True, alt=True, shift=True,
                                                                               oskey=True)