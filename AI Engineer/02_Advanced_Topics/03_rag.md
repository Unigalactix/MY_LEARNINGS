# Retrieval Augmented Generation (RAG)

## Overview
RAG combines retrieval of external knowledge with AI generation.

### Steps
1. Chunk data.
   - **Note**: Split large documents into smaller, manageable pieces.
   - **Code Snippet**:
     ```python
     def chunk_data(text, chunk_size=500):
         return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

     document = """Long text document..."""
     chunks = chunk_data(document)
     print(chunks)
     ```

2. Create embeddings.
   - **Note**: Convert text chunks into numerical representations.
   - **Code Snippet**:
     ```python
     from sentence_transformers import SentenceTransformer

     model = SentenceTransformer('all-MiniLM-L6-v2')
     embeddings = model.encode(chunks)
     print(embeddings)
     ```

3. Store embeddings in a vector database.
   - **Note**: Use a vector database like Pinecone for efficient storage and retrieval.
   - **Code Snippet**:
     ```python
     import pinecone

     pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")
     index = pinecone.Index("example-index")

     for i, embedding in enumerate(embeddings):
         index.upsert([(f"chunk-{i}", embedding)])
     ```

4. Retrieve relevant data.
   - **Note**: Query the vector database to find the most relevant chunks.
   - **Code Snippet**:
     ```python
     query_embedding = model.encode(["What is RAG?"])
     results = index.query(query_embedding, top_k=3)
     print(results)
     ```

5. Generate responses.
   - **Note**: Use an LLM to generate responses based on retrieved data.
   - **Code Snippet**:
     ```python
     import openai

     openai.api_key = "your-api-key"

     def generate_response(context, query):
         prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
         response = openai.Completion.create(
             engine="text-davinci-003",
             prompt=prompt,
             max_tokens=150
         )
         return response.choices[0].text.strip()

     context = "Relevant data retrieved from vector database."
     query = "What is RAG?"
     print(generate_response(context, query))
     ```

### Practical Exercise
- Implement RAG using LangChain.
   - **Code Snippet**:
     ```python
     from langchain.chains import RetrievalQA
     from langchain.llms import OpenAI
     from langchain.vectorstores import Pinecone

     llm = OpenAI(model_name="text-davinci-003")
     vectorstore = Pinecone(index_name="example-index")

     qa_chain = RetrievalQA(llm=llm, retriever=vectorstore.as_retriever())

     query = "Explain the concept of RAG."
     print(qa_chain.run(query))
     ```

- Build an AI agent using OpenAI Functions.
   - **Code Snippet**:
     ```python
     from openai import ChatCompletion

     openai.api_key = "your-api-key"

     def create_agent(prompt):
         response = ChatCompletion.create(
             model="gpt-4",
             messages=[
                 {"role": "system", "content": "You are an AI assistant."},
                 {"role": "user", "content": prompt}
             ]
         )
         return response.choices[0].message['content']

     prompt = "Create a chatbot that explains RAG."
     print(create_agent(prompt))
     ```
