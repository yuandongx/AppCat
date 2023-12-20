#!/bin/sh

appid=''

function getPid(){
    appid=`netstat  -tlnp|awk '{print $4,$7}'|awk -F / '{print $1}'|awk -F : '{print $2}'|grep "$APP_PORT "`
    if [ -n "$appid" ];then
        appid=$(echo $appid|awk '{print $2}')
        echo "The service port $APP_PORT is listening with $appid ."
    fi
}

function start(){
    if [ -n "$appid" ];then
        echo  'App is running, do not start again.'
    else
        echo 'App is starting...'
        python $APP_WORK_SPACE/main.py
    fi
}

function stop(){
    if [ -z "$appid" ];then
        echo "No pid for $APP_PORT found."
    else
        kill -9 $appid
        echo "Pid $appid for $APP_PORT stoped."
    fi
}

function restart(){
    stop
    start
}

getPid

if [ "$1" = "start" ];then
    start
elif [ "$1" = "stop" ];then
    stop
elif [ "$1" = "restart" ];then
    restart
else
    echo "$@ 命令不正确！"
fi