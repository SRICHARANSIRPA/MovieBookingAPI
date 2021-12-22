from rest_framework import serializers

from MyProject.users.models import *

#
# class BaseSerializer():
#     common_exclude = ['uid', 'created_time', 'updated_time']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'is_staff', 'date_joined','id', 'created_time', 'updated_time',
                    'groups','user_permissions','password','is_superuser']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    user = UserSerializer()

    class Meta:
        model = UserRole
        fields = ['role','user']
