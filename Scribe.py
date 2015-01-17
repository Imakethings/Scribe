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
    def __init__(self, title="", heading="", string_length=32, list_length=8):
        self.string_length = string_length
        self.list_length = list_length
        self.title  = self.Title(title)
        self.heading = self.Heading(heading)

    def Title(self, argv):
        '''
        Limit the length to 32 and reduce it if it exceeds.
        '''
        
        try:
            # This will try to append an integer to a string.
            # If it is a list the append will succeed thus we return.
            argv.append(1)
            print "Don't use lists"; return
        except:
            pass

        # Is the length of the string bigger then the length. (32)
        if len(argv) >= self.string_length: 
            return "%s..."%argv[:self.string_length]
        else: 
            return argv

    def Heading(self, argv):
        '''
        Limit the length of the headings to 16.
        '''
        
        head = []        
        
        for string in argv:
            
            # If the length of string exceeds the length (16)
            if len(string) > (self.string_length/2):
                head.append("%s-"%string[:(self.string_length/2)])
            
            # Just add it other wise
            else:
                head.append(string)
        
        return head
 
    def Newspace(self, argv):
        '''
        Take a list of all strings and convert them to a newspaced format.
        '''

        texts = []

        # See how many strings are given.
        for string in argv:
            words = []
            sentence = []
            text = []

            # Put all the words in a words array.
            words = string.split()
            
            # If the length of the string is bigger then 32. 
            # We're going to need 1 or more \n's.
            if len(words) > self.list_length:
                
                # How many new lines do we need to add?
                newlines = int(math.floor(len(words)/self.list_length))
                
                # +1) Because we don't start with 0.
                # +1) Because we need to loop through the excess characters also.
                for newadd in xrange(1, newlines + 2):
                    
                    # Take portions of 32 out of the list and add a \n.
                    sentence = words[
                        ( self.list_length * (newadd - 1) ):( self.list_length * newadd )
                        ]
                       
                    # Add the combined portion to the list
                    text.append("%s \n"%' '.join(sentence))
                            
                # Remove the last new line character. 
                # text[len(text)-1] = text[len(text)-1].replace("\n", "")
                
                texts.append(''.join(text))
            else:
                texts.append("%s \n"%' '.join(words))

        return texts
  
class MyAnimeList():
    def __init__(self):
        # User credential file.
        self.lst = 'pwd.ini'

        self.error = "Something went wrong, Are you sure you did it right?"

        # Initialize the reader.
        self.Reader = ConfigParser.ConfigParser()
        self.Reader.read(self.lst)

        # Bypass MAL Api.
        self.headers = {
                'User-Agent':''      
                }
        self.http = requests.Session()
         
        # Integer.
        # print [0]
        # String.
        # print [1][0]
        # Boolean
        # print [1][1]

    def Verify(self):    
        '''
        Verify the user.
        '''
        
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
               end_date=False,   synopsis=False, synopsis_length=140, 
               image=False):
        '''
        Make a tableview of the requested terms and their values.
        '''
        
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
        
        # The values for the heading
        heading_values = []
        
        for value in attr:
            if value[1][1]: 
                heading_values.append(value[1][0])
        
        # Lay the connection. 
        self.show = self.http.get(
                'http://myanimelist.net/api/anime/search.xml?q=%s'%search,
                auth=('', ''), headers=self.headers)
 
        tree = ELY.fromstring(self.show.text)
        
        def appendResult(which=1):
            if which > len(tree): which = len(tree)
            
            for root in xrange(0, which):
                this = []
                for value in attr:
                    if value[1][1]:
                        this.append(tree[root][value[0]].text)
                table_data.append(table_nav.Newspace(this))

        # Add the title and the heading elements to the nav.
        table_nav = Table(title = search, heading = heading_values) 
        
        # Add the heading to the table.
        # Append this table to add a row.
        table_data = [table_nav.heading]

        appendResult(500)

        # Build the table and add the title.
        table = AsciiTable(table_data, table_nav.title)

        print table.table

Scribe = MyAnimeList()

#Scribe.Verify()
Scribe.Search('Bleach', xid=True)

