This project gathers my personnal scripts, tools and tests in python for Blende.

## MaterialAsignementUtils.py

![](http://www.matthispralat.fr/wp-content/uploads/2019/07/Replace_Material.gif)

**Ce script permet de remplacer un material par un autre sur tout les objets de la scene.** 

Il le fait en fonctions des slots materials des objets. Ce qui permet de ne pas remplacer d’autres materials asigné à cet objet.
Bonus : J’ai aussi implémenté un bouton qui vas mettre un backface sur tout les matériaux, étant donné que blender l’à retiré de ses options dans le viewport shading dans la version que j’utilise.

## CollectionToHierarchy.py
Attention: Toujours en développement

**Collection to hierarchy permet d’organiser avec des empty une hiérarchie similaire à celle faites grâces aux collections. Dans un export vers unity ça reste sympa d’avoir un fichier lisible.**

D’ailleur le système de parenté d’objet de blender n’est pas tout à fait au point et c’est pourquoi ce script est un réel time-saver.

Si des objets sont parentés… Pas de soucis seul le parent sera assigné à un nouvel emplacement et ses enfants le suivrons tout en gardant cette parenté.

Attention : toutes les collections doivent être visible, les duplicate-instance vont poser des soucis !

**Mon scene outline**

![](http://www.matthispralat.fr/wp-content/uploads/2019/07/word-image-27.png)

**Mon scene view layer**

![](http://www.matthispralat.fr/wp-content/uploads/2019/07/word-image-26.png)

**Mon scene outline apres execution du script**

![](http://www.matthispralat.fr/wp-content/uploads/2019/07/word-image-28.png)

**_Problème connu :_**

Les instance mesh peuvent poser des problème
Si les view layer sont caché alors le script ne fonctionnera pas

## SelDoubleMesh.py
> Un missclick , une fausse opération, et vos mesh se sont dédoublé, superposé vous ne voyez pas qui est qui !

![](http://www.matthispralat.fr/wp-content/uploads/2019/07/word-image-3.gif)

**Sel double vient sélectionner tous les malencontreux objets qui serait l’un sur l’autre.**

Pour ce faire, Il fait une liste de chaque objets en prenant

-Le nombre de vertex de l’objet
-La position par vertex dans un espace world
-Additionne les position

Si un objet à le même nombre de vertex et la même addition de position de vertex. Alors c’est un double ! Et on le selectionne, pour le supprimer ou le réorganiser ailleur.



## Projet futurs

MaterialAsignementUtilsLinkedMat.py
Si, on ajoute une biliotheque de linked material, et qu’un material-non linked à le même nom que ces dernier alors qu’ils se convertissent en ce denier.

Add-on et UV-Set Utils
Créer une interface pour tous mes scripts dans un panel bien à lui sur un deuxième écrans.

Vérifier que je respecte la convention <Pep8> Partager ça avec la communauté pour quelques retour et publier mon petit add-on.

