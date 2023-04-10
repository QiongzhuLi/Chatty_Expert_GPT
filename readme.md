## Features
By using this repository, you quickly build your customized chatbot and make conversations with it. 
<br><br>

## Requirements
1. Please install the necessary python modules  
    ```pip install -r requirement.txt```
2. Update the file .env with two keys, one is your open ai key [link](https://openai.com/), another one is your xi-api-key [link](https://beta.elevenlabs.io/)
<br><br>

## How to interact with chatty_expert
1. Place any documents here for your chatty expert to learn from, e.g. mine is 'Book 1 - The Philosopher's Stone.txt' 
2. Run the following code in the terminal, then you can ask any questions by talking to the chatty expert. Please confirm that your device can use the **microphone and player**. This is to ensure that you can smoothly conduct voice communication and listen to guidance. If your device does not support these functions, you may not be able to talk with the bot. 
 
```python
python chatty_expert.py
```
<br><br>


## Structure
```
|─ (This is the root folder)
│  .env
│  chatty_expert.py
│  index.json
│  readme.md
│  requirement.txt
│
├─data (You can place any documents/knowledge here for your chatty expert to learn from)
│      Book 1 - The Philosopher's Stone.txt
│
└─output (All temporary output will be placed here)
        input.wav
```