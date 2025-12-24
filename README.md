# Twenty Questions - Fantastic AI Games

🎉 A fun, colorful Twenty Questions game for children ages 10-12 (grades 5-6) powered by Anthropic's AI!

## 🎮 How to Play

1. **Think of an object** - Keep it to yourself!
2. **Answer YES or NO** - Click the big colorful buttons
3. **20 Questions Challenge** - Can the AI guess what you're thinking?
4. **Have Fun!** - Enjoy the magical AI-powered guessing game!

## 🌈 Features

- **🎨 Child-Friendly Design** - Bright colors, large buttons, and cute styling
- **🤖 Smart AI** - Powered by Anthropic's Haiku 4.5 model
- **🎮 Interactive Gameplay** - Simple yes/no button interface
- **🔒 Privacy First** - No personal data stored or collected
- **📱 Responsive** - Works great on tablets and computers

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Anthropic API key

### Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd twentyqgames
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
export AKEY="your-anthropic-api-key"
```

4. **Run the game:**
```bash
streamlit run app.py
```

### Environment Variables

- `AKEY` - Your Anthropic API key (required)

## 🏗️ Project Structure

```
twentyqgames/
├── app.py              # Main Streamlit application
├── prompts.yaml        # AI prompt configurations
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project configuration
├── render.yaml         # Render deployment config
└── README.md          # This file
```

## 🎨 UI/UX Design

### Color Scheme
- **Background**: Purple/blue gradient
- **Buttons**: Green (YES) and Red (NO) with emojis
- **Text**: Yellow title, colorful accents
- **Cards**: White with colorful borders

### Interactive Elements
- **Large Buttons**: Easy-to-click YES/NO buttons
- **Progress Bar**: Visual indicator of questions used
- **Animations**: Hover effects and smooth transitions
- **Balloons**: Celebration animation on win

## 🔧 Development

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run app.py
```

### Testing
The application includes basic error handling and fallback mechanisms:
- Fallback questions if AI fails
- Session state management
- Error logging

## ☁️ Deployment

### Render.com Deployment
The project includes a `render.yaml` configuration file for easy deployment:

1. Fork this repository
2. Connect to Render.com
3. Add your `AKEY` environment variable
4. Deploy!

### Environment Requirements
- Python 3.11
- Required dependencies from `requirements.txt`
- Anthropic API key

## 🔐 Privacy & Safety

- **No Data Storage**: Names and game data are never saved
- **Session Only**: All data exists only during the current game session
- **Child-Safe**: AI responses are filtered for age-appropriate content
- **Transparent**: Clear privacy disclaimer at the bottom of every page

## 🤖 AI Integration

### Anthropic Model
- **Model**: Claude 3 Haiku
- **Purpose**: Generating strategic yes/no questions
- **Safety**: Configured with appropriate temperature and max tokens

### Prompt Engineering
- **System Prompts**: Guide AI behavior for child interaction
- **User Prompts**: Manage game flow and messaging
- **Configurable**: Easy to modify prompts in `prompts.yaml`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♀️ Support

For issues or questions, please open an issue on GitHub.

---

*Made with ❤️ for children everywhere!* 🌟
