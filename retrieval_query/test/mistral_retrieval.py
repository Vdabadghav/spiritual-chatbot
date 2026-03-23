from mistralai.client import Mistral
import os

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

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

query = input("Ask a question: ")

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
)

print("\nAnswer:", response.choices[0].message.content)