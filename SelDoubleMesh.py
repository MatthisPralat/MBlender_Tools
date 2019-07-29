# Script qui compare les mesh et delete les doubles
    # Je compare le nombre de vertex par objets
    # et la moyenne de leur emplacement
    #  
#je delete ceux qui ont la meme moyenne


import bpy

Item = {}

for obj in bpy.data.objects:
   
    ObjName = str(obj.name)
    VertexAvg = 0
    
    if obj.type == "MESH":
        vertices  = obj.data.vertices 
        
        for vert in vertices:
            vWorldPos = obj.matrix_world @ vert.co 
           
            for mint in vWorldPos:
                VertexAvg = VertexAvg + mint
        
        strVerAvg = str(VertexAvg)
        
        if strVerAvg in Item:
            print("c'est pas vide")
            Item[strVerAvg].append( {"name": ObjName } )
      
        else:
            print("cest vide")
            Item.update({ strVerAvg:[]}) 
            Item[strVerAvg].append( {"name": ObjName } )

print(Item)

d = Item

bpy.ops.object.select_all(action='DESELECT')
 
for key, value in d.items() :
    print("key")
    print("Value")
    print(len(value))
   
    if len(value) > 1 :
      i = 0      
      for key in value :
        print(i)
        if i > 0:
            print(key["name"]) 
            bpy.data.objects[key["name"]].select_set(True)
        i = i + 1