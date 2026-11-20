from pathlib import Path
import ifcopenshell
import ifcopenshell.util.element as el
import ifcopenshell.util.geolocation as geo

ifc_path = Path(r"D:\Repo\geobim-ids-ifc-citygml3\z_non_thsis_trials\sample_runs\sample.ifc")

if not ifc_path.exists():
    raise FileNotFoundError(f"IFC file not found at: {ifc_path.resolve()}")

model = ifcopenshell.open(str(ifc_path))

print("=== IFC MODEL SUMMARY ===")
print("File:", ifc_path.name)
print("IFC Schema:", model.schema)
print("Total Walls (IfcWall):", len(model.by_type("IfcWall")))
print("Total Slabs (IfcSlab):", len(model.by_type("IfcSlab")))
print("Total Doors (IfcDoor):", len(model.by_type("IfcDoor")))
print("Total Spaces (IfcSpace):", len(model.by_type("IfcSpace")))

print("\n=== BUILDING STOREYS ===")
storeys = model.by_type("IfcBuildingStorey")
print("Storey count:", len(storeys))
for s in storeys:
    print(" -", s.Name or "(unnamed)", "| Elevation:", s.Elevation)

print("\n=== WALL PROPERTY CHECK (Pset_WallCommon.IsExternal) ===")
walls = model.by_type("IfcWall")
checked = 0
for w in walls[:5]:  # check the first 5 walls as a quick sample
    psets = el.get_psets(w)
    is_ext = psets.get("Pset_WallCommon", {}).get("IsExternal", None)
    print(f" - Wall [{w.GlobalId}] Name={w.Name!r} | IsExternal={is_ext}")
    checked += 1
if checked == 0:
    print(" - No IfcWall elements found.")

print("\n=== GEOREFERENCING CHECK ===")
try:
    map_conv = geo.get_map_conversion(model)
    crs = geo.get_projected_crs(model)
    print("Projected CRS:", crs)
    print("Map Conversion:", map_conv)
except Exception as e:
    print("Georeferencing info not found or incomplete:", e)