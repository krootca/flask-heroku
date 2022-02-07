<p align="center">
  <img width="300px" src="https://miro.medium.com/max/1400/1*J1kzbHEN4r-kQs6kiVsS6A.jpeg">
</p>

<h1 align="center">flask-heroku</h1>

<p align="center">Some examples to upload a flask app on heroku - Algunos ejemplos para subir una aplicación de flask en heroku
.</p>

<p align="center">
  <a aria-label="license" href="https://github.com/krootca/flask-heroku/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/primer/css.svg" alt="">
  </a>
</p>

### Esto está apoyado por la organización de GitHub [King-Artorias](https://github.com/King-Artorias) 

<img src="https://avatars.githubusercontent.com/u/89755140?s=200&v=4" align="right"
     alt="King-Artorias Logo" width="110" height="110">
### El código es totalmente libre de ser modificado y distribuido.
<br>

[![Last Updated](https://img.shields.io/github/issues/krootca/flask-heroku)](https://github.com/krootca/flask-heroku/commits/main)

<h3 align="right">	
	<a href="https://github.com/King-Artorias">King-Artorias</a>
</h3>

-----------------

### ¿how to edit? - ¿Como editar?


| File/Folder | Edit |
|----|----|
| Procfile | No |
| wsgi.py | No |
| requeriments.txt | Yes |
| /app (folder) | Yes |

| Add modules to requeriments.txt


Freeze
```bash
pip freeze > requirements.txt
```
-----------------

### Upload an app to heroku - Subir a heroku una app

| ¿How to upload? - ¿Como subir?


```bash
git init
```

```bash
heroku git:remote -a <name_app>
```

```bash
git add .
```

```bash
git commit -am "This is a commit"
```

```bash
git push heroku master
```

------------



| Have a nice code!! 

<div align="center">
              <a href="https://krootca.github.io/">
			<div>
				<img src="https://github.com/krootca/Ofuscated-Python3/blob/main/logo.gif" width="300" alt="OSS Capital">
			</div>
			<div>
				<sup><b>Gracias por el apoyo a todos los que conmigo están trabajando<br>exclusivamente para contribuir en el codigo abierto.</b></sup>
			</div>
		</a>
                                                                                                                             </div>
