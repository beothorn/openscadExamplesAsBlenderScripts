
'''
Openscad Example001 converted to blender 2.67 python script

module example001()
{
	function r_from_dia(d) = d / 2;

	module rotcy(rot, r, h) {
		rotate(90, rot)
			cylinder(r = r, h = h, center = true);
	}

	difference() {
		sphere(r = r_from_dia(size));
		rotcy([0, 0, 0], cy_r, cy_h);
		rotcy([1, 0, 0], cy_r, cy_h);
		rotcy([0, 1, 0], cy_r, cy_h);
	}

	size = 50;
	hole = 25;

	cy_r = r_from_dia(hole);
	cy_h = r_from_dia(size * 2.5);
}

example001();
'''

import bpy
import mathutils
from math import radians

def set_active(mesh_name):
	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects[mesh_name]
	bpy.data.objects[mesh_name].select = True

def difference(*mesh_names):
	first_mesh = mesh_names[0]
	for other_mesh in mesh_names[1:]:
		difference_of_two(first_mesh, other_mesh)

def difference_of_two(mesh1, mesh2):
	set_active(mesh1)
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[mesh2]
	bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
	set_active(mesh2)
	bpy.ops.object.delete()	

def rotate(obj_name,value,rotation_array):
	set_active(obj_name)
	bpy.ops.transform.rotate(value=value, axis=rotation_array)

def sphere(r):
	bpy.ops.mesh.primitive_uv_sphere_add(size=r)
	return bpy.context.object.name

def cylinder(r,h):
	bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h)
	return bpy.context.object.name

def r_from_dia(d):
	return d/2

def rotcy(rot,r,h):
	new_cylinder=cylinder(r,h)
	rotate(new_cylinder,radians(90.0),rot)
	return new_cylinder

size = 50
hole = 25

cy_r = r_from_dia(hole)
cy_h = r_from_dia(size * 2.5)

difference(\
	sphere(r_from_dia(size)),\
	rotcy((0,0,0),cy_r,cy_h),\
	rotcy((1,0,0),cy_r,cy_h),\
	rotcy((0,1,0),cy_r,cy_h)\
)

