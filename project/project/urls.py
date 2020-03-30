"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import home_views, kontakt_views , misja_views, historia_views, galeria_views, bip_views , filmy_views, planlo_views, zajecialo_views, plantech_views, info4tech_views, info5tech_views, zajeciatech_views, egzamin_technikum_views, planmed_views,kierunkimed_views, terminarzmed_views, egzaminmed_views, rekrutacjamed_views, planpoli_views, kierpoli_views, terminarzpoli_views, egzaminpoli_views, rekrutacjapoli_views, planlod_views, egzamin_maturalny_views, terminarzlod_views, rekrutacjalod_views, dlanauczycieli_views, dlarodzicow_views, dlauczniow_views , bibilek_views, wolontariat_views, psychipedag_views, plantecharch_views
from main.views import anews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_views, name='index'),
    path('news', anews, name='news'),
    path('admin/', admin.site.urls),
    path('kontakt', kontakt_views, name='kontakt'),
    path('misja', misja_views, name='misja'),
    path('historia', historia_views, name='historia'),
    path('galeria', galeria_views, name='galeria'),
    path('bip', bip_views, name='bip'),
    path('filmy', filmy_views, name='filmy'),
    path('plan_liceum', planlo_views, name='planliceum'),
    path('zajecia_liceum', zajecialo_views, name='zajecialo'),
    path('plan_technikum', plantech_views, name='plantechnikum'),
    path('informacje_5letnie_technikum', info5tech_views, name='info5tech'),
    path('informacje_4letnie_technikum', info4tech_views, name='info4tech'),
    path('zajecia_technikum', zajeciatech_views, name='zajeciatechnikum'),
    path('egzamin_technikum', egzamin_technikum_views, name='egzamin_technikum'),
    path('plan_szkoly_medycznej', planmed_views, name='planszkolymed'),
    path('kierunki_szkoly_medycznej', kierunkimed_views, name='kierunkimedycznej'),
    path('terminarz_szkoly_medycznej', terminarzmed_views, name='terminarzmedycznej'),
    path('egzaminy_szkoly_medycznej', egzaminmed_views, name='egzaminmed'),
    path('rekrutacja_szkoly_medycznej', rekrutacjamed_views, name='rekrutacjamedycznej'),
    path('plan_szkoly_policealnej', planpoli_views, name='planpolicealnej'),
    path('kierunki_szkoly_policealnej', kierpoli_views, name='kierunkipolicealnej'),
    path('terminarz_szkoly_policealnej', terminarzpoli_views, name='terminarzpoli'),
    path('egzaminy_szkoly_policealnej', egzaminpoli_views, name='egzaminypolicealnej'),
    path('rekrutacja_szkoly_policealnej', rekrutacjapoli_views, name='rekrutacjapolicealnej'),
    path('plan_liceum_dla_doroslych', planlod_views, name='planliceumdoroslych'),
    path('egzamin_maturalny', egzamin_maturalny_views, name='kierunkilicdoroslych'),
    path('terminarz_liceum_dla_doroslych', terminarzlod_views, name='terminarzlicdoroslych'),
    path('rekrutacja_liceum_dla_doroslych', rekrutacjalod_views, name='rekrutacjalicdladoroslych'),
    path('dla_uczniow', dlauczniow_views, name='dlauczniow'),
    path('dla_rodzicow', dlarodzicow_views, name='dlarodzicow'),
    path('dla_nauczycieli', dlanauczycieli_views, name='dlanauczycieli'),
    path('biblioteka_i_lekarz', bibilek_views, name='bibliotekailekarz'),
    path('wolontariat', wolontariat_views, name='wolontariat'),
    path('psycholog_i_pedagog', psychipedag_views, name='psychologipedagog'),
    path('archiwum_planu_technikum', plantecharch_views, name='staryplantech'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


