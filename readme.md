## Features
By using this repository, you quickly build your customized chatbot and make conversations with it. 
<br><br>

## A short demo video
<!-- <div style="position: relative; padding-bottom: 54.166666666666664%; height: 0;"><iframe src="https://www.loom.com/embed/e5a3c68351ad4ed1b8ceb2fe26e696fb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div> -->

[![Watch the video](https://plus.unsplash.com/premium_photo-1677094310893-0d6594c211ea?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80)](https://www.loom.com/share/e5a3c68351ad4ed1b8ceb2fe26e696fb)



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