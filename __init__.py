bl_info = {
    "name": "Annotations Supercharged",
    "author": "R.M.K",
    "version": (1, 0, 2),
    "blender": (3, 3, 0),
    "warning": "",
    "description": "Handy tools for supercharging your annotations",
    "wiki_url": "",
    "category": "Misc",
}

import bpy
import sys

bpy_version=bpy.app.version
py_version=(sys.version_info.major,sys.version_info.minor,sys.version_info.micro)
addon_name=bl_info["name"]
addon_name_version=addon_name + " v" + str(bl_info["version"][0]) + "." + str(bl_info["version"][1]) + "." + str(bl_info["version"][2])

dynamicClasses = []

############################################################################################################################################
# Credits: https://www.geeksforgeeks.org/how-to-change-a-dictionary-into-a-class/#:~:text=We%20are%20calling%20a%20function%20here%20Dict2Class%20which,used%20to%20assign%20the%20object%20attribute%20its%20value.
############################################################################################################################################
# Turns a dictionary into a class
class Dict2Class(object):

    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])

    def dump(self, prefix=''):
        print('%sself: %s' % (prefix,self))
        if hasattr(self, 'type'): print('%s    type: %s' % (prefix,self.type))
        if hasattr(self, 'operator'): print('%s    operator: %s' % (prefix,self.operator))
        if hasattr(self, 'menu'): print('%s    menu: %s' % (prefix,self.menu))
        if hasattr(self, 'separator'): print('%s    separator: %s' % (prefix,self.separator))
        if hasattr(self, 'text'): print('%s    text: %s' % (prefix,self.text))

############################################################################################################################################

class ASHelper:
    validDynamicMenu = [
    'all_layers',
    'active_layer', 'inactive_layers',
    'shown_layers', 'hidden_layers',
    'all_palettes',
    ]

    def drawHelper(self, data):
        layout = self.layout
        for itm in data:
            #print('itm',itm)
            itm=Dict2Class(itm)
            if itm.type == 'separator':
                layout.separator()
            elif itm.type == 'label':
                layout.label(text=itm.text)
            elif itm.type == 'menu':
                if hasattr(itm, 'text'):
                    layout.menu(itm.classref.bl_idname, text=itm.text)
                else:
                    layout.menu(itm.classref)
                #end if hasattr(itm, 'text'):
            elif itm.type == 'operator':
                if hasattr(itm, 'text'):
                    layout.operator(itm.classref.bl_idname, text=itm.text)
                else:
                    layout.operator(itm.classref.bl_idname)
                #end if hasattr(itm, 'text'):
            #end if itm.type == 'separator':
        #end for itm in main_menu_layout:
    #end def drawHelper(self):

#end class ASHelper:
############################################################################################################################################

class ASOperatorHideAllLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.hide_all_layers"
    bl_label = "Hide All Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Hide all layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            for gpl in gp.layers:
                gpl.annotation_hide=True				
                #gpl.hide=True
            #end for gpl in gp.layers:
            self.report({'INFO'}, "All layers in the active annotation hidden!")
        else:
            self.report({'INFO'}, "No annotations or layer to hide!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorHideAllLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorShowAllLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.show_all_layers"
    bl_label = "Show All Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Show all layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            for gpl in gp.layers:
                gpl.annotation_hide=False				
                #gpl.hide=False
            #end for gpl in gp.layers:
            self.report({'INFO'}, "All layers in the active annotation shown!")
        else:
            self.report({'INFO'}, "No annotations or layer to show!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorShowAllLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorHideActiveLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.hide_active_layer"
    bl_label = "Hide Active Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Hide active layer of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            gplactive=gp.layers.active
            if gplactive is None: gplactive=gp.layers[0]
            gplactive.annotation_hide=True
            #gplactive.hide=True
            self.report({'INFO'}, "Active layer in the active annotation hidden!")
        else:
            self.report({'INFO'}, "No annotations or layer to hide!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorHideActiveLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorShowActiveLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.show_active_layer"
    bl_label = "Show Active Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Show active layer of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            gplactive=gp.layers.active
            if gplactive is None: gplactive=gp.layers[0]
            gplactive.annotation_hide=False
            #gplactive.hide=False
            self.report({'INFO'}, "Active layer in the active annotation shown!")
        else:
            self.report({'INFO'}, "No annotations or layer to show!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorShowActiveLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorHideInactiveLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.hide_inactive_layers"
    bl_label = "Hide Inactive Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Hide inactive layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            gplactive=gp.layers.active
            if gplactive is None: gplactive=gp.layers[0]
            for gpl in gp.layers:
                if gpl != gplactive:
                    gpl.annotation_hide=True				
                    #gpl.hide=True
                #end if gpl != gplactive:
            #end for gpl in gp.layers:
            self.report({'INFO'}, "Inactive layers in the active annotation hidden!")
        else:
            self.report({'INFO'}, "No annotations or layer to hide!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorHideInactiveLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorShowInactiveLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.show_inactive_layers"
    bl_label = "Show Inactive Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Show inactive layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            gplactive=gp.layers.active
            if gplactive is None: gplactive=gp.layers[0]
            for gpl in gp.layers:
                if gpl != gplactive:
                    gpl.annotation_hide=False				
                    #gpl.hide=False
                #end if gpl != gplactive:
            #end for gpl in gp.layers:
            self.report({'INFO'}, "Inactive layers in the active annotation shown!")
        else:
            self.report({'INFO'}, "No annotations or layer to show!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorShowInactiveLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorShowLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.show_layer"
    bl_label = "Show Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Show selected layer of the active annotation"

    layername: bpy.props.StringProperty(
        name = 'Layer Name',
        default = ''
    )

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        layername = self.layername

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if layername in gp.layers:
                gpl=gp.layers[layername]
                gpl.annotation_hide=False
                #gpl.hide=False
                self.report({'INFO'}, "Layer %s in the active annotation is now shown!" % (layername) )
            #end if layername in gp.layers:
        else:
            self.report({'INFO'}, "No annotations or layer to show!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorShowLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorHideLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.hide_layer"
    bl_label = "Hide Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Hide selected layer of the active annotation"

    layername: bpy.props.StringProperty(
        name = 'Layer Name',
        default = ''
    )

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        layername = self.layername

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if layername in gp.layers:
                gpl=gp.layers[layername]
                gpl.annotation_hide=True
                #gpl.hide=True
                self.report({'INFO'}, "Layer %s in the active annotation is now hidden!" % (layername) )
            #end if layername in gp.layers:
        else:
            self.report({'INFO'}, "No annotations or layer to hide!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorHideLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorClearLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.clear_layer"
    bl_label = "Clear Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Clear selected layer of the active annotation"

    layername: bpy.props.StringProperty(
        name = 'Layer Name',
        default = ''
    )

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        layername = self.layername

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if layername in gp.layers:
                gpl=gp.layers[layername]
                gpl.clear()
                self.report({'INFO'}, "Layer %s in the active annotation is now cleared!" % (layername) )
            #end if layername in gp.layers:
        else:
            self.report({'INFO'}, "No annotations or layer to clear!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorClearLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorSetActiveLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.set_active_layer"
    bl_label = "Set Active Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Set selected layer as active of the active annotation"

    layername: bpy.props.StringProperty(
        name = 'Layer Name',
        default = ''
    )

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        layername = self.layername

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if layername in gp.layers:
                gp.layers.active=gp.layers[layername]
                self.report({'INFO'}, "Annotation layer %s active!" % (layername) )
            #end if layername in gp.layers:
        else:
            self.report({'INFO'}, "No annotations or layer to make active!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorSetActiveLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorImportPaletteColors(bpy.types.Operator):
    bl_idname = "annotations_supercharged.import_palette_colors"
    bl_label = "Import Palette Colors"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Import Colors from Palette to all the layers of the active annotation"

    palettename: bpy.props.StringProperty(
        name = 'Palette Name',
        default = ''
    )

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        pals = bpy.data.palettes

        palettename = self.palettename

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if pals is not None and len(pals) > 0:
                if palettename in pals:
                    pal = pals[palettename]
                    if pal is not None and pal.colors is not None and len(pal.colors) > 0:
                        l_gp=len(gp.layers)
                        l_pal=len(pal.colors)
                        for i_gp in range(0,l_gp):
                            i_pal=i_gp%l_pal
                            print('i_gp',i_gp, i_pal)
                            print('color', pal.colors[i_pal].color)
                            gp.layers[i_gp].color=pal.colors[i_pal].color
                        #end for i_gp in range(0,l_gp):
                    #end if pal is not None and pal.colors is not None and len(pal.colors) > 0:
                #end if palettename in pals:
            else:
                self.report({'INFO'}, "No palette to import colors!")
            #end if pals is not None and len(pals) > 0:
        else:
            self.report({'INFO'}, "No annotations or layer to import colors!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorImportPaletteColors(bpy.types.Operator):
############################################################################################################################################

class ASOperatorClearAllLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.clear_all_layers"
    bl_label = "Clear All Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Clear all layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            for gpl in gp.layers:
                gpl.clear()
            #end for gpl in gp.layers:
            self.report({'INFO'}, "All layers in the active annotation cleared!")
        else:
            self.report({'INFO'}, "No annotations or layer to clear!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorClearAllLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorClearActiveLayer(bpy.types.Operator):
    bl_idname = "annotations_supercharged.clear_active_layer"
    bl_label = "Clear Active Layer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Clear active layer of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            gplactive=gp.layers.active
            if gplactive is None: gplactive=gp.layers[0]
            gplactive.clear()
            self.report({'INFO'}, "Active layer in the active annotation cleared!")
        else:
            self.report({'INFO'}, "No annotations or layer to clear!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorClearActiveLayer(bpy.types.Operator):
############################################################################################################################################

class ASOperatorClearInactiveLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.clear_inactive_layers"
    bl_label = "Clear Inactive Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Clear inactive layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            gplactive=gp.layers.active
            if gplactive is None: gplactive=gp.layers[0]
            for gpl in gp.layers:
                if gpl != gplactive:
                    gpl.clear()
                #end if gpl != gplactive:
            #end for gpl in gp.layers:
            gpl.clear()
            self.report({'INFO'}, "Inactive layers in the active annotation cleared!")
        else:
            self.report({'INFO'}, "No annotations or layer to clear!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorClearInactiveLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorClearShownLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.clear_shown_layers"
    bl_label = "Clear Shown Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Clear shown layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            for gpl in gp.layers:
                if not gpl.annotation_hide:
                    gpl.clear()
                #end if not gpl.annotation_hide:
            #end for gpl in gp.layers:
            self.report({'INFO'}, "Shown layers in the active annotation cleared!")
        else:
            self.report({'INFO'}, "No annotations or layer to clear!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorClearShownLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorClearHiddenLayers(bpy.types.Operator):
    bl_idname = "annotations_supercharged.clear_hidden_layers"
    bl_label = "Clear Hidden Layers"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Clear hidden layers of the active annotation"

    def execute(self, context):
        #gp = bpy.context.scene.grease_pencil

        # Grease Pencil owner.
        gpd_owner = context.annotation_data_owner
        gpd = context.annotation_data

        #print('gp',gp)
        #print('gpd',gpd)
        #print('ggpd_ownerp',gpd_owner)

        gp=gpd

        if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            for gpl in gp.layers:
                if gpl.annotation_hide:
                    gpl.clear()
                #end if gpl.annotation_hide:
            #end for gpl in gp.layers:
            self.report({'INFO'}, "Hidden layers in the active annotation cleared!")
        else:
            self.report({'INFO'}, "No annotations or layer to clear!")
        #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorClearHiddenLayers(bpy.types.Operator):
############################################################################################################################################

class ASOperatorShowMenu(bpy.types.Operator):
    bl_idname = "annotations_supercharged.show_main_menu"
    bl_label = "Show Main Menu"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Shows the Main Menu for %s Addon" % (addon_name_version)

    def execute(self, context):
        #bpy.ops.wm.call_menu(name=ASMainMenu.__name__)
        bpy.ops.wm.call_menu(name=ASMainMenu.bl_idname)
        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorShowMenu(bpy.types.Operator):
############################################################################################################################################

class ASOperatorShowInbuiltAnnotationLayerPanel(bpy.types.Operator):
    bl_idname = "annotations_supercharged.show_inbuilt_annotation_layer_panel"
    bl_label = "Show Inbuilt Annotation Layer Panel"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Shows the Inbuilt Annotation Layer Panel for %s Addon" % (addon_name_version)

    def execute(self, context):
        print('ASOperatorShowInbuiltAnnotationLayerPanel')
        #bpy.ops.wm.call_panel(name="NODE_PT_annotation", keep_open=True)
        #bpy.ops.wm.call_panel(name="TOPBAR_PT_annotation_layers", keep_open=True)
        bpy.ops.wm.call_panel(name="VIEW3D_PT_grease_pencil", keep_open=True)

        return {'FINISHED'}
    #end def execute(self, context):

#end class ASOperatorShowInbuiltAnnotationLayerPanel(bpy.types.Operator):
############################################################################################################################################

class ASStaticMenu(bpy.types.Menu, ASHelper):
    bl_label = "Static Menu"
    #bl_idname = "OBJECT_MT_dynamic_menu"

    menuitems = []

    def draw(self, context):
        print('ASStaticMenu')
        self.drawHelper(self.menuitems)
    #end def draw(self, context):
#end class ASStaticMenu(bpy.types.Menu, ASHelper):
############################################################################################################################################

class ASDynamicMenu(bpy.types.Menu):
    bl_label = "Dynamic Menu"
    #bl_idname = "OBJECT_MT_dynamic_menu"

    def draw(self, context):
        layout = self.layout
        print('ASDynamicMenu %s %s' % (self.dynamicMenuData, self.dynamicMenuSubData) )
        if self.dynamicMenuData == 'inactive_layers':
            #gp = bpy.context.scene.grease_pencil

            # Grease Pencil owner.
            gpd_owner = context.annotation_data_owner
            gpd = context.annotation_data

            #print('gp',gp)
            #print('gpd',gpd)
            #print('ggpd_ownerp',gpd_owner)

            gp=gpd

            i_l=1
            bHasItems=False
            layout.label(text='Inactive Layers')
            layout.separator()
            if gp is not None and gp.layers is not None and len(gp.layers) > 0:
                gplactive=gp.layers.active
                if gplactive is None: gplactive=gp.layers[0]
                for gpl in gp.layers:
                    if gpl != gplactive:
                        layout.operator(self.dynamicMenuSubData, text='(%d) %s' % (i_l, gpl.info)).layername=gpl.info
                        bHasItems=True
                    #else:
                    #    layout.label(text='(%d) %s' % (i_l, gpl.info))
                    i_l=i_l+1
                    #end if gpl != gplactive:
                #end for gpl in gp.layers:
            #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if not bHasItems: layout.label(text='--- None ---')

        elif self.dynamicMenuData == 'hidden_layers':
            #gp = bpy.context.scene.grease_pencil

            # Grease Pencil owner.
            gpd_owner = context.annotation_data_owner
            gpd = context.annotation_data

            #print('gp',gp)
            #print('gpd',gpd)
            #print('ggpd_ownerp',gpd_owner)

            gp=gpd

            i_l=1
            bHasItems=False
            layout.label(text='Hidden Layers')
            layout.separator()
            if gp is not None and gp.layers is not None and len(gp.layers) > 0:
                for gpl in gp.layers:
                    if gpl.hide:
                        layout.operator(self.dynamicMenuSubData, text='(%d) %s' % (i_l, gpl.info)).layername=gpl.info
                        bHasItems=True
                    #else:
                    #    layout.label(text='(%d) %s' % (i_l, gpl.info))
                    i_l=i_l+1
                    #end if gpl != gplactive:
                #end for gpl in gp.layers:
            #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if not bHasItems: layout.label(text='--- None ---')

        elif self.dynamicMenuData == 'all_layers':
            #gp = bpy.context.scene.grease_pencil

            # Grease Pencil owner.
            gpd_owner = context.annotation_data_owner
            gpd = context.annotation_data

            #print('gp',gp)
            #print('gpd',gpd)
            #print('ggpd_ownerp',gpd_owner)

            gp=gpd

            i_l=1
            bHasItems=False
            layout.label(text='All Layerss')
            layout.separator()
            if gp is not None and gp.layers is not None and len(gp.layers) > 0:
                for gpl in gp.layers:
                    layout.operator(self.dynamicMenuSubData, text='(%d) %s' % (i_l, gpl.info)).layername=gpl.info
                    bHasItems=True
                    i_l=i_l+1
                    #end if gpl != gplactive:
                #end for gpl in gp.layers:
            #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if not bHasItems: layout.label(text='--- None ---')

        elif self.dynamicMenuData == 'shown_layers':
            #gp = bpy.context.scene.grease_pencil

            # Grease Pencil owner.
            gpd_owner = context.annotation_data_owner
            gpd = context.annotation_data

            #print('gp',gp)
            #print('gpd',gpd)
            #print('ggpd_ownerp',gpd_owner)

            gp=gpd

            i_l=1
            bHasItems=False
            layout.label(text='Shown Layers')
            layout.separator()
            if gp is not None and gp.layers is not None and len(gp.layers) > 0:
                for gpl in gp.layers:
                    if not gpl.hide:
                        layout.operator(self.dynamicMenuSubData, text='(%d) %s' % (i_l, gpl.info)).layername=gpl.info
                        bHasItems=True
                    #else:
                    #    layout.label(text='(%d) %s' % (i_l, gpl.info))
                    i_l=i_l+1
                    #end if gpl != gplactive:
                #end for gpl in gp.layers:
            #end if gp is not None and gp.layers is not None and len(gp.layers) > 0:
            if not bHasItems: layout.label(text='--- None ---')

        elif self.dynamicMenuData == 'all_palettes':
            pals = bpy.data.palettes

            i_l=1
            bHasItems=False
            layout.label(text='All Palettes')
            layout.separator()
            if len(pals) > 0:
                for pal in pals:
                    layout.operator(self.dynamicMenuSubData, text='(%d) %s' % (i_l, pal.name)).palettename=pal.name
                    bHasItems=True
                    i_l=i_l+1
                #end for pal in pals:
            #end if len(pals) > 0:
            if not bHasItems: layout.label(text='--- None ---')

        #end if self.dynamicMenuData == 'inactive_layers':
    #end def draw(self, context):

#end class ASDynamicMenu(bpy.types.Menu):
############################################################################################################################################

class ASMainMenu(bpy.types.Menu, ASHelper):
    #bl_label = "%s Main Menu" % (addon_name_version)
    bl_label = "%s Main Menu" % (addon_name)
    bl_idname = "VIEW_MT_annotation_supercharged_main_menu"
    bl_description = "Main Menu for %s Addon" % (addon_name)

    def draw(self, context):
        self.drawHelper(config)
    #end def draw(self, context):

    def menu_draw(self, context):
        self.layout.menu(ASMainMenu.bl_idname, text=addon_name)
    #end def draw(self, context):

#end class ASMainMenu(bpy.types.Menu):
############################################################################################################################################

CLS_COMMONS = [
]

CLS_PANELS = [
]

CLS_MENUS = [
    ASMainMenu,
]

CLS_OPERATORS = [
    ASOperatorHideAllLayers,
    ASOperatorHideActiveLayer,
    ASOperatorHideInactiveLayers,
    ASOperatorHideLayer,

    ASOperatorShowAllLayers,
    ASOperatorShowActiveLayer,
    ASOperatorShowInactiveLayers,
    ASOperatorShowLayer,

    ASOperatorClearAllLayers,
    ASOperatorClearActiveLayer,
    ASOperatorClearInactiveLayers,
    ASOperatorClearShownLayers,
    ASOperatorClearHiddenLayers,
    ASOperatorClearLayer,

    ASOperatorSetActiveLayer,

    ASOperatorShowInbuiltAnnotationLayerPanel,

    ASOperatorImportPaletteColors,

    ASOperatorShowMenu,
]

config = [
    {
        'type': 'label',
        'text': addon_name_version
    },
    {
        'type': 'separator'
    },
    {
        'type': 'menu',
        'text': '(1) Hide Layers',
        'classref': type('%s_%s' % (ASStaticMenu.__name__, 'hide_layers'),
                            (ASStaticMenu,),
                            {'bl_idname': 'VIEW_MT_as_%s' % ('hide_layers'),
                             'menuitems': [
                                {
                                    'type': 'label',
                                    'text': 'Hide Layers'
                                },
                                {
                                    'type': 'separator'
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (1, ASOperatorHideAllLayers.bl_label),
                                    'classref': ASOperatorHideAllLayers
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (2, ASOperatorHideActiveLayer.bl_label),
                                    'classref': ASOperatorHideActiveLayer
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (3, ASOperatorHideInactiveLayers.bl_label),
                                    'classref': ASOperatorHideInactiveLayers
                                },
                                {
                                    'type': 'separator'
                                },
                                {
                                    'type': 'menu',
                                    'text': '(%d) %s' % (4, 'Hide Selected Layer'),
                                    'classref': type('%s_%s_%s' % (ASDynamicMenu.__name__, 'hide_layer', 'shown_layers'),
                                        (ASDynamicMenu,),
                                        {'bl_idname': 'VIEW_MT_as_%s_%s' % ('hide_layer', 'shown_layers'),
                                         'dynamicMenuData': 'shown_layers',
                                         'dynamicMenuSubData': ASOperatorHideLayer.bl_idname,
                                        })
                                },
                             ],
                            }),
    },
    {
        'type': 'menu',
        'text': '(2) Show Layers',
        'classref': type('%s_%s' % (ASStaticMenu.__name__, 'show_layers'),
                            (ASStaticMenu,),
                            {'bl_idname': 'VIEW_MT_as_%s' % ('show_layers'),
                             'menuitems': [
                                {
                                    'type': 'label',
                                    'text': 'Show Layers'
                                },
                                {
                                    'type': 'separator'
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (1, ASOperatorShowAllLayers.bl_label),
                                    'classref': ASOperatorShowAllLayers
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (2, ASOperatorShowActiveLayer.bl_label),
                                    'classref': ASOperatorShowActiveLayer
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (3, ASOperatorShowInactiveLayers.bl_label),
                                    'classref': ASOperatorShowInactiveLayers
                                },
                                {
                                    'type': 'separator'
                                },
                                {
                                    'type': 'menu',
                                    'text': '(%d) %s' % (4, 'Show Selected Layer'),
                                    'classref': type('%s_%s_%s' % (ASDynamicMenu.__name__, 'show_layer', 'hidden_layers'),
                                        (ASDynamicMenu,),
                                        {'bl_idname': 'VIEW_MT_as_%s_%s' % ('show_layer', 'hidden_layers'),
                                         'dynamicMenuData': 'hidden_layers',
                                         'dynamicMenuSubData': ASOperatorShowLayer.bl_idname,
                                        })
                                },
                             ],
                            }),
    },
    {
        'type': 'menu',
        'text': '(3) Clear Layers',
        'classref': type('%s_%s' % (ASStaticMenu.__name__, 'clear_layers'),
                            (ASStaticMenu,),
                            {'bl_idname': 'VIEW_MT_as_%s' % ('clear_layers'),
                             'menuitems': [
                                {
                                    'type': 'label',
                                    'text': 'Clear Layers'
                                },
                                {
                                    'type': 'separator'
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (1, ASOperatorClearAllLayers.bl_label),
                                    'classref': ASOperatorClearAllLayers
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (2, ASOperatorClearActiveLayer.bl_label),
                                    'classref': ASOperatorClearActiveLayer
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (3, ASOperatorClearInactiveLayers.bl_label),
                                    'classref': ASOperatorClearInactiveLayers
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (4, ASOperatorClearShownLayers.bl_label),
                                    'classref': ASOperatorClearShownLayers
                                },
                                {
                                    'type': 'operator',
                                    'text': '(%d) %s' % (5, ASOperatorClearHiddenLayers.bl_label),
                                    'classref': ASOperatorClearHiddenLayers
                                },
                                {
                                    'type': 'separator'
                                },
                                {
                                    'type': 'menu',
                                    'text': '(%d) %s' % (6, 'Clear Selected Layer'),
                                    'classref': type('%s_%s_%s' % (ASDynamicMenu.__name__, 'clear_layer', 'all_layers'),
                                        (ASDynamicMenu,),
                                        {'bl_idname': 'VIEW_MT_as_%s_%s' % ('clear_layer', 'all_layers'),
                                         'dynamicMenuData': 'all_layers',
                                         'dynamicMenuSubData': ASOperatorClearLayer.bl_idname,
                                        })
                                },
                             ],
                            }),
    },
    {
        'type': 'menu',
        'text': '(4) Set Active Layers',
        'classref': type('%s_%s_%s' % (ASDynamicMenu.__name__, 'active_layer', 'inactive_layers'),
            (ASDynamicMenu,),
            {'bl_idname': 'VIEW_MT_as_%s_%s' % ('active_layer', 'inactive_layers'),
             'dynamicMenuData': 'inactive_layers',
             'dynamicMenuSubData': ASOperatorSetActiveLayer.bl_idname,
            })
    },
    {
        'type': 'separator'
    },
    {
        'type': 'operator',
        'text': '(5) Show the Inbuilt Annotation Layer Panel',
        'classref': ASOperatorShowInbuiltAnnotationLayerPanel
    },
    {
        'type': 'separator'
    },
    {
        'type': 'menu',
        'text': '(6) Import Color Palette',
        'classref': type('%s_%s_%s' % (ASDynamicMenu.__name__, 'import_palette', 'all_palettes'),
            (ASDynamicMenu,),
            {'bl_idname': 'VIEW_MT_as_%s_%s' % ('import_palette', 'all_palettes'),
             'dynamicMenuData': 'all_palettes',
             'dynamicMenuSubData': ASOperatorImportPaletteColors.bl_idname,
            })
    },
]

def get_dynamic_class(config):
    for itm in config:
        #print(itm)
        itm=Dict2Class(itm)
        if hasattr(itm, 'classref'):
            classref=itm.classref
            if classref not in CLS_OPERATORS and classref not in CLS_MENUS:
                dynamicClasses.append(classref)
                if hasattr(classref, 'menuitems'):
                    #print('classref.menuitems',classref.menuitems, classref.menuitems)
                    get_dynamic_class(classref.menuitems)
                #end if hasattr(classref, 'menuitems'):
            #end if classref not in CLS_OPERATORS and classref not in CLS_MENUS:
        #end if hasattr(itm, 'classref'):
    #end for itm in config:
#end def get_dynamic_class(config):

def register():
    for cls in CLS_COMMONS:
        print(addon_name_version + ": Registering %s" % (cls))
        bpy.utils.register_class(cls)
    #end for cls in CLS_COMMONS:

    for cls in CLS_OPERATORS:
        print(addon_name_version + ": Registering %s" % (cls))
        bpy.utils.register_class(cls)
    #end for cls in CLS_OPERATORS:

    for cls in CLS_PANELS:
        print(addon_name_version + ": Registering %s" % (cls))
        bpy.utils.register_class(cls)
    #end for cls in CLS_PANELS:

    for cls in CLS_MENUS:
        print(addon_name_version + ": Registering %s" % (cls))
        bpy.utils.register_class(cls)
    #end for cls in CLS_MENUS:

    get_dynamic_class(config)
    print('dynamicClasses', dynamicClasses)
    for dyncls in dynamicClasses:
        print(addon_name_version + ": Registering %s" % (dyncls))
        bpy.utils.register_class(dyncls)
    #end for dyncls in reversed(dynamicClasses):

    bpy.types.IMAGE_MT_editor_menus.append(ASMainMenu.menu_draw)
    bpy.types.NODE_MT_editor_menus.append(ASMainMenu.menu_draw)
    bpy.types.VIEW3D_MT_editor_menus.append(ASMainMenu.menu_draw)
    bpy.types.SEQUENCER_MT_editor_menus.append(ASMainMenu.menu_draw)    
#end def register():

def unregister():
    bpy.types.SEQUENCER_MT_editor_menus.remove(ASMainMenu.menu_draw)    
    bpy.types.VIEW3D_MT_editor_menus.remove(ASMainMenu.menu_draw)
    bpy.types.NODE_MT_editor_menus.remove(ASMainMenu.menu_draw)
    bpy.types.IMAGE_MT_editor_menus.remove(ASMainMenu.menu_draw)

    for dyncls in reversed(dynamicClasses):
        print(addon_name_version + ": Unregistering %s" % (dyncls))
        bpy.utils.unregister_class(dyncls)
    #end for dyncls in reversed(dynamicClasses):

    for cls in reversed(CLS_MENUS):
        print(addon_name_version + ": Unregistering %s" % (cls))
        bpy.utils.unregister_class(cls)
    #end for cls in reversed(CLS_MENUS):

    for cls in reversed(CLS_PANELS):
        print(addon_name_version + ": Unregistering %s" % (cls))
        bpy.utils.unregister_class(cls)
    #end for cls in reversed(CLS_PANELS):

    for cls in reversed(CLS_OPERATORS):
        print(addon_name_version + ": Unregistering %s" % (cls))
        bpy.utils.unregister_class(cls)
    #end for cls in reversed(CLS_OPERATORS):

    for cls in reversed(CLS_COMMONS):
        print(addon_name_version + ": Unregistering %s" % (cls))
        bpy.utils.unregister_class(cls)
    #end for cls in reversed(CLS_COMMONS):

#end def unregister():

if __name__ == '__main__':
    register()
#end if __name__ == '__main__':
