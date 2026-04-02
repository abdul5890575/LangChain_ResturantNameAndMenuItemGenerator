from secretekeys import open_ai_key2
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableParallel
os.environ['OPENAI_API_KEY'] = open_ai_key2
parser = StrOutputParser()
llm = ChatOpenAI(model="gpt-5-nano")

def get_res_name(cuisine_name):
    name_chain = PromptTemplate.from_template(
        "I want to open a resturant for {cuisine} food. Suggest only 1 fancy name"
    ) | llm | parser

    menu_chain = PromptTemplate.from_template(
        "Suggest some food item name for the resturant {res_name}.return it as comma seperated list"
    ) | llm | parser

    full_chain = name_chain | RunnableParallel(
        restaurant_name=RunnableLambda(lambda x: x),  # keeps first output
        menu_items=menu_chain
    )
    result = full_chain.invoke({"cuisine": cuisine_name})

    return result