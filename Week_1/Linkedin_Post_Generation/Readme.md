# LinkedIn Post Generator (LangChain + Groq)

This project is a **LinkedIn Post Generator** built using **LangChain** and **Groq LLM**.  
It takes a topic and user preferences and generates a polished LinkedIn post step-by-step.

The system remembers past posts and uses them as context for better future generations.

---

## Features

- Generates professional LinkedIn posts
- Automatically detects user intent
- Creates structured content before writing
- Improves post quality using a review step
- Adds relevant hashtags at the end
- Stores past topics, audience, and tone in a memory file
- Uses Groq’s `llama-3.3-70b` model

---

## Tech Stack

- Python
- LangChain
- Groq LLM
- dotenv
- JSON (for memory storage)

---

## How the System Works (Step by Step)

### 1. User Input
The user provides:  
- Topic  
- Target audience  
- Tone  
- Preferred post length  

### 2. Intent Detection
The model first understands why the post is being written.  

**Possible intents:**  
- Personal Achievement  
- Thought Leadership  
- Hiring  
- Product Announcement  
- Educational  
- Personal Story  
- Opinion  

This helps the model write more relevant content.

### 3. Post Structure Creation
Instead of writing directly, the system:  
- Creates a hook  
- Lists key points in bullet form  

This ensures the post has a clear flow.

### 4. Content Draft Generation
Using:  
- Topic  
- Intent  
- Audience  
- Tone  
- Structure  
- Past memory  

The model generates the first draft of the LinkedIn post.  

**Rules applied:**  
- Strong opening  
- Short paragraphs  
- Professional but human tone  
- No generic LinkedIn phrases  
- No hashtags yet

### 5. Review & Improvement
The draft is reviewed internally to improve:  
- Clarity  
- Flow  
- Credibility  
- Professionalism  

*The user does not see what was changed internally.*

### 6. Final Formatting
In the final step:  
- Formatting is cleaned  
- 3–5 relevant hashtags are added  
- Only the final LinkedIn post is shown

### 7. Memory Storage
After generating the post:  
- Topic  
- Audience  
- Tone  

are saved in a `memory.json` file.  
This helps maintain context across multiple runs.

---

## Project Structure

