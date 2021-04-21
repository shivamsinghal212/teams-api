from django.db import models
from django.db.models import Q
from rest_framework import status as http_status


# Create your models here.


class TeamMember(models.Model):
    class Role(models.IntegerChoices):
        ADMIN = 0
        REGULAR = 1

    class Status(models.IntegerChoices):
        ACTIVE = 1
        INACTIVE = 0

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=False, unique=True)
    role = models.IntegerField(choices=Role.choices)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def insert(self, data):
        data_to_save = self.serialize(data)
        data_existed = TeamMember.objects.filter(
            Q(phone_number=data_to_save['phone_number']) | Q(email=data_to_save['email'])).first()
        if data_existed:
            return {'err': 'phone number or email already exists.'}, http_status.HTTP_400_BAD_REQUEST
        else:
            saved_data = TeamMember.objects.create(**data_to_save)
            data['id'] = saved_data.id
            status = http_status.HTTP_201_CREATED
        return data, status

    def update_member(self, data):
        serialized_data = self.serialize(data, update=True)
        TeamMember.objects.filter(pk=self.id).update(**serialized_data)
        return data

    def remove(self):
        # TeamMember.objects.filter(id=self.id).update(status=self.Status.INACTIVE)
        TeamMember.objects.filter(id=self.id).delete()

    def get_members(self, pk=None):
        q = {'status': self.Status.ACTIVE}
        if pk:
            q['id'] = pk
        return [self.deserialize(i) for i in TeamMember.objects.filter(**q).values()]

    @staticmethod
    def serialize(data, update=False):
        serialized_data = {'first_name': data.get('firstName', None),
                           'last_name': data.get('lastName', None),
                           'phone_number': data.get('phoneNumber', None),
                           'email': data.get('email', None),
                           'role': data.get('role', None)}
        if update:
            new_dict = {}
            for k, v in serialized_data.items():
                if v:
                    new_dict[k] = v
            return new_dict
        return serialized_data

    @staticmethod
    def deserialize(data):
        deserialized_data = {'firstName': data.get('first_name'),
                             'lastName': data.get('last_name'),
                             'phoneNumber': data.get('phone_number'),
                             'email': data.get('email'),
                             'role': data.get('role')}
        return deserialized_data
