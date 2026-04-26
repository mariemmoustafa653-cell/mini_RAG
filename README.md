# mini_RAG
AI-powered multi-tenant e-learning platform builder that enables teachers to create customized learning websites with integrated domain-specific chatbots. The chatbot uses RAG (Retrieval-Augmented Generation) to answer student queries based on uploaded course materials, ensuring accurate and context-aware responses.

## Requirments 


-Python 3.10 or later 

#### Install Python From Miniconda 

1)  Download and install Miniconda  from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) create enviroment using the following commad:
 '''bash 
$ conda create -n mini-RAG  python=3.10
'''
3) Activate The Enviroment :
'''bash
$conda activate mini-RAG
'''
### install the required packages 

'''bash
$pip install -r requirements.txt
'''

### setup the environment variables 

'''bash
$ cp .env.example .env
'''
set your environment variables in the '.env' file. like 'OPENAI_API_KEY' value.

## Run the FastAPI server 
'''bash 
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
'''













