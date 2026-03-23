import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.3)

context = """
The opulences of the universal form of the Lord are described herein. It is said that His mouth is the generating center of all kinds of 
voices, and its controlling deity is the fire demigod. And His skin and other six layers of bodily construction are the representative 
generating centers of the seven kinds of Vedic hymns, like the Gāyatrī. Gāyatrī is the beginning of all Vedic mantras, and it is 
explained in the first volume of Śrīmad-Bhāgavatam. Since the generating centers are the different parts of the universal form of the 
Lord, and since the form of the Lord is transcendental to the material creation, it is to be understood that the voice, the tongue, the 
skin, etc., suggest that the Lord in His transcendental form is not without them. The material voice, or the energy of taking in 
foodstuff, is generated originally from the Lord; such actions are but perverted reflections of the original reservoirs — the 
transcendental situation is not without spiritual variegatedness. In the spiritual world, all the perverted forms of material 
variegatedness are fully represented in their original spiritual identity. The only difference is that material activities are 
contaminated by the three modes of material nature, whereas the potencies in the spiritual world are all pure because they are engaged 
in the unalloyed transcendental loving service of the Lord. In the spiritual world, the Lord is the sublime enjoyer of everything, and 
the living entities there are all engaged in His transcendental loving service without any contamination of the modes of material nature.
The activities in the spiritual world are without any of the difficulties of the material world, but there is no question of impersonal 
voidness on the spiritual platform, as suggested by the impersonalists.
"""

query = "What are the generating centers of the seven kinds of Vedic hymns according to the context?"

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