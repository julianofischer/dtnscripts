#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# Juliano Fischer Naves
# julianofischer at gmail dot com
# 2015, Oct. 13

'''
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("inputFile",help="The input raw data to convert (target file).", type=str)
parser.add_argument("--lastNode",help="The last node. Nodes with higher Ids will be ignored.", type=int, required=False, nargs='?', default=9999999)
parser.add_argument("--output",help="The output file.", type=str, required=False, nargs='?', default="output.txt")

args = parser.parse_args()

last_node = args.lastNode
input_file = args.inputFile
output_file = args.output


def main():
    thelist = []
    with open(input_file) as f:
        thelist = [list(map(int,x.split())) for x in f.readlines()]

    thelist = sorted(thelist, key=lambda line : line[2])

    other_list = []

    initial_time = int(thelist[0][2]) #in order to convert timestamp to simulation time

    for l in thelist:
        from_node = int(l[0])-1 #minus 1 because ids in rollernet raw data starts with 1 
                            #and in ONE it starts with 0
        to_node = int(l[1])-1
        init_time = int(l[2]) - initial_time
        end_time = int(l[3]) - initial_time

        if from_node <= last_node and to_node <= last_node:
            connection_beginning = [str(init_time), "CONN", str(from_node), str(to_node), "up"]
            connection_end = [str(end_time), "CONN", str(from_node), str(to_node), "down"]
            other_list.append(connection_beginning)
            other_list.append(connection_end)

    with open(output_file,'w') as f:
        for l in other_list:
            f.write("\t".join(l)+"\n")

if __name__ == "__main__":
    main()
