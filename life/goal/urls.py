from django.contrib import admin
from django.urls import path
from goal import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}
urlpatterns = [
    path('',views.home,name='home'),
    path("get-semesters/", views.get_semesters, name="get_semesters"),

    path('subjects/',views.subject,name='subjects'),
    path('base/',views.base,name='base'),
    path('about/',views.about,name='about'),
    path('contact/',views.CONTACT,name='contact'),
    path('cgpa/',views.cgpa,name='cgpa'),
    path('resources/', views.res_page, name='resources'),  
    path("api/resources/", views.api_resources, name="api_resources"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),


       # main page
    ]
