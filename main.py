#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/16/2023
# @Author  : Ehwartz
# @Github  : https://github.com/Ehwartz
# @Software: PyCharm
# @File    : main.py

from graph import Graph, init_graph
from graph import BFS, DFS, UCS, GBFS, Astar


def main():
    # BFS
    print('-----------------------------------------------------------------------------------------------------------')
    print('BFS')
    graph = init_graph()

    bfs = BFS(graph=graph)
    routine = bfs.search('Arad', 'Bucharest')
    print('\nroutine: ', [node.name for node in routine], '\n')

    # DFS
    print('-----------------------------------------------------------------------------------------------------------')
    print('DFS')
    graph = init_graph()
    dfs = DFS(graph=graph)
    routine = dfs.search('Arad', 'Bucharest')
    print('\nroutine: ', [node.name for node in routine], '\n')

    # UCS
    print('-----------------------------------------------------------------------------------------------------------')
    print('UCS')
    graph = init_graph()
    ucs = UCS(graph=graph)
    routine = ucs.search('Arad', 'Bucharest')
    print('\nroutine: ', [node.name for node in routine], '\n')

    # GBFS
    print('-----------------------------------------------------------------------------------------------------------')
    print('GBFS')
    graph = init_graph()
    straight_line_dists = [366, 0, 160, 242, 161, 178, 77, 151, 226, 244,
                           241, 234, 380, 98, 193, 253, 329, 80, 199, 374]

    gbfs = GBFS(graph=graph, straight_line_dists=straight_line_dists)
    routine = gbfs.search('Arad', 'Bucharest')
    print('\nroutine: ', [node.name for node in routine], '\n')

    # A*
    print('-----------------------------------------------------------------------------------------------------------')
    print('A* Search')
    graph = init_graph()
    straight_line_dists = [366, 0, 160, 242, 161, 178, 77, 151, 226, 244,
                           241, 234, 380, 98, 193, 253, 329, 80, 199, 374]
    astar = Astar(graph=graph, straight_line_dists=straight_line_dists)
    routine = astar.search('Arad', 'Bucharest')
    print('\nroutine: ', [node.name for node in routine], '\n')

    print('-----------------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    main()
