from django import forms

class MusicRecommendationForm(forms.Form):
    music_recommendation = forms.CharField(label='Music Recommendation', max_length=100)
