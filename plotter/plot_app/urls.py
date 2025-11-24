from django.urls import path
from . import views

app_name = 'plot_app'

urlpatterns = [
    path('', views.PlotCreateView.as_view(), name='home'),
    path('plot/<int:pk>/', views.PlotDetailView.as_view(), name='plot_detail'),
    path('plot/<int:pk>/download/', views.PlotDownloadView.as_view(), name='download_plot'),
    path('saved-plots/', views.SavedPlotsView.as_view(), name='saved_plots'),
]