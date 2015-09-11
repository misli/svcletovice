# svcletovice
Web [svcletovice.cz](http://www.svcletovice.cz/)

## stažení a spuštění vývojové instance

```shell
curl https://www.svcletovice.cz/static/_sources.tar.gz | tar -xz
git clone git@github.com:misli/svcletovice.git
cd svcletovice
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

V prvním kroku se stáhne a rozbalí archiv všech balíčků, na kterých aplikace závisí.
Druhý krok naklonuje repozitář s aplikací.
Ve třetím kroku přejdeme do adresáře s aplikací.
Čtvrtý krok vytvoří databázi.
Pátý vytvoří uživatele
a šestý spustí testovací server.

## vytvoření stránek

Práce s redakčním systémem djangoCMS je poměrně intuitivní.
Více informací o redakčním systému je k dispozici zde:
http://www.django-cms.org/en/

## konfigurace rozšíření Domeček

Domeček je rozšíření djangoCMS. V CMS je třeba nejdříve vytvořit stránku, ve které bude domeček umístěný.
Na našem webu je to stránka *Můj Letokruh*
V pokročilém nastavení stránky je třeba nastavit *Id* na *domecek*
a ze seznamu *Aplikace* vybrat *Domeček*.
Po uložení a publikování stránky je třeba restartovat testovací server.
