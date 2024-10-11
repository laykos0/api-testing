First, we will need to install python 3, pip(Python package manager) and Git. You can choose any version on Python, as long as it support the tools we need. 
In our case, Python, pip and Git are built-in, but for you to be able to reproduce
this tutorial on your own Linux system, here is the command for installing them:
`sudo apt install -y python3 python3-pip git`{{exec}}

Now we can install our tools:
`pip install fastapi uvicorn pytest httpx`{{exec}}
