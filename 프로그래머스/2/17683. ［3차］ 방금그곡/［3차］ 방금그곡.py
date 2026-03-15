def split_musicinfo(musicInfo):
    li = musicInfo.split(",")
    return (time_to_minutes(li[0]), time_to_minutes(li[1]), li[2], li[3])

def time_to_minutes(time):
    h, m = map(int, time.split(":"))
    return 60*h+m

def normalize_melody(melody):
    return (
        melody.replace("C#", "c")
              .replace("D#", "d")
              .replace("F#", "f")
              .replace("G#", "g")
              .replace("A#", "a")
    )
    
    return n_melody
    
def solution(m, musicinfos):
    notes = normalize_melody(m)
    k = len(notes)

    titles = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, melody = split_musicinfo(musicinfo)
        music_notes = normalize_melody(melody)
        
        play_time = (end-start)
        
        if k>play_time:
            continue
    
        s = len(music_notes)
        for i in range(play_time-1):
            
            findMusic = True
            for j in range(k):
                if notes[j]!=music_notes[(i+j)%s]:
                    findMusic = False
                    break
                
            if findMusic:
                titles.append((end-start, idx, title))
                break

    titles.sort(key = lambda x:(-x[0], x[1]))
    
    return "(None)" if not titles else titles[0][2]