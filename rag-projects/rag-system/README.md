# RAG-based AI System

A complete implementation of a Retrieval-Augmented Generation (RAG) system.

## Features

- Semantic Search with OpenAI embeddings
- Vector Database (Pinecone)
- LLM Integration (OpenAI GPT)
- Interactive CLI Interface
- Modular Architecture

## Quick Start

### Prerequisites
- Python 3.9+
- OpenAI API key
- Pinecone account

### Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Usage

```bash
python src/cli.py
```

## Project Structure

- `src/` - Source code modules
- `data/` - Knowledge base
- `scripts/` - Utility scripts
- `tests/` - Unit tests
- `demo/` - Demo artifacts

## Implementation Steps

1. Data Preparation
2. Embeddings Generation
3. Vector Database Setup
4. Retrieval Engine
5. LLM Integration
6. CLI Interface
7. Full Integration
8. Testing & Optimization
9. Documentation

## Technology Stack

- Language: Python 3.9+
- Vector DB: Pinecone
- LLM: OpenAI API
- Embeddings: text-embedding-3-small
- CLI: Click framework

## Performance

- Embedding generation: ~100ms per query
- Vector search: ~50ms per query
- LLM response: 1-2 seconds
- Total latency: 1-2 seconds per query

## Author

Askhat Tuleshov
Date: December 8, 2025

## License

MIT License
