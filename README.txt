markers-range-to-m3u converts .CSV file with ranged markers (from Audition)
to .m3u with corresponding playback/pause markers for VLC.

Usage:
> python markers-range-to-m3u filename.csv

Output:
filename.m3u is generated. Also prints:
Generating filename.m3u...
Done. 4 pairs written


Input example:
Name	Start	Duration	Time Format	Type	Description
Marker 06	0:12.344	0:02.093	decimal	Cue	
Marker 08	1:04.608	0:02.309	decimal	Cue	
Marker 10	1:03:51.766	0:08.878	decimal	Cue	
Marker 12	1:04:00.645	0:04.331	decimal	Cue	


Desired output example:

#EXTM3U   
#EXTINF:0, 0:12.344
#EXTVLCOPT:play-and-pause
#EXTVLCOPT:start-time=12.344
#EXTVLCOPT:stop-time=14.437
filename
//
#EXTINF:0, 1:04.608
#EXTVLCOPT:play-and-pause
#EXTVLCOPT:start-time=64.608
#EXTVLCOPT:stop-time=66.918
filename
//
#EXTINF:0, 1:03:51.766
#EXTVLCOPT:play-and-pause
#EXTVLCOPT:start-time=3831.766
#EXTVLCOPT:stop-time=3840.645
filename
//
#EXTINF:0, 1:04:00.645
#EXTVLCOPT:play-and-pause
#EXTVLCOPT:start-time=3840.645
#EXTVLCOPT:stop-time=3844.946
filename
//