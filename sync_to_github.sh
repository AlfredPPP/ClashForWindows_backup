#!/bin/bash

# 设置项目目录
PROJECT_DIR=""  # 请替换为你的本地项目路径
REPO_URL="https://github.com/AlfredPPP/JY_data_monitor.git"  # 请替换为你的GitHub仓库URL

# 进入项目目录
cd "$PROJECT_DIR" || { echo "Failed to enter project directory"; exit 1; }

# 添加所有变更到Git
git add . || { echo "Failed to add changes"; exit 1; }

# 提交更改
echo "Enter commit message: "
read -r commit_message
git commit -m "$commit_message" || { echo "Failed to commit changes"; exit 1; }

# 推送到远程仓库
git push "$REPO_URL" main --force || { echo "Failed to push to repository"; exit 1; }

# 完成
echo "Changes pushed to GitHub successfully."
