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
CIRCUIT_NODE_NUM = 5
CIRCUIT_NODE_TYPE = 26

'''dataset generation'''


def clamp(minn, maxn, n):
    return max(min(maxn, n), minn)


def sample_topo_vector(edge_num):
    topo_vector = []
    for e in range(edge_num):
        if e <= 1:
            topo_vector.append(np.random.randint(0, 11))
        elif e == 2:
            topo_vector.append(np.random.randint(0, 25))
        else:
            topo_vector.append(np.random.randint(0, 5))
    return topo_vector


def sample_full_random(edge_num):
    topo_vector = []
    for e in range(edge_num):
        topo_vector.append(np.random.randint(0, 25))
    return topo_vector


def vector2row(topo_vector):
    CIRCUIT_DAG = []
    for i in range(CIRCUIT_NODE_NUM):
        if i == 0:
            CIRCUIT_DAG.append([0])  # node Vin
        elif i == 1:
            CIRCUIT_DAG.append([1, 5])  # node 1
        elif i == 2:
            CIRCUIT_DAG.append([1, topo_vector[0], 6])  # node 2
        elif i == 3:
            CIRCUIT_DAG.append([2, topo_vector[1], topo_vector[2], 5])  # node Vout
        elif i == 4:
            CIRCUIT_DAG.append([3, 0, topo_vector[3], topo_vector[4], 0])  # node GND
        else:
            pass
    return CIRCUIT_DAG


def row2vector(row):
    topo = []
    for i in range(len(row)):
        if i == 2:
            topo.append(row[i][1])
        elif i == 3:
            topo.append(row[i][1])
            topo.append(row[i][2])
        elif i == 4:
            topo.append(row[i][2])
            topo.append(row[i][3])
        else:
            pass
    return np.array(topo)


def g2topo(g):
    # plot_DAG(g, './', 'fuck')
    row_ = []
    for vo in range(2, g.vcount() - 1):
        for vi in range(1, vo):
            _eid = g.get_eid(vi, vo)
            row_.append(int(g.es[_eid]['weight']))
    topo_id = [1, 3, 4, 7, 8]
    topo = []
    for i in topo_id:
        if i == 1 or i == 3:
            topo.append(clamp(0, 11, row_[i]))
        elif i == 4:
            topo.append(clamp(0, 25, row_[i]))
        else:
            topo.append(clamp(0, 5, row_[i]))
    return np.array(topo)


'''Data preprocessing'''


def one_hot(idx, length):
    idx = torch.LongTensor([idx]).unsqueeze(0)
    x = torch.zeros((1, length)).scatter_(1, idx, 1)
    return x


def reorder_data2(value):
    # value = np.load("%s.npy" % datafile)
    value_new = np.zeros_like(value)
    value_new[0] = value[0]
    value_new[1] = value[3]
    value_new[2] = value[1]
    value_new[3] = value[2]
    value_new[4] = value[4]
    value_new[5] = value[5]
    return value_new


def load_CIRCUIT_graphs(rand_seed=0):
    # load DAG format CIRCUITs to igraphs
    g_list = []
    max_n = 10  # no connection to gnd, delete node gnd
    num_edge_feature = 32
    # max_n = 5  # maximum number of nodes
    value1 = np.load("../circuit1/value1000.npy")
    # print(value[0])
    value2 = np.load("../circuit2/value1000.npy")

    # len = np.shape(value[0])
    # print(value[0])
    value1 = value1.reshape((1000, 5, 32))
    value2 = value2.reshape((1000, 6, 32))
    for i in range(np.shape(value2)[0]):
        value2[i] = reorder_data2(value2[i])
    # print("value2:", value2)
    # value2 = reorder_data2(value2)

    # value = value[:, :, :num_edge_feature]
    performance1 = np.load("../circuit1/performance1000.npy")
    performance2 = np.load("../circuit2/performance1000.npy")
    for (value_, performance_) in zip(value1, performance1):
        g = decode_CIRCUIT_to_igraph1(value_)
        g_list.append((g, performance_))
    for (value_, performance_) in zip(value2, performance2):
        g = decode_CIRCUIT_to_igraph2(value_)
        g_list.append((g, performance_))
    graph_args.nvt = CIRCUIT_NODE_TYPE  # original types + virtual start/end types
    graph_args.max_n = max_n  # maximum number of nodes
    graph_args.edge_feature = num_edge_feature
    ng = len(g_list)
    print('# node types: %d' % graph_args.nvt)
    random.Random(rand_seed).shuffle(g_list)
    return g_list[:int(ng * 0.9)], g_list[int(ng * 0.9):], graph_args


def decode_CIRCUIT_to_igraph1(value):
    g = igraph.Graph(directed=True)
    n = 7
    g.add_vertices(n)
    g.vs[0]['type'] = 0  # virtual start
    # g.vs[0]['color'] = 'red'
    # g.vs[0]['label'] = 'start'
    g.vs[1]['type'] = 6  # gm+
    # g.vs[1]['color'] = 'blue'
    # g.vs[1]['label'] = 'gm+'
    g.vs[2]['type'] = 7  # gm-
    # g.vs[2]['color'] = 'green'
    # g.vs[2]['label'] = 'gm-'
    g.vs[3]['type'] = 6  # gm+
    # g.vs[3]['color'] = 'blue'
    # g.vs[3]['label'] = 'gm+'
    g.vs[4]['type'] = 7  # gm-
    # g.vs[4]['color'] = 'green'
    # g.vs[4]['label'] = 'gm-'
    g.vs[5]['type'] = 11  # gm-_c_series
    # g.vs[5]['color'] = 'brown'
    # g.vs[5]['label'] = 'gm-_c_series'
    g.vs[6]['type'] = 1  # virtual end
    # g.vs[6]['color'] = 'yellow'
    # g.vs[6]['label'] = 'end'

    for i in range(n):
        if i == 0 or i == n - 1:
            g.vs[i]['param'] = np.zeros(32)
        else:
            g.vs[i]['param'] = value[i - 1]

    # for i in range(n):
    #    print(g.vs[i]['param'])
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 6)
    g.add_edge(1, 4)
    g.add_edge(4, 6)
    g.add_edge(0, 5)
    g.add_edge(5, 6)

    return g


def decode_CIRCUIT_to_igraph2(value):
    g = igraph.Graph(directed=True)
    n = 8
    g.add_vertices(n)
    g.vs[0]['type'] = 0  # virtual start
    # g.vs[0]['color'] = 'red'
    # g.vs[0]['label'] = 'start'
    g.vs[1]['type'] = 6  # gm+
    # g.vs[1]['color'] = 'blue'
    # g.vs[1]['label'] = 'gm+'
    g.vs[2]['type'] = 6  # gm+
    # g.vs[2]['color'] = 'blue'
    # g.vs[2]['label'] = 'gm+'
    g.vs[3]['type'] = 7  # gm-
    # g.vs[3]['color'] = 'green'
    # g.vs[3]['label'] = 'gm-'
    g.vs[4]['type'] = 8  # gm+_r_series
    # g.vs[4]['color'] = 'grey'
    # g.vs[4]['label'] = 'gm+_r_series'
    g.vs[5]['type'] = 6  # gm+
    # g.vs[5]['color'] = 'blue'
    # g.vs[5]['label'] = 'gm+'
    g.vs[6]['type'] = 9  # gm+_c_series
    # g.vs[6]['color'] = 'purple'
    # g.vs[6]['label'] = 'gm+_c_series'
    g.vs[7]['type'] = 1  # virtual end
    # g.vs[7]['color'] = 'yellow'
    # g.vs[7]['label'] = 'end'

    for i in range(n):
        if i == 0 or i == n - 1:
            g.vs[i]['param'] = np.zeros(32)
        else:
            g.vs[i]['param'] = value[i - 1]

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(1, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 7)
    g.add_edge(0, 4)
    g.add_edge(4, 5)
    g.add_edge(0, 6)
    g.add_edge(6, 7)

    return g


'''Network visualization'''


def plot_DAG(g, res_dir, name, pdf=False):
    # backbone: puts all nodes in a straight line
    file_name = os.path.join(res_dir, name + '.png')
    if pdf:
        file_name = os.path.join(res_dir, name + '.pdf')
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
    # if g.vs[node_id]['type'] == 0 and node_id == 0:
    if g.vs[node_id]['type'] == 0:
        g.vs[node_id]['color'] = 'red'
        g.vs[node_id]['label'] = 'start'
    elif g.vs[node_id]['type'] == 1:
        g.vs[node_id]['color'] = 'yellow'
        g.vs[node_id]['label'] = 'end'
    elif g.vs[node_id]['type'] == 6:
        g.vs[node_id]['color'] = 'blue'
        g.vs[node_id]['label'] = 'gm+'
    elif g.vs[node_id]['type'] == 7:
        g.vs[node_id]['color'] = 'green'
        g.vs[node_id]['label'] = 'gm-'
    elif g.vs[node_id]['type'] == 8:
        g.vs[node_id]['color'] = 'grey'
        g.vs[node_id]['label'] = 'gm+_r_series'
    elif g.vs[node_id]['type'] == 9:
        g.vs[node_id]['color'] = 'purple'
        g.vs[node_id]['label'] = 'gm+_c_series'
    elif g.vs[node_id]['type'] == 11:
        g.vs[node_id]['color'] = 'brown'
        g.vs[node_id]['label'] = 'gm-_c_series'
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
    if g0.vcount() != g1.vcount():
        return False
    all_n = 0
    right_n = 0
    all_e = 0
    right_e = 0
    for vo in range(1, g0.vcount()):
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


def load_module_state(model, state_name):
    pretrained_dict = torch.load(state_name)
    model_dict = model.state_dict()

    # to delete, to correct grud names
    '''
    new_dict = {}
    for k, v in pretrained_dict.items():
        if k.startswith('grud_forward'):
            new_dict['grud'+k[12:]] = v
        else:
            new_dict[k] = v
    pretrained_dict = new_dict
    '''

    # 1. filter out unnecessary keys
    pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}

    # 2. overwrite entries in the existing state dict
    model_dict.update(pretrained_dict)
    # 3. load the new state dict
    model.load_state_dict(pretrained_dict)
    return


def decode_igraph_to_CIRCUIT(g):
    # decode an igraph to a flattend CIRCUIT string
    n = g.vcount()
    res = []
    adjlist = g.get_adjlist(igraph.IN)
    for i in range(1, n - 1):
        res.append(int(g.vs[i]['type']) - 2)
        row = [0] * (i - 1)
        for j in adjlist[i]:
            if j < i - 1:
                row[j] = 1
        res += row
    return ' '.join(str(x) for x in res)
    # return res


def decode_from_latent_space(
        latent_points, model, decode_attempts=500, n_nodes='variable', return_igraph=False):
    # decode points from the VAE model's latent space multiple attempts
    # and return the most common decoded graphs
    if n_nodes != 'variable':
        check_n_nodes = True  # check whether the decoded graphs have exactly n nodes
    else:
        check_n_nodes = False
    decoded_arcs = []  # a list of lists of igraphs
    pbar = tqdm(range(decode_attempts))
    for i in pbar:
        current_decoded_arcs = model.decode(latent_points)
        decoded_arcs.append(current_decoded_arcs)
        pbar.set_description("Decoding attempts {}/{}".format(i, decode_attempts))

    # We see which ones are decoded to be valid architectures
    valid_arcs = []  # a list of lists of strings
    if return_igraph:
        str2igraph = {}  # map strings to igraphs
    pbar = tqdm(range(latent_points.shape[0]))
    for i in pbar:
        valid_arcs.append([])
        for j in range(decode_attempts):
            arc = decoded_arcs[j][i]  # arc is an igraph
            if not check_n_nodes or check_n_nodes and arc.vcount() == n_nodes:
                cur = decode_igraph_to_CIRCUIT(arc)  # a flat circuit igraph string
                if return_igraph:
                    str2igraph[cur] = arc
                valid_arcs[i].append(cur)
        pbar.set_description("Check validity for {}/{}".format(i, latent_points.shape[0]))

    # select the most common decoding as the final architecture
    final_arcs = []  # a list of lists of strings
    pbar = tqdm(range(latent_points.shape[0]))
    for i in pbar:
        valid_curs = valid_arcs[i]
        aux = collections.Counter(valid_curs)
        if len(aux) > 0:
            arc, num_arc = list(aux.items())[np.argmax(aux.values())]
        else:
            arc = None
            num_arc = 0
        final_arcs.append(arc)
        pbar.set_description("Latent point {}'s most common decoding ratio: {}/{}".format(
            i, num_arc, len(valid_curs)))

    if return_igraph:
        final_arcs_igraph = [str2igraph[x] if x is not None else None for x in final_arcs]
        return final_arcs_igraph, final_arcs
    return final_arcs
