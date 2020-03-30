from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from main.models import Nowosci

def knews_add_main_news():
    ismain = Nowosci.objects.filter(glowny = True)

    if ismain[0].glowny == True:
        maintytul = ismain[0].tytul
        mainopis = ismain[0].opis
    else:
        maintytul = 'Najnowe Wiadomości ze Szkoły'
        mainopis = 'Zobacz sam :)'
    
    return [str(maintytul), str(mainopis)]

def home_views(request, *args, **kwargs):
    news1 = Nowosci.objects.all().order_by('-id')[:6]
    nazwastrony = 'Strona Główna'        
    knews = { 
        'nazwa_strony' : nazwastrony,
        'news1' : news1,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"home.html", knews)

def kontakt_views(request, *args, **kwargs):
    nazwastrony = 'Kontakt'
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/kontakt.html", knews)

def misja_views(request, *args, **kwargs):
    nazwastrony = 'Misja Szkół'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
        }
    return render(request,"pod/misja.html", knews)

def historia_views(request, *args, **kwargs):
    nazwastrony = 'Historia Szkoły'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/historia.html", knews)

def galeria_views(request, *args, **kwargs):
    nazwastrony = 'Galeria'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/galeria.html", knews)

def bip_views(request, *args, **kwargs):
    nazwastrony = 'BIP'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/bip.html", knews)

def filmy_views(request, *args, **kwargs):
    nazwastrony = 'FILMY'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/filmy.html", knews)

def planlo_views(request, *args, **kwargs):
    nazwastrony = 'Plan Lekcji Liceum'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/planlo.html", knews)

def zajecialo_views(request, *args, **kwargs):
    nazwastrony = 'Zajęcia Dodatkowe Liceum'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/zajecialo.html", knews)

def plantech_views(request, *args, **kwargs):
    nazwastrony = 'Plan Lekcji Technikum'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/plantech.html", knews)

def info5tech_views(request, *args, **kwargs):
    nazwastrony = 'Informacje o 5letnim technikum'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/info5tech.html", knews)

def info4tech_views(request, *args, **kwargs):
    nazwastrony = 'Informacje o 4letnim technikum'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/info4tech.html", knews)

def zajeciatech_views(request, *args, **kwargs):
    nazwastrony = 'Zajęcia dodatkowe Technikum'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/zajeciatech.html", knews)

def egzamin_technikum_views(request, *args, **kwargs):
    nazwastrony = 'Egzamin Technikum'        
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/rekrutacjatech.html", knews)

def planmed_views(request, *args, **kwargs):
    nazwastrony = 'Plan Lekcji Szkoły Medycznej'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/planmed.html", knews)

def kierunkimed_views(request, *args, **kwargs):
    nazwastrony = 'Kierunki Szkoły Medycznej'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/kierunkimed.html", knews)

def terminarzmed_views(request, *args, **kwargs):
    nazwastrony = 'Terminarz Szkoły Medycznej'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/terminarzmed.html", knews)

def egzaminmed_views(request, *args, **kwargs):
    nazwastrony = 'Egzaminy Szkoły Medycznej'       
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/egzaminmed.html", knews)

def rekrutacjamed_views(request, *args, **kwargs):
    nazwastrony = 'Rekrutacja Szkoły Medycznej'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()  
    }
    return render(request,"pod/rekrutacjamed.html", knews)

def planpoli_views(request, *args, **kwargs):
    nazwastrony = 'Plan szkoły Policealnej'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/planpoli.html", knews)

def kierpoli_views(request, *args, **kwargs):
    nazwastrony = 'Kierunki szkoły Policealnej'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()   
    }
    return render(request,"pod/kierpoli.html", knews)

def terminarzpoli_views(request, *args, **kwargs):
    nazwastrony = 'Terminarz szkoły Policealnej'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()   
    }
    return render(request,"pod/terminarzpoli.html", knews)

def egzaminpoli_views(request, *args, **kwargs):
    nazwastrony = 'Egzaminy szkoły Policealnej'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/egzaminpoli.html", knews)

def rekrutacjapoli_views(request, *args, **kwargs):
    nazwastrony = 'Rekrutacja szkoły Policealnej'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/rekrutacjapoli.html", knews)

def planlod_views(request, *args, **kwargs):
    nazwastrony = 'Plan Liceum dla dorosłch'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/planlod.html", knews)

def egzamin_maturalny_views(request, *args, **kwargs):
    nazwastrony = 'Matura Liceum dla dorosłch'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()   
    }
    return render(request,"pod/egzaminlod.html", knews)

def terminarzlod_views(request, *args, **kwargs):
    nazwastrony = 'Terminarz Liceum dla dorosłch'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()
    }
    return render(request,"pod/terminarzlod.html", knews)

def rekrutacjalod_views(request, *args, **kwargs):
    nazwastrony = 'Rekrutacja Liceum dla dorosłch'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/rekrutacjalod.html", knews)

def dlauczniow_views(request, *args, **kwargs):
    nazwastrony = 'Dla Uczniów'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/dlauczniow.html", knews)

def dlanauczycieli_views(request, *args, **kwargs):
    nazwastrony = 'Dla Nauczycieli'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/dlanauczycieli.html", knews)

def dlarodzicow_views(request, *args, **kwargs):
    nazwastrony = 'Dla Rodziców'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news()   
    }
    return render(request,"pod/dlarodzicow.html", knews)

def bibilek_views(request, *args, **kwargs):
    nazwastrony = 'Biblioteka I Lekarz'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/bibilek.html", knews)

def wolontariat_views(request, *args, **kwargs):
    nazwastrony = 'Wolontariat'          
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/wolontariat.html", knews)

def psychipedag_views(request, *args, **kwargs):
    nazwastrony = 'Psycholog i Pedagog'         
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/psychipedag.html", knews)

def plantecharch_views(request, *args, **kwargs):
    nazwastrony = 'Plan Technikum Archiwa'           
    knews = { 
        'nazwa_strony' : nazwastrony,
        'mainnews' : knews_add_main_news() 
    }
    return render(request,"pod/plantecharch.html", knews)

def anews(request, *args, **kwargs):
    nazwastrony = 'Nowości'
    news = Nowosci.objects.all().order_by('id')     
    knews = { 
        'nazwa_strony' : nazwastrony,
        'news' : news,
        'mainnews' : knews_add_main_news()   
    }
    return render(request, "news.html", knews)
