# datafun-03-analytics
STEP !
Create a New Repository From Scratch:
  Log in to GitHub. Open your browser and log in to your GitHub account.
  Go to the "Create Repository" Page
  In the top-right corner of GitHub, click the + dropdown menu.
  Select New repository.
  Name Your Repository
  Provide a brief description of your project. This is optional but recommended.
  Select the Public option so others can view your repository.
  Add a Default README File
    Check the box for Add a README file.
selecy Create the Repository

STEP 2
Use Git to clone the new repository to your local machine:
  Open your project repository in VS Code.
  We'll open a new terminal in VS Code and run a single command.
    git clone https://github.com/youraccount/yourrepo

STEP 3
Add files such as .gitignore and requirements.txt:

Step 4
Use Git to add, commit, and push your new files to GitHub:
  Using a terminal in VS Code (PowerShell, zsh, or bash).
    git add .
    git commit -m "Add .gitignore and requirements.txt files"
    git push -u origin main

STEP 5.
Create a Local Python Virtual Environment for your project:
  Open your project repository in VS Code. Open a new terminal in VS Code and run a single command to   
  create a new .venv folder.
    py -m venv .venv

Optional step 5.5 ( Im just trying remember everything and create cheat sheets for myself. Goodness knows I need them) Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub
    Open your project repository in VS Code.
    We'll open a new terminal in VS Code and run a single command
      git pull origin main

Optional STEP 5.7 Activate the Project Virtual Environment ( You do not always need this) 
    Run the following command from the project root directory. The command works in PowerShell.
      .venv\Scripts\activate
STEP 6 Install Dependencies
  -Ensure .venv is active.
  -Run the following commands from the project root directory. The commands work in PowerShell.
    .\.venv\Scripts\activate
    py -m pip install --upgrade pip setuptools wheel
    py -m pip install -r requirements.txt
STEP 7  Run Scripts ( Also known as the bane of my exsistance) 
 raw data to root folder. 
STEP 8
 >(run) script. Commit Changes 
STEP 9
Update README file

 
  






