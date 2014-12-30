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
        # ;; Removing the expanduser will cause python to create a '~' directory.
        # ;; That will without caution mess up your home folder on OSX and Linux.

        # Merely a batch of commands used later on. 
        # ;; Not even sure If I keep these because they caused only trouble.
        self.listCommands   = [ "-watch", "-viewing", "-finished"]
        self.shortCommands  = [ "-w", "W", "-v", "-V", "-f", "-F"]
        self.moveCommands   = [ "-view", "-finish" ] 
        self.manCommands    = [ "-add", "-remove" ]
        self.syncCommmands  = [ "-username", "-password", "-sync" ]
        
        # The files used for scribe.
        self.watch      = ["You need to watch i% more anime(s).", self.path + "watch.lst"]
        self.viewing    = ["You're watching i% anime(s)", self.path + "viewing.lst"]
        self.finished   = ["You finished i% anime(s).", self.path + "finished.lst"]
        
        # Reserve the array where we will stash the argv[] elements.
        self.arguments = []
        
        # Add every element but remove the first which is the file name.
        # This makes it easier to acces and start with 0 by default.
        for argument in argv: 
            self.arguments.append(argument)
        self.arguments.pop(0)
        
    def Main(self):
        """
        Here we run scribe.
        """
        self.actionCreate()

        self.actionOptarg()

    def actionCreate(self):
        
        """
        This code will execute everytime you run this script-
        without this you could mess up badly.
        SEE: 'self.path' for moving the place you stash your files.
        """

        # Do checks on every files every time it is ran to prevent missing file errors.
        
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
        if not os.path.exists(self.watch[1]):
            open(self.watch[1], 'a').close()
        
        if not os.path.exists(self.viewing[1]):
            open(self.viewing[1], 'a').close()
        
        if not os.path.exists(self.finished[1]):
            open(self.finished[1], 'a').close()
        
        # By default return when it is done checking. Resulting in a empty function-
        # if everything exists. 
        
        return

    def actionValidate(self, single=True, length=0, argument=0, 
                       validation=[], succes=None, succesarg=None,
                        failure=None, failurearg=None):
        
        """
        Validate the argument gived by the user and-
        weigh this with the other parameters.
        """
        
        # 'single' tells us if we need to check at only the length or-
        # Perform a second check on the argument.
        # ;; Supported values: Boolean.

        # 'length' is the length the arguments given when running scribe.
        # ;; Supported values are: List.

        # 'argument' is which argument should be checked.
        # ;; Supported values are: Integer.
        
        # 'validation' are the values used to weigh of if the 'argument' matches.
        # ;; Supported values: List or String.
        
        # 'succes' is what to do if the previous parameters decided they match.
        # ;; Supported values: Function.
        
        # 'succesarg' is the argument for the previous submitted function.
        # ;; Supported values: String, variables, list.

        # 'failure' is optional and does what executed when the parameters not match.
        # ;; Support values: Function.
        # ;; Leaving this empty will execute a return.
        
        # 'failurearg' is the argument for the previous submitted function
        # ;; Supported values: String, variables, list.
        
        # EXAMPLES
        # This is a example that only checks the length param.
        #
        # These are both valid examples that will do said function on no arguments.
        # ;; self.actionValidate(True, [0], 0, "Test", self.Test)
        # ;; self.actionValidate(True, [0], succes=self.Test)
        #
        # This is a example for a function that has everything to it.
        # ;; self.actionValidate(True, [1], 0, "Test", self.Test, 'testarg', self.Another)

        try:
            if single:
                if len(self.arguments) in length:
                    try: succes(succesarg)
                    except: return
                else:
                    try: failure(failurearg)
                    except: return 
            elif not single:    
                if len(self.arguments) in length and self.arguments[argument] in validation:
                    try: succes(succesarg)
                    except: return
                else:
                    try: failure(failurearg)
                    except: return 
        except: return

        # 'except: return' is a default fallback for whenever things don't go-
        # according to plan. It is most of the times replaced by the 'failure'.

    def actionOptarg(self):
        
        """
        Function to use the arguments set by 'actionValidate' and order these.
        """
        pass

        self.actionValidate(False, [1], 0, "-watch", self.actionList, self.watch)

        #if   len(self.arguments) in [0]: self.DEFAULT()

        #elif len(self.arguments) in [1] and self.arguments[0] in self.listCommands:
        #    self.actionList(self.getParameter(self.listCommands, 
        #                                      [0, 0 ,0 ], 
        #                                      [self.watch, self.viewing, self.finished],
        #                                      True))

        #elif len(self.arguments) in [2] and self.arguments[0] == self.moveCommands:
        #    self.actionMove

        #elif len(self.arguments) in [3] and self.arguments[0] == self.manCommands[0]:
        #    self.actionAdd(self.getParameter(self.shortCommands,
        #                                    [1,1,1,1,1,1],
        #                                    [self.watch,self.viewing,self.finished],
        #                                    False), self.arguments[2])

        #elif len(self.arguments) in [3] and self.arguments[0] == self.manCommands[1]:
        #    self.actionRemove(self.getParameter(self.shortCommands,
        #                                    [1,1,1,1,1,1],
        #                                    [self.watch,self.viewing,self.finished],
        #                                    False), self.arguments[2])

        #else: self.DEFAULT()

    def actionList(self, sort):
        """
        A nesting of all the listing to size it down a little.
        """
        print sort[1]
        
        stash = [line.strip() for line in open(sort[1])]
        stash = open(sort[1])
        print stash
        # print "The requested path seems to be unavailable."; return
        print sort[0]%len(stash)
        print sort
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
    
    def actionError(self):
        """
        Default string upon failure. /It's never the code, always the user/.
        """

        print """
        Please read the README.md located here:
        https://github.com/Imakethings/Scribe/blob/master/README.MD

        - Thanks in advance.
        """; return

# Make 'Scribe' a holder of the contents from 'Anime()'
Scribe = Anime()

# Run the main code which handles everything 'Scribe' does.
Scribe.Main()






























