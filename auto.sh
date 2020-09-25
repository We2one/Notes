#!/bin/bash

# 生成summary
#node generateSummary.js

git add -A;

if [[ -z "$1" ]];then
  git commit -am "update notes"
else
  git commit -am "$1"
fi

git push --all;
# git push ;
