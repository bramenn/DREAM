from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Medico
from app.views import MedicoSerializer


@api_view(['GET'])
def medico_api_view(request,pk):

	if request.method == 'GET':

		medico = Medico.objects.filter(id=pk).first()
		if medico:
			medico_serializer = MedicoSerializer(medico)
			return Response(medico_serializer.data, status=status.HTTP_200_OK)
		return Response({'message':'noticia no encontrado'}, status=status.HTTP_400_BAD_REQUEST)