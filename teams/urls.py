from django.urls import path
from .views import TeamView, TeamDetailVieaw


urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamDetailVieaw.as_view())
]