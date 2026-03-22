from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


print("=" * 50)
print("Gemini API Key Verifier (LangChain)")
print("=" * 50)


context = """
In India there are many sacred places through which holy rivers flow. Foolish persons eagerly seek redemption from their sins by 
bathing in these rivers but do not take instruction from learned devotees of the Lord who reside in such places. One should go to 
a holy place seeking spiritual enlightenment and not just for ritualistic bathing.
In this age, people tirelessly arrange their hair in different styles, trying to enhance their facial beauty and sexuality. They 
do not know that actual beauty comes from within the heart, from the soul, and that only a person who is pure is truly attractive. 
As the difficulties of this age increase, filling one’s belly will be the mark of success, and one who can maintain his own family
will be considered brilliant in economic affairs. Religion will be practiced, if at all, only for the sake of reputation and 
without any essential understanding of the Supreme Personality of Godhead.
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

    response = llm.invoke([HumanMessage(content="What do foolish persons seek?")])

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