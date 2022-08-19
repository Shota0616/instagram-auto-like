# docker_django

dockerでdjangoの開発環境を構築する

cloneしたらdocker-compose.ymlのあるディレクトリで以下を実行

```
docker-copose up -d
```
コンテナがすべて立ち上がったら以下コマンドでコンテナの情報を確認。appコンテナンのIDを確認し、appコンテナに入る
```
docker ps -a
docker exec -it [コンテナのID] bash
```

djangoプロジェクトを作成
```
django-admin startproject [config] .
```

settings.py修正。
```
import pymysql

# connect mysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

STATIC_ROOT = '/static'
```

以下のurlでdjangoアプリが立ち上がっていたら成功。
http://localhost:8000
