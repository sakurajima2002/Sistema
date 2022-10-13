from django.urls import path
from django.contrib.auth.decorators import login_required

from boss.views import (BossesView, BossCreateView, BossUpdateView,
                        BossDetailView, BossDeleteView)

app_name = 'boss'

urlpatterns = [
    path('', login_required(BossesView.as_view()), name='bosses'),
    path('create', login_required(BossCreateView.as_view()), name='create'),
    path('<int:pk>/detail', login_required(BossDetailView.as_view()), name='detail'),
    path('<int:pk>/update', login_required(BossUpdateView.as_view()), name='update'),
    path('<int:pk>/delete', login_required(BossDeleteView.as_view()), name='delete'),
]
