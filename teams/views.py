from rest_framework.views import status, Request, Response, APIView

class TeamView(APIView):
    def post(self, req: Request) -> Response:
        return Response
