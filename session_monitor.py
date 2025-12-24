import streamlit as st
import logging
import weakref
from streamlit.runtime.scriptrunner import get_script_run_ctx

# Configure logger
logger = logging.getLogger("TokenTracker")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class SessionMonitor:
    """
    A class that tracks session data and logs it upon destruction (disconnection/cleanup).
    """
    def __init__(self, session_id):
        self.session_id = session_id
        self.total_tokens = 0

    def update_tokens(self, count):
        self.total_tokens += count

    def __del__(self):
        # This method is called when the object is garbage collected,
        # which happens when the Streamlit session ends/expires.
        logger.info(f"Session {self.session_id} disconnected. Total Tokens Consumed: {self.total_tokens}")

def get_monitor():
    """
    Retrieves or creates the SessionMonitor for the current session.
    """
    if 'monitor' not in st.session_state:
        try:
            ctx = get_script_run_ctx()
            session_id = ctx.session_id if ctx else "unknown_session"
        except Exception:
            session_id = "unknown_session"
            
        st.session_state.monitor = SessionMonitor(session_id)
        logger.info(f"Session {session_id} started.")
        
    return st.session_state.monitor
