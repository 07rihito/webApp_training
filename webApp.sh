#!/bin/sh

set -e
# set -x

opt=$1

# 引数が2つでない場合の処理
#if [ $# != 2 ]; then
#  echo "指定された引数は$#個です。"
#  echo "実行例：./do.sh -h or -m start/stop/restart"
#  exit 1
#fi


if [ $1 = "-h" ]; then
# ここにhelpの表示を記載
echo " -h：help"
echo " -m：実行モード"
echo "    start : docker-composeのビルド"
echo "    stop : docker-composeのダウン"
echo "    restart : docker-composeのリスタート"
echo "    ps : docker-composeのプロセス"
echo "    rmi : docker-compose --rmi all"
elif [ $1 = "-m" ]; then
# 実行モードの変更
  if [ $2 = "start" ]; then
    docker-compose up -d
  elif [ $2 = "stop" ]; then
    docker-compose down
  elif [ $2 = "restart" ]; then
    docker-compose down
    docker-compose up -d
  elif [ $2 = "ps" ]; then
    docker-compose ps -a
  elif [ $2 = "rmi" ]; then
    docker-compose down --rmi all
  fi
else
#　ここにエラー処理を記載
echo "引数が正しくありません。"
echo "実行例：./do.sh ( -h | -m )"
echo " -h：help"
echo " -m：実行モード"
echo "    start : docker-composeのビルド"
echo "    stop : docker-composeのダウン"
echo "    restart : docker-composeのリスタート"
echo "    ps : docker-composeのプロセス"
echo "    rmi : docker-compose --rmi all"
fi


