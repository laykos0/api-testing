## Tools
First, we need to set up the development environment by installing **tools** and **packages** that are essential for **developing**, **running**, and **testing** our FastAPI project by running:


`sudo apt install -y python3 python3-pip git`{{exec}}

The following tools will be installed:

- **Python 3**: The programming language required for running FastAPI applications (versions 3.7+).
- **pip**: The package manager for Python.
- **Git**: A version control system to manage code and enable Git Hooks.

**Note**: Seen above tools are already installed in the tutorial virtual machine, you can skip running this part.

## Packages

Once **Python** and **pip** are installed, you can install the necessary packages using **pip**:


`pip install fastapi uvicorn pytest httpx`{{exec}}

This command installs:

- **FastAPI**: Web framework for building APIs with Python 3.7+.
- **Uvicorn**: ASGI server implementation, used to run FastAPI applications.
- **Pytest**: Python testing framework to run the test cases.
- **httpx**: Python HTTP client, required by Starlette's TestClient for making HTTP requests.


**Note**: The provided examples of commands are intended for use in a **Linux** environment with **apt** package manager. If you are using a different system, the installation commands may vary.