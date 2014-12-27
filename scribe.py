#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Mirko van der Waal
#
# Scribe - Keep track of anime the easy way.
#
# Distributed under terms of the MIT license.

from sys import argv
from os.path import expanduser
import os

class Anime():
    def __init__(self):
        # The place Scribe will install itself.
        self.path   = expanduser("~") + "/.config/scribe/"
        
        # Default action is always none.
        self.action     = None

        # The commands used to return values to the user.
        self.listCommands   = [ "-watch", "-viewing", "-finished" ]
        # The commands used to move values over various lists.
        self.moveCommands   = [ "-view", "-finish" ] 
        # The commands used to manipulate exisiting values.
        self.manCommands    = [ "-add", "-remove" ]
        # The commands used to handle syncing and remote adding with [mal]
        self.syncCommmands  = []
        
        # Here we create the array to store the arguments.
        self.arguments  = []

        # Contains values & paths.
        self.watch      = [0, self.path + "watch.lst"]
        self.viewing    = [1, self.path + "viewing.lst"]
        self.finished   = [2, self.path + "finished.lst"]

    def createScribe(self):
        """
        Create scribe if unexistant.
        """
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            if not os.path.exists(self.watch[1]):
                open(self.watch[1], 'a').close()
            if not os.path.exists(self.viewing[1]):
                open(self.viewing[1], 'a').close()
            if not os.path.exists(self.finished[1]):
                open(self.finished[1], 'a').close()
        else: return

    def handleArguments(self):
        """
        Advanced function to handle arguments set by the script.
        """
        for argument in argv: 
            self.arguments.append(argument)
        self.arguments.pop(0)
        
        if   len(self.arguments) in [0]: self.DEFAULT()
        elif len(self.arguments) in [1] and self.arguments[0] in self.listCommands:
            self.actionList("self.%s"%self.arguments[0].replace("-", ""))

        elif len(self.arguments) in [2] and self.arguments[0] == self.moveCommands[0]:
            self.actionView()

        elif len(self.arguments) in [2] and self.arguments[0] == self.moveCommands[1]:
            self.actionFinish()

        elif len(self.arguments) in [3, 4] and self.arguments[0] == self.manCommands[0]:
            self.actionAdd("", "")

        elif len(self.arguments) in [3, 4] and self.arguments[0] == self.manCommands[1]:
            self.actionRemove("", "")
        else: self.DEFAULT()

    def actionList(self, parameter):
        """
        A nesting of all the listing to size it down a little.
        """    
        parameter = eval(parameter)
        actionSentence = [  "You need to watch %i more anime(s).",
                            "You're watching %i anime(s).",
                            "You finished %i anime(s)." ]

        try: stash = [line.strip() for line in open(parameter[1])]
        except: print "The requested path seems to be unavailable."; return
        print "" + actionSentence[parameter[0]]%len(stash)
        for val in xrange(1, len(stash) + 1):
            print "[%i] - %s"%(val, stash[val - 1])
        return
     
    def actionView(self):
        try: watch_stash = [line.strip() for line in open(self.watch[1])]       
        except: print "The requested path seems to be unavailable."; return
        try: view_stash = [line.strip() for line in open(self.viewing[1])]       
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(watch_stash)):
            pass

    def actionFinish(self):
        pass

    def actionAdd(self, list_type, list_value):
        if list_type == "": list_type = self.getParameter()
        if list_value == "": list_valuue = self.arguments[2]

        try: stash = [line.strip() for line in open(list_type)]
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(stash)):
            if stash[val] == self.arguments[2]:
                print "You already have this added!"
                return 
        stash.append(self.arguments[2])
        with open(self.getParameter(), "w") as f:
            for val in xrange(0, len(stash)):
                f.write(stash[val] + "\n")
        f.close()
  
    def actionRemove(self, list_type, list_value):
        if list_type == "": list_type = self.getParameter()
        if list_value == "": list_value = self.arguments[2]

        try: stash = [line.strip() for line in open(self.getParameter())]
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(stash)):
            if stash[val] == self.arguments[2]: 
                del stash[val] 
                break    
        with open(self.getParameter(), "w") as f:
            for val in xrange(0, len(stash)):
                f.write(stash[val] + "\n")
        f.close()
    
    def getParameter(self):
        if self.arguments[1] in ["-v", "-V"]:
            return self.viewing[1]
        if self.arguments[1] in ["-w", "-W"]:
            return self.watch[1]
        if self.arguments[1] in ["-f", "-F"]:
            return self.finished[1]
    
    def DEFAULT(self):
         print """
        Please read the README.md located here:
        https://github.com/Imakethings/Scribe/blob/master/README.MD

        - Thanks in advance.
        """; return

Scribe = Anime()

Scribe.handleArguments()


















