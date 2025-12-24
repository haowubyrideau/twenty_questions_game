import streamlit as st
import os
import logging
from strands import Agent
from strands.models.anthropic import AnthropicModel
from session_monitor import get_monitor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Configuration ---
# The PRD mentions AKEY. We'll ensure it's available for the AnthropicModel.
api_key = os.environ.get("AKEY") or os.environ.get("ANTHROPIC_API_KEY")

# Model ID configuration
MODEL_ID = "claude-4-5-haiku-20251015" 

# --- Game Logic ---

def get_agent():
    """
    Initializes the Strands Agent with Anthropic Model.
    """
    try:
        if not api_key:
            st.error("Missing API Key (AKEY or ANTHROPIC_API_KEY).")
            return None

        # Configure the Anthropic Model
        model = AnthropicModel(
            client_args={
                "api_key": api_key,
            },
            model_id=MODEL_ID,
            max_tokens=1024,
            params={
                "temperature": 0.7, 
            }
        )

        system_prompt = (
            "You are playing '20 Questions' with a child (Grade 5-6). "
            "The child has an object in mind. Your goal is to guess it within 20 attempts. "
            "1. Ask simple, clear Yes/No questions. "
            "2. Use a friendly, cute, and exciting tone. "
            "3. Analyze the previous answers carefully to narrow down possibilities. "
            "4. You can make a direct guess (e.g., 'Is it a pizza?') when you are reasonably confident. "
            "5. If the user says 'Yes' to your specific guess, you have WON! "
            "6. WHEN YOU WIN: "
            "   - Celebrate with enthusiasm! "
            "   - Provide a short story or interesting history/fun fact about the item. "
            "     (e.g., 'Did you know that the crayon was invented by...'). "
            "   - END your response with the exact text: [GAME_WON]"
            "7. Do NOT number your questions. Just ask the question."
        )

        agent = Agent(
            model=model,
            system_prompt=system_prompt
        )
        return agent
    except Exception as e:
        st.error(f"Failed to initialize Agent: {e}")
        return None

def generate_response(history):
    """
    Generates a response from the agent based on conversation history.
    """
    monitor = get_monitor() # Ensure session tracking
    agent = get_agent()
    if not agent:
        return "Error: Agent not available."

    transcript = "Here is the game progress so far:\n"
    for role, text in history:
        transcript += f"{role}: {text}\n"
    
    transcript += "AI (You): "
    
    # Estimate input tokens (rough char count / 4)
    input_usage = len(transcript) / 4

    try:
        response_obj = agent(transcript)
        response_text = str(response_obj)
        
        # Estimate output tokens
        output_usage = len(response_text) / 4
        
        # Update monitor
        monitor.update_tokens(int(input_usage + output_usage))
        
        return response_text
    except Exception as e:
        logger.error(f"Agent generation failed: {e}")
        return "Oops! I got a bit confused. Can we try again?"

# --- UI ---

def main():
    st.set_page_config(page_title="20 Questions", page_icon="🧩")
    
    # Initialize session monitor early
    get_monitor()

    # Custom CSS for children-friendly font and UI
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
        
        html, body, [class*="css"]  {
            font-family: 'Comic Neue', cursive;
        }
        .title {
            color: #FF6B6B;
            text-align: center;
        }
        .big-text {
            font-size: 24px;
            color: #4ECDC4;
            font-weight: bold;
            text-align: center;
            margin: 20px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            height: 50px;
            font-size: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 class='title'>✨ 20 Questions Game ✨</h1>", unsafe_allow_html=True)

    if 'game_state' not in st.session_state:
        st.session_state.game_state = 'init'
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'question_count' not in st.session_state:
        st.session_state.question_count = 0
    if 'last_ai_msg' not in st.session_state:
        st.session_state.last_ai_msg = ""

    if st.session_state.game_state == 'init':
        st.write("Hello! I'm your guessing friend. What's your name?")
        name = st.text_input("Name", label_visibility="collapsed")
        if st.button("Next") and name:
            st.session_state.player_name = name
            st.session_state.game_state = 'ready'
            st.rerun()

    elif st.session_state.game_state == 'ready':
        st.markdown(f"<div class='big-text'>Hi {st.session_state.player_name}! 👋</div>", unsafe_allow_html=True)
        st.write("We are going to play a guessing game!")
        st.info("Think of ONE object and keep it in your mind. Don't tell me yet! I will try to guess it.")
        
        if st.button("I'm Ready! Start Game 🚀"):
            st.session_state.game_state = 'playing'
            st.session_state.history = []
            st.session_state.question_count = 0
            
            with st.spinner("Thinking of a good question..."):
                initial_prompt = "The game is starting. Ask the first question."
                response = generate_response([("System", initial_prompt)])
                st.session_state.last_ai_msg = response
                st.session_state.history.append(("AI", response))
                st.session_state.question_count += 1
            st.rerun()

    elif st.session_state.game_state == 'playing':
        # Clamp progress to 1.0 to avoid error if count goes over 20
        progress_val = min(st.session_state.question_count / 20, 1.0)
        st.progress(progress_val)
        st.write(f"Question {st.session_state.question_count} / 20")

        ai_msg = st.session_state.last_ai_msg
        # Handle the game won token display
        display_msg = ai_msg.replace("[GAME_WON]", "")
        st.markdown(f"<div class='big-text'>{display_msg}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("YES 👍"):
                process_answer("Yes")
        with col2:
            if st.button("NO 👎"):
                process_answer("No")

        if st.session_state.question_count >= 20:
             st.warning("I couldn't guess it within 20 questions! 😲")
             st.session_state.game_state = 'lost_guessing'
             st.rerun()

    elif st.session_state.game_state == 'lost_guessing':
        st.markdown("<div class='big-text'>I give up! What was it? 🤔</div>", unsafe_allow_html=True)
        item_name = st.text_input("The item was:", key="reveal_item")
        
        if st.button("Tell AI") and item_name:
            with st.spinner("Reading about it..."):
                # Custom prompt for the "Lost" reaction
                prompt = f"The user has revealed the item was: '{item_name}'. You failed to guess it. React with surprise (e.g., 'No way! really?') and provide a short story or fun fact about '{item_name}'."
                
                # Append to history so the AI has context
                st.session_state.history.append(("System", prompt))
                
                response = generate_response(st.session_state.history)
                st.session_state.last_ai_msg = response
                st.session_state.game_state = 'lost_finished'
                st.rerun()

    elif st.session_state.game_state == 'lost_finished':
        st.markdown(f"<div class='big-text'>{st.session_state.last_ai_msg}</div>", unsafe_allow_html=True)
        if st.button("Play Again 🔄"):
            reset_game()

    elif st.session_state.game_state == 'finished':
        # Display the winning message one last time (stored in last_ai_msg)
        display_msg = st.session_state.last_ai_msg.replace("[GAME_WON]", "")
        st.markdown(f"<div class='big-text'>{display_msg}</div>", unsafe_allow_html=True)
        
        st.balloons() # Celebrate!
        if st.button("Play Again 🔄"):
            reset_game()

def process_answer(answer):
    st.session_state.history.append(("Player", answer))
    
    with st.spinner("Hmm... let me think..."):
        response = generate_response(st.session_state.history)
        
        # Check for win condition
        if "[GAME_WON]" in response:
            st.session_state.game_state = 'finished'
            # Clean up the response for storage if needed, or just keep it
            # We keep it to strip it on display
        
        st.session_state.last_ai_msg = response
        st.session_state.history.append(("AI", response))
        st.session_state.question_count += 1
    
    st.rerun()

def reset_game():
    # Go back to 'ready' to skip name input, assuming player_name is still set.
    st.session_state.game_state = 'ready'
    st.session_state.history = []
    st.session_state.question_count = 0
    st.session_state.last_ai_msg = ""
    st.rerun()

if __name__ == "__main__":
    main()
    
    # Disclaimer Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: grey; font-size: 12px;'>
            We don't collect any data and store any answers. This is for education and recreational purposes.<br>
            Any question please email <a href="mailto:again.jigsaws9i@icloud.com">again.jigsaws9i@icloud.com</a>
        </div>
        """, 
        unsafe_allow_html=True
    )
