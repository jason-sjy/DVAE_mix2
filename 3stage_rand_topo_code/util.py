import gzip
import pickle
import numpy as np
import torch
from torch import nn
import random
from tqdm import tqdm
import os
import subprocess
import collections
import igraph
import argparse
import pdb
import pygraphviz as pgv
import sys
from PIL import Image

# create a parser to save graph arguments
cmd_opt = argparse.ArgumentParser()
graph_args, _ = cmd_opt.parse_known_args()

'''gobal variables'''
# CIRCUIT_NODE_TYPE = 9

'''dataset generation'''


def clamp(minn, maxn, n):
    return max(min(maxn, n), minn)


'''Data preprocessing'''


def one_hot(idx, length):
    idx = torch.LongTensor([idx]).unsqueeze(0)
    x = torch.zeros((1, length)).scatter_(1, idx, 1)
    return x


def load_circuit_graphs(topo_num, sizing_num, rand_seed=0):
    # load DAG format CIRCUITs to igraphs
    g_list = []
    max_n = 16
    num_node_feature = 16
    # max_n = 5  # maximum number of nodes
    random_topo = np.load("topo{}_{}.npy".format(topo_num, sizing_num))
    amp_phase = np.load("amp_phase{}_{}.npy".format(topo_num, sizing_num), allow_pickle=True)
    performance = np.load("performance{}_{}.npy".format(topo_num, sizing_num))
    for i in range(topo_num):
        for (amp_phase_, performance_) in zip(amp_phase[i * sizing_num:(i + 1) * sizing_num],
                                              performance[i * sizing_num:(i + 1) * sizing_num]):
            g = decode_circuit_to_igraph(random_topo[i], amp_phase_)
            g_list.append((g, performance_))
    graph_args.nvt = 9  # original types + virtual start/end/gnd types
    graph_args.max_n = max_n  # maximum number of nodes
    graph_args.node_feature = num_node_feature
    ng = len(g_list)
    print('# node types: %d' % graph_args.nvt)
    random.Random(rand_seed).shuffle(g_list)
    return g_list[:int(ng * 0.9)], g_list[int(ng * 0.9):], graph_args


def decode_circuit_to_igraph(random_topo, a_matrix):
    g = igraph.Graph(directed=True)
    n = np.shape(a_matrix)[0] + 3
    g.add_vertices(n)
    g.vs[0]['type'] = 8  # virtual start
    g.vs[1]['type'] = 4  # gm_diff_pos
    g.vs[2]['type'] = 5  # gm_middle_neg
    g.vs[n - 3]['type'] = 4  # gm_middle_pos
    id = 3
    for idx, c_type in enumerate(random_topo):
        if c_type == 1:
            g.vs[id]['type'] = 2
            id += 1
        elif c_type == 2:
            g.vs[id]['type'] = 3
            id += 1
        elif c_type == 3 or c_type == 4:
            g.vs[id]['type'] = 2
            g.vs[id + 1]['type'] = 3
            id += 2
        elif c_type == 5:
            g.vs[id]['type'] = 4
            id += 1
        elif c_type == 6:
            g.vs[id]['type'] = 5
            id += 1
        elif c_type == 7 or c_type == 11:
            g.vs[id]['type'] = 4
            g.vs[id + 1]['type'] = 2
            id += 2
        elif c_type == 8 or c_type == 12:
            g.vs[id]['type'] = 4
            g.vs[id + 1]['type'] = 3
            id += 2
        elif c_type == 9 or c_type == 13:
            g.vs[id]['type'] = 5
            g.vs[id + 1]['type'] = 2
            id += 2
        elif c_type == 10 or c_type == 14:
            g.vs[id]['type'] = 5
            g.vs[id + 1]['type'] = 3
            id += 2
        elif c_type == 15:
            g.vs[id]['type'] = 6
            id += 1
        elif c_type == 16:
            g.vs[id]['type'] = 7
            id += 1
        elif c_type == 17 or c_type == 18:
            g.vs[id]['type'] = 6
            g.vs[id + 1]['type'] = 2
            id += 2
        elif c_type == 19 or c_type == 20:
            g.vs[id]['type'] = 6
            g.vs[id + 1]['type'] = 3
            id += 2
        elif c_type == 21 or c_type == 22:
            g.vs[id]['type'] = 7
            g.vs[id + 1]['type'] = 2
            id += 2
        elif c_type == 23 or c_type == 24:
            g.vs[id]['type'] = 7
            g.vs[id + 1]['type'] = 3
            id += 2
    g.vs[-2]['type'] = 1  # gm-_c_series
    g.vs[-1]['type'] = 0  # virtual end

    for i in range(n):
        if i == 0 or i == n - 1 or i == n - 2:
            g.vs[i]['param'] = np.zeros(16)
        elif i == 1 or i == 2:
            g.vs[i]['param'] = a_matrix[i - 1]
        elif i == n - 3:
            g.vs[i]['param'] = a_matrix[2]
        else:
            g.vs[i]['param'] = a_matrix[i]

    # for i in range(n):
    #    print(g.vs[i]['param'])
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, n - 3)
    g.add_edge(n - 3, n - 1)
    id = 3
    for idx, c_type in enumerate(random_topo):
        if idx == 0:
            if c_type == 5 or c_type == 6:
                g.add_edge(0, id)
                g.add_edge(id, n - 3)
                id += 1
            elif c_type == 7 or c_type == 8 or c_type == 9 or c_type == 10:
                g.add_edge(0, id)
                g.add_edge(id, id + 1)
                g.add_edge(id + 1, n - 3)
                id += 2
        elif idx == 1:
            if c_type == 5 or c_type == 6:
                g.add_edge(0, id)
                g.add_edge(id, n - 1)
                id += 1
            elif c_type == 7 or c_type == 8 or c_type == 9 or c_type == 10:
                g.add_edge(0, id)
                g.add_edge(id, id + 1)
                g.add_edge(id + 1, n - 1)
                id += 2
        elif idx == 2:
            if c_type == 1 or c_type == 2 or c_type == 5 or c_type == 6 or c_type == 15 or c_type == 16:
                g.add_edge(1, id)
                g.add_edge(id, n - 1)
                id += 1
            elif c_type == 4 or c_type == 7 or c_type == 8 or c_type == 9 or c_type == 10 or c_type == 18 or c_type == 20 or c_type == 22 or c_type == 24:
                g.add_edge(1, id)
                g.add_edge(id, id + 1)
                g.add_edge(id + 1, n - 1)
                id += 2
            elif c_type == 3 or c_type == 11 or c_type == 12 or c_type == 13 or c_type == 14 or c_type == 17 or c_type == 19 or c_type == 21 or c_type == 23:
                g.add_edge(1, id)
                g.add_edge(id, n - 1)
                g.add_edge(1, id + 1)
                g.add_edge(id + 1, n - 1)
                id += 2
        elif idx == 3:
            if c_type == 1 or c_type == 2:
                g.add_edge(1, id)
                g.add_edge(id, n - 2)
                id += 1
            elif c_type == 3:
                g.add_edge(1, id)
                g.add_edge(id, n - 2)
                g.add_edge(1, id + 1)
                g.add_edge(id + 1, n - 2)
                id += 2
            elif c_type == 4:
                g.add_edge(1, id)
                g.add_edge(id, id + 1)
                g.add_edge(id + 1, n - 2)
                id += 2
        elif idx == 4:
            if c_type == 1 or c_type == 2:
                g.add_edge(2, id)
                g.add_edge(id, n - 2)
                id += 1
            elif c_type == 3:
                g.add_edge(2, id)
                g.add_edge(id, n - 2)
                g.add_edge(2, id + 1)
                g.add_edge(id + 1, n - 2)
                id += 2
            elif c_type == 4:
                g.add_edge(2, id)
                g.add_edge(id, id + 1)
                g.add_edge(id + 1, n - 2)
                id += 2
    return g


'''Network visualization'''


def plot_DAG(g, res_dir, name):
    file_name = os.path.join(res_dir, name + '.png')
    draw_network(g, file_name)
    return file_name


def draw_network(g, path):
    graph = pgv.AGraph(directed=True, strict=True, fontname='Helvetica', arrowtype='open')
    # add vertex
    for idx in range(0, g.vcount()):
        add_node(graph, g, idx)
    # add edge
    for idx in range(1, g.vcount()):
        for node in g.get_adjlist(igraph.IN)[idx]:
            graph.add_edge(node, idx)
    graph.layout(prog='dot')
    graph.draw(path)


def add_node(graph, g, node_id, shape='box', style='filled'):
    if g.vs[node_id]['type'] == 0:
        g.vs[node_id]['color'] = 'white'
        g.vs[node_id]['label'] = 'end'
    elif g.vs[node_id]['type'] == 1:
        g.vs[node_id]['color'] = 'white'
        g.vs[node_id]['label'] = 'gnd'
    elif g.vs[node_id]['type'] == 2:
        g.vs[node_id]['color'] = 'red'
        g.vs[node_id]['label'] = 'r'
    elif g.vs[node_id]['type'] == 3:
        g.vs[node_id]['color'] = 'yellow'
        g.vs[node_id]['label'] = 'c'
    elif g.vs[node_id]['type'] == 4:
        g.vs[node_id]['color'] = 'blue'
        g.vs[node_id]['label'] = 'gm+'
    elif g.vs[node_id]['type'] == 5:
        g.vs[node_id]['color'] = 'green'
        g.vs[node_id]['label'] = 'gm-'
    elif g.vs[node_id]['type'] == 6:
        g.vs[node_id]['color'] = 'brown'
        g.vs[node_id]['label'] = 'gm+_reverse'
    elif g.vs[node_id]['type'] == 7:
        g.vs[node_id]['color'] = 'purple'
        g.vs[node_id]['label'] = 'gm-_reverse'
    elif g.vs[node_id]['type'] == 8:
        g.vs[node_id]['color'] = 'white'
        g.vs[node_id]['label'] = 'start'
    else:
        g.vs[node_id]['color'] = 'white'
        g.vs[node_id]['label'] = 'new'
    graph.add_node(node_id, label=g.vs[node_id]['label'], color='black', fillcolor=g.vs[node_id]['color'],
                   shape=shape, style=style, fontsize=24)
    # if not (g.vs[node_id]['type'] == 0 and node_id != 0):
    #    graph.add_node(node_id, label=g.vs[node_id]['label'], color='black', fillcolor=g.vs[node_id]['color'],
    #                   shape=shape, style=style, fontsize=24)


'''Validity and novelty functions'''


def is_same_DAG(g0, g1):
    # Correct rate of edge type prediction
    all_n = 0
    right_n = 0
    all_e = 0
    right_e = 0
    for vo in range(2, g0.vcount() - 1):
        g0_node_type = g0.vs['type'][vo]
        g1_node_type = g1.vs['type'][vo]
        if g0_node_type == g1_node_type:
            right_n = right_n + 1
        all_n = all_n + 1
        for vi in g0.get_adjlist(igraph.IN)[vo]:
            if vi in g1.get_adjlist(igraph.IN)[vo]:
                right_e = right_e + 1
            all_e = all_e + 1
    node_correct = right_n / all_n
    edge_correct = right_e / all_e
    return node_correct and edge_correct
