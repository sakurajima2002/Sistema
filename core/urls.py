from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import HomeView, PrivacyPolicyView, TermsConditionsView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name="home"),
    path('PrivacyPolicy/', PrivacyPolicyView.as_view(), name="privacy-policy"),
    path('TermsConditions/', TermsConditionsView.as_view(), name="terms-conditions"),
    
    path('employee/', include('employee.urls', namespace='employee')),
    path('boss/', include('boss.urls', namespace='boss')),
    path('workArea/', include('workArea.urls', namespace='workArea')),
    path('accounts/', include('login.urls', namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)