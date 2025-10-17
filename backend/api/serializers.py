from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
# serializers are used to send data from frontend to backend 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"] #the fields of data about to send to frontend
        extra_kwargs = {"password": {"write_only": True}} #extra info : the password cannot be changed in the frontend 
        #it's write only bro !

    #when data is sent from the frontend to backend , that data is validated data! and and using that we
    #create a User in the backend
    def create(self, validated_data):
        print(validated_data)
        #BOOM ! user created baby! this syntax is in the build in user I guess
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        #just normal meta data
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

    #why isn't there a create function for notes?
    # well this uses the build in create user function that is provided by 
    # MidelSerializer 










