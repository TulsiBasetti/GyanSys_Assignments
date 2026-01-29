from langchain_groq import ChatGroq
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import json
from dotenv import load_dotenv


load_dotenv()


llm=ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.4
)

MEMORY_FILE = r"C:\GyanSys_Assignments\Week_1\Linkedin_Post_Generation\memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"sessions": []}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "sessions" not in data:
                data["sessions"] = []  
            return data
    except json.JSONDecodeError: 
        return {"sessions": []}


def save_memory(topic, audience, tone):

    memory = load_memory()

    new_session = {
        "topic": topic,
        "audience": audience,
        "tone": tone
    }

    memory["sessions"].append(new_session)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

parser=StrOutputParser()


# Get the user Intent
intent_prompt = ChatPromptTemplate.from_template("""
You are a LinkedIn content strategist.

Classify the user's intent into ONE of the following:
- Personal Achievement
- Thought Leadership
- Hiring
- Product Announcement
- Educational
- Personal Story
- Opinion

Topic: {topic}

Return ONLY the intent name.
""")


#Structure the content
structure_prompt = ChatPromptTemplate.from_template("""
Create a LinkedIn post structure.

Topic: {topic}
Intent: {intent}
Audience: {audience}
Tone: {tone}

Provide:
1. Hook (1–2 lines)
2. Key points (bullet form)

Only structure. No full sentences.
""")


#1st Content Draft
content_prompt=ChatPromptTemplate.from_template("""
Write a LinkedIn post using the structure below.

Structure:
{structure}

Topic: {topic}
Intent: {intent}
Audience: {audience}
Tone: {tone}
Preferred Length: {length}

Past context from memory:
{memory}

Rules:
- Strong opening hook
- Short paragraphs
- Professional but human
- Avoid generic LinkedIn phrases
- No hashtags yet
""")


#Review the draft
review_prompt = ChatPromptTemplate.from_template("""
Review the LinkedIn post below.
Improve:
- Clarity
- Professionalism
- Flow
- Credibility
Do not show the user what changes you have made.
Avoid marketing fluff.

Post:
{draft_post}
""")

#Final formatting and Hastags
final_prompt = ChatPromptTemplate.from_template("""
Finalize the LinkedIn post.
Do not show the user what changes you have made. 
Print only the final linkedln post.

Add:
- Clean formatting
- 3–5 relevant hashtags (not spammy)

Post:
{reviewed_post}
""")


#Chains
intent_chain = intent_prompt | llm | parser
structure_chain = structure_prompt | llm | parser
content_chain = content_prompt | llm | parser
review_chain = review_prompt | llm | parser
final_chain = final_prompt | llm | parser


def generate_linkedin_post(user_input):
    memory = load_memory()["sessions"]

    intent = intent_chain.invoke({"topic": user_input["topic"]})

    structure = structure_chain.invoke({
        "topic": user_input["topic"],
        "intent": intent,
        "audience": user_input["audience"],
        "tone": user_input["tone"]
    })

    draft_post = content_chain.invoke({
        "topic": user_input["topic"],
        "intent": intent,
        "audience": user_input["audience"],
        "tone": user_input["tone"],
        "length": user_input["length"],
        "structure": structure,
        "memory": memory
    })

    reviewed_post = review_chain.invoke({"draft_post": draft_post})

    final_post = final_chain.invoke({"reviewed_post": reviewed_post})

    save_memory(
        user_input["topic"],
        user_input["audience"],
        user_input["tone"]
    )

    return final_post


if __name__ == "__main__":
    print("------------LinkedIn Post Generator------------------\n")

    topic = input("Enter topic: ")
    audience = input("Enter target audience: ")
    tone = input("Enter tone: ")
    length = input("Enter preferred length (e.g. 150–180 words): ")

    user_input = {
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "length": length
    }

    final_post = generate_linkedin_post(user_input)

    print("\nFINAL LINKEDIN POST\n")
    print(final_post)