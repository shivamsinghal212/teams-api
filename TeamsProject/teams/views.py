from cerberus import Validator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import TeamMember
from .schema import member_create_schema, member_update_schema


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def team_member(request, pk=None):
    """
    Retrieve, update or delete a code snippet.
    """
    if request.method == 'POST':
        v = Validator(member_create_schema, allow_unknown=False)
        validated = v.validate(request.data)
        if validated:
            data, http_status = TeamMember().insert(data=request.data)
            return Response({'data': data}, status=http_status)
        else:
            return Response({'err': v.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        res = TeamMember().get_members(pk=pk)
        return Response({'data': res}, status=status.HTTP_200_OK)

    if request.method in ['PUT', 'DELETE']:
        if pk:
            try:
                member = TeamMember.objects.get(pk=pk)
            except TeamMember.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            member.remove()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            v = Validator(member_update_schema, allow_unknown=False)
            validated = v.validate(request.data)
            if validated:
                res = member.update_member(data=request.data)
                return Response({'data': res}, status=status.HTTP_200_OK)
            else:
                return Response({'err': v.errors}, status=status.HTTP_400_BAD_REQUEST)


s = {"firstName": "David",
     "lastName": "Jones", "phoneNumber": "+15101234567", "email":
         "test@test.com", "role": 0}
