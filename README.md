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

```

settings.pyでmysqlの設定を行ってください。


以下のurlでdjangoアプリが立ち上がっていたら成功です。
http://localhost:8000
