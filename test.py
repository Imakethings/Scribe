#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 mvdw
#
# Distributed under terms of the MIT license.

from sys import argv

val = [[0, "Hi"], [1, "Hi"]]
print val
print enumerate(val[0])

def Hi():
    #while True:
    for value in val:
        try: argv[value[0]] != value[1]
        except:
            print "invalid"

Hi()
