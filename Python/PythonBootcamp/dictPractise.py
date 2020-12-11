playlist = {
    'title': 'paragonia bus',
    'author': 'cold steele',
    'songs' : [{
        'title': 'song1',
        'artists': 'art1',
        'albumName': 'alb1',
        'duration': 2.5 
    },{
        'title': 'song2',
        'artists': 'art2',
        'albumName': 'alb2',
        'duration': 3
    }]
}

totalLen = 0
for song in playlist['songs']:
    totalLen += song['duration']

print(totalLen)