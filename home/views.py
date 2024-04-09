from django.shortcuts import render
from .models import RecommendedMusic

def home(request):
    recommendations = None
    if request.method == 'POST':
        genre = request.POST.get('genre')
        artist_name = request.POST.get('artist_name')
        
        if genre and artist_name:
            # Mapping of starting few letters to full genre names
            genre_mapping = {
                'rom': 'romantic',
                'sad': 'sadful',
                'cheer': 'cheerful',
                'senti': 'sentimental',
                'Nost': 'Nostalgic',
                'pass': 'Passionate',
                'soul': 'Soulful'
            }
            # Check if the input genre matches the starting few letters of any genre
            matched_genre = None
            for key, value in genre_mapping.items():
                if genre.lower().strip().startswith(key):
                    matched_genre = value
                    break
            # If no exact match is found, default to the input genre
            if not matched_genre:
                matched_genre = genre.lower().strip()
            
            # Query the database for songs based on genre and artist name
            recommendations_queryset = RecommendedMusic.objects.filter(genre__icontains=matched_genre, artist_name__icontains=artist_name)
            # Create a set to store unique song names
            unique_song_names = set()
            # Filter out the input song and remove duplicates
            input_song_name = artist_name.lower().strip()
            recommendations = []
            for song in recommendations_queryset:
                song_name = song.track_name.lower().strip()
                if song_name != input_song_name and song_name not in unique_song_names:
                    recommendations.append(song)
                    unique_song_names.add(song_name)
        
        elif genre and not artist_name:
            # If only genre is provided
            # Mapping of starting few letters to full genre names
            genre_mapping = {
                'rom': 'romantic',
                'sad': 'sadful',
                'cheer': 'cheerful',
                'senti': 'sentimental',
                'Nost': 'Nostalgic',
                'pass': 'Passionate',
                'soul': 'Soulful'
            }
            # Check if the input genre matches the starting few letters of any genre
            matched_genre = None
            for key, value in genre_mapping.items():
                if genre.lower().strip().startswith(key):
                    matched_genre = value
                    break
            # If no exact match is found, default to the input genre
            if not matched_genre:
                matched_genre = genre.lower().strip()
            
            # Query the database for songs based on genre
            recommendations_queryset = RecommendedMusic.objects.filter(genre__icontains=matched_genre)
            recommendations = [{'track_name': song.track_name, 'artist_name': song.artist_name, 'genre': song.genre} for song in recommendations_queryset]
            
        elif artist_name and not genre:
            # If only artist name is provided
            # Query the database for songs of that artist
            recommendations_queryset = RecommendedMusic.objects.filter(artist_name__icontains=artist_name)
            recommendations = [{'track_name': song.track_name, 'artist_name': song.artist_name, 'genre': song.genre} for song in recommendations_queryset]
            
    return render(request, 'home.html', {'recommendations': recommendations})
