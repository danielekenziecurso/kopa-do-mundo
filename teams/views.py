from django.forms import model_to_dict
from rest_framework.views import status, Request, Response, APIView
from exceptions import *
import teams

from utils import data_processing
from .models import Team


class TeamView(APIView):
    def post(self, req: Request) -> Response:
        try:
            data_processing(req.data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

        create_team = Team.objects.create(**req.data)
        converted_team = model_to_dict(create_team)
        return Response(converted_team, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        converted_team = [model_to_dict(team) for team in teams]
        return Response(converted_team, status.HTTP_200_OK)


class TeamDetailVieaw(APIView):
    def get(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except teams.models.Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        converted_team = model_to_dict(found_team)
        return Response(converted_team, status.HTTP_200_OK)

    def patch(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except teams.models.Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        for key, value in req.data.items():
            setattr(found_team, key, value)

        found_team.save()
        converted_team = model_to_dict(found_team)
        return Response(converted_team, status.HTTP_200_OK)

    def delete(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except teams.models.Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        found_team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
