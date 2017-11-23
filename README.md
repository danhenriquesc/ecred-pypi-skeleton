# ecred-pypi-skeleton
PyPI Private Repo for ecred common libraries


Instalar/ativar virtualenv

`mkvirtualenv ecredpypiskeleton` or `workon ecredpypiskeleton`

Instalar Pacotes

`pip install -r requirements.txt`

Servir PyPI Private Repo

`pypi-server -p 8080 pypiserver/packages/`

Instalar Módulo do Ecred (Para instalar junto no pip install -r requirements, precisa adicionar algumas configs, nada complexo, mas não fiz agora por ser só 1 pacote)

`pip install ecred-core --extra-index-url http://localhost:8080/simple`

Para testar o uso do pacote externo, rode:

`python project.py`


Este arquivo simplemente usa uma fn do módulo ecred-core que foi instalado a partir do pypiserver privado.


