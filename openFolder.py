import bpy

path = 'B:\MP_GDrive\3D\3DProject\M_Appartemen\MASTER_MATERIAL.blend '
pathUTF8 = path.encode(encoding='UTF-8',errors='strict')
pathStr = str(pathUTF8)

print(type(pathUTF8))
print(type(pathStr))

print(pathStr)

print(bpy.data.libraries.load(pathStr , relative=False) )
with bpy.data.libraries.load(pathStr, relative=False) as (data_from, data_to):
    print('hello')
    #print(data_to.scenes)
