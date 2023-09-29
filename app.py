import os
import openai
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_dotenv()  # Load environment variables from .env
openai.api_key = os.environ.get('OPENAI_API_KEY')

# # lang chain 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

response = ChatOpenAI(temperature=1)
# memory part
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=response,
    memory=memory,
    verbose=False
)

@app.route('/chat', methods = ['POST'])
def create():
    data = request.get_json()
    text = data.get('text')
    res = conversation.predict(input=text)
    return res


if __name__=="__main__":
    app.run(debug=True)


# def get_completion(prompt, model='gpt-3.5-turbo'):
#     messages = [{'role': 'user', 'content': prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=1.0
#     )
#     return response.choices[0].message['content']

# response = get_completion('what is 1+1 =')
# print('Response:', response)



# customer_email = "hey! where are you? why did you miss board meeting, Your this behabior is very bad"
# customer_style = "Indian language is very calm ans polite tone"

# prompt = """Transelate the text which is deliminated into the triple backticks into the style that is {style} the text is ```{text}```"""

# prompt_template = ChatPromptTemplate.from_template(prompt)
# customer_message = prompt_template.format_messages(
#     style= customer_style,
#     text=customer_email
# )
# # customer_response = response(customer_message)
# # print(customer_response)
# chat_model = ChatOpenAI()
# ans = chat_model.predict('what is 1+1')
# print(ans)
# # history part is here 