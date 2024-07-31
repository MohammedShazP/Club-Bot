from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import SequentialChain
import json

hf_key = json.load(open("keys.json"))
HF_TOKEN = hf_key["HF_TOKEN"]


llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct",
    task = "text-generation",
    do_sample = False,
    max_new_tokens = 100,
    temperature = 0.5,
    huggingfacehub_api_token = HF_TOKEN
)

def generate_restaurant_name_and_items(clubs_names):
    # Chain 1: Restaurant name
    prompt_template_name = PromptTemplate(
        input_variables = ['nation'],
        template="I want the name of only one famous football club in {nation}"
    )
    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "club_name")

    prompt_template_items = PromptTemplate(
        input_variables = ["club_name"],
        template = "Tell me the details of {club_name} and their famous players"
    )

    item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="players_name")

    chain = SequentialChain(
        chains = [name_chain,item_chain],
        input_variables = ['nation'],
        output_variables = ['club_name','players_name']
    )

    response = chain({"nation" : clubs_names})
    return response

if __name__ == "__main__" :
    print(generate_restaurant_name_and_items("Italian"))