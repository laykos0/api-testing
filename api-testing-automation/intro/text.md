## Automated API testing using FastAPI, Startlette TestClient and Git Hooks

### Motivation

Automation of testing is essential in DevOps, since it largely reduces the time taken to manually find pre-existing bugs, as well as significantly lowers the risk of accidentally introducing new ones. 

Moreover, this is especially vital in the area of API testing, in order to avoid regression bugs and ensure consistent performance and reliability across different environments and versions.

### Intended Learning Outcomes

After this tutorial, you will learn how to:

- Set up a sample **FastAPI** application and run it using **Uvicorn**.
- Interact with **API endpoints** using **curl**.
- Review and run test cases using **Pytest**, identifying and fixing failing tests.
- Write own API test cases with **Starlette TestClient** and **Pytest**.
- Configure **Git Hooks** to automate test execution before each commit.
- Implement automated regression testing to validate new changes in the API.

### Background

- **FastAPI**: A modern and fast web framework for building APIs with Python. Well-suited for building REST APIs with asynchronous structure.
- **Starlette TestClient**: A lightweight toolkit for FastAPI, provides a way to simulate requests to your FastAPI with built-in testing client.
- **Pytest**: Pytest is a popular and powerful testing framework for Python, supporting unit, functional, integration, and API testing.
- **Git Hooks**: Scripts that run automatically at certain points in Git workflow, in our case, before any change to the API source code is committed.
