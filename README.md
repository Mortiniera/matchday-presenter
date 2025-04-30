# Match Day Presenter 🏟️🎙️

**AI-powered football insights delivered like a pro presenter.**

This project automates the process of gathering match-specific football news and presenting it as natural speech, using a multi-agent pipeline powered by LLMs, summarizers, and text-to-speech tools.

---

## 🧠 What It Does

- Fetches trending football news and fan discussions from Reddit sources and specific subreddits .
- Summarizes key talking points using Gemini Flash as a summarizer agent.
- Converts the summary into spoken word using Eleven Labs (text-to-speech).
- Outputs audio clips styled like a sports news presenter giving match previews.


## 🎥 Demo Screenshot
![RedditMCP](https://raw.githubusercontent.com/Mortiniera/matchday-presenter/main/demo/redditMCP.png)
![Summarizer](https://raw.githubusercontent.com/Mortiniera/matchday-presenter/main/demo/Summarizer.png)
![SpeechToText](https://raw.githubusercontent.com/Mortiniera/matchday-presenter/main/demo/SpeechToText.png)

You can listen to an example of the match day presenter output here:  
[🔊 Listen on Gdrive](https://drive.google.com/file/d/1wJmyWdc-u6-cB-WIotvuo6hHJjk3iL2S/view?usp=sharing)

---


---

## 🛠️ Tech Stack

- **Gemini Flash** (or LLM of choice) – summarization and prompt-based dialogue generation
- **Reddit MCP server API** – trending topics and discussions
- **Eleven Labs MCP server** – realistic voice synthesis (text to speech)
- **Python** – script orchestration
- Optional: outputs can be paired with static images and/or passed to video tools like Kling for video generation and lyp syncing.

---

## 🚀 How to Install & Run

### 1. Clone or Fork the Repo

```bash
git clone https://github.com/yourusername/match-day-presenter.git
cd match-day-presenter
```

### 2. API Keys

You'll need the following:
- Google API Key
- Reddit Client ID and Secret
- Eleven Labs API Key

### 3. Set Up Environment Variables

```bash
cp .env.example .env
# Open .env and fill in the keys you obtained
```

### 4. Set Up Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

> Requires **Python 3.11+**

### 5. Run the Project (via ADK)

```bash
cd agents/
adk web
```

Then open [http://localhost:8000/dev-ui](http://localhost:8000/dev-ui) in your browser, select the `CoordinatorAgent`, and interact with it from the UI.

---

## 📌 Possible improvements

- Add multilingual presenter voices
- Automatically generate short video clips using Kling or Sora
- Add multiple personas ("experts") in panel-style debates

---

## 📄 License

MIT License — feel free to fork, remix, or adapt!

---

## 🙌 Credits

Built using:
- Gemini
- Eleven Labs
- Reddit API
- Google ADK

> Big thanks to [@chongdashu](https://github.com/chongdashu)

