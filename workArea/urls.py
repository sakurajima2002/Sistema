from django.urls import path
from django.contrib.auth.decorators import login_required

from workArea.views import WorkAreaView, WorkAreaUpdateView, WorkAreaDeleteView

app_name = 'workArea'

urlpatterns = [
    path('', login_required(WorkAreaView.as_view()), name='workAreas'),
    path('<int:pk>/update/', login_required(WorkAreaUpdateView.as_view()), name='update'),
    path('<int:pk>/delete/', login_required(WorkAreaDeleteView.as_view()), name='delete'),
]
