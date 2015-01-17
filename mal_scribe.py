#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 mvdw
#
# Distributed under terms of the MIT license.

# Default publicly available modules required.
import ConfigParser, random, getopt, sys, math
import xml.etree.ElementTree as ELY

# Costum modules required to run the following script.
try:
    import requests
except ImportError as e:
    print "%s.\n $ 'pip install requests'"%e;sys.exit()

try: 
    from terminaltables import AsciiTable
except ImportError as e:
    print "%s.\n $ pip install terminaltables"%e;sys.exit()

class Table():
    def __init__(self, title="", headings="", content=""):
        self.title  = self.Title(title)
        #self.headings = self.Headings()
        self.content = self.Content(content)

    def Title(self, argv):
        '''
        Limit the length to 32 and reduce it if it exceeds.
        '''
        if len(argv) >= 32: 
            return "%s-"%argv[:32]
        else: 
            return argv

    def Headings(self, argv):
        pass

    def Content(self, argv):
        words = sentence = text = []
        
        for string in argv:
            # Put all the words in a words array.
            words = string.split()
            print words
            for x in xrange(0, 40):
                try:
                    sentence.append(words[x])
                except:
                    break
        text.append(' '.join(sentence))
        sentence = []

        #     sentence = []
        #     for x in xrange(0, 40):
        #         try: 
        #             print words[x]
        #             sentence.append(words[x])
        #         except: break
        #     sentence.append("-\n")    
        # text.append(' '.join(sentence))
        print text

            #newlines = int(math.floor(len(value)/60))
            #for x in xrange(0, newlines):
            #    newval.append()value[:(60 * newlines - (x * 60))]
            #    print '\n'
        # return arr

    def test(self):
        pass

class MyAnimeList():
    def __init__(self):
        self.lst = 'lg.lst'

        self.error = "Something went wrong, Are you sure you did it right?"

        self.Reader = ConfigParser.ConfigParser()
        self.Reader.read(self.lst)

        # Bypass MAL Api.
        self.headers = {
                'User-Agent':'' 
                }
        
        self.http = requests.Session()
        pass

    def Optarg(self):
        pass

    def Verify(self):    
        # The session/client.
        self.client = self.http.get(
                'http://myanimelist.net/api/account/verify_credentials.xml',
                auth=('', ''), headers=self.headers)

        tree = ELY.fromstring(self.client.text)
                
        if self.client.status_code == requests.codes.ok:
            print "The user '%s' has succefully verified, (%s)"%(tree[1].text, tree[0].text)
        else: return

    def Search(self, search,
               xid=False,        title=True,     english=False, 
               score=True,       xtype=False,    episodes=True,    
               synonyms=False,   status=True,    start_date=False, 
               end_date=False, synopsis=False,    synopsis_length=140, 
               image=False):
        
        '''
        'False' will not show, whilst 'True' does show.
        '''

        # Stash all the values and bind them to a number (Location)
        attr = [
            [0, ['Id', xid]],
            [1, ['Title', title]],
            [2, ['English', english]],
            [3, ['Synonyms', synonyms]],
            [4, ['Episodes', episodes]],
            [5, ['Score', score]],
            [6, ['Type', xtype]],
            [7, ['Status', status]],
            [8, ['Start date', start_date]],
            [9, ['End date', end_date]],
            [10,['Synopsis', synopsis]],
            [11,['Image', image]]
        ]

        # Integer.
        # print [0]
        
        # String.
        # print [1][0]
        
        # Boolean
        # print [1][1]

        # table = []

        cols = []

        # for index in attr:
        #     if index[1][1]:
        #         table.append(index[1][0])
        #     cols.append(index[0])
        # row = ", ".join(table)


        wow = Table(content=[])
        wow.Content(["hi", 'wow spooky wow spookywow spookywow spookywow spookywow spookywow spookywow spookywow spookywow spookywow spookywow spookywow spookywow spooky'])

        tdata = [
            ['Hey', 'WOWWW!'],
            ['THIS IS A LINE', 'ANOETHER LINEANOETHER LINEANOETHER LINEANOETHER LINEANOETHER LINEANOETHER\nLINEANOETHER LINEANOETHER LINEANOETHER \nLINEANOETHER LINEANOETHER LINEANOETHER LINE'],
            ['THIS IS A LINE', 'MITNIDSSHEHS']
            ]

        table = AsciiTable(tdata)

        # print table.table
           
        self.show = self.http.get(
                'http://myanimelist.net/api/anime/search.xml?q=Kill la kill',
                auth=('', ''),headers=self.headers)

        tree = ELY.fromstring(self.show.text)

        for x in xrange(0, len(tree)):
            anime = []
            for y in cols:
                if len(tree[0][y].text) <= 6:
                    anime.append("%s\t\t"%tree[x][y].text)    
                else:
                    anime.append("%s\t"%tree[x][y].text)
            #print "".join(anime)
        #print self.show.text

Scribe = MyAnimeList()

Scribe.Search('')

