# RAG-Based Chatbot using Simple and Advanced RAG Pipeline

This repository contains two implementations of Retrieval-Augmented Generation (RAG) pipelines using LangChain:

1. **Simple RAG Pipeline**: A basic implementation of a RAG pipeline to demonstrate the core concepts of retrieval-augmented generation.
2. **Advanced RAG Pipeline**: This is an enhanced version of the RAG pipeline with practical tips and tricks to improve retrieval, generation, and overall performance. This is demonstrated by a useful example of building a chatbot to assist with a large amount of data.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Data Sources](#data-sources)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)

---

## Overview

### Simple RAG Pipeline
This pipeline demonstrates the basic components of a RAG system:
- **Retrieval**: Fetching relevant documents or information from a knowledge base.
- **Generation**: Using a language model to generate responses based on the retrieved information.

### Advanced RAG Pipeline
This pipeline builds on the simple RAG pipeline and introduces advanced techniques to improve:
- **Retrieval Quality**: Better document retrieval using advanced indexing, filtering, and ranking.
- **Generation Quality**: Enhanced response generation with fine-tuned models, context-aware prompts, and post-processing.
- **Practical Application**: A chatbot designed to assist or emulate a human, showcasing how RAG can be applied in real-world scenarios.

---

## Features

### Simple RAG Pipeline
- Basic document retrieval using a vector store.
- Response generation using a pre-trained language model.
- Easy-to-understand implementation for beginners.

### Advanced RAG Pipeline
- Improved retrieval using hybrid search (keyword + semantic).
- Context-aware generation with dynamic prompt engineering.
- Post-processing techniques to refine responses.

---

## Data Sources
The project uses the following books as the primary data sources for retrieval and generation:

1. "Verity" by Colleen Hoover
Genre: Psychological Thriller

Description: A gripping novel about a struggling writer, Lowen Ashleigh, who is hired to complete the remaining books in a successful series by the injured author, Verity Crawford. As Lowen works on the manuscripts, she uncovers dark secrets about Verity's life.

Use Case: The book's complex narrative and character dynamics make it an excellent source for testing retrieval and generation capabilities.

2. "The Girl on the Train" by Paula Hawkins
Genre: Mystery, Thriller

Description: A suspenseful story about Rachel, a woman who becomes entangled in a missing persons investigation that she observes during her daily train commute. The novel explores themes of memory, truth, and deception.

Use Case: The intricate plot and unreliable narration provide rich content for testing advanced RAG techniques.

Both books are preprocessed and indexed in a vector store for efficient retrieval. The text is segmented into chunks to facilitate context-aware retrieval and generation.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SaurabhZodex/RAG-Based-Chatbot.git
   cd RAG-Based-Chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your API keys and other configurations (e.g., OpenAI API key, vector store credentials).

---

## Project Structure

```
rag-pipeline-langchain/

├── Dataset/
│   ├── verity.txt                  # Text file for "Verity" by Colleen Hoover
│   └── the_girl_on_the_train.txt   # Text file for "The Girl on the Train" by Paula Hawkins
├── RAG_without_memory.ipynb     # RAG pipeline without memory to access previous chat history
├── RAG.ipynb                    # RAG pipeline with memory to access previous chat history
├── Advanced_RAG.ipynb           # Advanced retrieval 
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
└── README.md                    # Main project documentation
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch and open a pull request.

Please ensure your code follows the project's style guidelines and includes appropriate tests.

---

## Acknowledgments
- [LangChain](https://www.langchain.com/) for providing the framework to build RAG pipelines.
- ABC for their language models and APIs.

