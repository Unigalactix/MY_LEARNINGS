# Building Your First AI App
## Hands-On Project: Customer Service Chatbot

### 🎯 Learning Objectives
By the end of this lesson, you'll have:
- Built a working AI chatbot from scratch
- Integrated OpenAI API with a simple web interface
- Implemented conversation memory and context
- Created a deployable application for your portfolio

## Project Overview

We'll build a customer service chatbot that can:
- Answer common questions about a fictional company
- Maintain conversation context
- Escalate complex issues to human agents
- Provide a professional web interface

### What You'll Learn
- API integration with OpenAI
- Simple web development with Streamlit
- Conversation management
- Error handling and user experience

### No Programming Experience? No Problem!
This guide assumes zero programming background. We'll explain every step and provide all the code you need.

## Setup and Prerequisites

### Step 1: Install Required Software

#### Install Python
1. Go to [python.org](https://python.org)
2. Download Python 3.8 or newer
3. Run the installer (check "Add Python to PATH")
4. Open Command Prompt/Terminal and type: `python --version`

#### Install Required Libraries
Open Command Prompt/Terminal and run these commands one by one:
```bash
pip install streamlit
pip install openai
pip install python-dotenv
```

### Step 2: Get OpenAI API Key
1. Go to [platform.openai.com](https://platform.openai.com)
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and save it securely (you'll need this)

### Step 3: Create Project Folder
1. Create a new folder on your computer called `ai-chatbot`
2. Open this folder in a text editor (like Notepad++ or VS Code)

## Building the Chatbot

### Step 1: Create Environment File
Create a file called `.env` in your project folder and add:
```
OPENAI_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual OpenAI API key.

### Step 2: Create Main Application File
Create a file called `app.py` with this code:

```python
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="TechCorp Customer Service",
    page_icon="🤖",
    layout="wide"
)

# Company information (customize this for your demo)
COMPANY_INFO = """
You are a helpful customer service representative for TechCorp, a software company.

Company Information:
- We sell project management software called "TaskMaster Pro"
- Our software costs $29/month per user
- We offer a 14-day free trial
- Support hours: Monday-Friday, 9 AM - 6 PM EST
- We integrate with Slack, Microsoft Teams, and Google Workspace
- Our software works on Windows, Mac, and mobile devices

Common Issues and Solutions:
- Password reset: Send users to techcorp.com/reset-password
- Billing questions: Transfer to billing team at billing@techcorp.com
- Technical issues: First ask about browser/device, then suggest clearing cache
- Integration problems: Check our integration guides at techcorp.com/integrations

Always be polite, helpful, and professional. If you can't answer something, 
offer to escalate to a human agent.
"""

def get_ai_response(messages):
    """Get response from OpenAI API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": COMPANY_INFO}
            ] + messages,
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I'm sorry, I'm having technical difficulties. Please try again or contact support at support@techcorp.com. Error: {str(e)}"

def main():
    # Title and header
    st.title("🤖 TechCorp Customer Service")
    st.markdown("Welcome! I'm here to help with your TaskMaster Pro questions.")
    
    # Initialize session state for conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("How can I help you today?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ai_response(st.session_state.messages)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with additional options
    with st.sidebar:
        st.header("Quick Actions")
        
        if st.button("🔄 Start New Conversation"):
            st.session_state.messages = []
            st.experimental_rerun()
        
        if st.button("👤 Talk to Human Agent"):
            st.info("Connecting you to a human agent... \n\nPlease call: 1-800-TECHCORP \nOr email: support@techcorp.com")
        
        st.header("Common Questions")
        quick_questions = [
            "How much does TaskMaster Pro cost?",
            "How do I reset my password?",
            "What integrations do you support?",
            "How do I start a free trial?"
        ]
        
        for question in quick_questions:
            if st.button(question):
                # Add the question to the chat
                st.session_state.messages.append({"role": "user", "content": question})
                response = get_ai_response(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.experimental_rerun()

if __name__ == "__main__":
    main()
```

### Step 3: Test Your Application
1. Open Command Prompt/Terminal
2. Navigate to your project folder: `cd path/to/ai-chatbot`
3. Run the application: `streamlit run app.py`
4. Your browser should open with your chatbot!

## Understanding the Code

### Key Components Explained

#### 1. Environment Setup
```python
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```
This securely loads your API key from the `.env` file.

#### 2. Company Information
```python
COMPANY_INFO = """
You are a helpful customer service representative...
"""
```
This is the "system prompt" that tells the AI how to behave and what information it knows.

#### 3. AI Response Function
```python
def get_ai_response(messages):
    response = openai.ChatCompletion.create(...)
```
This sends your conversation to OpenAI and gets back a response.

#### 4. User Interface
```python
st.chat_input("How can I help you today?")
```
Streamlit creates the web interface automatically.

## Customizing Your Chatbot

### Change the Company Information
Edit the `COMPANY_INFO` section to match any business:

```python
COMPANY_INFO = """
You are a customer service representative for [YOUR COMPANY NAME].

Company Information:
- We sell [YOUR PRODUCT/SERVICE]
- Our prices are [YOUR PRICING]
- Contact information: [YOUR CONTACT INFO]
- Business hours: [YOUR HOURS]

[Add any specific information about your business]
"""
```

### Add More Features

#### 1. Conversation Saving
Add this function to save conversations:

```python
def save_conversation():
    """Save conversation to a file"""
    if st.session_state.messages:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.txt"
        
        with open(filename, "w") as f:
            for message in st.session_state.messages:
                f.write(f"{message['role']}: {message['content']}\n\n")
        
        st.success(f"Conversation saved as {filename}")
```

#### 2. Customer Satisfaction Survey
Add a feedback section:

```python
# Add to sidebar
st.header("How did we do?")
rating = st.select_slider("Rate your experience:", 
                         options=["😞", "😐", "😊", "😄", "🤩"])
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
```

#### 3. FAQ Section
Add a collapsible FAQ:

```python
with st.expander("📋 Frequently Asked Questions"):
    st.markdown("""
    **Q: How do I reset my password?**
    A: Visit our password reset page at example.com/reset
    
    **Q: What are your support hours?**
    A: Monday-Friday, 9 AM - 6 PM EST
    
    **Q: How much does your service cost?**
    A: Our basic plan starts at $29/month per user
    """)
```

## Testing Your Chatbot

### Test Scenarios to Try

#### 1. Basic Information Requests
- "What does your software do?"
- "How much does it cost?"
- "What are your support hours?"

#### 2. Technical Support
- "I forgot my password"
- "The software isn't working"
- "How do I integrate with Slack?"

#### 3. Edge Cases
- Ask about something completely unrelated
- Ask for personal information
- Test conversation memory by referring to earlier messages

### Evaluation Criteria
- ✅ Stays in character as customer service rep
- ✅ Provides accurate company information
- ✅ Handles unknown questions gracefully
- ✅ Maintains professional tone
- ✅ Remembers conversation context

## Deployment Options

### Option 1: Streamlit Cloud (Free)
1. Create a GitHub account
2. Upload your project to GitHub
3. Connect to Streamlit Cloud
4. Deploy with one click

### Option 2: Local Sharing
1. Run `streamlit run app.py`
2. Note the network URL (usually shows as "Network URL")
3. Share this URL with others on your network

### Option 3: Heroku (Free Tier)
1. Create a Heroku account
2. Install Heroku CLI
3. Follow Heroku's deployment guide for Python apps

## Portfolio Presentation

### Demo Script (3 minutes)
1. **Introduction** (30 seconds): "I built an AI-powered customer service chatbot that can handle common inquiries and escalate complex issues."

2. **Basic Functionality** (1 minute): Show asking basic questions about pricing, features, support hours.

3. **Context Awareness** (1 minute): Demonstrate how it remembers previous conversation points.

4. **Edge Case Handling** (30 seconds): Show how it handles questions it can't answer.

### Technical Highlights to Mention
- "Integrated OpenAI's GPT model for natural language understanding"
- "Implemented conversation memory to maintain context"
- "Designed user-friendly interface with Streamlit"
- "Added error handling and graceful degradation"
- "Customizable for any business domain"

### Business Value Proposition
- Reduces support ticket volume by 40-60%
- Available 24/7 for customer inquiries
- Consistent responses and brand voice
- Easy to update with new information
- Scalable to handle unlimited conversations

## Troubleshooting Common Issues

### Issue: "ModuleNotFoundError"
**Solution**: Make sure you installed all packages:
```bash
pip install streamlit openai python-dotenv
```

### Issue: "Authentication Error"
**Solution**: Check your API key in the `.env` file:
- Make sure there are no extra spaces
- Verify the key is correct from OpenAI dashboard
- Ensure the `.env` file is in the same folder as `app.py`

### Issue: "Empty Response"
**Solution**: Check your OpenAI account:
- Verify you have API credits
- Check if your API key has proper permissions
- Try using a simpler prompt

### Issue: "App Won't Start"
**Solution**: 
- Make sure Python is installed correctly
- Try running `python --version` and `streamlit --version`
- Navigate to the correct folder in terminal

## Next Level Enhancements

### 1. Add Authentication
```python
# Simple password protection
password = st.sidebar.text_input("Enter password:", type="password")
if password != "demo123":
    st.error("Please enter the correct password to continue.")
    st.stop()
```

### 2. Add Analytics
```python
# Track conversation metrics
if "conversation_count" not in st.session_state:
    st.session_state.conversation_count = 0

# Increment counter on new conversations
st.sidebar.metric("Conversations Today", st.session_state.conversation_count)
```

### 3. Multiple Language Support
```python
language = st.sidebar.selectbox("Language:", ["English", "Spanish", "French"])

if language == "Spanish":
    COMPANY_INFO = """
    Eres un representante de servicio al cliente para TechCorp...
    """
```

## Success Metrics for Your Portfolio

### Technical Metrics
- Response time under 3 seconds
- 95% uptime during demo periods
- Handles 100+ message conversations without errors
- Successfully integrates with OpenAI API

### User Experience Metrics
- Intuitive interface requiring no training
- Clear escalation path to human agents
- Professional and consistent tone
- Helpful error messages and fallbacks

### Business Impact Metrics
- Can handle 80% of common customer inquiries
- Reduces average response time from 2 hours to 30 seconds
- Available 24/7 unlike human agents
- Easily customizable for different businesses

## Key Takeaways

1. **Start Simple**: Begin with basic functionality and add features incrementally
2. **User Experience Matters**: The interface is as important as the AI capability
3. **Handle Errors Gracefully**: Always have fallback options when AI fails
4. **Test Thoroughly**: Try edge cases and unexpected inputs
5. **Document Everything**: Clear setup instructions help others use your work

## Next Steps

### Immediate Actions:
1. Build and test your basic chatbot
2. Customize it for a specific business scenario
3. Deploy it for others to try
4. Document your process and learnings

### Future Enhancements:
1. Add voice interface capabilities
2. Integrate with real customer service systems
3. Add sentiment analysis for customer satisfaction
4. Implement multi-language support

### Portfolio Integration:
1. Add this project to your GitHub
2. Create a professional README
3. Record a demo video
4. Prepare your 3-minute presentation

## 🤔 Quick Self-Check
Can you explain to someone how your chatbot works and why businesses would want to use it? Practice your explanation until it's clear and compelling!

---
**Remember**: This is more than just a technical exercise - it's a real solution that businesses need. Focus on the value it creates, not just the technology it uses! 💡
