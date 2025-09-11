# 久瓴代码编写助手使用插件使用教程

## 目录
1. [简介](#简介)
2. [安装 Cline 插件](#安装-cline-插件)
3. [连接本地模型](#连接本地模型)
4. [使用 Cline 编写 Hello World 程序](#使用-cline-编写-hello-world-程序)
5. [常见问题解答](#常见问题解答)

## 简介

本教程使用 `VScode + Cline + Qwen3-coder-480b` 组合实现公司内部 AI 编程助手，可以直接在 VSCode 中使用。它可以帮助您编写代码、调试程序、解释代码逻辑等。本教程将指导您如何安装 Cline 插件、连接本地模型以及使用 Cline 编写简单的程序。

## 安装 Cline 插件

### 步骤 1: 打开 VSCode 扩展市场
1. 启动 Visual Studio Code
2. 点击左侧活动栏中的扩展图标（或使用快捷键 `Ctrl+Shift+X` / `Cmd+Shift+X`）

### 步骤 2: 搜索 Cline 插件
1. 在搜索框中输入 "Cline"
2. 在搜索结果中找到官方发布的 Cline 插件

### 步骤 3: 安装插件
1. 点击 Cline 插件卡片
2. 点击 "Install" 按钮进行安装
3. 等待安装完成后，重启 VSCode（如果提示需要重启）

### 步骤 4: 验证安装
1. 重启 VSCode 后，在左侧活动栏应该能看到 Cline 的图标
2. 或者使用快捷键 `Ctrl+Shift+P` / `Cmd+Shift+P` 打开命令面板，输入 "Cline" 查看相关命令

## 连接本地模型

Cline 支持连接多种本地模型，公司使用的模型是 `Qwen3-coder-480b`，使用vLLM部署，以下是连接本地模型的步骤：

1. 记录本地大模型连接所需信息：
   ```json
   {
    "model_url": "http://192.168.100.30:15000/v1",
    "api_key": "your_api_key"
    "model_name": "qwen3-coder-480b"
   }
   ```
2. 在 VSCode 中配置 Cline：
   1. 打开Cline配置界面（一般可在侧边栏找到）
   2. 按照如下信息配置：
    - 找到 "Api Provider" 设置项，选择 "OpenAI Compatible"
    - 设置 "Base Url"为 `http://192.168.100.30:15000/v1`
    - 设置 "OpenAI CompatibleApi Key"为 `empty`
    - 设置 "Model ID" 为 `qwen3-coder-480b`

3. 配置完成，Cline 就可以开始工作了

## 使用 Cline 编写 Hello World 程序

以下是如何使用 Cline 编写简单的 "Hello World" 程序的示例：

### Python 版本

1. 打开 Cline 面板（点击左侧活动栏的 Cline 图标）

2. 在 Cline 输入框中输入以下提示：
   ```
   请帮我写一个 Python 的 Hello World 程序，要求：
   1. 包含函数定义
   2. 添加适当的注释
   3. 使用类型提示
   ```

3. Cline 会生成类似以下的代码：
   ```python
   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-
   
   """
   A simple Hello World program in Python.
   """
   
   def greet(name: str = "World") -> str:
       """
       Generate a greeting message.
       
       Args:
           name (str): The name to greet. Defaults to "World".
           
       Returns:
           str: The greeting message.
       """
       return f"Hello, {name}!"
   
   def main() -> None:
       """Main function to run the program."""
       message = greet()
       print(message)
       
       # Greet a specific person
       personalized_message = greet("Alice")
       print(personalized_message)
   
   if __name__ == "__main__":
       main()
   ```

4. 可以直接由cline新建和保存文件 `hello_world.py`，也可以选择复制代码到你指定的文件中

6. 运行程序：
   ```bash
   python hello_world.py
   ```

### 其他语言
其他语言样例步骤类似，请根据实际情况修改提示，并生成对应的代码。


## 常见问题解答

### Q: 安装 Cline 插件后找不到图标？
A: 请尝试重启 VSCode。如果仍然看不到，请检查插件是否正确安装，可以在扩展页面查看已安装的插件列表。

### Q: 连接本地模型时出现连接错误？
A: 请确认：
1. 本地模型服务已经启动并在正确的端口监听
2. Cline 的 API URL 设置正确
3. 防火墙没有阻止连接

### Q: Cline 生成的代码不符合预期？
A: 可以尝试：
1. 更详细地描述你的需求
2. 指定编程语言和版本
3. 明确说明需要包含的功能点
4. 给出具体的代码风格要求

### Q: 如何提高 Cline 生成代码的质量？
A: 建议：
1. 提供清晰明确的需求描述
2. 指定技术栈和版本要求
3. 说明目标平台和环境
4. 给出示例代码作为参考

通过以上步骤，您应该能够成功安装 Cline 插件、连接本地模型并开始使用 Cline 编写程序了！

*Happy Coding! :)*
