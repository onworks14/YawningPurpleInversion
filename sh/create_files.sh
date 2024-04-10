#!/bin/bash

# 创建txt目录（如果不存在）
mkdir -p txt

# 使用循环创建文件
for i in {1..25}
do
   # 使用printf格式化数字，确保小于10的数字前面加0
   filename=$(printf "txt/day%02d.txt" $i)
   touch $filename
done

echo "文件创建成功。"