from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password', 'email', 'username', 'bio', 'created_at', 'phone_number', 'address', 'avatar']
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
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
           instance.set_password(password)
        
        for attr,value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

           
    
    


        