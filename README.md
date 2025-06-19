# GPT Data Insights Agent

A conversational AI agent that allows users to query structured CSV datasets using natural language. Built using OpenAI GPT-4, LangChain, and FAISS.

## 🔍 Features
- Natural language queries over uploaded CSV data.
- Uses FAISS for document retrieval and LangChain for LLM orchestration.
- Modular design for easy expansion.
- Built-in prompt engineering and evaluation examples.

## 🛠️ Tech Stack
- Python 3.8+
- OpenAI API
- LangChain
- FAISS
- Pandas
- Streamlit

## 🚀 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/Manav2315/gpt-data-insights-agent.git
cd gpt-data-insights-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your OpenAI API key**  
Create a `.env` file and add:
```env
OPENAI_API_KEY=your_openai_key_here
```

> ⚠️ **Note:** The current version does not include an OpenAI API key due to API quota limitations. Please use your own key from [platform.openai.com](https://platform.openai.com/account/api-keys) to activate LLM functionalities.

4. **Run the Streamlit app**
```bash
streamlit run app.py
```

## 🧪 Sample Prompt
> "What was the average sales in Q3 2023?"  
> "List the top 5 products by revenue."

## 📁 Sample CSV Structure
| Product | Sales | Date |
|---------|-------|------|
| A       | 1200  | 2023-07-10 |
| B       | 980   | 2023-07-15 |

---

Built by Manav More
