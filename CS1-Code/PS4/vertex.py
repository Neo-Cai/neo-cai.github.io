# Author: Neo Cai
# Date: 03/06/22
# File Name: vertex.py
# Course: Computer Science 1
# Purpose: creates a Vertex class that for vertex objects

from cs1lib import *

# initialize variables for the vertices
STROKE_WIDTH = 5
VERTEX_RADIUS = 10


class Vertex:

    # given name, adjacency_list, x, and y, initializes variables
    def __init__(self, name, adjacency_list, x, y):
        self.name = name
        self.x = int(x.strip())
        self.y = int(y.strip())
        self.adjacency_list = adjacency_list

    # creates a string output for the vertex objects that gives name, location, and adjacent vertices
    def __str__(self):
        adj_string = ""

        if self.adjacency_list:
            for i in range(len(self.adjacency_list) - 1):
                adj_string += self.adjacency_list[i].name + ", "

            adj_string += self.adjacency_list[len(self.adjacency_list) - 1].name

        return str(self.name) + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " \
               + str(adj_string)

    # given, r, g, b draws a vertex
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # given another vertex, r, g, and b draws a line between the vertex
    def draw_edge(self, other_vertex, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(STROKE_WIDTH)
        draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

    # given r, g, and b draws all edges between vertex and all vertices in adjacency list
    def draw_adjacent_edges(self, r, g, b):
        for adj_vertex in self.adjacency_list:
            self.draw_edge(adj_vertex, r, g, b)

    # given x and y coordinates, determines if the mouse is over the vertex
    def is_under(self, x, y):
        if (self.x - VERTEX_RADIUS) < x < (self.x + VERTEX_RADIUS) and \
                (self.y - VERTEX_RADIUS) < y < (self.y + VERTEX_RADIUS):
            return True

        else:
            return False

