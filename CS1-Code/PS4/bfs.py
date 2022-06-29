# Author: Neo Cai
# Date: 03/09/22
# File Name: bfs.py
# Course: Computer Science 1
# Purpose: implements breadth first search given a start and a goal vertex


from load_graph import load_graph
from collections import deque

# load the dartmouth map graph
vertex_dict = load_graph("dartmouth_graph.txt")


# given a start and a goal vertex object, implements breadth first search to return a list of vertices to create a path
def bfs(start, goal):
    # create to_explore queue
    to_explore = deque([start])

    # create reached_from dictionary
    reached_from = {start: None}

    while len(reached_from) <= len(vertex_dict):

        current = to_explore.popleft()

        # if the goal is found
        if current == goal:
            # begin back tracing
            backtrace_list = [goal]

            while reached_from[current] is not None:
                backpointer = reached_from[current]
                backtrace_list.append(backpointer)
                current = backpointer

            backtrace_list.reverse()

            return backtrace_list

        # else if not, append adjacent vertices to those that need to be explored
        for vertex in current.adjacency_list:
            if vertex not in reached_from:
                to_explore.append(vertex)
                reached_from[vertex] = current
