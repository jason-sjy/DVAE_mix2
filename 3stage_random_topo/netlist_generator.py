# created by jialin
# translate a DAG into a spectre netlist file 

import os
import sys
import string
import random
import numpy as np


def get_node_info(x, idx):
    instance_head = []
    node = []
    instance = []
    instance_val = []
    unit = []
    bound = []
    additional_node = []
    additional_ins_head = []
    additional_ins = []
    additional_ins_val = []
    additional_ins_unit = []
    additional_ins_bound = []
    if x == 0:
        instance_head = []
        node = []
        instance = []
        instance_val = []
        unit = []
        bound = []
        additional_node = []
        additional_ins_head = []
        additional_ins = []
        additional_ins_val = []
        additional_ins_unit = []
        additional_ins_bound = []
    elif x == 1:  # R
        instance_head = ['R']
        node = [0, 1]
        instance = []
        instance_val = ['r']
        unit = ['*1meg']
        bound = ['1']
        additional_node = []
        additional_ins_head = []
        additional_ins = []
        additional_ins_val = []
        additional_ins_unit = []
        additional_ins_bound = []
    elif x == 2:  # C
        instance_head = ['C']
        node = [0, 1]
        instance = []
        instance_val = ['c']
        unit = ['*1p']
        bound = ['10']
        additional_node = []
        additional_ins_head = []
        additional_ins = []
        additional_ins_val = []
        additional_ins_unit = []
        additional_ins_bound = []
    elif x == 3:  # RC parallel
        instance_head = ['R', 'C']
        node = [0, 1]
        instance = []
        instance_val = ['r', 'c']
        unit = ['*1meg', '*1p']
        bound = ['1', '10']
        additional_node = []
        additional_ins_head = []
        additional_ins = []
        additional_ins_val = []
        additional_ins_unit = []
        additional_ins_bound = []
    elif x == 4:  # RC series
        instance_head = ['R', 'C']
        node = [0, 1]
        instance = []
        instance_val = ['r', 'c']
        unit = ['*1meg', '*1p']
        bound = ['10', '10']
        additional_node = [2]
        additional_ins_head = []
        additional_ins = []
        additional_ins_val = []
        additional_ins_unit = []
        additional_ins_bound = []
    elif x == 5:  # Feedforward +gm
        instance_head = ['X']
        node = [0, 1]
        instance = ['gm+']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        # additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb']
            unit = ['*1u', '*1u', '*1u']
            bound = ['50', '50', '50']
        else:
            instance_val = ['wp', 'wb']
            unit = ['*1u', '*1u']
            bound = ['50', '50']
    elif x == 6:  # Feedforward -gm
        instance_head = ['X']
        node = [0, 1]
        instance = ['gm-']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        # additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb']
            unit = ['*1u', '*1u', '*1u']
            bound = ['50', '50', '50']
        else:
            instance_val = ['wp', 'wn']
            unit = ['*1u', '*1u']
            bound = ['50', '50']
    ###
    elif x == 7:  # R&5 series
        instance_head = ['X', 'R']
        node = [0, 1]
        instance = ['gm+']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'r']
            unit = ['*1u', '*1u', '*1u', '*1meg']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wb', 'r']
            unit = ['*1u', '*1u', '*1meg']
            bound = ['50', '50', '10']
    elif x == 8:  # C&5 series
        instance_head = ['X', 'C']
        node = [0, 1]
        instance = ['gm+']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'c']
            unit = ['*1u', '*1u', '*1u', '*1p']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wb', 'c']
            unit = ['*1u', '*1u', '*1p']
            bound = ['50', '50', '10']
    elif x == 9:  # R&6 series
        instance_head = ['X', 'R']
        node = [0, 1]
        instance = ['gm-']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'r']
            unit = ['*1u', '*1u', '*1u', '*1meg']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wn', 'r']
            unit = ['*1u', '*1u', '*1meg']
            bound = ['50', '50', '10']
    elif x == 10:  # C&6 series
        instance_head = ['X', 'C']
        node = [0, 1]
        instance = ['gm-']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'c']
            unit = ['*1u', '*1u', '*1u', '*1p']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wn', 'r']
            unit = ['*1u', '*1u', '*1meg']
            bound = ['50', '50', '10']
    elif x == 11:  # R&5 parallel
        instance_head = ['X', 'R']
        node = [0, 1]
        instance = ['gm+']
        additional_node = [1]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'r']
            unit = ['*1u', '*1u', '*1u', '*1meg']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wb', 'r']
            unit = ['*1u', '*1u', '*1meg']
            bound = ['50', '50', '10']
    elif x == 12:  # C&5 parallel
        instance_head = ['X', 'C']
        node = [0, 1]
        instance = ['gm+']
        additional_node = [1]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'c']
            unit = ['*1u', '*1u', '*1u', '*1p']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wb', 'c']
            unit = ['*1u', '*1u', '*1p']
            bound = ['50', '50', '10']
    elif x == 13:  # R&6 parallel
        instance_head = ['X', 'R']
        node = [0, 1]
        instance = ['gm-']
        additional_node = [1]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'r']
            unit = ['*1u', '*1u', '*1u', '*1meg']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wn', 'r']
            unit = ['*1u', '*1u', '*1meg']
            bound = ['50', '50', '10']
    elif x == 14:  # C&6 parallel
        instance_head = ['X', 'C']
        node = [0, 1]
        instance = ['gm-']
        additional_node = [1]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        if idx <= 1:
            instance_val = ['wn', 'wp', 'wb', 'c']
            unit = ['*1u', '*1u', '*1u', '*1p']
            bound = ['50', '50', '50', '10']
        else:
            instance_val = ['wp', 'wn', 'c']
            unit = ['*1u', '*1u', '*1p']
            bound = ['50', '50', '10']
    ###
    elif x == 15:  # Feedback +gm
        instance_head = ['X']
        node = [1, 0]
        instance = ['gm+']
        instance_val = ['wp', 'wb']
        unit = ['*1u', '*1u']
        bound = ['50', '50']
        additional_node = [1]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
    elif x == 16:  # Feedback -gm
        instance_head = ['X']
        node = [1, 0]
        instance = ['gm-']
        instance_val = ['wp', 'wn']
        unit = ['*1u', '*1u']
        bound = ['50', '50']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
    elif x == 17:  # R&15 parallel
        instance_head = ['R', 'X']
        node = [1, 0]
        instance = ['gm+']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['r', 'wp', 'wb']
        unit = ['*1meg', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 18:  # R&15 series
        instance_head = ['R', 'X']
        node = [1, 0]
        instance = ['gm+']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['r', 'wp', 'wb']
        unit = ['*1meg', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 19:  # C&15 parallel
        instance_head = ['C', 'X']
        node = [1, 0]
        instance = ['gm+']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['c', 'wp', 'wb']
        unit = ['*1p', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 20:  # C&15 series
        instance_head = ['C', 'X']
        node = [1, 0]
        instance = ['gm+']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['c', 'wp', 'wb']
        unit = ['*1p', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 21:  # R&16 parallel
        instance_head = ['R', 'X']
        node = [1, 0]
        instance = ['gm-']
        instance_val = ['r', 'gm']
        unit = ['*1M', '*-1m']
        bound = ['10', '10']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['r', 'wp', 'wn']
        unit = ['*1meg', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 22:  # R&16 series
        instance_head = ['R', 'X']
        node = [1, 0]
        instance = ['gm-']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['r', 'wp', 'wn']
        unit = ['*1meg', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 23:  # C&16 parallel
        instance_head = ['C', 'X']
        node = [1, 0]
        instance = ['gm-']
        additional_node = [0]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['c', 'wp', 'wn']
        unit = ['*1p', '*1u', '*1u']
        bound = ['10', '50', '50']
    elif x == 24:  # C&16 series
        instance_head = ['C', 'X']
        node = [1, 0]
        instance = ['gm-']
        additional_node = [2]
        additional_ins_head = ['R', 'C']
        additional_ins = ['resistor', 'capacitor']
        additional_ins_val = ['r', 'c']
        additional_ins_unit = ['*1K', '*1p']
        additional_ins_bound = ['80', '1']
        instance_val = ['c', 'wp', 'wn']
        unit = ['*1p', '*1u', '*1u']
        bound = ['10', '50', '50']

    return instance_head, node, instance, instance_val, unit, bound, additional_node, additional_ins_head, additional_ins, additional_ins_val, additional_ins_unit, additional_ins_bound


def amp_generator(topo_vector):
    '''
    os.chdir('tmp_circuit')
    os.system('mkdir ' + design_id)
    os.chdir(design_id)
    os.system('mkdir circuit')
    os.chdir('circuit')
    os.system('mkdir netlist')
    os.chdir('../../..')

    tmp_conf = open('./tmp_circuit/' + design_id + '/tmp.conf', 'w')
    netlist = open('./tmp_circuit/' + design_id + '/circuit/netlist/netlist', 'w')
    '''
    tmp_conf = open('./conf', 'w')
    netlist = open('./opamp.sp', 'w')
    # netlist.writelines('V0 (net_vin 0) vsource mag=1 type=sine\n')     # V_source setting
    '''
    netlist.writelines('.title Project: Three-STAGE OPAMP\n')
    netlist.writelines('.LIB "\home\shenjinyi\behavioral_model\sm046005-1j.hspice" typical\n')
    netlist.writelines('.inc \'param\'\n')

    netlist.writelines('.param l=1u\n')
    netlist.writelines('.param Vr=3.3\n')
    netlist.writelines('.param Vc=1.3\n')
    netlist.writelines('.param Vb1=0.9\n')
    netlist.writelines('.param Vb2=2.3\n')
    '''
    netlist.writelines('.inc \'gm+.sp\'\n')
    netlist.writelines('.inc \'gm-.sp\'\n')
    netlist.writelines('.inc \'gm+_middle.sp\'\n')
    netlist.writelines('.inc \'gm-_middle.sp\'\n')
    netlist.writelines('.subckt opamp vp vn out vb1 vb2 vdd\n')

    netlist.writelines('X_vin_1 net_vinp net_vinn net_1 vb1 vdd gm+ wp=wp_in_1*1u wn=wn_in_1*1u wb=wb_in_1*1u\n')
    tmp_conf.writelines('des_var wp_in_1 2 50\n')
    tmp_conf.writelines('des_var wn_in_1 2 50\n')
    tmp_conf.writelines('des_var wb_in_1 2 50\n')
    # netlist.writelines('R_1_0_prs net_1 0 r=rscl_vin_1_prs/g_vin_1*1K\n')
    # tmp_conf.writelines('des_var rscl_vin_1_prs 40 80\n')
    # netlist.writelines('C_1_0_prs net_1 0 c=g_1_2/6.28*5p\n')

    netlist.writelines('X_1_2 net_1 net_2 vb2 vdd gm-_middle wp=wp_1_2*1u wn=wn_1_2*1u\n')
    tmp_conf.writelines('des_var wp_1_2 2 50\n')
    tmp_conf.writelines('des_var wn_1_2 2 50\n')
    # netlist.writelines('R_2_0_prs (net_2 0) resistor r=rscl_1_2_prs/g_1_2*1K\n')
    # tmp_conf.writelines('des_var rscl_1_2_prs 40 80\n')
    # netlist.writelines('C_2_0_prs (net_2 0) capacitor c=g_2_vo/6.28*5p\n')

    netlist.writelines('X_2_vo net_2 net_vo vb1 vdd gm+_middle wp=wp_2_out*1u wb=wb_2_out*1u\n')
    tmp_conf.writelines('des_var wp_2_out 2 50\n')
    tmp_conf.writelines('des_var wb_2_out 2 50\n')
    # netlist.writelines('R_vo_0_prs (net_vo 0) resistor r=rscl_2_vo_prs/g_2_vo*1K\n')
    # tmp_conf.writelines('des_var rscl_2_vo_prs 40 80\n')
    # netlist.writelines('C_vo_0_prs (net_vo 0) capacitor c=c_vo_0_prs*1p\n')
    # tmp_conf.writelines('des_var c_vo_0_prs 0.01 10\n')

    netlist.writelines('R_L net_vo 0 r=0.15meg\n')  # RC load setting
    netlist.writelines('C_L net_vo 0 c=10n\n')

    node_pairs = [['_vin', '_2', '_vin_2'], ['_vin', '_vo', '_vin_vo'], ['_1', '_vo', '_1_vo'], ['_1', '_0', '_1_0'],
                  ['_2', '_0', '_2_0']]

    for idx, node in enumerate(node_pairs):
        x = topo_vector[idx, 0]
        node_pair = node_pairs[idx]
        instance_head, node, instance, instance_val, unit, bound, additional_node, additional_ins_head, additional_ins, additional_ins_val, additional_ins_unit, additional_ins_bound = get_node_info(
            x, idx)
        if x == 0:
            pass
        elif 1 <= x <= 2:
            if idx <= 2:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' 0 ' +
                    instance_val[0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[
                        node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
        elif x == 3:
            if idx <= 2:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ' ' + instance_val[1] + '=' + instance_val[1] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[1] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' 0 ' +
                    instance_val[0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[
                        node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' 0 ' +
                    instance_val[1] + '=' + instance_val[1] + node_pair[node[0]] + node_pair[
                        node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[1] + '\n')
        elif x == 4:
            if idx <= 2:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' net' + node_pair[
                        node[0]] + ' net' + node_pair[additional_node[0]] + ' ' + instance_val[
                        0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[
                        0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 0.01 ' +
                    bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' net' + node_pair[
                        additional_node[0]] + ' net' + node_pair[node[1]] + ' ' + instance_val[
                        1] + '=' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[
                        1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[
                        1] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' net' + node_pair[
                        node[0]] + ' net' + node_pair[additional_node[0]] + ' ' + instance_val[
                        0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[
                        0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 0.01 ' +
                    bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' net' + node_pair[
                        additional_node[0]] + ' 0 ' + instance_val[1] + '=' + instance_val[1] +
                    node_pair[additional_node[0]] + node_pair[node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[
                        1] + '\n')
        elif x in [15, 16]:
            if x == 15:
                netlist.writelines(instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                    node[0]] + ' net' + node_pair[node[1]] + ' vb1 vdd ' + instance[0] + '_middle ' + instance_val[
                                       0] + '=' +
                                   instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + ' ' +
                                   instance_val[1] + '=' +
                                   instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
            else:
                netlist.writelines(instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                    node[0]] + ' net' + node_pair[node[1]] + ' vb2 vdd ' + instance[0] + '_middle ' + instance_val[
                                       0] + '=' +
                                   instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + ' ' +
                                   instance_val[1] + '=' +
                                   instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
            for i in range(len(instance_val)):
                tmp_conf.writelines(
                    'des_var ' + instance_val[i] + node_pair[node[0]] + node_pair[node[1]] + ' 2 ' + bound[
                        i] + '\n')
        elif x in [5, 6]:
            if idx <= 1:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net_vinp net_vinn net' +
                    node_pair[node[1]] + ' vb1 vdd ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] +
                    node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + ' ' + instance_val[1] + '=' + instance_val[1] +
                    node_pair[
                        node[0]] + node_pair[node[1]] + unit[1] + ' ' + instance_val[2] + '=' + instance_val[2] +
                    node_pair[
                        node[0]] + node_pair[node[1]] + unit[2] + '\n')
            else:
                if x == 5:
                    netlist.writelines(instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                        node[0]] + ' net' + node_pair[node[1]] + ' vb1 vdd ' + instance[0] + '_middle ' + instance_val[
                                           0] + '=' +
                                       instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + ' ' +
                                       instance_val[1] + '=' +
                                       instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
                else:
                    netlist.writelines(instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                        node[0]] + ' net' + node_pair[node[1]] + ' vb2 vdd ' + instance[0] + '_middle ' + instance_val[
                                           0] + '=' +
                                       instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + ' ' +
                                       instance_val[1] + '=' +
                                       instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
            for i in range(len(instance_val)):
                tmp_conf.writelines(
                    'des_var ' + instance_val[i] + node_pair[node[0]] + node_pair[node[1]] + ' 2 ' + bound[
                        i] + '\n')
        elif 7 <= x <= 14:
            if 11 <= x <= 14:
                if idx <= 1:
                    netlist.writelines(
                        instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net_vinp net_vinn net' +
                        node_pair[node[1]] + ' vb1 vdd ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] +
                        node_pair[
                            node[0]] + node_pair[node[1]] + unit[0] + ' ' + instance_val[1] + '=' + instance_val[1] +
                        node_pair[
                            node[0]] + node_pair[node[1]] + unit[1] + ' ' + instance_val[2] + '=' + instance_val[2] +
                        node_pair[
                            node[0]] + node_pair[node[1]] + unit[2] + '\n')
                else:
                    if x == 11 or x == 12:
                        netlist.writelines(
                            instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                                node[0]] + ' net' + node_pair[node[1]] + ' vb1 vdd ' + instance[0] + '_middle ' +
                            instance_val[
                                0] + '=' +
                            instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + ' ' +
                            instance_val[1] + '=' +
                            instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
                    else:
                        netlist.writelines(
                            instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                                node[0]] + ' net' + node_pair[node[1]] + ' vb2 vdd ' + instance[0] + '_middle ' +
                            instance_val[
                                0] + '=' +
                            instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + ' ' +
                            instance_val[1] + '=' +
                            instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ' ' + instance_val[-1] + '=' + instance_val[-1] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[-1] + '\n')
                for i in range(len(instance_val) - 1):
                    tmp_conf.writelines(
                        'des_var ' + instance_val[i] + node_pair[node[0]] + node_pair[node[1]] + ' 2 ' + bound[
                            i] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[-1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[
                        -1] + '\n')
            else:
                if idx <= 1:
                    netlist.writelines(
                        instance_head[0] + node_pair[node[0]] + node_pair[
                            additional_node[0]] + ' net_vinp net_vinn net' +
                        node_pair[additional_node[0]] + ' vb1 vdd ' + instance[0] + ' ' + instance_val[0] + '=' +
                        instance_val[0] +
                        node_pair[
                            node[0]] + node_pair[additional_node[0]] + unit[0] + ' ' + instance_val[1] + '=' +
                        instance_val[1] +
                        node_pair[
                            node[0]] + node_pair[additional_node[0]] + unit[1] + ' ' + instance_val[2] + '=' +
                        instance_val[2] +
                        node_pair[
                            node[0]] + node_pair[additional_node[0]] + unit[2] + '\n')
                else:
                    if x == 7 or x == 8:
                        netlist.writelines(
                            instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' net' + node_pair[
                                node[0]] + ' net' + node_pair[additional_node[0]] + ' vb1 vdd ' + instance[
                                0] + '_middle ' +
                            instance_val[
                                0] + '=' +
                            instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[0] + ' ' +
                            instance_val[1] + '=' +
                            instance_val[1] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[1] + '\n')
                    else:
                        netlist.writelines(
                            instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' net' + node_pair[
                                node[0]] + ' net' + node_pair[additional_node[0]] + ' vb2 vdd ' + instance[
                                0] + '_middle ' +
                            instance_val[
                                0] + '=' +
                            instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[0] + ' ' +
                            instance_val[1] + '=' +
                            instance_val[1] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[1] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' net' + node_pair[
                        additional_node[0]] + ' net' +
                    node_pair[node[1]] + ' ' + instance_val[-1] + '=' + instance_val[-1] + node_pair[
                        additional_node[0]] + node_pair[node[1]] + unit[-1] + '\n')
                for i in range(len(instance_val) - 1):
                    tmp_conf.writelines(
                        'des_var ' + instance_val[i] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 2 ' +
                        bound[
                            i] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[-1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.01 ' +
                    bound[
                        -1] + '\n')

        elif 17 <= x <= 24:
            if x % 2 != 0:
                if x == 17 or x == 19:
                    netlist.writelines(
                        instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                            node[0]] + ' net' + node_pair[node[1]] + ' vb1 vdd ' + instance[0] + '_middle ' +
                        instance_val[
                            1] + '=' +
                        instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + ' ' +
                        instance_val[2] + '=' +
                        instance_val[2] + node_pair[node[0]] + node_pair[node[1]] + unit[2] + '\n')
                else:
                    netlist.writelines(
                        instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[
                            node[0]] + ' net' + node_pair[node[1]] + ' vb2 vdd ' + instance[0] + '_middle ' +
                        instance_val[
                            1] + '=' +
                        instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + ' ' +
                        instance_val[2] + '=' +
                        instance_val[2] + node_pair[node[0]] + node_pair[node[1]] + unit[2] + '\n')
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + '\n')
                for i in range(len(instance_val) - 1):
                    tmp_conf.writelines(
                        'des_var ' + instance_val[i + 1] + node_pair[node[0]] + node_pair[node[1]] + ' 2 ' + bound[
                            i + 1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[
                        0] + '\n')

            else:
                if x == 18 or x == 20:
                    netlist.writelines(
                        instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' net' + node_pair[
                            additional_node[0]] + ' net' + node_pair[node[1]] + ' vb1 vdd ' + instance[
                            0] + '_middle ' +
                        instance_val[
                            1] + '=' +
                        instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[1] + ' ' +
                        instance_val[2] + '=' +
                        instance_val[2] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[2] + '\n')
                else:
                    netlist.writelines(
                        instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' net' + node_pair[
                            additional_node[0]] + ' net' + node_pair[node[1]] + ' vb2 vdd ' + instance[
                            0] + '_middle ' +
                        instance_val[
                            1] + '=' +
                        instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[1] + ' ' +
                        instance_val[2] + '=' +
                        instance_val[2] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[2] + '\n')
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' net' + node_pair[
                        node[0]] + ' net' +
                    node_pair[additional_node[0]] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[node[0]] +
                    node_pair[additional_node[0]] + unit[0] + '\n')
                for i in range(len(instance_val) - 1):
                    tmp_conf.writelines(
                        'des_var ' + instance_val[i + 1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 2 ' +
                        bound[
                            i + 1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 0.01 ' +
                    bound[
                        0] + '\n')

        else:
            print('error topo input !')

    netlist.close()
    tmp_conf.close()


def dac21_amp_generator(design_id, topo_vector):
    os.chdir('dac21_tmp_circuit')
    os.system('mkdir ' + design_id)
    os.chdir(design_id)
    os.system('mkdir circuit')
    os.chdir('circuit')
    os.system('mkdir netlist')
    os.chdir('../../..')

    netlistFooter = open('./dac21_tmp_circuit/' + design_id + '/circuit/netlist/netlistFooter', 'w')
    netlistFooter.writelines('// Footer end\n')
    netlistFooter.close()
    netlistHeader = open('./dac21_tmp_circuit/' + design_id + '/circuit/netlist/netlistHeader', 'w')
    netlistHeader.writelines('// Generated by amp topo opt program\n')
    netlistHeader.writelines('simulator lang=spectre\n')
    netlistHeader.writelines('global 0\n')
    netlistHeader.writelines('// Header end\n')
    netlistHeader.close()

    tmp_conf = open('./dac21_tmp_circuit/' + design_id + '/tmp.conf', 'w')
    netlist = open('./dac21_tmp_circuit/' + design_id + '/circuit/netlist/netlist', 'w')

    netlist.writelines('V0 (net_vin 0) vsource mag=1 type=sine\n')  # V_source setting

    netlist.writelines('G_vin_1 (net_1 0 net_vin 0) vccs gm=g_vin_1*1m\n')
    tmp_conf.writelines('des_var g_vin_1 0.01 1\n')
    netlist.writelines('R_1_0_prs (net_1 0) resistor r=rscl_vin_1_prs/g_vin_1*1K\n')
    tmp_conf.writelines('des_var rscl_vin_1_prs 40 80\n')
    netlist.writelines('C_1_0_prs (net_1 0) capacitor c=g_1_2/6.28*5p\n')

    netlist.writelines('G_1_2 (net_2 0 net_1 0) vccs gm=g_1_2*-1m\n')
    tmp_conf.writelines('des_var g_1_2 0.01 1\n')
    netlist.writelines('R_2_0_prs (net_2 0) resistor r=rscl_1_2_prs/g_1_2*1K\n')
    tmp_conf.writelines('des_var rscl_1_2_prs 40 80\n')
    netlist.writelines('C_2_0_prs (net_2 0) capacitor c=g_2_vo/6.28*5p\n')

    netlist.writelines('G_2_vo net_vo 0 net_2 0 vccs gm=g_2_vo*1m\n')
    tmp_conf.writelines('des_var g_2_vo 0.01 1\n')
    netlist.writelines('R_vo_0_prs (net_vo 0) resistor r=rscl_2_vo_prs/g_2_vo*1K\n')
    tmp_conf.writelines('des_var rscl_2_vo_prs 40 80\n')
    # netlist.writelines('C_vo_0_prs (net_vo 0) capacitor c=c_vo_0_prs*1p\n')
    # tmp_conf.writelines('des_var c_vo_0_prs 0.01 10\n')

    netlist.writelines('R_L net_vo 0 resistor r=0.15meg\n')  # RC load setting
    netlist.writelines('C_L net_vo 0 capacitor c=10n\n')

    node_pairs = [['_vin', '_2', '_vin_2'], ['_vin', '_vo', '_vin_vo'], ['_1', '_vo', '_1_vo'], ['_1', '_0', '_1_0'],
                  ['_2', '_0', '_2_0']]

    for idx, node in enumerate(node_pairs):
        x = topo_vector[idx, 0]
        node_pair = node_pairs[idx]
        instance_head, node, instance, instance_val, unit, bound, additional_node, additional_ins_head, additional_ins, additional_ins_val, additional_ins_unit, additional_ins_bound = get_node_info(
            x)
        if x == 0:
            pass
        elif 1 <= x <= 2:
            if idx <= 2:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ') ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' 0) ' +
                    instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[
                        node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
        elif x == 3:
            if idx <= 2:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ') ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ') ' + instance[1] + ' ' + instance_val[1] + '=' + instance_val[1] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[1] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' 0) ' +
                    instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[
                        node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' 0) ' +
                    instance[1] + ' ' + instance_val[1] + '=' + instance_val[1] + node_pair[node[0]] + node_pair[
                        node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[1] + '\n')
        elif x == 4:
            if idx <= 2:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' (net' + node_pair[
                        node[0]] + ' net' + node_pair[additional_node[0]] + ') ' + instance[0] + ' ' + instance_val[
                        0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[
                        0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 0.01 ' +
                    bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' (net' + node_pair[
                        additional_node[0]] + ' net' + node_pair[node[1]] + ') ' + instance[1] + ' ' + instance_val[
                        1] + '=' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[
                        1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[
                        1] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' (net' + node_pair[
                        node[0]] + ' net' + node_pair[additional_node[0]] + ') ' + instance[0] + ' ' + instance_val[
                        0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[
                        0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 0.01 ' +
                    bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + instance[1] + ' ' + instance_val[1] + '=' + instance_val[1] +
                    node_pair[additional_node[0]] + node_pair[node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.5 ' + bound[
                        1] + '\n')
        elif x in [15, 16]:
            netlist.writelines(
                instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' 0 net' +
                node_pair[node[1]] + ' 0) ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                    node[0]] + node_pair[node[1]] + unit[0] + '\n')
            tmp_conf.writelines(
                'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')

            netlist.writelines(
                additional_ins_head[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                    additional_node[0]] + ' 0) ' + additional_ins[0] + ' ' + additional_ins_val[0] + '=' +
                additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + '/' + instance_val[0] +
                node_pair[node[0]] + node_pair[node[1]] + additional_ins_unit[0] + '\n')
            tmp_conf.writelines(
                'des_var ' + additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 40 ' +
                additional_ins_bound[0] + '\n')
            netlist.writelines(
                additional_ins_head[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                    additional_node[0]] + ' 0) ' + additional_ins[1] + ' ' + additional_ins_val[1] + '=' +
                additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + additional_ins_unit[
                    1] + '\n')
            tmp_conf.writelines(
                'des_var ' + additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 0.5 ' +
                additional_ins_bound[1] + '\n')
        elif x in [5, 6]:
            netlist.writelines(
                instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' 0 net' +
                node_pair[node[1]] + ' 0) ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                    node[0]] + node_pair[node[1]] + unit[0] + '\n')
            tmp_conf.writelines(
                'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')

            netlist.writelines(
                additional_ins_head[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                    additional_node[0]] + ' 0) ' + additional_ins[0] + ' ' + additional_ins_val[0] + '=' +
                additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + '/' + instance_val[0] +
                node_pair[node[0]] + node_pair[node[1]] + additional_ins_unit[0] + '\n')
            tmp_conf.writelines(
                'des_var ' + additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 40 ' +
                additional_ins_bound[0] + '\n')
            netlist.writelines(
                additional_ins_head[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                    additional_node[0]] + ' 0) ' + additional_ins[1] + ' ' + additional_ins_val[1] + '=' +
                additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + additional_ins_unit[
                    1] + '\n')
            tmp_conf.writelines(
                'des_var ' + additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 0.5 ' +
                additional_ins_bound[1] + '\n')
            # add input parasitic capacitor
            netlist.writelines(
                'C_input_' + str(int(idx)) + ' (net' + node_pair[node[1]] + ' 0) capacitor c=' + instance_val[0] +
                node_pair[node[0]] + node_pair[node[1]] + '/6.28*5p' + '\n')
        elif 7 <= x <= 14:
            if 11 <= x <= 14:
                netlist.writelines(instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[
                    node[0]] + ' 0 net' + node_pair[node[1]] + ' 0) ' + instance[0] + ' ' + instance_val[0] + '=' +
                                   instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ') ' + instance[1] + ' ' + instance_val[1] + '=' + instance_val[1] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[1] + '\n')

                netlist.writelines(
                    additional_ins_head[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[0] + ' ' + additional_ins_val[0] + '=' +
                    additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + '/' + instance_val[
                        0] + node_pair[node[0]] + node_pair[node[1]] + additional_ins_unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 40 ' +
                    additional_ins_bound[0] + '\n')
                netlist.writelines(
                    additional_ins_head[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[1] + ' ' + additional_ins_val[1] + '=' +
                    additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + additional_ins_unit[
                        1] + '\n')
                tmp_conf.writelines('des_var ' + additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(
                    int(idx)) + ' 0.5 ' + additional_ins_bound[1] + '\n')
                # add input parasitic capacitor
                netlist.writelines(
                    'C_input_' + str(int(idx)) + ' (net' + node_pair[node[1]] + ' 0) capacitor c=' + instance_val[0] +
                    node_pair[node[0]] + node_pair[node[1]] + '/6.28*5p' + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[additional_node[0]] + node_pair[node[0]] + ' (net' + node_pair[
                        additional_node[0]] + ' 0 net' + node_pair[node[0]] + ' 0) ' + instance[0] + ' ' + instance_val[
                        0] + '=' + instance_val[0] + node_pair[additional_node[0]] + node_pair[node[0]] + unit[
                        0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[additional_node[0]] + node_pair[node[0]] + ' 0.01 ' +
                    bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' (net' + node_pair[
                        additional_node[0]] + ' net' + node_pair[node[1]] + ') ' + instance[1] + ' ' + instance_val[
                        1] + '=' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[
                        1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.01 ' +
                    bound[1] + '\n')

                netlist.writelines(
                    additional_ins_head[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[0] + ' ' + additional_ins_val[0] + '=' +
                    additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + '/' + instance_val[
                        0] + node_pair[additional_node[0]] + node_pair[node[0]] + additional_ins_unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 40 ' +
                    additional_ins_bound[0] + '\n')
                netlist.writelines(
                    additional_ins_head[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[1] + ' ' + additional_ins_val[1] + '=' +
                    additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + additional_ins_unit[
                        1] + '\n')
                tmp_conf.writelines('des_var ' + additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(
                    int(idx)) + ' 0.5 ' + additional_ins_bound[1] + '\n')
                # add input parasitic capacitor
                netlist.writelines(
                    'C_input_' + str(int(idx)) + ' (net' + node_pair[node[0]] + ' 0) capacitor c=' + instance_val[0] +
                    node_pair[additional_node[0]] + node_pair[node[0]] + '/6.28*5p' + '\n')
        elif 17 <= x <= 24:
            if x % 2 != 0:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[node[0]] + ' net' +
                    node_pair[node[1]] + ') ' + instance[0] + ' ' + instance_val[0] + '=' + instance_val[0] + node_pair[
                        node[0]] + node_pair[node[1]] + unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[0] + '\n')
                netlist.writelines(instance_head[1] + node_pair[node[0]] + node_pair[node[1]] + ' (net' + node_pair[
                    node[0]] + ' 0 net' + node_pair[node[1]] + ' 0) ' + instance[1] + ' ' + instance_val[1] + '=' +
                                   instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + unit[1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[node[0]] + node_pair[node[1]] + ' 0.01 ' + bound[1] + '\n')

                netlist.writelines(
                    additional_ins_head[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[0] + ' ' + additional_ins_val[0] + '=' +
                    additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + '/' + instance_val[
                        1] + node_pair[node[0]] + node_pair[node[1]] + additional_ins_unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 40 ' +
                    additional_ins_bound[0] + '\n')
                netlist.writelines(
                    additional_ins_head[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[1] + ' ' + additional_ins_val[1] + '=' +
                    additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + additional_ins_unit[
                        1] + '\n')
                tmp_conf.writelines('des_var ' + additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(
                    int(idx)) + ' 0.5 ' + additional_ins_bound[1] + '\n')
            else:
                netlist.writelines(
                    instance_head[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' (net' + node_pair[
                        node[0]] + ' net' + node_pair[additional_node[0]] + ') ' + instance[0] + ' ' + instance_val[
                        0] + '=' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + unit[
                        0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[0] + node_pair[node[0]] + node_pair[additional_node[0]] + ' 0.01 ' +
                    bound[0] + '\n')
                netlist.writelines(
                    instance_head[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' (net' + node_pair[
                        additional_node[0]] + ' 0 net' + node_pair[node[1]] + ' 0) ' + instance[1] + ' ' + instance_val[
                        1] + '=' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + unit[
                        1] + '\n')
                tmp_conf.writelines(
                    'des_var ' + instance_val[1] + node_pair[additional_node[0]] + node_pair[node[1]] + ' 0.01 ' +
                    bound[1] + '\n')

                netlist.writelines(
                    additional_ins_head[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[0] + ' ' + additional_ins_val[0] + '=' +
                    additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + '/' + instance_val[
                        1] + node_pair[additional_node[0]] + node_pair[node[1]] + additional_ins_unit[0] + '\n')
                tmp_conf.writelines(
                    'des_var ' + additional_ins_val[0] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' 40 ' +
                    additional_ins_bound[0] + '\n')
                netlist.writelines(
                    additional_ins_head[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + ' (net' + node_pair[
                        additional_node[0]] + ' 0) ' + additional_ins[1] + ' ' + additional_ins_val[1] + '=' +
                    additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(int(idx)) + additional_ins_unit[
                        1] + '\n')
                tmp_conf.writelines('des_var ' + additional_ins_val[1] + node_pair[additional_node[0]] + '_0' + str(
                    int(idx)) + ' 0.5 ' + additional_ins_bound[1] + '\n')
        else:
            print('error topo input !')

    netlist.writelines('.ends')
    netlist.close()
    tmp_conf.close()
