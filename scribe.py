#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Mirko van der Waal
#
# Scribe - Keep track of anime the easy way.
#
# I suck at this btw.
# Distributed under terms of the MIT license.

from sys import argv
from os.path import expanduser
import os

class Anime():
    def __init__(self):
        # The place Scribe will install itself.
        self.path   = expanduser("~") + "/.config/scribe/"
        
        self.listCommands   = [ "-watch", "-viewing", "-finished"]
        self.shortCommands  = [ "-w", "W", "-v", "-V", "-f", "-F"]
        self.moveCommands   = [ "-view", "-finish" ] 
        self.manCommands    = [ "-add", "-remove" ]
        self.syncCommmands  = [ "-username", "-password", "-sync" ]
        
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
        return

    def handleArguments(self):
        """
        Advanced function to handle arguments set by the script.
        """
        for argument in argv: 
            self.arguments.append(argument)
        self.arguments.pop(0)
        
        # Whenever you don't fill any arguments you get the expected.
        if   len(self.arguments) in [0]: self.DEFAULT()

        elif len(self.arguments) in [1] and self.arguments[0] in self.listCommands:
            self.actionList(self.getParameter(self.listCommands, 
                                              [0, 0 ,0 ], 
                                              [self.watch, self.viewing, self.finished],
                                              True))

        elif len(self.arguments) in [2] and self.arguments[0] == self.moveCommands:
            self.actionMove

        elif len(self.arguments) in [3] and self.arguments[0] == self.manCommands[0]:
            self.actionAdd(self.getParameter(self.shortCommands,
                                            [1,1,1,1,1,1],
                                            [self.watch,self.viewing,self.finished],
                                            False), self.arguments[2])

        elif len(self.arguments) in [3] and self.arguments[0] == self.manCommands[1]:
            self.actionRemove(self.getParameter(self.shortCommands,
                                            [1,1,1,1,1,1],
                                            [self.watch,self.viewing,self.finished],
                                            False), self.arguments[2])

        else: self.DEFAULT()

    def actionList(self, parameter):
        """
        A nesting of all the listing to size it down a little.
        """
        actionSentence = [  "You need to watch %i more anime(s).",
                            "You're watching %i anime(s).",
                            "You finished %i anime(s)." ]

        try: stash = [line.strip() for line in open(parameter[1])]
        except: print "The requested path seems to be unavailable."; return
        print "" + actionSentence[parameter[0]]%len(stash)
        for val in xrange(1, len(stash) + 1):
            print "[%i] - %s"%(val, stash[val - 1])
        return

    def actionMove(self, parameter):
        pass

    def actionView(self):
        """
        Moves an anime from the watch to the viewing list.
        """
        try: watch_stash = [line.strip() for line in open(self.watch[1])]       
        except: print "The requested path seems to be unavailable."; return
        try: view_stash = [line.strip() for line in open(self.viewing[1])]       
        except: print "The requested path seems to be unavailable."; return
        for x in xrange(0, len(watch_stash)):
            if watch_stash[x] in view_stash:
                print "You're already watching this..."
                return
        self.actionRemove(self.watch[1], self.arguments[1])
        self.actionAdd(self.viewing[1], self.arguments[1])

    def actionFinish(self):
        pass

    def actionAdd(self, list_type=None, list_value=None):
        """
        Used to add anime to an list.
        """
        
        try: stash = [line.strip() for line in open(list_type)]
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(stash)):
            if stash[val] == list_value:
                print "You already have this added!"
                return 
        stash.append(list_value)
        with open(list_type, "w") as f:
            for val in xrange(0, len(stash)):
                f.write(stash[val] + "\n")
        f.close()
  
    def actionRemove(self, list_type=None, list_value=None):
        """
        Used to remove anime from an list.
        """
        print list_value

        try: stash = [line.strip() for line in open(list_type)]
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(stash)):
            if stash[val] == list_value: 
                del stash[val] 
                break    
        with open(list_type, "w") as f:
            for val in xrange(0, len(stash)):
                f.write(stash[val] + "\n")
        f.close()
    
    def getParameter(self, values, argument_integer, returns, listing):
        """
        Obtain x parameter and returns the matching file
        """
        num = -1
        for value in values:
            num = num + 1
            # print value, values, argument_integer, returns
            if self.arguments[argument_integer[num]] in value:
                if listing:     return returns[num]
                if not listing: return returns[2][1]

    def DEFAULT(self):
        """
        Default string upon failure. /It's never the code, always the user/.
        """
        print """
        Please read the README.md located here:
        https://github.com/Imakethings/Scribe/blob/master/README.MD

        - Thanks in advance.
        """; return

Scribe = Anime()
Scribe.createScribe()
Scribe.handleArguments()

