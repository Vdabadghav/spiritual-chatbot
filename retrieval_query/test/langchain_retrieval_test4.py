import os
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.3)

context = """
    There are undoubtedly different planetary systems for different persons. As stated in Bhagavad-gītā (14.18), ūrdhvaṁ 
    gacchanti sattva-sthāḥ: persons in the mode of goodness can go to the upper planets. Those in the modes of darkness and 
    passion, however, are not allowed to enter the higher planets. The word divam refers to the higher planetary system known as 
    Svargaloka. Indra, King of the higher planetary system, has the power to push down any conditioned soul attempting to go from 
    the lower to the higher planets without proper qualifications. The modern attempt to go to the moon is also an attempt by 
    inferior men to go to Svargaloka by artificial, mechanical means. This attempt cannot be successful. From this statement of 
    Indra it appears that anyone attempting to go to the higher planetary systems by mechanical means, which are here called māyā,
    is condemned to go to the hellish planets in the lower portion of the universe. To go to the higher planetary system, one 
    needs sufficient good qualities. A sinful person situated in the mode of ignorance and addicted to drinking, meat-eating and 
    illicit sex will never enter the higher planets by mechanical means."""

query = "What does a sinful person do?"

filtered_docs = []

for c in context:
    check_prompt = f"""
    Query: {query}
    Document: {c}

    Is this relevant? Answer YES or NO.
    """
    res = llm.invoke(check_prompt)
    
    if "YES" in res.content.upper():
        filtered_docs.append(c)

context = "\n".join(filtered_docs)

final_prompt = f"{context}\n\nQuestion:{query}"

answer = llm.invoke(final_prompt)

print(answer.content)