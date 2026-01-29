## LinkedIn Post Generator (LangChain + Groq)

This project is a **LinkedIn Post Generator** built using **LangChain** and **Groq LLM**.  
It takes a topic and user preferences and generates a polished LinkedIn post .


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
```bash
LinkedIn_Post_Generation/
│
├── main.py
├── memory.json
└── README.md
```
---

---

## Memory File (`memory.json`)

The memory file stores past sessions like this:

```json
{
  "sessions": [
    {
      "topic": "AI in Finance",
      "audience": "Students",
      "tone": "Professional"
    }
  ]
}
```
---
## Environment Setup
1. Install Dependencies
```bash
pip install langchain langchain-groq python-dotenv
```
2.Create .env File
```bash
GROQ_API_KEY=your_api_key_here
```
3. Run the Program
```bash
python main.py
```
---
## Future Improvements
   - Add UI using Streamlit
   - Allow editing before final output
   - Add post tone validation
   - Generate multiple post variations
   - Retrieve high-quality LinkedIn examples using a vector database for better context and consistency
   - Use a state-based workflow with conditional steps and retry logic
   - Track and compare prompt changes over time
   - Expose the system via a FastAPI service
---
