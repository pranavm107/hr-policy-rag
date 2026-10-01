
# HR Policy Assistant (RAG)

An AI-powered HR Policy Assistant built using Retrieval-Augmented Generation (RAG). The system allows employees to ask questions about company HR policies and receive context-aware answers based on the organization's HR policy document.

The project uses LangChain for the RAG pipeline, Groq-hosted LLMs for generation and safety checks, Jina AI for embeddings, Qdrant Cloud for vector storage, and Streamlit for the web interface.

## Features

- Retrieval-Augmented Generation (RAG)
- HR policy document ingestion
- Intelligent document chunking
- Semantic search using Jina embeddings
- Qdrant Cloud vector database
- Groq-hosted LLM for response generation
- LangChain agent-based architecture
- Input and output safety guardrails
- Prompt injection protection
- PII and sensitive-information protection
- LangSmith tracing and monitoring
- Command-line interface
- Streamlit web interface
- Jupyter Notebook for experimentation

## How It Works

```text
                    HR Policy Document
                           |
                           v
                  Document Loading
                           |
                           v
                    Text Splitting
                           |
                           v
                   Jina Embeddings
                           |
                           v
                  Qdrant Vector Store
                           |
                           |
                    User Question
                           |
                           v
                  Input Guardrails
                           |
                           v
                   Policy Retrieval
                           |
                           v
                    LangChain Agent
                           |
                           v
                    Groq LLM
                           |
                           v
                  Output Guardrails
                           |
                           v
                     Final Answer


## RAG Pipeline

### 1. Document Ingestion

The HR policy document is loaded from:

```text
data/hr_policy.txt
```

The document is processed and divided into smaller chunks to make retrieval more effective.

Configuration:

```text
CHUNK_SIZE = 500
CHUNK_OVERLAP = 60
```

The document loading functionality is implemented in:

```text
hr_assistant/document_loader.py
```

Text splitting is handled by:

```text
hr_assistant/splitter.py
```

### 2. Embedding Generation

The project uses Jina AI embeddings to convert HR policy text into numerical vector representations.

Embedding model:

```text
jina-embeddings-v2-base-en
```

Implementation:

```text
hr_assistant/embeddings.py
```

### 3. Vector Database

The generated embeddings are stored in Qdrant Cloud.

Qdrant is used to perform semantic similarity searches against the HR policy content.

Implementation:

```text
hr_assistant/vector_store.py
```

The existing Qdrant collection can be reused on subsequent executions to avoid unnecessary re-embedding.

### 4. Information Retrieval

The retrieval system searches the Qdrant vector database for policy sections relevant to the user's question.

The retriever is exposed through the:

```text
search_hr_policy
```

tool.

Implementation:

```text
hr_assistant/tools.py
```

The system retrieves the top 3 relevant results by default.

### 5. AI Agent

The LangChain agent is responsible for processing the user's question, calling the HR policy search tool, and generating a response using the retrieved information.

Implementation:

```text
hr_assistant/agent.py
```

The project uses the following Groq-hosted model:

```text
openai/gpt-oss-20b
```

### 6. Safety Guardrails

The application includes separate input and output safety checks.

Input checks include:

* Prompt injection attempts
* Requests for unauthorized employee information
* Suspicious requests
* Attempts to bypass system instructions

Output checks include:

* Potential PII exposure
* Unauthorized promises
* Suspicious links
* Unsafe or unsupported responses

Implementation:

```text
hr_assistant/guardrails.py
```

Safety model:

```text
openai/gpt-oss-safeguard-20b
```

### 7. Application Pipeline

All components are connected through:

```text
hr_assistant/pipeline.py
```

The main functions are:

```python
build_hr_assistant()
ask()
```

Both the CLI application and Streamlit application use this pipeline.

## Project Structure

```text
cognivexa-hr-rag/
│
├── hr_assistant/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── tools.py
│   ├── llm.py
│   ├── agent.py
│   ├── guardrails.py
│   ├── pipeline.py
│   ├── logger.py
│   └── tracing.py
│
├── data/
│   └── hr_policy.txt
│
├── docs/
│   ├── logging.md
│   ├── langsmith.md
│   ├── qdrant.md
│   └── guardrail-testing.md
│
├── NOTES/
│   └── reference-materials/
│
├── logs/
│
├── app.py
├── main.py
├── rag.ipynb
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Technologies Used

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| Python           | Core programming language                    |
| LangChain        | RAG pipeline and agent framework             |
| Groq             | LLM inference and safety model               |
| Jina AI          | Text embeddings                              |
| Qdrant Cloud     | Vector database                              |
| Streamlit        | Web application                              |
| LangSmith        | Tracing and monitoring                       |
| Jupyter Notebook | Experimentation                              |
| uv               | Python environment and dependency management |

## Requirements

Before running the project, make sure you have:

* Python 3.10 or higher
* A Groq API key
* A Jina AI API key
* A Qdrant Cloud account and API key
* Optional LangSmith account for tracing

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/cognivexa-hr-rag.git
cd cognivexa-hr-rag
```

### 2. Install uv

```bash
pip install uv
```

### 3. Create a Virtual Environment

```bash
uv venv ragenv
```

### 4. Activate the Virtual Environment

#### macOS / Linux

```bash
source ragproject/bin/activate
```

#### Windows

```bash
ragenv\Scripts\activate
```

### 5. Install Dependencies

```bash
uv pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key

QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION_NAME=hr_policy

LANGSMITH_TRACING=false
LANGSMITH_ENDPOINT=your_langsmith_endpoint
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=your_langsmith_project
```

### Environment Variable Description

| Variable                 | Description                           |
| ------------------------ | ------------------------------------- |
| `GROQ_API_KEY`           | API key used for Groq LLM inference   |
| `JINA_API_KEY`           | API key used for Jina embeddings      |
| `QDRANT_URL`             | Qdrant Cloud cluster URL              |
| `QDRANT_API_KEY`         | Qdrant API key                        |
| `QDRANT_COLLECTION_NAME` | Name of the Qdrant collection         |
| `LANGSMITH_TRACING`      | Enables or disables LangSmith tracing |
| `LANGSMITH_ENDPOINT`     | LangSmith API endpoint                |
| `LANGSMITH_API_KEY`      | LangSmith API key                     |
| `LANGSMITH_PROJECT`      | LangSmith project name                |

> Never commit your `.env` file or API keys to GitHub.

## Running the Application

### CLI Application

Run:

```bash
python main.py
```

The CLI application runs sample HR policy questions and displays the generated responses.

### Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser and provide an interactive HR policy chat interface.

### Jupyter Notebook

Open:

```text
rag.ipynb
```

The notebook can be used to experiment with the individual stages of the RAG pipeline.

## Example Questions

The assistant can answer questions such as:

```text
What is the company's annual leave policy?
```

```text
How many sick leaves are available to employees?
```

```text
What is the work-from-home policy?
```

```text
What is the maternity leave policy?
```

```text
What are the company's working hours?
```

```text
What is the notice period?
```

The answers are generated using information retrieved from the HR policy document.

## Safety and Security

This project implements multiple layers of protection.

### Input Protection

User questions are checked before being passed to the main RAG pipeline.

The system attempts to identify:

* Prompt injection
* Instruction manipulation
* Unauthorized data requests
* Suspicious queries

### Output Protection

Generated responses are checked before being displayed to the user.

The system checks for:

* Personally identifiable information
* Unauthorized commitments
* Suspicious URLs
* Potentially unsafe responses
* Unsupported information

This provides an additional safety layer between the user and the underlying language model.

## Logging

Application logging is handled by:

```text
hr_assistant/logger.py
```

Logs can be stored in:

```text
logs/
```

Logging helps with debugging, monitoring, and understanding application behavior.

## LangSmith Tracing

The project supports LangSmith tracing for monitoring the RAG pipeline.

Configure the following variables in `.env`:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=your_langsmith_endpoint
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=cognivexa-hr-rag
```

LangSmith can be used to inspect:

* LLM calls
* Retrieval steps
* Tool calls
* Agent execution
* Pipeline performance

## Qdrant Cloud

The project uses Qdrant Cloud as its vector database.

Configure:

```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION_NAME=hr_policy
```

Once the collection has been created and populated, subsequent runs can reuse the stored vectors instead of generating embeddings again.

## Development Workflow

The project is designed to demonstrate the complete development of a RAG application:

```text
Document
   ↓
Chunking
   ↓
Embedding
   ↓
Vector Database
   ↓
Retriever
   ↓
Agent
   ↓
LLM
   ↓
Guardrails
   ↓
Response
```

## Future Improvements

Possible future enhancements include:

* Support for multiple HR documents
* Document upload functionality
* Role-based access control
* Conversation history
* Source citations in responses
* Multilingual HR policy support
* Advanced document metadata filtering
* Admin dashboard
* Employee authentication
* Improved evaluation and testing
* Hybrid keyword and semantic search
* Automated document re-indexing

## Git Commands

### Check Repository Status

```bash
git status
```

### Add Changes

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Initial HR policy RAG assistant"
```

### Push Changes

```bash
git push
```

## Project Purpose

This project demonstrates the practical implementation of a production-oriented Retrieval-Augmented Generation system for enterprise knowledge retrieval.

It combines:

* Document processing
* Semantic embeddings
* Vector search
* LLM-based generation
* Agentic retrieval
* Safety guardrails
* Logging
* Observability

The system is designed to provide responses grounded in the organization's HR policy document rather than relying solely on the language model's general knowledge.

## License

This project is intended for educational and development purposes.

```
```
