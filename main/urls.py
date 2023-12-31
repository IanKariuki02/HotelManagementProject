from django.urls import path
from . import views
from .views import delete_reservation

urlpatterns = [
    path('modd', views.Moddview.as_view(), name="modd"),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservation/create/', views.ReservationCreateView.as_view(), name='reservation_create'),
    path('reservation/<int:pk>/update', views.ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservation/<int:pk>', views.ReservationDetailView.as_view(), name='reservation_detail'),
    path('delete-reservation/<int:reservation_id>', delete_reservation, name='delete-reservation'),

]
