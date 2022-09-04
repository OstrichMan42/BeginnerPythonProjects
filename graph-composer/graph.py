
"""
Empty Graph Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {} # dictionary of edges to wieght
        self.neighbors = []
        self.neighborWeights = []
        

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
                self.neighbors.append(vertex)
                self.neighborWeights.append(weight)

    def next_word(self):
        # pick random adjacent neighbor, favoring weighted edges
        return random.choices(self.neighbors, weights=self.neighborWeights)[0]
        


# put verticies in a graph
class Graph(object):
    def __init__(self):
        # map of string to vertex
        self.verticies = {}

    def get_vertex_values(self):
        # values of all verticies
        return set(self.verticies.keys())

    def add_vertex(self, value):
        self.verticies[value] = Vertex(value)

    def get_vertex(self, value):
        # create node if none exists
        if value not in self.verticies:
            self.add_vertex(value)
        return self.verticies[value]

    def get_next_word(self, current_vertex):
        return self.verticies[current_vertex].next_word()

    def generate_probability_mappings(self):
        for vertex in self.verticies.values():
            vertex.get_probability_map()
