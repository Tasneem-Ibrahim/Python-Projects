
uv init
uv add "fastapi[standard]" "uvicorn[standard]"
uv add sqlmodel
uv run uvicorn main:app --reload/
uv run python -m uvicorn main:app --reload