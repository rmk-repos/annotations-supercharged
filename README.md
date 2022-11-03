# Annotations Supercharged Blender Add On

Handy tools for supercharging your annotations

Current version: 1.0.2
Blender version: 3.3.0


## Features:
1. Hide Layers
2. Show Layers
3. Clear Layers
4. Set Active Layers
5. Import color from Color Palette to the layers


It adds itself to the headers of the relevant spaces where annotations are available (3D view, Node editors, Imaged editor, Sequence editor). Also there is a main menu which can be used either with Blender inbuild Quick Favourites or with other addons like https://github.com/passivestar/quickmenu

### For Blender inbuilt quick favourites
1. Use menu search and search for text "super main".

2. If the addon is installed, you will see the following

annotations_supercharged.show_main_menu ▶Show Main Menu

3. Right click and "Add to Quick Favourites"

### For Quickmenu, this is the configuration to add. 
```
{
     "path": "Custom/Annottation Supercharged",
     "menu": "VIEW_MT_annotation_supercharged_main_menu"
},
```
Note: You may need the latest version of Quickmenu which supports adding menus to the config.json. Here is the Github patch details https://github.com/passivestar/quickmenu/commit/87634d793d40f39af4939bfb927d8e4c00e347fd



**This is my first addon and my first exploration in Python. So please expect the unexpected. :)**
