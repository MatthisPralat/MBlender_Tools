import bpy


objs = bpy.data.objects

# list of materials
global Context_M, Context_Doubles_M, Double
Context_M = {}
Context_Doubles_M = {}
Double = False

# loop init 


def init():
    for obj in objs:
        Mslots_doubles(obj)

# Find Double materials slots


def Mslots_doubles(obj):
    
    # ReInit Globals Var
    Double = False
    Context_M.clear()
    Context_Doubles_M.clear()
    
    # check if obj have multiple slot
    if len(obj.material_slots) > 0:
        i = 0
        for m_slots in obj.material_slots:

            # set double index matslot and good index as value
            if m_slots.name in Context_M:
                Double = True
                name = str(m_slots.name)
                Context_Doubles_M.update({i:Context_M[name]})

            # set material name as index with the index of mat slot as value
            else:
                Context_M.update({m_slots.name: i})
            i = i + 1
    
    if Double == True:
        Mslots_reasign(obj)

def Mslots_reasign(obj):

    for face in obj.data.polygons:
        if face.material_index in Context_Doubles_M:
            print(face, face.index, "material_index", face.material_index)
            fmi = str(face.material_index) + " material slot"
            Cdm = str( Context_Doubles_M[face.material_index] ) + " material slot" 
            Fi = " at " + str (face.index) + " face index " 
            print(" Remplacing ", fmi , " by " , Cdm , Fi)
            face.material_index = Context_Doubles_M[face.material_index]
         
        else:
            print(face, face.index, "material_index", face.material_index)
    #print(face, face.index, "material_index", face.material_index)
    #for f in mesh.polygons:  # iterate over faces
    #print("face", f.index, "material_index", f.material_index)
    #if f.material_index == 3:
        #f.material_index = 1
        
def clearUnusedMatSlot(obj):
    print("hello")
    i = 0
    rMatslots ={}
    uMatslots = {}
    matslots = {}
    
    if len(obj.material_slots) > 0: 
        
        # first loop for material slots
        for mats in obj.material_slots:
            matslots.update({str(i) : str(mats.name) } )
            i= i + 1
      
        uMatslots = matslots
        # Loop to know slot mesh to clean Slots
        for face in obj.data.polygons:
            if str(face.material_index) in matslots:
                del matslots[str(face.material_index)]
                print(face.material_index)
                print("hello")
            else:
                print("continue")
            
        print("unused mat")
        print(matslots)
        rMatslots = sorted(matslots, reverse=True)
            
        for uMat in rMatslots:
    
            obj.active_material_index = int(uMat)
            # overide context
            ctx = bpy.context.copy ()
            ctx['object'] = obj
            bpy.ops.object.material_slot_remove(ctx)
            #print(int(float(Umat)))
            print(uMat)
            
    
        print(sorted(matslots.keys(), reverse=True))
        print(rMatslots)
    print(rMatslots) 
 
def ClearMatslot():
    for obj in objs:
        clearUnusedMatSlot(obj)

init()
ClearMatslot()