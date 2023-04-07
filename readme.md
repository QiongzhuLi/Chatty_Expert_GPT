## Features
By using this repository, you can actually talk with any book you like if you are too lazy to read a book :D
<br><br>

## Requirements
1. Please install the necessary python modules  
    ```pip install -r requirement.txt```
2. You update the file .env with two keys, one is your open ai key [link](https://openai.com/), another one is your xi-api-key [link](https://beta.elevenlabs.io/)
<br><br>

## How to talk with book
1. Put a digital version of book in the data folder, e.g. mine is 'Book 1 - The Philosopher's Stone.txt' 
2. Run the following code in the terminal, then you can ask any questions.
```python
python chatwithbook_v3.py
```
<br><br>


## Structure
```
|──
│  .env
│  chatwithbook_v3.py
│  index.json
│  readme.md
│  requirement.txt
│
├─data
│      Book 1 - The Philosopher's Stone.txt
│
└─output
        input.wav
```