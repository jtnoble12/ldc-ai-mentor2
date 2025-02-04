import streamlit as st
import random

# Define LDC scenarios
def ldc_scenarios():
    return [
        {"challenge": "A new competitor releases a breakthrough AI device that threatens your flagship product. Do you:",
         "options": {"A": "Double down on existing strategy and improve current product", 
                     "B": "Pivot quickly and integrate AI into your roadmap", 
                     "C": "Wait and observe the market reaction"},
         "ldc_principle": "Leading Through Fog – Making decisions without full clarity."},
        
        {"challenge": "Your organization faces resistance to disruptive change due to its strong existing culture. Do you:",
         "options": {"A": "Mandate the change top-down", 
                     "B": "Incentivize teams to explore adaptive approaches", 
                     "C": "Conduct internal workshops on innovation mindset"},
         "ldc_principle": "Go Deep to Find the Real Problem – Identifying hidden cultural barriers."},
        
        {"challenge": "Your company needs to balance short-term profit goals with long-term innovation investments. Do you:",
         "options": {"A": "Allocate resources strictly based on current ROI", 
                     "B": "Adopt a balanced portfolio approach with high-risk, high-reward bets", 
                     "C": "Defer innovation until profitability improves"},
         "ldc_principle": "Both/And Thinking – Managing paradoxical demands."},
        
        {"challenge": "Your leadership team is divided on an important decision. Do you:",
         "options": {"A": "Force a decision quickly", 
                     "B": "Encourage open debate and deliberation", 
                     "C": "Defer to historical best practices"},
         "ldc_principle": "Disagree to Agree – Constructive conflict helps innovation."},

        {"challenge": "You notice your team avoids risk-taking. Do you:",
         "options": {"A": "Create financial incentives for innovation", 
                     "B": "Encourage failure as a learning process", 
                     "C": "Ensure all projects have a clear ROI before proceeding"},
         "ldc_principle": "Fail to Succeed – Encouraging calculated risks."},

        {"challenge": "Your company culture is highly hierarchical, stifling innovation. Do you:",
         "options": {"A": "Flatten decision-making structures", 
                     "B": "Encourage more junior employee-led initiatives", 
                     "C": "Rely on leadership to dictate change"},
         "ldc_principle": "Lead by Letting Go – Empowering employees at all levels."},

        {"challenge": "A major market shift threatens your business model. Do you:",
         "options": {"A": "Stick to core strengths", 
                     "B": "Experiment with new revenue models", 
                     "C": "Wait for more data before pivoting"},
         "ldc_principle": "Decisively Hedge – Balancing risk and stability."},

        {"challenge": "Your product is experiencing slow adoption. Do you:",
         "options": {"A": "Aggressively market the existing product", 
                     "B": "Adjust product based on early feedback", 
                     "C": "Delay launch until further testing"},
         "ldc_principle": "Adaptive Thinking – Learning through iterations."},
    ]

# Track user progress
if 'score' not in st.session_state:
    st.session_state['score'] = 0
if 'question_number' not in st.session_state:
    st.session_state['question_number'] = 0
if 'questions' not in st.session_state:
    st.session_state['questions'] = random.sample(ldc_scenarios(), 10)

st.title("LDC AI Mentor: The Leadership Challenge")

if st.session_state['question_number'] < len(st.session_state['questions']):
    scenario = st.session_state['questions'][st.session_state['question_number']]
    st.write(f"### Question {st.session_state['question_number'] + 1}: {scenario['challenge']}")
    choice = st.radio("Choose your response:", list(scenario["options"].values()))

    if st.button("Submit Answer"): 
        selected_key = [k for k, v in scenario["options"].items() if v == choice][0]
        st.session_state['score'] += 1  # Simple scoring mechanism (can be enhanced)
        st.session_state['question_number'] += 1
        st.write(f"## Your choice: {choice}")
        st.write(f"### LDC Principle Applied: {scenario['ldc_principle']}")
        st.success("Reflection: How does this align with your leadership style?")
        st.experimental_rerun()
else:
    st.write(f"## Game Over! Your final score: {st.session_state['score']}/10")
    st.balloons()
    st.write("Want to play again?")
    if st.button("Restart Game"):
        st.session_state['score'] = 0
        st.session_state['question_number'] = 0
        st.session_state['questions'] = random.sample(ldc_scenarios(), 10)
        st.experimental_rerun()