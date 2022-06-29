# Author: Neo Cai
# Date: 03/09/22
# File Name: map_plot.py
# Course: Computer Science 1
# Purpose: runs a map that uses breadth first search to determine a path from a start to a goal

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

# initializing global variables
WINDOW_X = 1012
WINDOW_Y = 811

# initialize booleans for things that need to be drawn
image_drawn = False
map_drawn = False
path_complete = True


# load image and graph
vertex_dict = load_graph("dartmouth_graph.txt")
map = load_image("dartmouth_map.png")

# initialize start and goal vertices
start = None
goal = None


# given mouse location, determined if start is selected
def my_mpressed(mx, my):
    global start, map_drawn

    for a_vertex in vertex_dict.values():

        if a_vertex.is_under(mx, my):
            start = a_vertex
            a_vertex.draw_vertex(1, 0, 0)

        else:
            map_drawn = 0


# given mouse location, determine where the goal vertex is
def my_mlocation(mx, my):
    global goal

    for a_vertex in vertex_dict.values():

        if start is not None and a_vertex.is_under(mx, my):
            goal = a_vertex


# runs the breath first search function to figure out the best path
def run_bfs():
    global map_drawn, path_complete

    if start is not None and goal is not None:

        current_path = bfs(start, goal)

        if path_complete:
            map_drawn = False
            path_complete = False

        if not path_complete:
            old_vertex = start

            for a_vertex in current_path[1:]:
                a_vertex.draw_vertex(1, 0, 0)
                a_vertex.draw_edge(old_vertex, 1, 0, 0)
                old_vertex = a_vertex

            path_complete = True


# draws the map of vertices and edges
def draw_map():
    for vertex in vertex_dict.values():
        vertex.draw_vertex(0, 0, 1)
        vertex.draw_adjacent_edges(0, 0, 1)

        if start is not None:
            start.draw_vertex(1, 0, 0)


# runs the map and its features
def run_map():
    global image_drawn, map_drawn

    if not image_drawn:
        draw_image(map, 0, 0)
        image_drawn = True

    if not map_drawn:
        draw_map()
        map_drawn = True

    run_bfs()


start_graphics(run_map, mouse_move=my_mlocation, mouse_press=my_mpressed, width=WINDOW_X, height=WINDOW_Y)
