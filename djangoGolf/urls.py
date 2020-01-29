
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

import index.views
import place.views
import next.views
import pairing.views
import score.views

urlpatterns = [
    path('',          index.views.IndexTemplateView.as_view()),
    path('index/',    index.views.IndexTemplateView.as_view()),
    path('place/',    place.views.PlaceTemplateView.as_view()),
    path('next/',     next.views.NextTemplateView.as_view()),
    path('pairing/',  pairing.views.PairingTemplateView.as_view()),
    path('pairing/1', pairing.views.PairingTemplateView.as_view()),
    path('score/',    score.views.ScoreTemplateView.as_view()),
    url(r'^pairing/', pairing.views.PairingTemplateView.as_view()),
    url(r'^score/',   score.views.ScoreTemplateView.as_view()),
]
