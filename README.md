# AI-Resume Builder App

## Description

We will utilize an NLP(OpenAI) and demonstrate how we can easily create a personalized resume by providing essential details. See the article [here](https://towardsdatascience.com/using-openai-and-python-to-enhance-your-resume-a-step-by-step-guide-e2c1a359e194). The original github site is [here](https://github.com/PieroPaialungaAI/AI_CV_improver?source=post_page-----e2c1a359e194--------------------------------).

The app at a high level of abstraction would work like this:

![image info](/images/flow_chart.png)

Below, are the implementation details of the AI-Resume generator app Using _Python_ and _Streamlit_ step-by-step.

### Implementation

Install [python](https://www.python.org/downloads/) if you haven't already. Confirm its installation with comand _python -V_.

Next, create the virtual environment using the below commands

_python -m venv env_

then activate the environment (if necessary, see Note)

_.\env\Scripts\activate.ps1_

## Notes on setting up Python project & environment

- Create a .env file in root directory and then add the key OPENAI_API_KEY="My_API_Key".
  Because we have specifically named the env variable "\_OPENAI_API_KEY*" the OpenAI module will automatically import it, no need to add it when initializing the client. Or else you can assign a variable with the _load_dotenv_ library and call it:

  _from **dotenv** import \*\*\_load_dotenv_\*\*

  **_load_dotenv()_**

  Retrieving the environment variables is easy peezy - just use the **_os_** module:

  **_import os_**

  _**os.getenv**("CUSTOM_API_LINK")_

- Creating a _**requirements.txt**_ file once your project dependencies are all installed and you want to lock down all project package versions

  Run this command

  **pip freeze > requirements.txt** and you'll see that the requirements file gets added

  then to install packages run:

  **pip install -r requirements.txt**

- Integrating Python environment in Visual Code _[see article](https://code.visualstudio.com/docs/python/environments)_

- Download a .gitignore file with **_wget https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -O .gitignore_**

For Linting and styling also add extentions **[pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)** & **[autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)**

To run the app at the prompt type:

_**streamlit run app.py**_

## Note

- You will have to run Powershell script _.\env\Scripts\Activate.ps1_ everytime you start a new seesion if you havent associated the virtual environment thru VS Code. To check from powershell command line - echo $Env:VIRTUAL_ENV
