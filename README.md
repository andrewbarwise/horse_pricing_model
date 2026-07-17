# horse_pricing_model

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### Install uv

If you don't already have `uv` installed:

**macOS (Homebrew)**

```bash
brew install uv
```

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create the virtual environment

```bash
uv venv
```

Activate it:

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\activate
```

### Install project dependencies

```bash
uv sync
```

This will install all dependencies specified in `pyproject.toml` and `uv.lock`.

### Running the project

Run Python scripts with:

```bash
uv run python path/to/script.py
```

or, if you've activated the virtual environment:

```bash
python path/to/script.py
```
