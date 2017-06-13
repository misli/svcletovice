# svcletovice
Web [svcletovice.cz](http://www.svcletovice.cz/)

## instalace

```shell
git clone git@github.com:misli/svcletovice.git
cd svcletovice
sudo docker-compose up -d
sudo docker-compose exec svcletovice leprikon migrate
sudo docker-compose exec svcletovice leprikon createsuperuser
```

První krok naklonuje repozitář s aplikací.
Ve druhém kroku přejdeme do adresáře s aplikací.
Třetí krok vytvoří databázi.
Čtvrtý vytvoří uživatele
a spustí testovací server.

Server bude dostupný na adrese
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## vytvoření stránek

Práce s redakčním systémem djangoCMS je poměrně intuitivní.
Více informací o redakčním systému je k dispozici zde:
[http://www.django-cms.org/en/](http://www.django-cms.org/en/)

## konfigurace systému Leprikón

Leprikón je rozšíření djangoCMS. V CMS je třeba nejdříve vytvořit stránku,
ve které bude aplikace Leprikón umístěný.
Na našem webu je to stránka *Můj Letokruh*
V pokročilém nastavení stránky je třeba nastavit *Id* na *leprikon*
a ze seznamu *Aplikace* vybrat *Leprikón*.
Po uložení a publikování stránky je třeba restartovat testovací server.
