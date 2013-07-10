
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

def setActive(meshName):
	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects[meshName]
	bpy.data.objects[meshName].select = True

def difference(*meshNames):
	first = meshNames[0]
	for other in meshNames[1:]:
		differenceOfTwo(first, other)

def differenceOfTwo(mesh1, mesh2):
	setActive(mesh1)
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[mesh2]
	bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
	setActive(mesh2)
	bpy.ops.object.delete()	

def rotate(objName,value,rotationArray):
	setActive(objName)
	bpy.ops.transform.rotate(value=value, axis=rotationArray)

def sphere(r):
	bpy.ops.mesh.primitive_uv_sphere_add(size=r)
	return bpy.context.object.name

def cylinder(r,h):
	bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h)
	return bpy.context.object.name

def r_from_dia(d):
	return d/2

def rotcy(rot,r,h):
	newcylinder=cylinder(r,h)
	rotate(newcylinder,radians(90.0),rot)
	return newcylinder

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

