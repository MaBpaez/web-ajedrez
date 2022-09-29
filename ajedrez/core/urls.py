from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Path del core
    path('', views.home, name='inicio'),
    path('agenda/', views.agenda, name='agenda'),
    path(
        'torneo/<int:year>/<int:month>/<int:day>/<slug:torneo>/',
        views.torneo_detail,
        name='torneo-detail',
    ),
]
