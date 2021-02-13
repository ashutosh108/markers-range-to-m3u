import argparse
import csv
import os
import re
import sys

def convert_ranged_markers_csv_to_m3u(csvfile):
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, dialect=dialect)
    
    m3u_filename = os.path.splitext(csvfile.name)[0] + ".m3u"
    wav_filename = os.path.splitext(csvfile.name)[0] + ".wav"
    print("Generating {}...".format(m3u_filename))
    rowcount = 0
    with open(m3u_filename, "w") as m3u:
    #with sys.stdout as m3u:
        for row in reader:
            rowcount += 1
            write_marker_pair(m3u, wav_filename, row['Start'], row['Duration'])
    print("Done. {} pairs written".format(rowcount))
    pass

def parse_hms_as_seconds(hms):
    r = re.compile(r"(?:(?P<h>\d+):)?(?P<m>\d+):(?P<s>\d+\.\d+)")
    m = r.match(hms)
    sec = int(m['m']) * 60 + float(m['s'])
    if m['h'] is not None:
        sec += int(m['h']) * 3600
    if not m:
        raise "can't parse hms: " + hms
    return sec

def write_marker_pair(file, wav_filename, start, duration):
    print("#EXTM3U   ", file=file)
    print("#EXTINF:0, {} ({})".format(start, duration), file=file)
    start_sec = parse_hms_as_seconds(start)
    duration_sec = parse_hms_as_seconds(duration)
    end_sec = start_sec + duration_sec
    print("#EXTVLCOPT:play-and-pause", file=file)
    print("#EXTVLCOPT:start-time={:.3f}".format(start_sec), file=file)
    print("#EXTVLCOPT:stop-time={:.3f}".format(end_sec), file=file)
    print(wav_filename, file=file)
    print("//", file=file)
    pass

def main():
    parser = argparse.ArgumentParser(description="Convert CSV with ranged markers (from Audition) to .m3u with playback/pause markers for VLC")
    parser.add_argument('infile', metavar='file.csv', type=argparse.FileType('r'))

    args = parser.parse_args()
    
    convert_ranged_markers_csv_to_m3u(args.infile)

if __name__ == "__main__":
    main()
