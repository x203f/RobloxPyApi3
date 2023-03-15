from Place import * # Imports the main package with every function without needing to type Place.Place.
import CallMethods # A helper file which got Enums of Call methods possible, like Color3.new, color3.fromRGB and more. It also got Default Property Types like number, string, bool.
place = Place("TestPlace") # Creates a place class which is an XML root that will be written inside TestPlace.rbxl.

place.init() #Initializate the place, adding workspace and StarterPlayer


root = place.PlaceRoot # place itself
workspace = place.Workspace # Place's Workspace
ServerScriptServive = place.AddService("ServerScriptService") # Adds ServerScriptService to the place, the only services that are made with initialization inside a place is Place.StarterPlayer, Place.StarterCharacterScripts, Place.StarterPlayerScripts and Place.Workspace. Other services you need to create throught this function (AddService).
# There is no GetStorage function, you need to create ReplicatedStorage with AddService.
script = place.AddScript(ServerScriptServive.GetService(),"MyServerScript","print('Hello from python')") # ServerScriptService variable is a ServerScriptService inside a place, ServerScriptService.GetService() will get XML content of ServerScriptService.
# "MyServerScript" is the name of the script, 'print('Hello from python')' is the scripts code.

Model = place.AddInstance("Model",place.Workspace) # Adding a model inside a workspace. place.workspace is the parent of Model
Model.AddProperty("Name",CallMethods.DefaultPropertyTypes.string,"MyModel") # Setting Name property to "MyModel"
# Name is a string. inside the CallMethods.DefaultPropertyTypes there are string, number and bool.
print(Model.InstanceContent) # prints the XML content of the model converted to string


part = place.AddInstance("Part",Model.GetInstance()) # Adding a part inside the Model, Model.GetInstance() Gets full Instance.
part.AddProperty("Name",CallMethods.DefaultPropertyTypes.string,'MyPartInsideModel') # setting up name
part.AddProperty("Anchored",CallMethods.DefaultPropertyTypes.bool,True) # Setting Bool property "Anchored" to true
part.AddPropertyVector3("Position",Vector3(213,13,532)) # Setting up Vector3 position of the part. THERE IS NO ENUM VECTOR3 INSIDE THE CallMethods.DefaultPropertyTypes . THERE IS ONLY BOOL, STRING, NUMBER.
# To set Vector3 Property use AddPropertyVector3 ONLY!
part.AddProperty("Transparency", CallMethods.DefaultPropertyTypes.number, 0.7) # Setting a number property of "Transparency" to 0.7
part.AddPropertyEnum("Material",Enum(["Enum","Material",'Wood']))
part.AddPropertyCFrame('CFrame',CFrame(1,1,4)) # A CFrame  property Setter. it will set Part.CFrame to 1,1,4. it will change the CFrame.

StarterGui = place.AddService("StarterGui")
ScreenGui = place.AddInstance("ScreenGui",StarterGui.GetService())
GUI = place.AddInstance("TextLabel",ScreenGui.GetInstance())
GUI.AddPropertyUDim2("Size",CallMethods.UDim2.new, UDim2(0.1,200,0.1,200)) # Setting the UI Size to UDIm2.new(0.1,200,0.1,200)
GUI.AddPropertyUDim2("Size",CallMethods.UDim2.fromscale,UDim2(xScale=1,YScale=1)) # Setting the UI size only using Scales, no offsets used.
GUI.AddPropertyUDim2("Size",CallMethods.UDim2.fromscale,UDim2(xOffset=200,YOffSet=1)) # Setting the UI size only using offsets, no scales used.
part.AddHexPropertyColor3("Color",'FF0000') # Setting color3 Property "Color" to FF0000 (Red)

print(part.Parent) # Gets the parented part of the Instance.

# Instead of AddHexPropertyColor3 You can use:  part.AddPropertyColor3(CallMethod:CallMethod.Color3 (Enum) ,FullPropertyName:string,Value:Color3(Value1:Number,Value2:Number,Value3:Number)



# Example: part.AddPropertyColor3(CallMethods.Color3.fromRGB,"Color",Color3(255,255,255)) # This is going to be in lua:


# part.Color = Color3.fromRGB(255,255,255) .
print(part.InstanceContent) # prints the XML content formatted to string of part


part2 = place.AddInstance("Part",Model.GetInstance()) # Adding a part inside the Model, Model.GetInstance() Gets full Instance.
part2.AddProperty("Name",CallMethods.DefaultPropertyTypes.string,'MyPartInsideModel') # setting up name
part2.AddProperty("Anchored",CallMethods.DefaultPropertyTypes.bool,True) # Setting Bool property "Anchored" to true
part2.AddPropertyMultipleValues("CFrame","CFrame.new(291,210,3) * 29 + CFrame.new(1,1,1)") # Putting complicated values like CFrame. This is useful for calculations.
part2.AddProperty("Transparency", CallMethods.DefaultPropertyTypes.number, 0.7) # Setting a number property of "Transparency" to 0.7
part2.AddPropertyBrickColor("BrickColor",CallMethods.BrickColor.new,BrickColor("White")) # A basic BrickColor. The call method is BrickColor.new
part2.AddPropertyBrickColor_shorthand("BrickColor",CallMethods.BrickColor_Shorthanded.Red) # The brickColor version of this is just like BrickColor.Red(), its shorthanded! This function is allowing Brickcolor functions where you dont need to pass any arguments like brickcolor.random() or brickcolor.blue.
script2 = place.AddLocalScript(place.StarterPlayerScripts,"StarterPlayerLol","""
print("YO BROOO")
""") # Same thing as AddScript, here the parent is StarterPlayerScripts of the place.
script2.Disabled = False # The property 'Disabled' in LocalScript is False. Property 'Enabled' is in Script only.
# REMEMBER, PropertyType like Color and BrickColor, Color is a Color3 Property so USE ONLY COLOR3 PROPERTY, BRICKCOLOR PROPERTY IS A BRICKCOLOR PROPERTY, SO USE BRICKCOLOR SETTERS. DONT USE Color3 PROPERTY on BrickColor, Dont use BrickColor on Color3 property.
print(place.PlaceContent) # Printing out full XML place content converted to string
place.Tree_Write() # Writing the rbxl file

place.Open_In_Studio() # Opening session of Roblox studio with the project.
# Here are the indexes of CallMethods:
"""
UDim2:

    new = 0
    fromscale = 1
    fromoffset = 2
Color3:
    new = 0
    fromRGB = 1
    fromHex = 2
    fromHSV = 3
DefaultPropertyTypes:
    string = 0
    number = 1
    bool = 2
BrickColor:
    new = 0

    Palette = 10
BrickColor_Shorthanded:
    Random = 1
    Red = 2
    White = 3
    Gray = 4
    DarkGray = 5
    Black = 6
    Yellow = 7
    Green = 8
    Blue = 9

"""
#Property Setters:

"""
AddProperty - Only bool, string, number properties
AddPropertyVector3 - Vector3 setter
AddPropertyBrickColor_shortHanded - CallMethods.BrickColor_Shorthanded. Only void functions were you dont need any arguments in brickcolor.
AddPropertyBrickColor - BrickColor setter, can be an ID and a brickcolor Name.
AddPropertyColor3 - Color3 setter
AddPropertyVector2 - Vector2 setter.
AddPropertyEnum - EnumItem setter
AddPropertyCFrame - CFrame setter
AddPropertyUDim2 - UDim2 setter.
"""