from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


print("=" * 50)
print("Gemini API Key Verifier (LangChain)")
print("=" * 50)


context = """
In order that human beings be distinct from the animals, the great saint Nārada recommends that every human being be educated in terms 
of the above-mentioned thirty qualifications. Nowadays there is propaganda everywhere, all over the world, for a secular state, a state 
interested only in mundane activities. But if the citizens of the state are not educated in the above-mentioned good qualities, how can 
there be happiness? For example, if the total populace is untruthful, how can the state be happy? Therefore, without consideration of 
one’s belonging to a sectarian religion, whether Hindu, Muslim, Christian, Buddhist or any other sect, everyone should be taught to 
become truthful. Similarly, everyone should be taught to be merciful, and everyone should observe fasting on certain days of the month. 
Everyone should bathe twice a day, cleanse his teeth and body externally, and cleanse his mind internally by remembering the holy name of
the Lord. The Lord is one, whether one is Hindu, Muslim or Christian. Therefore, one should chant the holy name of the Lord, regardless 
of differences in linguistic pronunciation. Also, everyone should be taught to be very careful not to discharge semen unnecessarily. 
This is very important for all human beings. If semen is not discharged unnecessarily, one becomes extremely strong in memory, 
determination, activity and the vitality of one’s bodily energy.
"""

system_prompt = f"""You are a helpful assistant. Answer questions ONLY based on the
following context. If the answer is not in the context, say "I don't have enough
information to answer that."

Context:
{context}
"""
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key= GOOGLE_API_KEY,
        temperature=0.3,
    )
    print("  LLM Object : Created successfully")
    print(f"  Model : gemini-2.5-flash")

    response = llm.invoke([HumanMessage(content="Why is it said that god is one?")])

    print("\n SUCCESS — Your API key is VALID!")
    print(f"\n  Model says : {response.content.strip()}")


except Exception as e:
    print(f"\n FAILED — {type(e).__name__}")
    print(f"  Reason : {e}")

    err = str(e).lower()
    if "api_key_invalid" in err or "invalid" in err:
        print("  Fix    : Double-check your API key.")
    elif "permission" in err or "403" in err:
        print("  Fix    : Key may be restricted. Check Google Cloud Console.")
    elif "429" in err or "quota" in err:
        print("  Fix    : Rate limit hit. Wait a moment and try again.")
    elif "module" in err or "import" in err:
        print("  Fix    : Run -> pip install langchain-google-genai")

print("\n" + "=" * 50)