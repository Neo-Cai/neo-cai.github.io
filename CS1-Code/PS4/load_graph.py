# Author: Neo Cai
# Date: 03/06/22
# File Name: load_graph.py
# Course: Computer Science 1
# Purpose: loads a graph of vertexes for campus locations

from vertex import Vertex


# helper function: given a line, parses the line and isolates variables (name, adjacency_list, coordinates)
def parse_line(line):
    section_split = line.split(";")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    coordinates = section_split[2].strip().split(",")

    return vertex_name, adjacent, coordinates[0], coordinates[1]


# given a file, returns a dictionary of vertices where the key is the name and value is the vertex object
def load_graph(filename):
    vertex_dict = {}

    file = open(filename, "r")

    # first pass to just get the name and coordinates of vertexes
    for l in file:

        if len(l.split(";")) == 3:
            vertex_name, adjacent_vertices, x, y = parse_line(l)
            vertex_dict[vertex_name] = Vertex(vertex_name, [], x, y)

    file.close()

    file = open(filename, "r")

    # second pass creates adjacency list based on the vertices created in the first pass
    for l in file:

        if len(l.split(";")) == 3:
            vertex_name, adjacent_vertices, x, y = parse_line(l)
            adjacent_vertices_list = []

            for a in adjacent_vertices:
                adjacent_vertices_list.append(vertex_dict[a])

            vertex_dict[vertex_name].adjacency_list = adjacent_vertices_list

    file.close()

    return vertex_dict
