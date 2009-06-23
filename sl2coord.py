#!/usr/bin/env python2.6
""" outputs two files: for labels and features. """
from __future__ import print_function
import os,sys

# +1 1:1 5:10 6:2
# -1 1:-5 3:4 5:9

args = sys.argv[1:]
outbase = args[-1]
out_labels = open("%s.labels" % outbase,'w')
out_feats = open("%s.feats" % outbase, 'w')
print(out_labels, file=sys.stderr)
print(out_feats, file=sys.stderr)
for i,line in enumerate(sys.stdin):
  parts = line.split()
  label = parts.pop(0)
  print(i+1, 1, label,   file=out_labels, sep='\t')
  for fv_pair in parts:
    f,v = fv_pair.split(":")
    print(i+1, f, v,  file=out_feats, sep='\t')
out_labels.close()
out_feats.close()
