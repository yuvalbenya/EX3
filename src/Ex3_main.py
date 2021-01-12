from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import random
import time
import networkx as nx
# random.random()*10
from GraphInterface import GraphInterface


def make_graph(node_size):
    # start = time.time()
    g = DiGraph()
    for i in range(node_size):
        g.add_node(i, (random.randint(0, node_size), random.randint(0, node_size), 0))

    x = 0
    for i in range(node_size * 2):
        x += 1
        if x == node_size:
            x = 0
        g.add_edge(x, random.randint(0, node_size), (random.random() * 100))

    ga = GraphAlgo(g)
    # ga.save_to_json("/Users/yuval/PycharmProjects/OOP_EX3/src/data/ofir")
    # ga.load_from_json("/Users/yuval/PycharmProjects/OOP_EX3/src/data/ofir")

    # end = time.time()
    # Time = end - start
    # print(Time)

    # ga.plot_graph()
    return g


def check():
    """
        This file represents a simple function name tester.
        Make sure you run this example to check your naming.
        ***** output: ******
        Graph: |V|=4 , |E|=5
        {0: 0: score inf, 1: 1: score inf, 2: 2: score inf, 3: 3: score inf}
        {0: 1}
        {0: 1.1, 2: 1.3, 3: 10}
        (3.4, [0, 1, 2, 3])
        [[0, 1], [2], [3]]
        (3.4, [0, 1, 2, 3])
        (inf, None)
        4.244296649514735 [1, 9, 10, 11, 7]
        20.546312400537253 [47, 46, 45, 44, 43, 42, 41, 40, 39, 15, 27, 26, 25, 17, 18, 19]
        18.197159401343114 [20, 21, 32, 31, 30, 29, 38, 14, 13, 12, 11, 9, 1, 0, 2]
        inf None
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
        """
    check0()
    check1()
    check2()


def checkME(graph: GraphAlgo):
    start = time.time()
    graph.connected_components()
    print("The time took for the Graph (GraphInterface) with ", len(graph.get_graph().get_all_v().keys()), "Nodes is: ",
          time.time() - start, "for connected_components")
    start = time.time()
    print(graph.shortest_path(0, 4))
    print("The time took for the Graph (GraphInterface) with ", len(graph.get_graph().get_all_v().keys()), "Nodes is: ",
          time.time() - start, "for shortestPath")


def checkNetworkX(graph: GraphInterface):
    G = nx.DiGraph()
    for i in graph.get_all_v().keys():
        G.add_node(i)
    for src in graph.get_all_v().keys():
        for dest, weight in graph.all_out_edges_of_node(i).items():
            G.add_edge(src, dest, weight=weight)

    start = time.time()
    nx.strongly_connected_components(G)
    print("The time took for the Graph (NetworkX) with ", len(graph.get_all_v().keys()), "Nodes is: ",
          time.time() - start, "for connected_components")
    start = time.time()
    nx.dijkstra_path(G=G, source=0, target=4)
    print("The time took for the Graph (NetworkX) with ", len(graph.get_all_v().keys()), "Nodes is: ",
          time.time() - start, "for shortestPath")


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g_algo = GraphAlgo(g)
    g_algo
    # print(g_algo.shortest_path(0, 3))
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    g_algo2 = GraphAlgo(GraphInterface)
    g_algo2.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs/G_30000_240000_0.json")
    s1 = time.time()
    print("time taken for ")
    print(time.time() - s1)
    """***********NetworkX***********"""
    nx.DiGraph
    # print(g)  # prints the __repr__ (func output)
    # print(g.get_all_v())  # prints a dict with all the graph's vertices.
    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(1))
    # g_algo = GraphAlgo(g)
    #  g_algo.load_from_json("../data/A1")
    # g_algo.save_to_json("/Users/yuval/Desktop/g1.txt")
    s = time.time()
    # print(g_algo2.connected_components())
    # print(g_algo2.connected_components())
    f = time.time() - s


#  print(f)
# print(g_algo.shortest_path(0, 3))
# g_algo.connected_components()
# g_algo.load_from_json("/Users/yuval/Desktop/g.txt")
# g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.connected_components())
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()


if __name__ == '__main__':
    # ****check 10/80
    g = GraphAlgo(GraphInterface)
    g.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs_on_circle/G_10_80_1.json")
    checkNetworkX(g.get_graph())
    checkME(g)
    # ****check 100/800
    g.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs_on_circle/G_100_800_1.json")
    checkNetworkX(g.get_graph())
    checkME(g)
    # ****check 1000/8000
    g.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs_on_circle/G_1000_8000_1.json")
    checkNetworkX(g.get_graph())
    checkME(g)
    # ****check 10000/80000
    g.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs_on_circle/G_10000_80000_1.json")
    checkNetworkX(g.get_graph())
    checkME(g)
    # ****check 20000/16000
    g.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs_on_circle/G_20000_160000_1.json")
    checkNetworkX(g.get_graph())
    checkME(g)
    # ****check 30000/240000
    g.load_from_json("/Users/Yuval/PycharmProjects/EX_3/Graphs_on_circle/G_30000_240000_1.json")
    checkNetworkX(g.get_graph())
    checkME(g)

