# ai-cicd-test

Minimal repository for validating an AI-assisted CI/CD setup.

## What’s inside

- A tiny Python module in `src/`
- A unit test suite in `tests/` (stdlib `unittest`)
- GitHub Actions CI workflow in `.github/workflows/ci.yml`

## Run locally

```bash
python -m compileall -q src
python -m unittest discover -s tests -p "test_*.py"
```

