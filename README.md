# webApp

過去に学習用に作成したwebAppを公開できるように修正しながらアップしていく。

あと、学習が途中で止まってしまっていたので再開して行く予定。

## TODO(暫定)

- DBのCRUD操作
- 管理者用のページ作成
- htmlファイルのテンプレート作成
- htmlファイル装飾
- todoアプリ？
- api連携したい
- ログは自作したメソッドではなく、標準パッケージを使う
- nginxコンテナはhttps-portalでhttps化しているがリバプロとして使用して、複数コンテナに割り振るようにしたい
- pythonのパッケージ管理をpoetryに変更したい

## このアプリの利用方法(***画像ファイルなどはgithub上にあげていないので現段階では完全に再現はできません．***)

任意のディレクトリにリポジトリを`git clone`してください。

### コンテナ起動

次のコマンドでコンテナを起動できます。

```shell
docker-compose up (-d)
```

`-d`オプションはバックグラウンドで起動するという意味。
起動ログなどを確認したい場合は`-d`オプション無しで起動すれば良い。

### コンテナ

次のコマンドでdocker-compose.ymlファイルに記載されているコンテナなどを停止し、コンテナとネットワークを削除する。

```shell
docker-compose down (--rmi all)
```

`--rmi all`オプションを使用すると`docker-compose up`の際に作成したimageも合わせて削除してくれる。


## ディレクトリ構成

ディレクトリ構造は下記のようになっています。

```
-> tree
.
├── certs
│
├── docker-compose.yml
├── web
│   ├── Dockerfile
│   ├── app
│   │   ├── index.py
│   │   ├── static
│   │   │   ├── css            
│   │   │   ├── favicon_package_v0.16
│   │   │   ├── img
│   │   │   └── js
│   │   └── templates
│   └── requirements.txt
└── webApp.sh
```




