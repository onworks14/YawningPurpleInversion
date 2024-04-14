#!/bin/bash

# 定义输出文件路径
output_file="../output.txt"

# 清空输出文件
> "$output_file"

# 遍历当前目录下的所有.cpp文件
for file in *.cpp; do
    # 提取文件名中的数字和后缀
    if [[ $file =~ ^day_([0-9]{2})([ab])\.cpp$ ]]; then
        day=${BASH_REMATCH[1]}
        suffix=${BASH_REMATCH[2]}
        # 编译文件
        g++ "$file" -o "temp_exec" 2>/dev/null
        # 如果编译成功，运行生成的可执行文件
        if [ $? -eq 0 ]; then
            # 运行并捕获输出
            output=$(./temp_exec 2>/dev/null)
            # 将结果写入到output.txt文件中
            echo "Day $day ${suffix^^}:" >> "$output_file"
            echo "$output" >> "$output_file"
            echo "" >> "$output_file"
        else
            echo "Compilation of $file failed."
        fi
    fi
done

# 删除临时生成的可执行文件
rm temp_exec
