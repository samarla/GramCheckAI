import streamlit as st
from transformers import pipeline
import time

grammarChecker = pipeline(task='sentiment-analysis', model='samarla/RoBERTa-base-cola')

header = 'GramcheckAI'

caption1 = "Enhance Your Writing with GramChekAI: Your Ultimate Grammar Assistant"

caption2 = "Powered by CoLA Fine-Tuned Reborta-base Model - A Smart App to Ensure Flawless Grammar and Language Acceptability!"

body = """Introducing "GramCheckAI" - Your Ultimate Grammar Assistant!

GramChekAI is a cutting-edge web application designed to enhance your writing skills and ensure impeccable grammar in every sentence you compose. Powered by the state-of-the-art "Reborta-base" language model, fine-tuned with the comprehensive CoLA dataset, this app promises to revolutionize the way you communicate.

Key Features:

1. Grammar Accuracy: Say goodbye to embarrassing grammar mistakes! GramChekAI uses advanced Natural Language Processing (NLP) algorithms to meticulously analyze each sentence you input, detecting potential grammatical errors with precision.

2. CoLA Dataset Fine-Tuning: Our language model has been fine-tuned on the Corpus of Linguistic Acceptability (CoLA) dataset, which makes it exceptionally proficient in evaluating sentence acceptability, ensuring reliable and trustworthy results.


Say farewell to grammar mistakes and unlock your true writing potential with GramcheckAI. Use the app now and experience the seamless blend of AI sophistication and user-friendly design that will empower you to write with confidence and clarity like never before. Happy writing!"""

#header section
st.header(f':violet[{header}]', )
st.caption(caption1)
st.caption(caption2)
st.markdown("Let's dive and check your sentence :eyes:")

#image = Image.open('./gramcheck.jpg')
#st.image(image=image, caption='check grammer')


def coloringAcceptance(acc, conf):
    if acceptance == 'Acceptable':
        st.subheader(f"Sentence is :green[{acceptance}] with confidence of {conf} %")
    else:
        st.subheader(f"Sentence is :red[{acceptance}] with confidence of {conf} %") 

options = (
        '',
        'GramcheckAI helps writers improve their language skills and confidence',
        'The app identifies errors and provides real-time suggestions for corrections',
        "The app finded sentence errors, but it's still useful"
    )

container = st.container()
selected_option = container.selectbox(
    'Test with an example', options=options
)

count =1 

while len(selected_option)>0:
    text = container.text_input('Type your own Sentence', selected_option, key=f'opted_sentence{count}')
    count+=1
    break
else:
    text = container.text_input('Type your own Sentence',key='typed_sentence')
    
button_bool = container.button('Check now')
if len(text) > 0:
    with st.spinner('Wait for it...'):
        result = grammarChecker(text)
    acceptance = result[0]['label']
    conf_score = round(result[0]['score']*100,2)
    coloringAcceptance(acceptance, conf_score)
else:
    container.text('Input the sentence please!')


expander = st.expander("Brief about")
expander.text('\n\n\n\n\n')
expander.title(body)


