import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.3)

context = """
From all the authoritative statements of the great sages, the Vedic hymns and the aphorisms of the Vedānta-sūtra, the components 
of this world can be understood as follows. First there are earth, water, fire, air and ether. These are the five great elements 
(mahā-bhūta). Then there are false ego, intelligence and the unmanifested stage of the three modes of nature. Then there are five 
senses for acquiring knowledge: the eyes, ears, nose, tongue and skin. Then five working senses: voice, legs, hands, anus and 
genitals. Then, above the senses, there is the mind, which is within and which can be called the sense within. Therefore, including
the mind, there are eleven senses altogether. Then there are the five objects of the senses: smell, taste, form, touch and sound. 
Now the aggregate of these twenty-four elements is called the field of activity. If one makes an analytical study of these 
twenty-four subjects, then he can very well understand the field of activity. Then there are desire, hatred, happiness and 
distress, which are interactions, representations of the five great elements in the gross body. The living symptoms, represented 
by consciousness, and convictions are the manifestation of the subtle body – mind, ego and intelligence. These subtle elements are 
included within the field of activities.
"""

query = "What are the five great elements according to the Vedic hymns?"

prompt = f"""
Answer the question ONLY using the context below.
If the answer is not present, say "Not found in context".

Context:
{context}

Question:
{query}
"""

response = llm.invoke([HumanMessage(content=prompt)])

print(response.content)