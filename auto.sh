#!/bin/bash

# 生成summary
node generateSummary.js

git add -A;
git commit -am "update notes";
git push ;
