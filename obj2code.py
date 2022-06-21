#!/usr/bin/env python

import sys

class Vertex:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class Face:
	def __init__(self, one, two, three):
		self.one   = one
		self.two   = two
		self.three = three

def only_relevant_lines(text):
	rlines = []

	lines = text.splitlines()
	for line in lines:
		if line[0] == 'v' or line[0] == 'f':
			rlines.append(line)
	return rlines

def parse_vertices(relevant_lines):
	vertices = []

	for line in relevant_lines:
		if not line[0] == 'v':
			continue
		tmp = line.split(' ')
		x = round(float(tmp[1]), 3)
		y = round(float(tmp[2]), 3)
		z = round(float(tmp[3]), 3)

		if x == -0.0:
			x = 0.0
		if y == -0.0:
			y = 0.0
		if z == -0.0:
			z = 0.0

		vertex = Vertex(x, y, z)
		vertices.append(vertex)
	return vertices

def parse_faces(relevant_lines):
	faces = []

	for line in relevant_lines:
		if not line[0] == 'f':
			continue
		tmp = line.split(' ')
		face = Face(int(tmp[1]) - 1, int(tmp[2]) - 1, int(tmp[3]) - 1)
		faces.append(face)
	return faces

def print_vertices(vertices):
	print("static const rdVertex modelModelVertices[] = {")

	for vertex in vertices:
		xSpace = ""
		ySpace = ""
		zSpace = ""

		if vertex.x >= 0.0:
			xSpace = " "
		if vertex.y >= 0.0:
			ySpace = " "
		if vertex.z >= 0.0:
			zSpace = " "
		f = "	{{{:s}{:.3f}f,{:s}{:.3f}f,{:s}{:.3f}f }},".format(xSpace, vertex.x, ySpace, vertex.y, zSpace, vertex.z)
		print(f)
	print("};")
	return

def print_faces(faces):
	print("static const rdIndex modelModelIndices[] = {")
	for face in faces:
		f = "	{:d}, {:d}, {:d},".format(face.one, face.two, face.three)
		print(f)
	print("};")

def main():
	vertices = None
	faces    = None

	if len(sys.argv) < 2:
		print("Need .obj filename")
		return
	file = open(sys.argv[1], 'r')
	text = file.read()
	relevant_lines = only_relevant_lines(text)
	vertices = parse_vertices(relevant_lines)
	faces = parse_faces(relevant_lines)

	print_vertices(vertices)
	print_faces(faces)

if __name__ == "__main__":
	main()
