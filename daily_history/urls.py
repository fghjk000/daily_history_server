from django.urls import path

from daily_history.views import ContentsListCreateAPI, ContentsDetailAPI, ImageListCreateAPI, ImageDetailAPI

urlpatterns = [
    path('', ContentsListCreateAPI.as_view()),
    path('<int:contents_id>/', ContentsDetailAPI.as_view()),
    path('<int:contents_id>/image/', ImageListCreateAPI.as_view()),
    path('<int:contents_id>/image/<int:image_id>/', ImageDetailAPI.as_view())
]
