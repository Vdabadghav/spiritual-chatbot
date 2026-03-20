from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


print("=" * 50)
print("   Gemini API Key Verifier (LangChain)")
print("=" * 50)


context = """
The conception of God and the conception of Absolute Truth are not on the same level. The Śrīmad-Bhāgavatam hits on the target of 
the Absolute Truth. The conception of God indicates the controller, whereas the conception of the Absolute Truth indicates the 
summum bonum or the ultimate source of all energies. There is no difference of opinion about the personal feature of God as the 
controller because a controller cannot be impersonal. Of course modern government, especially democratic government, is impersonal 
to some extent, but ultimately the chief executive head is a person, and the impersonal feature of government is subordinate to 
the personal feature. So without a doubt whenever we refer to control over others we must admit the existence of a personal 
feature. Because there are different controllers for different managerial positions, there may be many small gods. According to 
the Bhagavad-gītā any controller who has some specific extraordinary power is called a vibhūtimat sattva, or controller empowered 
by the Lord. There are many vibhūtimat sattvas, controllers or gods with various specific powers, but the Absolute Truth is one 
without a second. This Śrīmad-Bhāgavatam designates the Absolute Truth or the summum bonum as the paraṁ satyam.
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

    response = llm.invoke([HumanMessage(content="What is the difference between the conception of God and the conception of Absolute Truth?")])

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