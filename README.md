# CI/CD Dependency Error Demo

This project intentionally imports `requests` without declaring it in
`requirements.txt`. In a clean environment, `pytest` fails during collection
with `ModuleNotFoundError: No module named 'requests'`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

To fix the error, add `requests` to `requirements.txt`.
