#!/bin/bash

# ---------- Part1 -------------
# 定义一个函数，包含你想要执行的脚本内容
execute_script() {
    # 创建目录
    mkdir -p inputs

    # 循环创建文件
    for i in $(seq -w 1 25); do
        touch inputs/$i.txt
    done
}

# 条件为假时，不执行函数
if false; then
    # 如果条件为真，执行脚本
    execute_script
else
    # 如果条件为假，不执行任何操作
    echo "1.条件为假，脚本不执行。"
fi

# ---------- Part2 -------------
# 定义一个函数，包含你想要执行的脚本内容
run_python_scripts() {
    # 定义Python文件夹的路径
    PYTHON_DIR="./python"

    # 定义输出文件的路径
    OUTPUT_FILE="output.txt"

    # 定义错误日志文件的路径
    ERROR_LOG="errno.log"

    # 清空输出文件和错误日志文件
    > $OUTPUT_FILE
    > $ERROR_LOG

    # 遍历Python文件夹中的所有文件
    for file in $PYTHON_DIR/day_*.py; do
        # 提取文件名中的日期部分
        day=$(basename $file .py | cut -d'_' -f2)

        echo "====================== Day $day Output ======================" >> $OUTPUT_FILE

        # 执行Python文件，并将输出重定向到输出文件，将错误重定向到错误日志文件
        python $file >> $OUTPUT_FILE 2>> $ERROR_LOG
        
        # 在输出文件中添加一个分隔符，以便于区分不同日期的输出
        echo "" >> $OUTPUT_FILE

    done

    echo "All scripts have been executed. Check $OUTPUT_FILE for outputs and $ERROR_LOG for errors."
}

# 调用函数
# 条件为假时，不执行函数
if true; then
    # 如果条件为真，执行脚本
    run_python_scripts
else
    # 如果条件为假，不执行任何操作
    echo "2.条件为假，脚本不执行。"
fi