
uv init

uv add "fastapi[standard]" "uvicorn[standard]"

uv run uvicorn main:app --reload


#### If uv run uvicorn main:app --reload gives a trampoline/path error on Windows, use:

uv run python -m uvicorn main:app --reload 