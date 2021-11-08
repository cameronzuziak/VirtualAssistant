Virtual Assistant
*************************
@author Cameron Zuziak

DESCRIPTION: 
This app uses voice recognition to convert any question you ask into text. 
It then runs a google search of this text and retrieves the top google result. Next the app 
opens the webpage of the first result and scrapes all the article content of said webpage. 
After that, the app then tokenizes all article content and uses cosine similarity to determine
which sentences are most relevant to the question that you asked. It then takes the most relevant 
sentences, concatenates them into a larger string, and converts the string to audio. 

TL;DR 
Ask the app anything, it'll search google and give you a relevant answer most of the time. 

*************************

Set Up:

1. open up your terminal and cd into this folder 

2. create new venv using:

	python3 -m venv venv	

3. activate the virtual environment by running the following command: 
		
	source venv/bin/activate
 
4. download and install newspaper corpora (you need to do this before installing requirements):

    curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3

5. install requirements by running:

	pip3 install -r requirements.txt

6. run the command: python3 recognize.py

7. ask a question and be amazed by the power of nlp, such aww, many wow. ૮･ﻌ･ა 