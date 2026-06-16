# Multi-Agent System

A modular AI agent platform built with FastAPI and Python, designed to support multiple LLM providers and extensible agent capabilities.

## Overview

This project provides a foundation for building production-ready AI agents using a clean, scalable architecture.

The initial implementation includes a Retrieval Agent with support for multiple LLM providers through a provider-agnostic abstraction layer.

Current supported providers:

* OpenAI
* Google Gemini

Future enhancements include:

* RAG (Retrieval-Augmented Generation)
* Vector databases
* Tool integration
* Multi-agent orchestration
* Memory management
* Docker deployment
* CI/CD pipelines
* Monitoring and observability

---

## Architecture

```text
Client
  │
  ▼
FastAPI API Layer
  │
  ▼
Agent Layer
  │
  ▼
LLM Abstraction Layer
  │
  ├── OpenAI Service
  └── Gemini Service
```

---

## Project Structure

```text
multi-agent-system/

├── agents/
│   └── ragagent/
│       └── rag_agent.py
│
├── common/
│   └── llm/
│       ├── llm_factory.py
│       ├── llm_service.py
│       ├── openai_llm_service.py
│       └── gemini_ai_service.py
│
├── config/
│   └── settings.py
│
├── main.py
├── startup.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Features

* Provider-agnostic LLM abstraction
* Factory pattern for LLM selection
* Modular agent architecture
* FastAPI REST APIs
* Environment-based configuration
* Async request handling

---

## Supported LLM Providers

### OpenAI

Configure the following environment variables:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4o-mini
```

### Gemini

Configure the following environment variables:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-2.5-flash
```

---

## Setup

### Clone the repository

```bash
git clone <repository-url>
cd multi-agent-system
```

### Create a virtual environment

```bash
python -m venv env
```

### Activate the virtual environment

Windows:

```bash
env\Scripts\activate
```

Linux/macOS:

```bash
source env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root.

Example:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4o-mini
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Sample response:

```json
{
  "agent": "rag_agent",
  "status": "healthy"
}
```

### Query Agent

```http
POST /rag_agent
```

Request:

```json
{
  "query": "What is groundwater monitoring?",
  "context": "Groundwater monitoring is the process of collecting and analyzing groundwater samples."
}
```

Response:

```json
{
  "answer": "Generated response",
  "context": "Groundwater monitoring is the process of collecting and analyzing groundwater samples."
}
```

---

## Roadmap

### Phase 1

* [x] Agent implementation
* [x] LLM abstraction
* [x] LLM factory
* [x] FastAPI integration

### Phase 2

* [ ] Dockerization
* [ ] Logging
* [ ] Health and readiness endpoints

### Phase 3

* [ ] CI/CD with GitHub Actions
* [ ] Azure deployment
* [ ] Monitoring and observability

### Phase 4

* [ ] RAG implementation
* [ ] Embeddings
* [ ] Vector database integration

### Phase 5

* [ ] Multi-agent orchestration
* [ ] Memory management
* [ ] Tool integration

---

## License

This project is licensed under the MIT License.
