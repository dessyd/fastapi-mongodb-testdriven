# fastapi-mongodb-testdriven
From: https://testdriven.io/blog/fastapi-mongo/

### Local Setup

```
# Create virtual environment
python3 -m venv venv
# Activate it
source venv/bin/activate
# make sure pip is up to date
pip install --upgrade pip
# install project's requirements
pip install -r requirements.txt
```

### To Do
- Validation in model does not apply to updates
- put credentials into `.env`
- in `database.py` read from `.env`