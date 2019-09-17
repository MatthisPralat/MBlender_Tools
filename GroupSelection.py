import bpy

SelObj = bpy.context.selected_objects  # get my selection
X, Y, Z = 0.000000, 0.000000, 0.000000  # Pseudo Vector 3
i = 0  # number of objects
Null = 0


def Unparent():
    ''' Just unparent sel for escape errors'''
    for obj in SelObj:
        obj2 = obj
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

def Location():
    ''' Add the Location of each selected objects'''

    global X, Y, Z
    global i

    for obj in SelObj:
        i = i + 1
        X, Y, Z = X + obj.matrix_world.to_translation().x, Y + obj.matrix_world.to_translation().y, Z + obj.matrix_world.to_translation().z
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


Unparent() # unparent, selected objects
Location() # get the location of objects
average()  # Add and divide the location by the number of objects
CreateNull() # create a null to the average position
ParentToNull() # Parent the objects in the new null object
