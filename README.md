# Twenty Questions - Fantastic AI Games 🧩

🎉 A fun, colorful Twenty Questions game for children ages 10-12 (grades 5-6) powered by Anthropic's AI!

## 🎮 How to Play

1. **Think of an object** - Keep it to yourself!
2. **Answer YES or NO** - Click the big colorful buttons.
3. **20 Questions Challenge** - Can the AI guess what you're thinking?
4. **Learn Fun Facts!** - When the AI wins, learn a cool history or fun fact about your object!

## 🌈 Features

- **🎨 Child-Friendly Design** - Bright colors, "Comic Neue" font, and cute styling.
- **🤖 Smart AI** - Powered by **Anthropic Claude 3.5 Haiku** via the `strands-agents` library.
- **🧠 Educational** - Provides fun facts and history about the guessed objects.
- **🔒 Privacy First** - No personal data stored or collected. Sessions are ephemeral.
- **📱 Responsive** - Works great on tablets and computers.
- **🐳 Dockerized** - Ready for easy deployment on any VPS.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ (or Docker)
- Anthropic API key

### Method 1: Using uv (Recommended) 🚀

If you have `uv` installed, you don't need to manually create environments or install dependencies. `uv` handles it all in one command.

```bash
# Run immediately (uv will set up the environment and install packages)
AKEY="your-anthropic-api-key" uv run streamlit run app.py
```

### Method 2: Standard Python (pip) 🐍

1. **Clone the repository:**
   ```bash
   git clone https://github.com/haowubyrideau/twenty_questions_game.git
   cd twenty_questions_game
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   export AKEY="your-anthropic-api-key"
   streamlit run app.py
   ```

### Method 2: Docker / VPS

This project includes a `Dockerfile` for easy container deployment (e.g., on Hostinger VPS).

1. **Build the image:**
   ```bash
   docker build -t twentyqgames .
   ```

2. **Run the container:**
   ```bash
   docker run -d \
     -p 8501:8501 \
     -e AKEY="your-api-key-here" \
     --restart always \
     --name twentyqgames \
     twentyqgames
   ```

3. Access at `http://localhost:8501` (or your VPS IP).

## ☁️ Deployment on Render.com

1. Create a new **Web Service** on Render.
2. Connect your GitHub repository.
3. Add the Environment Variable:
   - `AKEY`: Your Anthropic API Key.
4. Render will automatically use the `render.yaml` configuration to build and deploy.

## 🏗️ Project Structure

```
twentyqgames/
├── app.py              # Main Streamlit application
├── session_monitor.py  # Session token logging utility
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project configuration (uv)
├── Dockerfile          # Container configuration
├── render.yaml         # Render.com configuration
└── PRD.md              # Project Requirements Document
```

## 🔐 Privacy & Safety

- **No Data Storage**: Names and game data are never saved permanently.
- **Session Only**: All data exists only during the current game session.
- **Disclaimer**: We don't collect any data and store any answers. This is for education and recreational purposes.

## 🙋‍♀️ Support

For any questions, please email: [again.jigsaws9i@icloud.com](mailto:again.jigsaws9i@icloud.com)

---

*Made with ❤️ for children everywhere!* 🌟