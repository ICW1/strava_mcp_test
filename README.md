# Strava MCP Test

This project provides a Gradio-based web interface to interact with your Strava activities using a Large Language Model (LLM) via the Mistral API and a custom MCP (Model Control Protocol) server.

## Features

- **Ask questions about your Strava activities** in natural language.
- **Quick example queries** to get started.
- **Powered by Mistral LLMs** and a custom Strava MCP server.

## Requirements

- Python 3.12+
- [Mistral API access](https://docs.mistral.ai/).  
   For Mistral API keys go to: https://console.mistral.ai/home
- Strava API credentials.  
   For Strava API keys go to: https://developers.strava.com/docs/getting-started/ & https://www.strava.com/settings/api

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/strava_mcp_test.git
   cd strava_mcp_test
   ```

2. **Create and activate a virtual environment**

   ```sh
   python3 -m venv strava_mcp_demo_env
   source strava_mcp_demo_env/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your credentials:

   ```
   cp .env.example .env
   ```

   Edit `.env`:

   ```
   MISTRAL_API_KEY=your_mistral_api_key
   STRAVA_CLIENT_ID=your_strava_client_id
   STRAVA_CLIENT_SECRET=your_strava_client_secret
   STRAVA_ACCESS_TOKEN=your_strava_access_token
   STRAVA_REFRESH_TOKEN=your_strava_refresh_token
   ```

5. **Ensure the Strava MCP server is available**

   Follow the instructions in the README at: https://github.com/ctvidic/strava-mcp-server
   ```
   /path/to/strava_server.py
   ```
   Update the path in [`llm_module.py`](llm_module.py) if your server is elsewhere.

## Usage

Start the Gradio web app:

```sh
python gradio_all.py
```

- The app will launch in your browser at [http://localhost:7860](http://localhost:7860).
- Enter your question or use a quick example to interact with your Strava data.

## File Overview

- [`gradio_all.py`](gradio_all.py): Gradio UI for querying Strava activities.
- [`llm_module.py`](llm_module.py): Handles communication with the Mistral LLM and MCP server.
- `.env.example`: Example environment variable configuration.
- `requirements.txt`: Python dependencies.

## License

MIT License

---

**Note:** This project requires valid API keys and access tokens for both Mistral and Strava.
```
