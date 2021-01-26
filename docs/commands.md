conda create --name py python=3.7
pip install -r requirements.txt
conda env remove --namw py
conda create --name py2 --clone py


git add . && git commit -m "Message" && git push origin master

pip freeze > requirements.txt