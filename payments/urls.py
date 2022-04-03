from django.urls import path
from payments.views import Payment

urlpatterns = [
    path("", Payment.as_view(), name="payment"),
]
