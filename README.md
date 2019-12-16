
# Denuncia Anónima por Drogas

## Ministerio de Seguridad de la Provincia de Tucumán
Módulo Django para la Página Web del [Ministerio de Seguridad](https://minsegtuc.gov.ar). Permite la percepción de denuncias de manera anónima, con la posibilidad de exportar los registros por parte de los administradores.

## Requerimientos
- Django >= 2.x
- [django-cruds](https://github.com/bmihelac/django-cruds)
- django-import-export


## Instalación
- Copiar App en la carpeta de su Proyecto.
- Instalar requerimientos.
```
pip install -r requirements.txt
```
- Agregar las siguientes Apps en `settings.py`.
```
INSTALLED_APPS = [
  ...
  'import_export',
  'cruds',
  'denuncia',
  ...
]
```
- Agregar Secret Key de Google Captcha en `settings.py`.
```
GOOGLE_RECAPTCHA_SECRET_KEY = 'secret-key'
```
- Agregar en `urls.py` las vistas de alta de denuncias.
```
url(r'^denuncia/', include('denuncia.urls')),
```
- Migraciones.
```
./manage.py migrate
./manage.py makemigrations
```
- Iniciar.
```
./manage.py runserver
```
