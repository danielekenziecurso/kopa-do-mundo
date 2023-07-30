from django.forms import model_to_dict
from rest_framework.views import status, Request, Response, APIView
from exceptions import *

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
