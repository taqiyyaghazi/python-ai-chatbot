import numpy as np
import json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
from tensorflow.keras.models import load_model
import json
import string
import database

def predict_msg(msg):

    with open('../data/content.json') as content:
        data1 = json.load(content)

    responses={}
    for intent in data1['intents']:
        responses[intent['tag']]=intent['responses']

    model = load_model('model.h5')

    with open('../data/tokenizer.json') as f:
        token = json.load(f)
        tokenizer = tokenizer_from_json(token)

    texts_p = []
    #removing punctuation and converting to lowercase
    prediction_input = [letters.lower() for letters in msg if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    texts_p.append(prediction_input)
    #tokenizing and padding
    prediction_input = tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = pad_sequences([prediction_input], model.input_shape[1])
    
    #getting output from model
    predict = model.predict(prediction_input)
    output = predict.argmax()
    classes = ['goodbye', 'greeting', 'howami', 'kontak', 'salam',
        'selamattinggal', 'siapakamu', 'whereareyou', 'whoareyou']
    response_tag = classes[output]

    if predict[0][output] > 0.6:
        return {
            'status': 'success',
            'data': {
                'response': random.choice(responses[response_tag]),
                'probability': str(predict[0][output])
            }
        }
        
    else:
        database.handling_msg_missed(msg)
        return {
            'status': 'success',
            'data': {
                'response': "Hi, I haven't learned what you're asking. I'll ask Ghazi first, okay?",
                'probability': str(predict[0][output])
            }
        }