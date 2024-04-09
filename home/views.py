from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MusicRecommendationForm
from .models import RecommendedMusic  # Import your model

def home(request):
    album_name = None
    singer_name = None
    if request.method == 'POST':
        form = MusicRecommendationForm(request.POST)
        if form.is_valid():
            music_name = form.cleaned_data['music_recommendation']
            # Query the database for songs with the given name
            try:
                song = RecommendedMusic.objects.filter(track_name__iexact=music_name).first()
                if song:
                    album_name = song.album_name
                    singer_name = song.artist_name
                    # Print album and singer names on console
                    print(f"Album: {album_name}, Singer: {singer_name}")
                else:
                    print(f"No song found with the name '{music_name}'.")
            except RecommendedMusic.DoesNotExist:
                print(f"No song found with the name '{music_name}'.")

            # Render the template with the form and the album and singer names
            return render(request, 'home.html', {'form': form, 'album_name': album_name, 'singer_name': singer_name})
    else:
        form = MusicRecommendationForm()
    return render(request, 'home.html', {'form': form, 'album_name': album_name, 'singer_name': singer_name})
