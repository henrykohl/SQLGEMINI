# SQLGEMINI
End to End Gen AI Project using Google Gemini Pro | 2024 [Video](https://www.youtube.com/watch?v=7uR3JFYOa7s)

* Syllabus
```
Agenda - Text To SQL LLM Application

Prompt--->LLM--->Gemini Pro--->Query--->SQL Database--->Response

Implementation

1. SQLlite---Inset some records--Python Programming
2. LLM Application-->Gemini Pro--->SQL Database
```

* 建立 virtual environment
```bash
>conda create -p venv python==3.10 -y 
>conda activate venv/
```

* requirements.txt

* <font color="red">.env (Github不會保存此檔，clone 此 reposiotry 一定要重新建立)
> ``` 
> GOOGLE_API_KEY = '...'
> ```

```bash
pip install -r requiremetns.txt
```

* sqlite.py

> ```python
> python sqlite.py
> ```

* sql.py
> ```bash
> >streamlit run sql.py
> ```