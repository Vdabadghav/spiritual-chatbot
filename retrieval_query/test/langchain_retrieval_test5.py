from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


print("=" * 50)
print("Gemini API Key Verifier (LangChain)")
print("=" * 50)


context = """
Although Kṛṣṇa is manifested before Arjuna in His universal form, Arjuna remembers his friendly relationship with Kṛṣṇa and is 
therefore asking pardon and requesting Kṛṣṇa to excuse him for the many informal gestures which arise out of friendship. He is 
admitting that formerly he did not know that Kṛṣṇa could assume such a universal form, although Kṛṣṇa explained it as his 
intimate friend. Arjuna did not know how many times he may have dishonored Kṛṣṇa by addressing Him “O my friend,” “O Kṛṣṇa,” 
“O Yādava,” etc., without acknowledging His opulence. But Kṛṣṇa is so kind and merciful that in spite of such opulence He played 
with Arjuna as a friend. Such is the transcendental loving reciprocation between the devotee and the Lord. The relationship 
between the living entity and Kṛṣṇa is fixed eternally; it cannot be forgotten, as we can see from the behavior of Arjuna. 
Although Arjuna has seen the opulence in the universal form, he cannot forget his friendly relationship with Kṛṣṇa.
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

    response = llm.invoke([HumanMessage(content="What is Arjuna asking Kṛṣṇa for?")])

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