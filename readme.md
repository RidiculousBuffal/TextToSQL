# 🌟 LLM TEXT-TO-SQL TOOLBOX
> 一个使用大模型进行数据库问答的工具箱 🤖

## 🎉 Features
- **自定义数据库连接信息** 🔗  
  ![Snipaste_2024-09-20_15-47-31.png](pic%2FSnipaste_2024-09-20_15-47-31.png)

- **自动识别数据库中的表格** 📊

- **基本的Markdown输出** 📝  
  ![Snipaste_2024-09-20_15-41-20.png](pic%2FSnipaste_2024-09-20_15-41-20.png)  
  ![Snipaste_2024-09-20_15-41-24.png](pic%2FSnipaste_2024-09-20_15-41-24.png)

- **前端支持流式输出** 🌊

- **基本的UI样式** 🎨

## 💭 思考过程
- **提取表的建表语句DDL:** [getTableDDL.py](backend%2Fconnector%2FgetTableDDL.py)
- **把用户的问题转换为若干个子问题(自然语言):** [extractQuestion.py](backend%2Fllm%2Fagent%2FextractQuestion.py)
- **把这些自然语言的问题转换为SQL查询语句:** [getSqlSentence.py](backend%2Fllm%2Fagent%2FgetSqlSentence.py)
- **执行这些查询语句:** [excutorQuery.py](backend%2Fconnector%2FexcutorQuery.py)
- **把查询到的结果一起给大模型:** [DefaultLLM.py](backend%2Fllm%2FDefaultLLM.py)

## 🖥️ 一个UI:
> 一个可以固定在底部且只能径向拉升的基本聊天框: [ResizableInputBox.vue](frontend%2Fsrc%2Fplayground%2FResizableInputBox.vue)

## 🚀 开发
### 前端
- 在 [.env](frontend%2F.env) 和 [.env.development](frontend%2F.env.development) 中替换为你自己的 backendURL 🔄
- 在 [figure.ts](frontend%2Fsrc%2Fconst%2Ffigure.ts) 中替换你自己喜欢的欢迎页面图形和 bot, user 的头像 🎭

```bash
cd frontend
npm install yarn -g
yarn dev
```

### 后端
将 `.env.example` 替换成 `.env` 填入相关变量 📝  
可以替换相关的 Prompt 在: [Prompt.py](backend%2FConst%2FPrompt.py)

```bash
python.exe -m uvicorn app:app --reload 
```

## 📝 TODO
- 优化UI ✨
- 现在没有记忆功能，可以考虑本地存储聊天记录 💾
- 支持上传 CSV 文件转换为 SQL 之后再解析 📁
- 在数据量不大的情况下，增加一个保底措施即把所有数据都查出来 `select *` 然后再去问 🔍
