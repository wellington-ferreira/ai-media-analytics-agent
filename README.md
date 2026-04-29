
# 🤖 AI Media Analytics Agent

🌎 This README is available in Portuguese: [README.pt-BR.md](./README.pt-BR.md)

---

## Overview

This project implements an **Autonomous AI Agent** that acts as a **Junior Media Analyst**, specializing in e-commerce. It is capable of interpreting business questions in natural language, querying real data from acquisition channels, and transforming complex metrics into actionable and structured insights for decision-making.

**Stack: Python | FastAPI | LangGraph | BigQuery | Groq/OpenAI**

---

## The agent:

Understands the intent of the question (descriptive vs analytical)
Decides when to query real data (BigQuery)
Processes business metrics
Returns actionable insights, not just raw numbers

---

## Case Objective

Solve the business problem:

> Analysts waste time cross-referencing traffic and sales data to understand ROI by channel.
---

## Solution

This agent automates the entire workflow:

* **Understands questions in natural language**
* **Direct query (real data) to the Data Warehouse (BigQuery)**
* **Intelligent interpretation via LLM**
* **Processes metrics (conversion, revenue, volume)**
* **Provides structured business insights**
* **Standardized output for decision-making**

---

## Key Features

- ✅ Natural language understanding
- ✅ Real **Tool Calling (BigQuery)**
- ✅ Multi-step agent (LangGraph)
- ✅ Analytical vs Descriptive reasoning
- ✅ Business-oriented output (not raw data)
- ✅ Clean architecture

---

## Solution Architecture

This project uses a **LangGraph-based agent pipeline**.

### Agent Flow:

User Question
↓ 
API (FastAPI): Request input interface.
↓ 
Classifier: Identifies intent (Descriptive vs. Analytical).
↓ 
Tool Calling (BigQuery): Execution of queries on real data.
↓ 
Response Generator (LLM): Synthesizes data into natural language.
↓ 
Delivery: Structured and decision-oriented response.

---

### Components

#### 1. **Orchestration (LangGraph)**

Responsible for the agent flow:

* `classify_question` → defines the mode (descriptive vs. analytical)
* `fetch_data` → calls BigQuery
* `generate_response` → calls LLM

---

#### 2. **LLM (Groq / OpenAI compatible)**

Responsible for:

* interpreting data
* applying business rules
* generating final response

---

#### 3. **Tool Calling (BigQuery)**

Tool created:

```python get_media_data()

```

Responsible for:

* querying real dataset
* aggregating metrics by channel

---

#### 4. **Specialized Prompts**

Clear separation:

* `descriptive_prompt.py` → objective responses (volume)
* `analytic_prompt.py` → strategic responses (performance)

👉 This avoids:

* context confusion
* inconsistent responses

---

## Project Structure

```
app/
│
├── agent/
│   ├── graph.py                # Workflow orchestration (LangGraph)
│   ├── nodes.py                # Agent step logic and decision making
│   └── state.py                # Agent state definition
│
├── api/
│   └── routes.py               # API Endpoints (FastAPI)
│
├── config/
│   └── settings.py             # Environment variables and API key management
│
├── core/
│   └── llm.py                  # Model initialization and configuration
│
├── prompts/
│   ├── analytic_prompt.py      # Prompts for data analysis logic
│   └── descriptive_prompt.py   # Prompts for narrative response generation
│
├── schemas/
│   └── query_schema.py         # Data models and validation (Pydantic)
│
├── services/
│   ├── bq_service.py           # Direct Google BigQuery connection service
│   └── formatter.py            # Data cleaning and output formatting
│
├── tools/
│   └── bigquery_tool.py        # Tool for the agent to execute BigQuery queries
│
├── validators/
│   └── validator.py            # Logic and security validation layers
│
└── main.py                     # Application entry point

```

## BigQuery Query

The query used aggregates real data from the last 30 days:

* users by channel
* orders
* revenue
* conversion
* revenue per user

Main tables:

* `users`
* `orders`
* `order_items`

### Why use tools?

To ensure:

- Absence of distorted data
- Real-time insights
- Separation of responsibilities (LLM ≠ Data Layer)

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-media-analyst-agent
cd ai-media-analyst-agent

```

### 2. Create the virtual environment

```bash
python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows

```

### 3. Install the dependencies

```bash
pip install -r requirements.txt

```

### 4. Environment variable configuration

Create a `.env`:

```env 
GROQ_API_KEY=your_api_key_here 
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
```

### 5. Configure Google Cloud

* Create project in GCP
* Enable BigQuery API
* Create Service Account
* Download credentials JSON
* Define variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/credentials.json"

Make sure the path in your .env file points to the downloaded credentials JSON file
```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```
🚀 Live Demo: http://localhost:8000/docs

```

## Using the API

### Endpoint:

``` POST /ask

```

### Example:

```json
{
"question": "Which channel performs best? And why?"

}
```

## Sample Questions

### 🔹 Descriptive

* "What was the volume of users coming from 'Search' last month?"

### 🔹 Analytical

* "Which channel performs best?"

* "Where should I invest more?"

---

## Sample Response

Summary:
Search shows the best performance by maximizing total revenue...

Analysis:
- Revenue: ...
- Conversion: ...
- Volume: ...
- RPU: ...

Recommendation:
...

Risks:
...

Opportunities:
...

![Sample Response](./image.png)

...

## Important Technical Decisions

### ✔ Separation of prompts

Avoids ambiguity and improves accuracy.

---

### ✔ Tool Calling (mandatory in this case)

The agent decides when to retrieve data — it's not a static prompt.

---

### ✔ Optimized Query

* Use of `COUNT DISTINCT`
* `SAFE_DIVIDE`

* Filter by last 30 days

---

### ✔ Output Validation

* Format standardization
* Rule control (e.g., use of multiples vs. %)

---

## Solution Differentiators

* **Real agent architecture (not a giant prompt)**
* Integration with real data (BigQuery)
* Responses with **business insight**
* Clear separation of responsibilities
* Ready to scale (new tools, new datasets)

---

## Next Steps (Evolution)

- Add memory (question history)
- Implement multiple tools (e.g., CAC, LTV, cohort analysis)
- Integrated dashboard
- Automatic response validation (LLM-as-judge)
- Implement dynamic tool selection based on user intent
- Robust error handling (retry/fallback)
- Implement automated tests (pytest)
- Support for out-of-scope questions

---

## Author

Developed as a solution for a technical case study of **AI + Data + Growth**.

---

## Conclusion

This project demonstrates:

* mastery of agent architecture
* integration with real data
* ability to transform data into decisions

👉 It's not just a chatbot — it's an **automated media analyst**.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.