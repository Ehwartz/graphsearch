#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/2023
# @Author  : Ehwartz
# @Github  : https://github.com/Ehwartz
# @Software: PyCharm
# @File    : graph.py

import numpy as np


class Node(object):
    def __init__(self, name: str):
        """

        :param name:
        """
        self.name = name
        self.neibs = []
        self.parent = None
        self.children = None

    def add_neibs(self, neibs: list):
        """

        :param neibs: list of dicts  {neib: dist}
        """
        self.neibs = neibs
        return self


class Graph(object):
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.n = len(nodes)
        self.nodes_dict = {}
        self.node_names = []
        for i in range(self.n):
            self.nodes_dict[self.nodes[i].name] = self.nodes[i]
            self.node_names.append(nodes[i].name)
        self.adjMatrix = -np.ones(shape=[self.n, self.n])
        for i in range(self.n):
            for neib in self.nodes[i].neibs:
                node, dist = neib
                j = self.node_names.index(node.name)
                self.adjMatrix[i][j] = dist

    def find_node(self, name):
        return self.nodes_dict.get(name)


class BFS(object):
    def __init__(self, graph: Graph):
        self.graph = graph
        self.queue = []
        self.n = graph.n
        self.node_names = graph.node_names
        self.visited = np.zeros(shape=[self.n])
        self.visited_nodes = []

    def search(self, start, dest):
        self.queue.clear()
        for node in self.graph.nodes:
            node.parent = None

        start_node = self.graph.find_node(start)

        if start_node.name == dest:
            return start_node
        i = self.node_names.index(start_node.name)
        self.visited[i] = 1
        self.queue.append(start_node)
        self.visited_nodes.append(start_node)
        self.print_quere()

        state = self.step(dest)
        self.print_quere()
        while not state:
            state = self.step(dest)
            self.print_quere()
        routine = []
        rev = state
        routine.append(rev)
        while rev.parent:
            routine.append(rev.parent)
            rev = rev.parent
        routine.reverse()
        return routine

    def step(self, dest):
        for neib in self.queue[0].neibs:
            node, dist = neib
            i = self.node_names.index(node.name)
            if self.visited[i]:
                continue
            node.parent = self.queue[0]
            self.visited[i] = 1
            self.visited_nodes.append(node)
            self.queue.append(node)
            if node.name == dest:
                return node

        self.queue.pop(0)

    def print_quere(self):
        print([node.name for node in self.queue])


class DFS(object):
    def __init__(self, graph: Graph):
        self.graph = graph
        self.stack = []
        self.n = graph.n
        self.node_names = graph.node_names
        self.visited = np.zeros(shape=[self.n])
        self.visited_nodes = []
        self.search_tree = None
        self.state = None

    def search(self, start, dest):
        self.stack.clear()
        for node in self.graph.nodes:
            node.parent = None

        start_node = self.graph.find_node(start)
        self.search_tree = Node(name=start)
        self.state = start_node

        if start_node.name == dest:
            return start_node
        i = self.node_names.index(start_node.name)
        self.visited[i] = 1
        self.stack.append(start_node)
        self.visited_nodes.append(start_node)
        self.print_quere()

        state = self.step(dest)
        self.print_quere()
        while not state:
            state = self.step(dest)
            self.print_quere()
        routine = []
        rev = state
        routine.append(rev)
        while rev.parent:
            routine.append(rev.parent)
            rev = rev.parent
        routine.reverse()
        return routine

    def step(self, dest):
        node_pop = self.stack.pop()
        for neib in node_pop.neibs:
            node, dist = neib
            i = self.node_names.index(node.name)
            if self.visited[i]:
                continue
            node.parent = node_pop
            self.visited[i] = 1
            self.visited_nodes.append(node)
            self.stack.append(node)
            if node.name == dest:
                return node

    def print_quere(self):
        print([node.name for node in self.stack])


class UCS(object):
    def __init__(self, graph: Graph):
        self.graph = graph
        self.queue = []
        self.costs = []
        self.n = graph.n
        self.node_names = graph.node_names
        self.visited = np.zeros(shape=[self.n])
        self.visited_nodes = []

    def search(self, start, dest):
        self.queue.clear()
        for node in self.graph.nodes:
            node.parent = None
        start_node = self.graph.find_node(start)

        if start_node.name == dest:
            return start_node
        i = self.node_names.index(start_node.name)
        self.visited[i] = 1
        self.queue.append(start_node)
        self.costs.append(0)
        self.visited_nodes.append(start_node)
        self.print_quere()
        print(self.costs)

        state = self.step(dest)
        self.print_quere()
        print(self.costs)

        while not state:
            state = self.step(dest)
            self.print_quere()
            print(self.costs)
        routine = []
        rev = state
        routine.append(rev)
        while rev.parent:
            routine.append(rev.parent)
            rev = rev.parent
        routine.reverse()
        return routine

    def step(self, dest):
        cost_min = min(self.costs)
        i_min = self.costs.index(cost_min)
        for neib in self.queue[i_min].neibs:
            node, dist = neib
            i = self.node_names.index(node.name)
            if self.visited[i]:
                continue
            node.parent = self.queue[i_min]
            self.visited[i] = 1
            self.visited_nodes.append(node)
            self.queue.append(node)
            self.costs.append(cost_min + dist)
            if node.name == dest:
                return node

        self.queue.pop(i_min)
        self.costs.pop(i_min)

    def print_quere(self):
        print([node.name for node in self.queue])


class GBFS(object):
    def __init__(self, graph: Graph, straight_line_dists):
        self.graph = graph
        self.straight_line_dists = straight_line_dists
        self.queue = []
        self.dists = []
        self.n = graph.n
        self.node_names = graph.node_names
        self.visited = np.zeros(shape=[self.n])
        self.visited_nodes = []

    def search(self, start, dest):
        self.queue.clear()
        for node in self.graph.nodes:
            node.parent = None
        start_node = self.graph.find_node(start)

        if start_node.name == dest:
            return start_node
        i = self.node_names.index(start_node.name)
        self.queue.append(start_node)
        self.dists.append(self.straight_line_dists[i])
        self.visited_nodes.append(start_node)
        self.print_quere()
        print(self.dists)

        state = self.step(dest)
        self.print_quere()
        print(self.dists)

        while not state:
            state = self.step(dest)
            self.print_quere()
            print(self.dists)
        routine = []
        rev = state
        routine.append(rev)
        while rev.parent and rev.name != start:
            routine.append(rev.parent)
            rev = rev.parent
        routine.reverse()
        return routine

    def step(self, dest):
        dist_min = min(self.dists)
        i_min = self.dists.index(dist_min)
        for neib in self.queue[i_min].neibs:
            node, dist = neib
            i = self.node_names.index(node.name)
            node.parent = self.queue[i_min]
            # self.visited[i] = 1
            self.visited_nodes.append(node)
            self.queue.append(node)
            self.dists.append(self.straight_line_dists[i])
            if node.name == dest:
                return node

        self.queue.pop(i_min)
        self.dists.pop(i_min)

    def print_quere(self):
        print([node.name for node in self.queue])


class Astar(object):
    def __init__(self, graph: Graph, straight_line_dists):
        self.graph = graph
        self.straight_line_dists = straight_line_dists
        self.queue = []
        self.costs = []
        self.n = graph.n
        self.node_names = graph.node_names
        self.visited = np.zeros(shape=[self.n])
        self.visited_nodes = []

    def search(self, start, dest):
        self.queue.clear()
        for node in self.graph.nodes:
            node.parent = None
        start_node = self.graph.find_node(start)

        if start_node.name == dest:
            return start_node
        i = self.node_names.index(start_node.name)
        self.queue.append(start_node)
        self.costs.append(self.straight_line_dists[i])
        self.visited_nodes.append(start_node)
        self.print_quere()
        print(self.costs)

        state = self.step(dest)
        self.print_quere()
        print(self.costs)

        while not state:
            state = self.step(dest)
            self.print_quere()
            print(self.costs)
        print([node.name for node in self.visited_nodes])
        routine = []
        routine_name = []
        rev = state
        routine.append(rev)
        routine_name.append(rev.name)
        while rev.parent and rev.name != start:
            routine.append(rev.parent)
            rev = rev.parent
        routine.reverse()
        return routine

    def step(self, dest):
        cost_min = min(self.costs)
        i_min = self.costs.index(cost_min)
        for neib in self.queue[i_min].neibs:
            node, dist = neib
            i = self.node_names.index(node.name)
            if self.queue[i_min].parent:
                if self.queue[i_min].parent.name == node.name:
                    continue
            node.parent = self.queue[i_min]
            # self.visited[i] = 1
            self.visited_nodes.append(node)
            self.queue.append(node)
            self.costs.append(self.straight_line_dists[i] + dist)
            if node.name == dest:
                return node

        self.queue.pop(i_min)
        self.costs.pop(i_min)

    def print_quere(self):
        print([node.name for node in self.queue])


def init_graph():
    names = ['Arad', 'Bucharest', 'Craiova', 'Dobreta',
             'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova',
             'Iasi', 'Lugoj', 'Mehadia', 'Neamt',
             'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu',
             'Timisoara', 'Urziceni', 'Vaslui', 'Zerind']
    neibsl = [[('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
              [('Fagaras', 211), ('Giurgiu', 90), ('Pitesti', 101), ('Urziceni', 85)],
              [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
              [('Craiova', 120), ('Mehadia', 75)],
              [('Hirsova', 86)],
              [('Bucharest', 211), ('Sibiu', 99)],
              [('Bucharest', 90)],
              [('Eforie', 86), ('Urziceni', 98)],
              [('Neamt', 87), ('Vaslui', 92)],
              [('Mehadia', 70), ('Timisoara', 111)],
              [('Dobreta', 75), ('Lugoj', 70)],
              [('Iasi', 87)],
              [('Sibiu', 151), ('Zerind', 71)],
              [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vilcea', 97)],
              [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)],
              [('Arad', 140), ('Fagaras', 99), ('Oradea', 151), ('Rimnicu Vilcea', 80)],
              [('Arad', 118), ('Lugoj', 111)],
              [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
              [('Iasi', 92), ('Urziceni', 142)],
              [('Arad', 75), ('Oradea', 71)]]

    nodes = []
    for name in names:
        nodes.append(Node(name=name))
    for i, node in enumerate(nodes):
        for neib in neibsl[i]:
            name, dist = neib
            for node_ in nodes:
                if node_.name == name:
                    node.neibs.append((node_, dist))
    return Graph(nodes=nodes)


