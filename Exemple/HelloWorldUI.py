import bpy
#
# Les operator de blender permettent d'enregister des classes qui peuvent appeler des fonctions customisés
#
class MonOperator(bpy.types.Operator):
   # Ma classe qui va se ranger dans les operator ou ops
  
   bl_idname = "hello.hello_world"
   # l'emplacement de ma commande pour l'appeller.
   # on ne peut pas mettre de majuscule ou avoir 2 id name identique

   bl_label = "Minimal Operator"
   # son petit nom si c'est affiché dans un bouton

   def execute(self, context): #c' est ici ma fonction qui va être executé
       print("Hello World")
       return {'FINISHED'}

bpy.utils.register_class(MonOperator) # ici on enregistre cette classe !
bpy.ops.hello.hello_world()# la le teste 
# avec les () permet de retourner la fonction