from django.urls import path
from django.views.generic import TemplateView

app_name = 'mapping-community-groups'
urlpatterns = [
    path('', TemplateView.as_view(template_name="mapping-community-groups/coming-soon.html"), name='comingsoon'),
    path('cookies', TemplateView.as_view(template_name="mapping-community-groups/cookies.html"), name='cookies'),
]
