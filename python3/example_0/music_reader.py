#!/usr/bin/env python3

import pickle, time

class Song:

    def __init__(self, title, length_in_seconds, singer):
        self.title = title
        self.length_in_seconds = length_in_seconds
        self.singer = singer

track1 = Song("Happy Birthday", "37", "Everyone")

# Write track metadata to file
pickle.dump(track1, open('track_file','wb'))

time.sleep(3)

loaded_track = pickle.load(open('track_file','rb'))

print(loaded_track.title)