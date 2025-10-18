from django.urls import path
from . import views


urlpatterns = [
    path("notes/",views.NoteListCreate.as_view() , name="note-list"),
    path("notes/delete/<int:pk>",views.NoteDelete.as_view() , name="delete-note")
    #pk stands for primary key . why isn't it given as a argument for delete note view??
    #becuase the whole thing is automated . the function automatically uses pk to search for 
    # the note to delete . that is the difference between FunctionBasedViews and 
    #ClassBasedViews
]