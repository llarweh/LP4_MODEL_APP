# LP4_MODEL_APP
🚀 Friendly Web Interface for ML Projects with Gradio &amp; Streamlit 🚀
# Hi there, I'm Lawrence 👋
# I'm a Data Analyst !
# Description
This project is a Python-based application that can predict the sales of Corporation Favorita Grocery, a large Ecuadorian supermarket chain. The application uses Streamlit, an open-source framework that allows creating interactive web apps for machine learning and data science. The user can input various factors such as product category, store location, date, and promotion, and the app will output the expected sales for that scenario. This project can help Corporation Favorita Grocery optimize its inventory management and marketing strategies.

# Installation
You have two ways in order to setup and run this project.

# Manual Setup
For manual installation, you need to have Python3 on your system. Then you can clone this repo and being at the repo's root :: friendly_web_interface_for_ML_models> ... follow the steps below:

## Windows:

  python -m venv venv;
  venv\Scripts\activate;
  python -m pip install -q --upgrade pip;
  pip install -r requirements.txt;  
## Linux & MacOs:

  python3 -m venv venv;
  source venv/bin/activate;
  python -m pip install -q --upgrade pip;
  python install -r requirements.txt  
The both long command-lines have a same structure, they pipe multiple commands using the symbol ; but you may manually execute them one after another.

Create the Python's virtual environment that isolates the required libraries of the project to avoid conflicts;
Activate the Python's virtual environment so that the Python kernel & libraries will be those of the isolated environment;
Upgrade Pip, the installed libraries/packages manager to have the up-to-date version that will work correctly;
Install the required libraries/packages listed in the requirements.txt file so that it will be allow to import them into the python's scripts and notebooks without any issue.
NB: For MacOs users, please install Xcode if you have an issue.

Run the demo apps (being at the repository root):

# Streamlit:

streamlit run streamlit_project\app.py;

# Gradio:

gradio gradio_project\app.py;

The above code redirect you to your default browser, if not

Go to your browser at the following address for streamlit:

http://localhost:8501;
Go to your browser at the following address for gradio:

  http://127.0.0.1:7860; # or
  http://127.0.0.1:7861
# Screenshots
Streamlit Basic Demo
<img width="382" alt="streamlit" src="https://github.com/llarweh/LP4_MODEL_APP/assets/131138224/b214827e-4ebe-4c0a-8646-465dd59a0c0e">

Gradio Basic Demo
<img width="947" alt="gradio" src="https://github.com/llarweh/LP4_MODEL_APP/assets/131138224/3ddc7b66-39e4-47d0-a3d1-b3bd902b7248">

# Resources
Here are some ressources you would read to have a good understanding of Gradio and Streamlit :

Get started with Streamlit

Get started with Gradio

# Contributing
[HENOK SOLOMON](https://github.com/Henamen21/model_app/blob/master/www.linkedin.com/in/henok-solomon-a3b537206) 

# Author
[LAWRENCE LARWEH](https://www.linkedin.com/in/lawrencelarweh/?originalSubdomain=gh)
