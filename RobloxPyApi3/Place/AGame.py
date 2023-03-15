from Place import *
import CallMethods

place = Place("BaseplateExample")
place.init()

root = place.PlaceRoot
workspace = place.Workspace

# Create a Baseplate Part and add it to the Workspace
baseplate = place.AddInstance("Part", workspace)
baseplate.AddProperty("Name", CallMethods.DefaultPropertyTypes.string, "Baseplate")
baseplate.AddPropertyVector3("Size", Vector3(2048, 1, 2048))
baseplate.AddPropertyEnum("Material", Enum(["Enum.Material.Grass"]))
baseplate.AddProperty("Anchored", CallMethods.DefaultPropertyTypes.bool, True)
baseplate.AddProperty("Locked", CallMethods.DefaultPropertyTypes.bool, True)
baseplate.AddProperty("CanCollide", CallMethods.DefaultPropertyTypes.bool, True)

# Create a SpawnLocation object and add it to a new part
spawn_part = place.AddInstance("Part", workspace)
spawn_part.AddProperty("Name", CallMethods.DefaultPropertyTypes.string, "SpawnLocation")
spawn_location = place.AddInstance("SpawnLocation", spawn_part.GetInstance())
teleporter1 = place.AddInstance("Part", workspace)
teleporter1.AddProperty("Name", CallMethods.DefaultPropertyTypes.string, "Teleporter1")
teleporter1.AddPropertyVector3("Size", Vector3(4, 8, 4))
teleporter1.AddPropertyEnum("Material", Enum(["Enum.Material.Neon"]))
teleporter1.AddProperty("Anchored", CallMethods.DefaultPropertyTypes.bool, True)
teleporter1.AddProperty("Locked", CallMethods.DefaultPropertyTypes.bool, True)
teleporter1.AddProperty("CanCollide", CallMethods.DefaultPropertyTypes.bool, False)
teleporter1.AddProperty("TouchTransparency", CallMethods.DefaultPropertyTypes.number, 1)

teleporter2 = place.AddInstance("Part", workspace)
teleporter2.AddProperty("Name", CallMethods.DefaultPropertyTypes.string, "Teleporter2")
teleporter2.AddPropertyVector3("Size", Vector3(4, 8, 4))
teleporter2.AddPropertyEnum("Material", Enum(["Enum.Material.Neon"]))
teleporter2.AddProperty("Anchored", CallMethods.DefaultPropertyTypes.bool, True)
teleporter2.AddProperty("Locked", CallMethods.DefaultPropertyTypes.bool, True)
teleporter2.AddProperty("CanCollide", CallMethods.DefaultPropertyTypes.bool, False)
teleporter2.AddProperty("TouchTransparency", CallMethods.DefaultPropertyTypes.number, 1)

# Create scripts for the teleporters
teleport_script1 = place.AddScript(teleporter1.GetInstance(), "TeleportScript1" ,'''function onTouched(other)
        local humanoid = other.Parent:FindFirstChildOfClass("Humanoid")
        if humanoid then
            humanoid.RootPart.CFrame = game.Workspace.Teleporter2.CFrame + Vector3.new(0, 3, 0)
        end
    end
    script.Parent.Touched:Connect(onTouched)''')
teleport_script1.Enabled = True
teleport_script2 = place.AddScript(teleporter2.GetInstance(),"TeleportScript2",'''function onTouched(other)
        local humanoid = other.Parent:FindFirstChildOfClass("Humanoid")
        if humanoid then
            humanoid.RootPart.CFrame = game.Workspace.Teleporter1.CFrame + Vector3.new(0, 3, 0)
        end
    end
    script.Parent.Touched:Connect(onTouched)''')
# Save the Place to disk
place.Tree_Write()
place.Open_In_Studio()