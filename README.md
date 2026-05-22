# autogen-playground

Small experiments with [Microsoft AutoGen](https://github.com/microsoft/autogen) using local models via [Ollama](https://ollama.com).

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) running locally (`ollama serve`)
- A pulled model that matches the script config (e.g. `ollama pull llama3.1`)

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

pip install autogen-agentchat autogen-ext autogen
```

Adjust model names and Ollama host in each script if yours differ from the defaults.

## Scripts

| File | Description |
|------|-------------|
| `main.py` | Classic AutoGen chat: assistant + user proxy over Ollama (`llama3.1:latest`). |
| `app.py` | Assistant writes Python; user proxy runs it locally in `coding/`. |
| `autogen-app.py` | AutoGen AgentChat: Writer and Reviewer agents in a round-robin group chat. |

Run any script:

```bash
python main.py
python app.py
python autogen-app.py
```

## Notes

- `app.py` uses `client_host` for Ollama — set it to your machine (e.g. `http://localhost:11434`).
- Generated code and artifacts go under `coding/` (gitignored).
- This repo is for learning and demos, not the official AutoGen project.

## License

Personal playground — use and modify as you like.
