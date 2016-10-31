# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import urllib


class trackNameList(dict):
    '''
    Klasa pobierania playlisty, dziedziczy po klasie slownika
    
    '''
    
    trackList = {}
    
    
    def __init__(self, PlaylistUrl=None):
        '''
        metoda init - przypisuje do klucza klasy (dict) adres playlisty
        '''
        dict.__init__(self) # Wywolanie dict
        self["PlaylistUrl"] = PlaylistUrl
        #przypisanie do slownika
        
    def downloadPlaylist(self):
        '''
        metoda pobierania playlisty
        '''
        page = urllib.urlopen(self["PlaylistUrl"])
        #otworzenie strony
        htmlSource = page.read()
        #przeczytanie strony
        page.close()
        #zamkniecie strony
        #htmlSource = '''
        
                    
        Parser = MyHTMLParser()
        #utworzenie obiektu 
        #Parser.feed('<h3 class="video-title-container"><a href="/watch?v=-zLEI9oEHwI&amp;list=PLILQ9EPFNDtfUCEyXafekiWml5K8XqCve&amp;index=42" title="Art Department Presents Martina Topley-Bird featuring Mark Lanegan - Crystalised" class="yt-uix-sessionlink" data-sessionlink="feature=plpp_video&amp;ei=KFFEUr-1BcqOiAbZ-IHYDw"><span class="title video-title" dir="ltr">Art Department Presents Martina Topley-Bird featuring Mark Lanegan - Crystalised</span> </a></h3>')
        #Parser.feed('')
        Parser.feed(htmlSource)
        #nakarmienie klasy analizy strony - uruchamia uchwyty do znacznikow
        
        Parser.close()
        self.trackList = Parser.lista1
        #zamkniecie parsera
    
    def setUrl(self, PlaylistUrl):
        ''' 
        metoda ustawiania adresu
        '''
        self["PlaylistUrl"] = PlaylistUrl
        
    def track(self):
        pass
            
            
                    

class MyHTMLParser(HTMLParser):
    '''nasza klasa parsera - dziedziczy po HTMLParser
    '''
    
    readTag = False #zezwoleie na czytanie zawartosci tagu
    num = 0 # numeracja pobran
    string ='' #nazwa
    lista1 = {} #lista utworow
    
    def handle_starttag(self, tag, attrs):
        ''' 
        metoda obslugujaca wejscie do kazdego tagu
        '''
        if tag == 'span': 
            # wyszukanie tagu SPAN
            if ('class','title video-title') in attrs:
                #jesli tag posiada konkretny atrybut classy 
                self.perReadTag(True)  # zezwol na czytanie zawartosci
                
                
   
    def handle_data(self, data):
        '''
        Metoda obslugujaca dane
        '''
        if self.readTag:
            self.string += data
            # zaobserwowane urywanie nazw tagow dlatego tazdy tag jest sklejany z wielu wywolan tej metody
            

    def handle_endtag(self,tag):
        '''
        Metoda obslugujaca wyjscie z danego tagu
        '''
        if tag == 'span':
            self.perReadTag(False)
            if self.string:
                #jesli pobrano string
                self.num += 1
                #print self.num,".   ", self.string
                self.lista1[self.num] = self.string
                #self.lista1.extend([krotka])
                self.string = '' # wyczyszczenie stringu
            
    def perReadTag(self, read):
        self.readTag = read
