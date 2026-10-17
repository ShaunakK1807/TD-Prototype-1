# TD Prototype 1

This is the first prototype of my tower defence game, built with Python, Pygame, and NumPy.

## Setup

### Windows

From the project folder, create the virtual environment and install the dependencies:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### macOS

Run these commands from the project folder:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

VS Code uses `.vscode/settings.json` to select the project environment automatically. If it does not select it, use **Python: Select Interpreter** and choose the `.venv` interpreter (`.venv\Scripts\python.exe` on Windows or `.venv/bin/python` on macOS).

## Run

```bash
.venv/bin/python main.py
```

On Windows, use `.\.venv\Scripts\python.exe main.py` instead.

You can also press `F5` in VS Code or run the `Run game` task.

## Dependencies

- Pygame for the game window and event loop
- NumPy for numerical game logic
