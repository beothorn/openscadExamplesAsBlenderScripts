'''
Openscad Example002 converted to blender 2.67 python script

module example002()
{
	intersection() {
		difference() {
			union() {
				cube([30, 30, 30], center = true);
				translate([0, 0, -25])
					cube([15, 15, 50], center = true);
			}
			union() {
				cube([50, 10, 10], center = true);
				cube([10, 50, 10], center = true);
				cube([10, 10, 50], center = true);
			}
		}
		translate([0, 0, 5])
			cylinder(h = 50, r1 = 20, r2 = 5, center = true);
	}
}

example002();
'''

import bpy
import mathutils
from math import radians

def set_active(mesh_name):
	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects[mesh_name]
	bpy.data.objects[mesh_name].select = True

def apply_boolean_modifier(operation,mesh_names):
	first_mesh = mesh_names[0]
	resulting_mesh=first_mesh
	for other_mesh in mesh_names[1:]:
		resulting_mesh=boolean_modifier(first_mesh, other_mesh,operation)
	return resulting_mesh

def boolean_modifier(mesh1, mesh2, operation):
	print(mesh1+" "+operation+" "+mesh2)
	set_active(mesh1)
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[mesh2]
	bpy.context.object.modifiers["Boolean"].operation = operation
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
	set_active(mesh2)
	bpy.ops.object.delete()
	return mesh1

def difference(*mesh_names):
	return apply_boolean_modifier('DIFFERENCE',mesh_names)

def union(*mesh_names):
	return apply_boolean_modifier('UNION',mesh_names)

def intersection(*mesh_names):
	return apply_boolean_modifier('INTERSECT',mesh_names)

def rotate(obj_name,value,rotation_array):
	set_active(obj_name)
	bpy.ops.transform.rotate(value=value, axis=rotation_array)

def cone(h, r1, r2, position):
	bpy.ops.mesh.primitive_cone_add(radius1=r1, radius2=r2, depth=h, location=position)
	return bpy.context.object.name

def cube(dimensions=(100,100,100),position=(0,0,0)):
	bpy.ops.mesh.primitive_cube_add(location=position)
	bpy.ops.transform.resize(value=dimensions)
	return bpy.context.object.name

'''
intersection(\
	difference(\
		union(\
			cube(dimensions=(30,30,30),position=(0,0,-25)),\
			cube(dimensions=(15,15,50))\
		),\
		union(\
			 cube(dimensions=(50,10,10)),\
			 cube(dimensions=(10,50,10)),\
			 cube(dimensions=(10,10,50))\
		)\
	),\
	cone(50, 20, 5, (0,0,5))
)
'''

union(\
			 cube(dimensions=(50,10,10)),\
			 cube(dimensions=(10,50,10)),\
			 cube(dimensions=(10,10,50))\
)\


