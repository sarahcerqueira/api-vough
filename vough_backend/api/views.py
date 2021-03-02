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


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def retrieve(self, request, login=None):

        if login != None:
            gitapi = GithubApi()
            result = gitapi.get_organization(login)

            if result != None:
                org = Organization()
                org.login = login
                org.name = result.get('name')
                org.score = result.get('public_repos') + gitapi.get_organization_public_members(login)
                org.save()
                return Response(serializers.OrganizationSerializer(org).data)
            else:
                return Response(status=404)

        return Response({})

    def destroy(self, request, login=None):
        org = Organization.objects.filter(login=login).delete()
        if org[0] != 0:
            return Response(status=204)
        
        return Response(status=404)