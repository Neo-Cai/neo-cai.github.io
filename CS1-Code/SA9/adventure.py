# Author: Neo Cai
# Date: 03/04/22
# File Name: adventure.py
# Course: Computer Science 1
# Purpose: runs a chose your own adventure story!


# create a Vertex class to make vertex objects that take an adjacency list and some data
class Vertex:
    def __init__(self, data, adjacency_list):
        self.data = data
        self.adjacency_list = adjacency_list


# given a line, parses through it and assigns variables
def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


# given a file containing a story, loads the story into a story dictionary
def load_story(filename):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

        # YOU WRITE THIS PART
        vertex_dict[vertex_name] = Vertex(text, adjacent_vertices)

    file.close()

    return vertex_dict


# given a story_dictionary, run the adventure through each vertex
def run_story(story_dictionary):
    vertex = "START"
    while story_dictionary[vertex].adjacency_list:
        # checks if input is valid
        try:
            next_step = ord(input(story_dictionary[vertex].data + "\n" + "--> "))
            vertex = (story_dictionary[vertex].adjacency_list[next_step - 97])

        except Exception:
            print("error, this input is not valid, try again")

    print(story_dictionary[vertex].data)


# run the adventure
story_dict = load_story("story.txt")
run_story(story_dict)
