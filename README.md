# Natural Language Processing Based Chatbot
This Natural Language Processing-based chatbot can provide answers based on the predictions of the Neural Network model that has been trained using some conversational data.
The architecture model used is Long Short-Term Memory (LSTM) Neural Network.

## API Reference

#### Get App Status

```http
  GET /
```

#### Predict Message

```http
  POST /msg
```

Body Request
```json
{
    "msg": "Your message",
}
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/taqiyyaghazi/python-ai-chatbot
```

Go to the project directory

```bash
  cd python-ai-chatbot
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```

## Tech Stack

- Python
- Tensorflow
- MongoDB
