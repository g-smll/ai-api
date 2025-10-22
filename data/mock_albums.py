from typing import List, Dict

ALBUMS: List[Dict] = []
_genres = ["Pop", "Rock", "Jazz", "Hip-Hop", "Classical"]

for i in range(100):
    singer_idx = (i % 10) + 1
    genre = _genres[i % len(_genres)]
    ALBUMS.append({
        "id": i + 1,
        "singerName": f"Singer {singer_idx}",
        "albumName": f"Album {i + 1}",
        "releaseDate": f"2021-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        "genre": genre,
    })