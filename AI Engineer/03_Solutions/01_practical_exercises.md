# Practical Exercises

## Basics

1. Implement a simple prompt engineering task.
   - **Note**: Prompt engineering involves crafting inputs to guide AI models effectively.
   - **Code Snippet**:
     ```python
     import openai

     def generate_response(prompt):
         response = openai.Completion.create(
             engine="text-davinci-003",
             prompt=prompt,
             max_tokens=100
         )
         return response.choices[0].text.strip()

     prompt = "Write a short story about AI in healthcare."
     print(generate_response(prompt))
     ```

2. Use OpenAI API to generate text.
   - **Note**: The OpenAI API allows interaction with models like GPT for text generation.
   - **Code Snippet**:
     ```python
     import openai

     openai.api_key = "your-api-key"

     def generate_text(prompt):
         response = openai.Completion.create(
             engine="text-davinci-003",
             prompt=prompt,
             max_tokens=150
         )
         return response.choices[0].text.strip()

     print(generate_text("Explain the concept of embeddings in AI."))
     ```

## Advanced Topics

1. Create embeddings and store them in a vector database.
   - **Note**: Embeddings represent data in a numerical format for semantic understanding.
   - **Code Snippet**:
     ```python
     from sentence_transformers import SentenceTransformer
     import pinecone

     model = SentenceTransformer('all-MiniLM-L6-v2')
     pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")

     index = pinecone.Index("example-index")

     sentences = ["AI is transforming industries.", "Machine learning is a subset of AI."]
     embeddings = model.encode(sentences)

     for i, embedding in enumerate(embeddings):
         index.upsert([(f"sentence-{i}", embedding)])
     ```

2. Implement Retrieval Augmented Generation (RAG).
   - **Note**: RAG combines retrieval of external knowledge with AI generation.
   - **Code Snippet**:
     ```python
     from langchain.chains import RetrievalQA
     from langchain.llms import OpenAI
     from langchain.vectorstores import Pinecone

     llm = OpenAI(model_name="text-davinci-003")
     vectorstore = Pinecone(index_name="example-index")

     qa_chain = RetrievalQA(llm=llm, retriever=vectorstore.as_retriever())

     query = "What are the applications of AI in healthcare?"
     print(qa_chain.run(query))
     ```

## Multimodal AI

1. Use OpenAI's Vision API for image understanding.
   - **Note**: The Vision API processes and analyzes images.
   - **Code Snippet**:
     ```python
     import openai

     openai.api_key = "your-api-key"

     def analyze_image(image_path):
         with open(image_path, "rb") as image_file:
             response = openai.Image.create(
                 file=image_file,
                 purpose="analyze"
             )
         return response

     print(analyze_image("example.jpg"))
     ```

2. Generate images using DALL-E API.
   - **Note**: DALL-E API generates images from textual descriptions.
   - **Code Snippet**:
     ```python
     import openai

     openai.api_key = "your-api-key"

     def generate_image(prompt):
         response = openai.Image.create(
             prompt=prompt,
             n=1,
             size="1024x1024"
         )
         return response['data'][0]['url']

     print(generate_image("A futuristic cityscape with AI robots."))
     ```
