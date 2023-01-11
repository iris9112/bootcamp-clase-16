# Clase 16 - Relaciones entre Modelos

App de prueba

![model_db.png](docs%2Fmodel_db.png)

## Pasos

- Asegurate de que `movies_app` sea el actual directorio de trabajo 
- Crea un ambiente virtual: `python3 -m venv venv`
- Activa el ambiente virtual: `source venv/bin/activate`
- Instala las dependencias: `pip install -r requirements.txt`
- Ejecuta migraciones (y crear base de datos) `python manage.py migrate`
- Crea un super usuario `python manage.py createsuperuser`
- Cargar backup `python manage.py loaddata docs/db.json`


## Ejercicios

- Listar top de 10 peliculas con mayor raiting.

- Listar actores con mayor participación en películas de los últimos 5 años.

- Para cada actor, listar 3 peliculas en las que haya participado.

- Por cada genero, obtener el nombre de la película con mayor Recaudo. 


### Recursos

- [¿Qué es un ORM?](https://codigofacilito.com/articulos/orm-explicacion) 
- [Top 1000 Movies by IMDB Rating](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
- [Classy Class-Based Views](https://ccbv.co.uk/)
- [Scrolling Nav](https://startbootstrap.com/template/scrolling-nav): A basic, unstyled Bootstrap page layout for creating smooth scrolling, one page websites
