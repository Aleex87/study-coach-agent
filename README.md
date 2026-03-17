
# Study Coach Agent

## How to run

git clone <repo-url>  
cd study-coach-agent  
uv sync  
uv run python main.py  

---

## Overview

Study Coach Agent is a simple conversational agent designed to help students study a topic, understand concepts, and prepare for homework or exams.

The agent works through a terminal interface and provides:
- clear explanations
- step-by-step reasoning
- simple study guidance

It is built using LangChain and Ollama with a school-provided endpoint.

---

## Features

- Terminal-based interaction
- Structured system prompt (MEEPO-style)
- Conversational memory (chat history)
- Simple and explainable architecture
- Uses Ollama (no external APIs required)

---

## Project structure
study-coach-agent/
│
├── main.py # Entry point (CLI loop)
├── agent.py # Agent logic
├── memory.py # Conversation memory
├── prompts.py # System prompt (MEEPO structure)
├── config.py # Settings and configuration
├── .env.example # Example environment variables
├── .env # Your local configuration (not committed)
│
└── util/
├── models.py
├── streaming_utils.py
└── pretty_print.py


---

## Installation

### For development (you)

Initialize project:
> uv init

Add dependencies:

uv add langchain langchain-ollama langgraph python-dotenv


---

### For users (after cloning)

Install dependencies:

uv sync 


This ensures the same environment as the original project.

---

## Environment configuration

Create a `.env` file in the root of the project.


Then edit `.env` and insert your real token:

OLLAMA_BASE_URL=

OLLAMA_BEARER_TOKEN=YOUR_REAL_TOKEN


Important:
- Do not commit your `.env` file
- Each user must provide their own token

---

## System prompt design

The agent uses a structured prompt based on the MEEPO framework:

- Mission: help the student study and understand topics
- Expertise: explanation, simplification, questioning
- Environment: terminal-based chat
- Process: step-by-step reasoning and guidance
- Output: clear and structured answers
- Guardrails: avoid hallucinations and overcomplexity

This makes the agent predictable and easy to explain during an exam.

---

## Memory

The agent includes a simple conversational memory:

- Stores recent messages (user + assistant)
- Sends history to the model at each step
- Keeps only the last N messages (configurable)

This allows:
- follow-up questions
- contextual explanations
- progressive learning

---

## Tools

This agent does not use tools.

It is intentionally kept simple to focus on:
- prompt design
- conversation flow
- learning support

Other agents in the project may include tools.

---

## Example usage
Ask your study question: What is photosynthesis?


Agent response:
- explains the concept
- may give examples
- may suggest follow-up questions

You can also use commands:

reset -> clears conversation memory
exit -> exits the program


---

## Limitations

- No external knowledge retrieval (no RAG)
- No tools (by design)
- Depends on the quality of the LLM responses
- Limited memory window (recent messages only)

---

## Notes

- The project is designed to be simple and explainable for exam purposes
- Focus is on clarity, structure, and usability rather than complexity

## Performed by

Alessandro Abbate
