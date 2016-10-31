# -*- coding: utf-8 -*-


import MyHTMLParser
import SpotifyAPI
from time import localtime, strftime


selectTrackList = False

if selectTrackList == True:
    
    playlistAddress = 'http://www.youtube.com/playlist?list=PLILQ9EPFNDtfUCEyXafekiWml5K8XqCve&feature=mh_lolz'
    trackList = []


    test = MyHTMLParser.trackNameList(playlistAddress)
    test.downloadPlaylist()

    track = test.trackList
    
else:
    trackList = []
    trackUnNum = [
          
'cat power - wish I was here',
'allie moss - wait it out',
'marianne faithfull - falling back',
'the shins - so now what',
'bon iver - heavenly father',
'angelo badalamenti - love theme from twin peaks',
'the head and the heart - no one to let you down',
'the black keys - in our prime'

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




