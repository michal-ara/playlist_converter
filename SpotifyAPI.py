# -*- coding: utf-8 -*-
from xml.dom import minidom
import urllib


class SpotifyAPI(object):
    
    def __init__(self):
        self.xmlAdress = '' #adres url dla xml
        self.xmlDoc = '' # pobrany dokument
        self.trackReWrite = False # reczne poprawianie adresow
        self.track = {"exist": False, "quary": None, "artist":None,"name":None, "href":None, "popular":None  } #artist,name,address
        
    def correctQuary(self):
        '''
        metoda poprawiajaca adres
        '''
        cl = {'[':']', '(':')'}
        
        for cl1 in cl:
            cStart = self.quaryName().find(cl1)
            if cStart > 0:
                cEnd = self.quaryName().find(cl[cl1])
                if cEnd > 0:
                    cStr = self.quaryName()[cStart:cEnd+1]
                    return self.quaryName().replace(cStr, '').encode('utf-8')
        return ''
                
            
    def reWriteTrack(self):
        '''
        metoda pobierajaca nowy adres z klawiatury
        '''        
        print "brak wyników dla "+self.quaryName()
        nowy = raw_input("podaj: ")
        self.createAdress(nowy)
        self.openAdress()
        
    def searchTrack(self, track, nr):
        '''
        Funkcja wyszukujaca utwory
        '''
        
        self.__init__()
        self.createAdress(track)
        self.openAdress()
        print "Szukana nazwa: "+self.quaryName()
        #print "Liczba wynikow: "+self.totalResults()
        
        if self.totalResults()=='0':
            nQuary = self.correctQuary()
            if len(nQuary) > 1:
                self.createAdress(nQuary)
                print "poprawka automatyczna: " + nQuary
                self.openAdress()
        
        if self.trackReWrite == True :
            if self.totalResults()=='0':
                self.reWriteTrack() # reczne poprawienie adresu
            
            
        
        self.findTrack()
        self.track['nr'] = nr+1
        
        #print self.track
        
        return self.track
        
    
    def createAdress(self, track):
        '''
        Funkcja tworząca adres URL i zapisujaca go do xmlAddress
        '''
        self.xmlAdress = 'http://ws.spotify.com/search/1/track?q='+track
        
    def openAdress(self):
        '''
        Odwieranie adresu URL i pobieranie XML (do xmldoc)
        '''
        sock = urllib.urlopen(self.xmlAdress)
        
        self.xmldoc = minidom.parse(sock).documentElement
        sock.close()
        #print self.xmldoc.toxml()
    
    def __openXml(self):
        '''
        Otwieranie pliku z dysku - funkcja ukryta
        '''
        self.xmldoc = minidom.parse('test.xml')
    
    def findTrack(self):
        '''
        Przeszukiwanie pliku xml i znajdowanie utworów (wzgledem popularności)
        '''
                
        trackNodes = self.xmldoc.getElementsByTagName('track')
        
        self.track["quary"] = self.quaryName()
        mostPopular = 0
        
        
        
        for node in trackNodes:
        
            if mostPopular >= node.getElementsByTagName('popularity')[0].firstChild.data:
                continue
            try:
                self.track["territories"] = self.trackAvailable(node)
            except AttributeError:
                print "AttributeError !!!! "
                self.track["territories"] = '-'
            
            self.track["name"] = node.getElementsByTagName('name')[0].firstChild.data 
            self.track["artist"] = node.getElementsByTagName('artist')[0].childNodes[1].firstChild.data 
            self.track["href"] = node.attributes['href'].value
            self.track["popular"] = node.getElementsByTagName('popularity')[0].firstChild.data
            mostPopular = self.track["popular"]
            self.track['exist'] = True
            print 'Znaleziono : '+ self.track["artist"]+' '+self.track['name']
            
        #print self.track
        
        
        
    def quaryName(self):
        '''
        zwraca nazwe wygenerowanego zapytania z XML
        '''
        return self.xmldoc.getElementsByTagName('opensearch:Query')[0].attributes['searchTerms'].value
        
    def totalResults(self):
        '''
        Zwraca liczbe wyników uzyskanych z jednego zapytania.
        '''
        return self.xmldoc.getElementsByTagName('opensearch:totalResults')[0].firstChild.data
    
    def trackAvailable(self,node,territories = 'PL'):
        '''
        Sprawdza czy utwor dostepny w PL - niewiadomo czy działa! 
        '''
        terr = node.getElementsByTagName('album')[0].getElementsByTagName('availability')[0].childNodes[1].firstChild.data
        return terr
        
        
