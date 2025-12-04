def solution(genres, plays):
    genreSet = set(genres)
    genreSongs = {genre:[] for genre in genreSet}
    genrePlayCount = {genre:0 for genre in genreSet}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genreSongs[genre].append((i, play))
        genrePlayCount[genre] += play
    
    genreRank = sorted(list(genrePlayCount.items()), key=lambda x:-x[1])
    
    answer = []
    for genre, _ in genreRank:
        songRank = sorted(genreSongs[genre], key=lambda x:(-x[1], x[0]))
        
        for i, _ in songRank[:2]:
            answer.append(i)
            
    return answer