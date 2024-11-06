##Python flask basic api


- setup environment variable
```bash
cp .env.example .env
```

- (conditional) If venv folder is not available
```bash
python3 -m venv venv
```

- enable virtual environment
```bash
source venv/bin/activate
```

- install required dependencies
```bash
pip install -r requirements.txt
```



- run dev
```bash
python app.py
```


- turn off virtual environment
```bash
deactivate
```

- generate requirements.txt
```bash
pip freeze > requirements.txt
```