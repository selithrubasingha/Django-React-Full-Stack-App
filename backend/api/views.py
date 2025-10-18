from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer , NoteSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note

# Create your views here.

#generics in rest_framework pretty much does most of the stuff for you
#ListCreate api view allows you to list all the model data and create all the. model data
#but since this is a multi user platform , we need to modify the built in get_queryset and perform create views.
#for get query : you gotta filter them by author , otherwise the user can see EVERYBODY'S messages
#as for perform create you gotta give it the author data because the json data input is not going to give you
#that info.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

#why did we modify the get query here? becuase we eed to make sure the relavent user's note is deleted.
# what if the user asked to delete id.5 note . but if query set was all the notes of all the users . 
# os A user could mistakenly delete B user's id.5 note .

#also why can't we use queryset = Note.objects.filter(author=user) on the top ? because this is a class .
# and the user is defined in the http request . the program doesn't know who the user is a the start of the 
#program
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

#no modification needed this is a create API view
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] #AllowAny is used bacause anyone should be able to create an account not 
    #just the authorized people
