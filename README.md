# webApp

過去に学習用に作成したwebAppを公開できるように修正しながらアップしていく。

あと、学習が途中で止まってしまっていたので再開する。


## このアプリの利用方法

任意のディレクトリにリポジトリを`git clone`してください。

次のコマンドでコンテナを起動できます。
`-d`オプションはバックグラウンドで起動するという意味。
起動ログなどを確認したい場合は`-d`オプション無しで起動すれば良い。

```shell
docker-compose up -d
```


ディレクトリ構造は下記のようになっています。
```
work(任意のディレクトリ)
|-- webApp.sh (docker-composeコマンドを操作するスクリプト。作成予定)
|-- docker-compose.yml
|-- certs/
|-- web/
|    |-- Dockerfile
|    |-- requirements.txt
|    |-- app/
|         |-- index.py
|         |-- static/ (js, css, imgファイルなどを入れる)
|         |-- templates/ (htmlファイルを入れる)
|
|
|
|-- db/

```