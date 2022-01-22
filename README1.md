# DEPLOIEMENT DE L'APPLICATION

le deploiement de notre application c'est fait en plusieurs etapes a savoir:

1. Installation des packages utilises
 - ces packages se retrouve dans le requirement.txt a savoir: gunicorn, 
 dj-database-url, psycopg2, whitenoise

2. Deploiement proprement dit
    Le deploiement c'est fait a de heroku CLI et pour ce faire nous avons effectuernles etapes suivantes:
    - creation d'un compte heruko et installation de heroku CLI
    - en ligne de commande nous avons creer une application appele findrepeater en executant >> heroku create findrepeater
    - nous avons creer un fichier Procfile qui sera utiliser par heroku afin de pouvoir repondre au requette http qui sera effectue via notre serveur gunicorn
    - nous avons creer un fichier runtime.txt pour specifier a heroku la version de python qu'il doit utiliser pour notre application
    - nous avons par la suite creer des serveur distant pour heroku
    et nous avons commit notre notre application sur heroku en faisant git push heroku main. des lors notre application a donc ete deployer sur heroku. bien que ce n'etait pas styliser

 3. Stylisation de l'application et connexion a une base de donne posgresql

   - connexion a la base de donne posgresql
   nous avons utiliser sqlite3 lors de la conception de notre projet en local. mais etant donne que heroku ne prend pas en charge sqlite3, nous avons utiliser le package dj-database-url et nous l'avons configurer dans le fichier production_settings.py; car lors du deploiement il fallait prendre en compte certains parametres comme la stylisation.

   - pour style le produit deployer nous avons utiliser les packages
   whitenoise et psycopg2 tels que definit dans les le fichier production_settings.py.

4. LIEN DE L'APPLICATION DEPLOYER
    https://findrepeater.herokuapp.com


 