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

        # The files used for scribe.
        self.watch      = ["You need to watch", self.path + "watch.lst"]
        self.viewing    = ["You're watching", self.path + "viewing.lst"]
        self.finished   = ["You finished", self.path + "finished.lst"]
        
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

    def actionValidate(self, single=True, length=0, argument_validation=[0, ""], 
                       succes=None, succesarg=None, failure=None, failurearg=None):
        
        """
        Validate the argument(s) given by the user and-
        weigh this with the other parameters.
        """
        
        # 'single' tells us if we need to check at only the length or-
        # Perform a second check on the argument.
        # ;; Supported values: Boolean.

        # 'length' is the length the arguments given when running scribe.
        # ;; Supported values are: List.
        
        # 'argument_validation' compares the location and the string and sees-
        # if they match. If they do not it will break out of it and return 'failure'

        # 'succes' is what to do if the previous parameters decided they match.
        # ;; Supported values: Function.
        
        # 'succesarg' is the argument for the previous submitted function.
        # ;; Supported values: String, variables, list.

        # 'failure' is optional and does what executed when the parameters not match.
        # ;; Support values: Function.
        # ;; Leaving this empty will execute a return.
        
        # 'failurearg' is the argument for the previous submitted function
        # ;; Supported values: String, variables, list.
        
        if succes == failure and failurearg != None:
            try: failure(failurearg) if failurearg != None else failure(); return
            except: return
        # Prevent duplicates by comparing the two set functions.

        try:
            if single:
                if len(self.arguments) == length:
                    succes(succesarg) if succesarg != None else succes(); return
                else: failure(failurearg) if failurearg != None else failure(); return
            elif not single:
                if len(self.arguments) == length:
                    for value in argument_validation:
                        if self.arguments[value[0]] == value[1].lower(): pass
                        else: failure(failurearg) if failurearg != None else failure(); return
                    succes(succesarg) if succesarg != None else succes(); return
                else: failure(failurearg) if failurearg != None else failure(); return
        except: return

        # 'except: return' is a default fallback for whenever things don't go-
        # according to plan. It is most of the times replaced by the 'failure'.

    def actionOptarg(self):
        
        """
        Function to use the arguments set by 'actionValidate' and order these.
        """
        try: self.actionValidate(True, 0, succes=self.actionError)
        except: return
        
        try: self.actionValidate(False, 1, [[0, "-watch"]], self.actionList, self.watch)
        except: return
        
        try: self.actionValidate(False, 1, [[0, "-viewing"]], self.actionList, self.viewing)
        except: return
        
        try: self.actionValidate(False, 1, [[0, "-finished"]], self.actionList, self.finished)
        except: return

        try: self.actionValidate(False, 2, [[0, "-view"]], self.actionMove, [self.watch[1], self.viewing[1]])
        except: return

        try: self.actionValidate(False, 2, [[0, "-finish"]], self.actionMove, [self.viewing[1], self.finished[1]])
        except: return

        try: self.actionValidate(False, 3, [[0, "-add"], [1, "-v"]], self.actionAdd, [self.arguments[2], self.viewing[1]])
        except: return
        
        try: self.actionValidate(False, 3, [[0, "-add"], [1, "-w"]], self.actionAdd, [self.arguments[2], self.watch[1]])
        except: return
        
        try: self.actionValidate(False, 3, [[0, "-add"], [1, "-f"]], self.actionAdd, [self.arguments[2], self.finished[1]])
        except: return

        try: self.actionValidate(False, 3, [[0, "-remove"], [1, "-v"]], self.actionRemove, [self.arguments[2], self.viewing[1]])
        except: return
        
        try: self.actionValidate(False, 3, [[0, "-remove"], [1, "-w"]], self.actionRemove, [self.arguments[2], self.watch[1]])
        except: return
 
        try: self.actionValidate(False, 3, [[0, "-remove"], [1, "-f"]], self.actionRemove, [self.arguments[2], self.finished[1]])
        except: return
  
    def actionList(self, sort):
        """
        We read the given file and return the contents in a nice viewable list.
        """
        # 'sort' is the list presented to the function used to read

        # We try try to open a file and strip its contents through a '\n' filter.
        # It will give us every line in the files on a place in the list.
        try: stash = [line.strip() for line in open(sort[1])]
        
        # Except this when it goes wrong 
        # ;; If for some fucking reason the file doesnt exist.
        except: print "The requested path seems to be unavailable."; return
        
        # How many does the user have to watch?
        print "%s %i anime(s)"%(sort[0],len(stash)) 
        
        # All the animes he/she is watching in list format.
        for val in xrange(1, len(stash) + 1):
            print "[%i] - %s"%(val, stash[val - 1])
        
        # Default return to escape breaking outside of the function 
        return

    def actionMove(self, lists=[]):
        try: watch_stash = [line.strip() for line in open(lists[0])]       
        except: print "The requested path seems to be unavailable."; return
        try: view_stash = [line.strip() for line in open(lists[1])]       
        except: print "The requested path seems to be unavailable."; return
        
        for x in xrange(0, len(watch_stash)):
            if watch_stash[x] in view_stash:
                print "We've detected duplicates."    
                return

        self.actionRemove([self.arguments[1], lists[0]])
        self.actionAdd([self.arguments[1], lists[1]])

    def actionAdd(self, listing=[]):
        """
        Used to add anime to an list.
        """

        try: stash = [line.strip() for line in open(listing[1])]
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(stash)):
            if stash[val] == listing[0]:
                print "You already have this added!"
                return 
        stash.append(listing[0])
        with open(listing[1], "w") as f:
            for val in xrange(0, len(stash)):
                f.write(stash[val] + "\n")
        f.close()
  
    def actionRemove(self, listing=[]):
        """
        Used to remove anime from an list.
        """

        try: stash = [line.strip() for line in open(listing[1])]
        except: print "The requested path seems to be unavailable."; return
        for val in xrange(0, len(stash)):
            if stash[val] == listing[0]: 
                del stash[val] 
                break    
        with open(listing[1], "w") as f:
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






























