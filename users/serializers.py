from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password', 'email', 'username', 'bio', 'created_at']
        extra_kwargs = {
            'password': {
                'write_only':True
            },
            'id':{
                'read_only': True
            },
            'created_at':{
                'read_only':True
            }
        }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)