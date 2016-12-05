#!/usr/bin/env python

import sys
import re

class Subvolume(object):
  def __init__(self, line, id, gen, top_level, path):
    self.line = line.rstrip()
    self.id = id
    self.gen = gen
    self.top_level = top_level
    self.path = path
    self.children = []

  def __str__(self):
    return '{} {} {} {}'.format(self.id, self.gen, self.top_level, self.path)

p = re.compile('^ID\s+(\d+)\s+gen\s+(\d+)\s+top level\s+(\d+)\s+path\s+(.*?)$')

root = Subvolume('ID 5', '5', '-', '-', '-')
dict = {'5': root}

for line in sys.stdin:
  m = p.match(line)
  t = m.group(1, 2, 3, 4)
  subvolume = Subvolume(line, *t)
  #print subvolume
  dict[subvolume.id] = subvolume
  parent = dict[subvolume.top_level]
  parent.children.append(subvolume)

def walk(subvolume, level=0):
  print '|   '*(level-1) + '|-- '*(0 if level<1 else 1) + str(subvolume.line)
  for child in subvolume.children:
    walk(child, level+1)
 
walk(root)
