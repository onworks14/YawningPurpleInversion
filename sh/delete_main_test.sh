#!/bin/bash

# 在idol目录下查找并删除所有名为main_test.go的文件
find idol -type f -name "main_test.go" -exec rm {} \;

echo "所有main_test.go文件已被删除。"
