# Modulo para la importacion de diagramas en DIA 

import sys, math, dia, types, string

def distribute_objects (objs) :
    width = 0.0
    height = 0.0


    # Si los objetos no son conectores, o hacerlo antes de los conectores  ( UML association )  
    for o in objs :
        if width < o.properties["elem_width"].value : width = o.properties["elem_width"].value
        if height < o.properties["elem_height"].value : height = o.properties["elem_height"].value
        
        
    # add 20% 'distance'
    width *= 1.2
    height *= 1.2
    area = len (objs) * width * height
    max_width = math.sqrt (area)
    x = 0.0
    y = 0.0
    dy = 0.0 # used to pack small objects more tightly
    for o in objs :
        if dy + o.properties["elem_height"].value * 1.2 > height :
            x += width
            dy = 0.0
        if x > max_width :
            x = 0.0
            y += height
        o.move (x, y + dy)
        dy += (o.properties["elem_height"].value * 1.2)
        if dy > .75 * height :
            x += width
            dy = 0.0
        if x > max_width :
            x = 0.0
            y += height


# Creacion del modelo leido del XML 
def newModel(data, flags) :
    
    # Lectura XML 
      
    modelName = "Nuevo 1"
    
    
    # Creacion del diagrama ( Mdeolo ) 
    if not data : # not set when called by the toolbox menu
        diagram = dia.new( modelName)
        # passed in data is not necessary valid - we are called from the Toolbox menu
        data = diagram.data
        display = diagram.display()
    else :
        diagram = None
        display = None
    layer = data.active_layer


dia.register_action ("ImportProto", "Import Proto", 
                       "/ToolboxMenu/Help/HelpExtensionStart", 
                       newModel)


