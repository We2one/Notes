#!/bin/bash

# 生成summary
#node generateSummary.js

git add -A;

if [[ ! $1 ]];then
  git commit -am "$1"
else
  git commit -am "update notes"
fi

git push --all;
# git push ;
