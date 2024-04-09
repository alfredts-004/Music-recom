import csv
from datetime import datetime
from home.models import RecommendedMusic

def import_music_data_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            popularity = int(row['Popularity'])
            track_name = row['Track Name']
            release_date = datetime.strptime(row['Release Date'], '%Y-%m-%d').date()
            genre = row['Genre']
            subgenre = row['Subgenre']
            length_seconds = int(row['Length (seconds)'])
            artist_name = row['Artist Name']
            album_name = row['Album Name']

            # Create an instance of RecommendedMusic model
            recommended_music = RecommendedMusic(
                popularity=popularity,
                track_name=track_name,
                release_date=release_date,
                genre=genre,
                subgenre=subgenre,
                length_seconds=length_seconds,
                artist_name=artist_name,
                album_name=album_name
            )
            recommended_music.save()

# Call the function to import data from the CSV file
csv_file_path = 'music_data.csv'  # Update with your CSV file path
import_music_data_from_csv(csv_file_path)
