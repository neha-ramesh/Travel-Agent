🧭 Travel Planner AI Assistant
An intelligent and interactive Travel Planning Assistant built using Streamlit and Google Gemini / Cohere APIs.
This app provides tailored travel suggestions, answers your destination queries, and serves as a helpful AI travel buddy 🌍✈️.

🔥 Features
🧠 Generative AI-Powered Chat

Ask anything travel-related: best time to visit, top attractions, local food, safety tips, etc.

Powered by Google Gemini or Cohere Command R (switchable).

🗺️ Customized Travel Recommendations

Get destination suggestions based on your mood, preferences, or time of year.

Works conversationally like ChatGPT but focused entirely on travel!

🖼️ Interactive & Minimal UI

Built with Streamlit for a smooth, reactive user interface.

Clean layout with intuitive prompt box and instant responses.

🔐 Secure Key Management

Uses .env locally and Streamlit secrets on cloud deployment.

No sensitive keys exposed in the codebase.

🤖 Tech Stack
Component	Description
Streamlit	For building the frontend & deploying as a web app
Pillow	To render and customize image display
python-dotenv	For managing environment variables locally
Google Generative AI	For generative travel responses (e.g., Gemini Pro)
Cohere	Optional alternative for natural language generation

🛠️ How It Works
💬 Input
User enters a question or query like:

“What are some romantic destinations to visit in December?”

🤖 AI Response
Based on your selected model (Cohere or Gemini), it generates:

Lists of locations

Travel tips

Estimated costs or cultural insights

🌐 Output
Answers are displayed in real-time on the Streamlit app interface.

🚀 Getting Started
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/travel-planner-ai.git
cd travel-planner-ai
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up API Key
Create a .env file and add your API key:

env
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
Note: On Streamlit Cloud, use the Secrets section instead.

🌐 Deployment (Streamlit Cloud)
Push this repo to GitHub

Go to Streamlit Cloud

Create a new app from this repo

Add the secret key in Settings > Secrets:

toml
Copy
Edit
GOOGLE_API_KEY = "your_api_key_here"
📂 Folder Structure
bash
Copy
Edit
travel-planner-ai/
│
├── app.py              # Main Streamlit app
├── download.jpg        # Travel-themed image shown in UI
├── .env                # API keys (not uploaded)
├── requirements.txt    # Required packages
└── README.md           # You're reading it!
🎨 Sample UI

(Replace with actual screenshot once deployed)

💡 Future Enhancements
🌍 Add maps integration for visualizing suggestions

📆 Let users build itineraries from the chat

📥 Export recommendations as PDFs

🗣️ Enable speech-to-text for inputs
