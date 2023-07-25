from django.urls import path
from apps import views

urlpatterns = [
    path('index/<int:pk>/', views.IndexView.as_view(), name='index'),
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio'),
    path('blog/<int:pk>/', views.blog, name='blog'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.login, name='login'),
    path('updete_servis/<int:pk>/', views.UpdateServisView.as_view(), name='updete_servis'),
    path('updete_anketa/<int:pk>/', views.UpdateAnketaView.as_view(), name='updete_anketa'),
    path('updete_blog/<int:pk>/', views.UpdateBlogView.as_view(), name='updete_blog'),
    path('updete_skill/<int:pk>/', views.UpdateSkillView.as_view(), name='updete_skill'),
    path('updete_portfolio/<int:pk>/', views.UpdatePortfolioView.as_view(), name='updete_portfolio'),
    path('contact_us/<int:pk>', views.contact_form, name='contact_us')
]