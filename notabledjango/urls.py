from django.contrib import admin
from api.resources import NoteResource
from django.urls import include, path



note_resource = NoteResource()

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^api/', include(note_resource.urls)),

]

