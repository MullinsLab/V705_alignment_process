#!/usr/bin/python

# align sequences via Muscle
# Wenjie Deng
# 2021-10-29

import os
import argparse

def main(infile, outfile):
    print("input: " + infile)
    print("output: " + outfile)
    os.system("muscle -quiet -in "+infile+" -out "+outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="input sequence fasta file")
    parser.add_argument("outfile", help="output aligned sequence fasta file")
    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile

    main(infile, outfile)