from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register(r"schedule", views.AllScheduleViewSet, basename="all_schedule"),
router.register(r"customer", views.CustomViewSet, basename="customer"),
router.register(r"drivers", views.DriversViewSet, basename="list_drivers"),

urlpatterns = [
    path("filterDriver/<int:id>/<str:date>", views.FilterDriversView.as_view(), name="filter_driver"),
    path(
        "searchDriver/<str:time>/<str:date>/<int:lat>/<int:lng>",
        views.SearchDriversView.as_view(),
        name="search_driver",
    ),
    path("time_schedule/<str:date>", views.TimeScheduleView.as_view(), name="time_schedule"),
    path("", include(router.urls)),
]
