# 运动康复智能 Agent

这是一个用于课堂展示的运动康复智能 Agent 原型项目。

## 功能

1. 通过对话收集用户运动后的身体状态
2. 判断风险等级：低风险 / 中风险 / 高风险
3. 生成个性化康复建议
4. 对高风险症状进行就医提醒
5. 包含大语言模型版本和不消耗 API 的规则版

## 文件说明

- `sports_rehab_agent.py`：大语言模型版本，需要 OpenAI API Key
- `simple_rehab_agent.py`：规则版，不需要 API Key，适合课堂演示备用
- `requirements.txt`：依赖库
- `README.md`：使用说明

## 安装依赖

```bash
pip install -r requirements.txt
```

## 设置 OpenAI API Key

macOS / Linux：

```bash
export OPENAI_API_KEY="你的API_KEY"
```

Windows PowerShell：

```powershell
setx OPENAI_API_KEY "你的API_KEY"
```

## 运行大语言模型版本

```bash
python sports_rehab_agent.py
```

## 运行规则版

```bash
python simple_rehab_agent.py
```

## 项目简介

本项目构建了一个基于大语言模型的运动康复智能 Agent，主要用于帮助用户在运动后进行身体状态评估、恢复建议生成和风险提醒。项目解决的核心痛点是：普通用户在运动后出现肌肉酸痛、关节不适或疲劳时，往往缺乏专业康复知识，容易忽视潜在损伤，或者采用不合适的恢复方式。

Agent 的核心逻辑流程包括：
1. 询问用户运动类型、运动强度、疼痛部位、疼痛程度和持续时间
2. 根据规则判断风险等级
3. 结合 Prompt Engineering 生成个性化康复建议
4. 对高风险情况优先进行安全提醒和就医建议

## 注意事项

本系统只能提供基础康复建议，不能替代医生诊断。
