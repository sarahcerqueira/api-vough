from rest_framework import viewsets, status
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi
from api.models import Organization

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet (viewsets.ModelViewSet):

    queryset = models.Organization.objects.all().order_by('-score')
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def retrieve (self, request, login=None):
        """ Se a organização existe, retorna, senão erro 404.
        """
        gitapi = GithubApi()
        result = gitapi.get_organization(login)
        public_members = gitapi.get_organization_public_members(login)

        #Se alguma requisição retornar 403 significa que o GitHub bloqueo temporariamente
        if result == 403 or public_members == 403:
            return Response(status=503)

        #Se a requisição existe salva no banco de dados
        elif result != None:
            org = Organization()
            org.login = login
            org.name = result.get('name')
            org.score = result.get('public_repos') + public_members
            org.save()
            return Response(serializers.OrganizationSerializer(org).data)
        
        return Response(status=404)

    def destroy (self, request, login=None):
        """ Remove organização.
        """
        org = Organization.objects.filter(login=login).delete()

        if org[0] != 0:
            return Response(status=204)
        
        return Response(status=404)
    
    def create (self, request):
        """ Retorna erro ao tenta fazer um POST
        """
        return Response(status=405)

    def update (self, request, login=None):
        """ Retorna erro ao tenta fazer um PUT
        """
        return Response(status=405)

    def partial_update (self, request, login=None):
        """ Retorna erro ao tenta fazer um PATCH
        """
        return Response(status=405)
