# The project requirements:

## Technical:
* **UI Framework:** Streamlit (Children friendly font and UI design, reference PBR Wow in the world theme).
* **Agent Library:** `strands-agents` (specifically with Anthropic provider).
* **AI Model:** Anthropic Claude 4.5 Haiku (`claude-4-5-haiku-20251015`).
* **Language:** Python 3.11+.
* **Package Manager:** `uv` (preferred) or `pip`.
* **Deployment:** 
    *   **Render.com** (Web Service).
    *   **Docker** (Containerized for VPS hosting).
* **Environment Variables:** `AKEY` (Anthropic API Key).

## Development Environment
* You use `uv` for dependency management.
* You need to use the `strands-agents` API to build the agent.

## User Stories
You are playing with children in grade 5-6.  
You play a game called "Twenty Questions". This game is different from the classic version.

**Game Rules:**
1. Ask the player to have an object in mind and keep it secret.
2. The AI (You) needs to try to guess the item.
3. The player can only response 'Yes' or 'No'.
4. Maximum attempts: 20.

## Operation & Logging
* **Hosting:** Render.com or Docker on VPS.
* **Source Code:** GitHub.
* **Logging:** In server-side logs, upon session disconnect, show the total estimated token consumption for that session.

## User Experience

### 1. Launch / Init
* Ask for the player's name.
* Show an intro note: "We are going to play a guessing game. Ask the player to think about one thing and keep that in mind. I will guess it out. When you are ready click 'start'."
* Show a 'Start' button.

### 2. Gameplay (Loop)
* AI makes a guess or asks a question in a cute font.
* Player clicks "YES" or "NO" buttons.
* AI follows the clue and asks the next question, using previous context.
* Repeat until the item is guessed or 20 questions are used.

*Example Flow:*
> AI: Is it something you can see? -> Player: Yes
> AI: Is it something on the earth? -> Player: No
> AI: Is it something far away? -> Player: Yes
> AI: Is it the moon? -> Player: No
> AI: Is it the Neptune? -> Player: Yes (Win)

### 3. Game Won
* **Celebration:** Give positive feedback/balloons.
* **Educational Content:** Create a summary and give a short story or history/fun fact about the item (e.g., "Did you know that crayon was invented by...").
* **Play Again:** Provide a button to restart the game. The question counter must reset. **Do not** ask for the name again; jump straight to the "Ready" state.

### 4. Game Lost (20 Questions Reached)
* **Prompt:** The AI should ask "I give up! What was the item?"
* **Action:** User inputs the item name.
* **Reaction:** AI acts surprised ("No way! really?") and provides a short story or history/fun fact about the revealed item.
* **Play Again:** Provide a button to restart.

### 5. Disclaimer
* At the bottom of the app, show a disclaimer:
  > "We don't collect any data and store any answers. This is for education and recreational purposes. Any question please email again.jigsaws9i@icloud.com"

## Resources
* Strands Agent Library: https://github.com/strands-agents/samples/blob/main/01-tutorials/01-fundamentals/01-first-agent/01-first-agent.ipynb
* Anthropic Provider: https://strandsagents.com/0.1.x/documentation/docs/user-guide/concepts/model-providers/anthropic/