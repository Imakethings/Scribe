#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 mvdw
#
# Distributed under terms of the MIT license.

import requests, ConfigParser, random, getopt, sys
import xml.etree.ElementTree as ELY

class MyAnimeList():
    def __init__(self):
        self.lst = 'lg.lst'

        self.error = "Something went wrong, Are you sure you did it right?"

        self.Reader = ConfigParser.ConfigParser()
        self.Reader.read(self.lst)

        # Bypass MAL Api.
        self.headers = {
                'User-Agent':'api-indiv-'
                }
        
        self.http = requests.Session()
        pass

    def Optarg(self):
        pass

    def Verify(self):    
        # The session/client.
        self.client = self.http.get(
                'http://myanimelist.net/api/account/verify_credentials.xml',
                auth=('u', 'p'), headers=self.headers)

        tree = ELY.fromstring(self.client.text)
                
        if self.client.status_code == requests.codes.ok:
            print "The user '%s' has succefully verified, (%s)"%(tree[1].text, tree[0].text)
        else: return
    
    def Search(self, search,
              xid=False, title=True, english=False, episodes=True,
              synonyms=False, status=True, start_date=False, end_date=False,
              synopsis=True, synopsis_length=140, image=False):
        '''
        'False' will not show, whilst 'True' does show.
        '''

        self.show = self.http.get(
                'http://myanimelist.net/api/anime/search.xml?q=Kill la kill',
                auth=('u', 'p'),headers=self.headers)

        print self.show.text

Scribe = MyAnimeList()

#Scribe.Sim()
Scribe.Search('')


