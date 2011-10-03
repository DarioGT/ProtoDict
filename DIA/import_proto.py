# Modulo para la importacion de diagramas en DIA 
# "/ToolboxMenu/Help/HelpExtensionStart", newModel


import sys, math, dia, types, string

def distribute_objects (objs) :
    width = 0.0
    height = 0.0


    # Si los objetos no son conectores, o hacerlo antes de los conectores  ( UML association )  
    for o in objs :
        if o.type.name == "UML - Class" :
            if width < o.properties["elem_width"].value : width = o.properties["elem_width"].value
            if height < o.properties["elem_height"].value : height = o.properties["elem_height"].value
        
        
    # add 20% 'distance'
    width *= 2
    height *= 2
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


# Creacion un diagrama  ( model ) 
def newDiagram(modelName ) :
    
#   diagram = dia.active_display().diagram

    diagram = dia.new( modelName)
    data = diagram.data
#   layer = data.active_layer
    display = diagram.display()
        
    return data


# Creacion de Objetos 
def newObject(oName, data ) :

    oType = dia.get_object_type("UML - Class")        
    layer = data.active_layer

    o, h1, h2 = oType.create (0,0) # p.x, p.y
    layer.add_object (o)
    o.properties["name"] = oName 

    return o 

def newAssociation(oName, data ) :

    oType = dia.get_object_type("UML - Association")        
    layer = data.active_layer
    
    o, h1, h2 = oType.create (0,0) # p.x, p.y
    layer.add_object (o)
    o.properties["name"] = oName 

    return o 



# * * * * * * *  * * * * * * *  * *   
def newModel(self ) :

    modelName = "Nuevo1"
    data = newDiagram( modelName )
    o1 = newObject ( "O1", data )
    o2 = newObject ( "O1", data )

    l1 = newAssociation( "L1", data ) 


    layer = data.active_layer
    distribute_objects (layer.objects)
    
dia.register_action ("ImportProto", "Import Proto", "/ToolboxMenu/Help/HelpExtensionStart", newModel)




o.properties["name"] = pname
o.properties["template"] = 1
o.properties["templates"] = [(p.type, '')]

# coloring depending on use
o.properties["fill_colour"] = "lightblue"
o.properties["fill_colour"] = "lightcyan"
o.properties["fill_colour"] = "lightgreen"
o.properties["fill_colour"] = "lightyellow"


o.properties["comment"] = names[0]
o.properties["visible_comments"] = 1
o.properties["comment_line_length"] = 60

# store position for next in row
# x += (dx + o.properties["elem_width"].value)
# grid[p.type] = (x,y)
