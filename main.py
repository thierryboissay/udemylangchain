import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL")


def main():
    print("Hello from langchain-course!")
    information = """
    Elon Musk, né le 28 juin 1971 à Pretoria (Afrique du Sud), est un entrepreneur, homme d'affaires international, chef d'entreprise, homme politique et milliardaire sud-africain, canadien et américain. Il est considéré comme la personne la plus riche du monde.

Elon Musk commence sa carrière en affaires comme cofondateur de la société de logiciels Zip2 avec son frère, Kimbal Musk. La start-up est acquise par Compaq pour 307 millions de dollars en 1999. La même année, Musk cofonde la banque en ligne X.com, qui fusionne avec Confinity en 2000 pour former PayPal. eBay rachète PayPal en 2002 pour 1,5 milliard de dollars.

Il est le cofondateur et le président-directeur général de la société astronautique SpaceX en 2002 ainsi que le cofondateur et directeur général de la société automobile Tesla depuis 2004. En octobre 2022, il devient le propriétaire de Twitter par un achat à 44 milliards de dollars, qu'il renomme « X » l'année suivante.
    """
    summary_template = """
    given the information {information} about a person, i want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        template=summary_template, 
        input_variables=["information"])


    llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0)
    #llm = ChatOllama(model="gemma3:270m", temperature=0)

    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
