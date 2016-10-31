# -*- coding: utf-8 -*-


import MyHTMLParser
import SpotifyAPI
from time import localtime, strftime


selectTrackList = False
needTrackSort = True


if selectTrackList == True:
    

    playlistAddress = 'http://www.youtube.com/playlist?list=PL_5JSyF0vTMQfLQ31LI06lrrFIxHL_3LL'
    trackList = []


    test = MyHTMLParser.trackNameList(playlistAddress)
    test.downloadPlaylist()

    track = test.trackList
    
else:
    
    if needTrackSort == True:
        trackList = []
        trackUnNum = []
        AtelierList = '''Amazonics - Let's Spend The Night Together
Washed Out - All I Know
Lapslay - 8896
Jeanne
Jeanne
Koop - Waltz For Koop
Freedom Dub - Sympathy For The Devil
Viet Cong
Maciej Maleńczuk - St. James Infirmary
Bob Dylan - Blind Willie McTell
SBB - Singer
The Wedding Present - My Favourite Dress /Live BBC Radio 1/
Associates /Live BBC Radio 1/
Fucked Up - Queen Of Hearts
Florence & The Machine - What Kind Of Man
Jeanne
The Beatles - A Day In The Life
Bob Dylan - Scarlet Town
Bob Dylan - That Lucky Old Sun
Duke Ellington & Louis Armstrong - Duke's Place
Dual Sessions - Ruby Tuesday
The White Stripes - I Just Don't Know What To Do With Myself
Dusty Springfield - I Just Don't Know What To Do With Myself
Aretha Franklin - I Say A Little Prayer
Lush - Shut up
Lush - Pudding
Piotr Orzechowski Pianohooligan - Study 1
Piotr Orzechowski Pianohooligan - Study 2
Piotr Orzechowski Pianohooligan - Study 4
Focus - Kindergarten
Jane's Addiction - Tree Days
The National - This Is The Last Time
'''        
        

        
        AtelierList = AtelierList.replace('/', " -")
        AtelierList = AtelierList.replace('&', " ")
        
        
        'AtelierList = " ".join(AtelierList.split())'
        AtelierList = AtelierList.splitlines()
        
        
        for track in AtelierList:
            track = " ".join(track.split())
            trackUnNum.append(track)
        
        print trackUnNum
        
    
    else:
        trackList = []
        trackUnNum = [
        'Heavy Seas Of Love - Albarn Damon',
        'Shot By Both Sides (Original Single Version) - Magazine',
        'The Light Pours Out Of Me - Magazine',
        'A Song From Under The Floorboards - Magazine',
        'Visage - Visage',
        'Fade To Grey - Visage',
        'Christine - Siouxsie  The Banshees',
        'Spellbound - Siouxsie  The Banshees',
        'Melt! - Siouxsie The Banshees',
        'Seattle - Public Image Limited',
        'Same Old Story - Public Image Ltd',
        'God - PIL',
        'Chasing Sheep Is Best Left To Shepherds - Nyman Michael',
        'Memorial - Nyman Michael',
        'The Upside-Down Violin: Slow - Nyman Michael',
        'The Upside-Down Violin: Faster - Nyman Michael',
        'The Upside-Down Violin: Faster Still - Nyman Michael' 
        ]
        
        
    track = {}
    trackNumber =0
    for nameTrack in trackUnNum:
        trackNumber +=1
        track[trackNumber]=nameTrack
        



#track ={ 11: 'Phantogram - When Im Small', 12: 'Jesus Zola, Where Did You Sleep Last Night?', 32: 'Flume - Holdin On', 33: 'Myslovitz - Czerwony notes b\xc5\x82\xc4\x99kitny prochowiec', 34: 'Agnes Obel - The Curse (Berlin Live Session)', 39: 'R\xc3\x81J - Ghost (Official Music Video)'}
#track = {1:'Primal Scream - Rocks (Live From Abbey Road)'}



print track

#Czyszczenie playlisty
reservedName = '[Film usunięty]'

for tr in track.items():
    if '[Film usunięty]' == tr[1]:
        print '---removed '+tr[1]
        del track[tr[0]]
    if '[Film prywatny]' == tr[1]:
        print '---removed '+tr[1]
        del track[tr[0]]  

print track
print '\n\n\n'

api = SpotifyAPI.SpotifyAPI()

api.trackReWrite = False


for tr in track.items():
    trackList.append( api.searchTrack(tr[1], len(trackList) ) )
    

print trackList

logfile = open("playlist.log", 'w')
logfile.write('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
logfile.write('--------------------------------------------\n')
logfile.write(strftime("%a, %d %b %Y %H:%M:%S \n", localtime()))
logfile.write('--------------------------------------------\n')


ileTrack = 0

for test in trackList:
    if test['artist'] == None:
        logfile.write('\n--- NOT FOUND : '+test['quary'])
        continue
    ileTrack +=1
    logfile.write('\nTrack nr: '+ str(ileTrack))
    logfile.write('\n'+'\tZapytanie: \t'+test['quary'])
    logfile.write('\n\tOdpowiedz: \t'+test['artist']+'\t'+test['name']+'\t'+test['popular'])
    #logfile.write('\n\t \t'+test['territories'])
    
    print test["href"]

wynik = (float(ileTrack)/float(len(trackList)))*100

logfile.write('\n\n--------------------------------------------')
logfile.write('\n Statystyki : \n\tZnaleziono '+str(ileTrack)+'\\'+str(len(trackList)) +' ('+str(wynik)+'%)')

logfile.write("\n\nLISTA: \n")
for mTrack in trackList:
    if mTrack['artist'] == None:
        
        continue
    logfile.write("\n"+mTrack["href"])

logfile.write('\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n')
logfile.close()

tracklog = open('track.log', 'a')
for mTrack in trackList:
    if mTrack['artist'] == None:
        continue
    tracklog.write("\n"+mTrack["href"])

tracklog.write('\n')
tracklog.close()
ileTrack1 =0
lostStr = ''

for mTrack in trackList:
    if mTrack['artist'] == None:
        ileTrack1+=1
        lostStr += '\''+ mTrack['quary']+'\',\n'  
        

trackLostLog = open('trackLost.log','a')
trackLostLog.write('\n')
trackLostLog.write(lostStr)

        
print lostStr
print 'Statystyki : \n\tZnaleziono '+str(ileTrack)+'\\'+str(len(trackList)) +' ('+str(wynik)+'%)'




