#!/usr/bin/env python3

#For Savannah's research. This script will:
# Check to make sure no two passcodes are not 5 or 6 characters in a row in similarity (4 > ok) but also not 1234_6 or 1_23456

import argparse
import sys,os
import subprocess
import shutil
import pandas as pd
import numpy as np

#Command line options
parser = argparse.ArgumentParser(description= 'Check to see if any passcode is too similar')
parser.add_argument("-f", "--file",
								type=str,
								help="Input file with all passcodes")

parser.add_argument("-o", "--output",
								type=str,
								help="Output name",
								default="Out.csv")

args = parser.parse_args()
input = args.file
output = args.output

df = pd.read_csv(input, error_bad_lines=False)
coln = list(df.columns)
first = []
second = []
for index,row in df.iterrows():
    for id in df[coln[0]]:
        n = 0
        if (row[0][0]) == id[0]:
            n = n+1
        if (row[0][1]) == id[1]:
            n = n+1
        if (row[0][2]) == id[2]:
            n = n+1
        if (row[0][3]) == id[3]:
            n = n+1
        if (row[0][4]) == id[4]:
            n = n+1
        if (row[0][5]) == id[5]:
            n = n+1
        if (row[0][0:5] == id[1:6]):
            n = n+5
        if (row[0][1:6] == id[0:5]):
            n = n+5
        if row[0] == id:
            s = 1
        elif n >= 5:
            print(row[0] + " is too similar to " + id)
            first.append(row[0])
            second.append(id)

similars = pd.DataFrame()
similars['First'] = first
similars['Second'] = second
print(similars)

similars = similars.loc[pd.DataFrame(np.sort(similars[['First','Second']],1),index=similars.index).drop_duplicates(keep='first').index]

similars.to_csv(output, sep=',', index=False)