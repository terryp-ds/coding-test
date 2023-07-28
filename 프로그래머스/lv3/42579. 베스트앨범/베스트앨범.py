def solution(genres, plays):
    
    genre_dict = dict(zip(set(genres), [0]*len(set(genres))))
    
    for genre, play in zip(genres, plays):
        genre_dict[genre] += play
        
    genre_rank = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
    
    ans = []
    
    for genre, _ in genre_rank:
        genre_music = [i for i, g in enumerate(genres) if g == genre]
        genre_play = [i for i, _ in sorted([(j, plays[j]) for j in genre_music], key=lambda x: x[1], reverse=True)]
        ans.extend(genre_play[:2])
        
        
    return ans
        