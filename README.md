<div align="center">
  <h1>Menu-ify Photo API</h1>
  <div align="center"><img src="images/food_photo.jpeg" alt="Deschutes Brewery GIF" class="center" width="480" height="320"></div>
</div>

<br>

# Table of Contents 
- [Project Overview](#project-overview)
- [Learning Goals](#learning-goals)
- [Developer Setup](#developer-setup)
- [Testing](#testing)
- [Tech and Tools](#tech-and-tools)
- [Endpoint](#endpoint)
- [Contributers](#contributors)


# Project Overview

Menu-ify is a full-stack application created by Backend and Frontend students of [Turing School of Software and Design](https://turing.edu/). The Menu-ify app allows restaurant owners the ability to easily create mobile-friendly menus to increase user experience. Instead of scrolling through a difficult to navigate pdf of a menu, a restaurant diner can view menu items in our user friendly app. This repo is one of two REST API microservices created for the Frontend to implement. This REST API utilizes the [Unsplash Photo Search API](https://unsplash.com/documentation#search-photos) and returns 10 images for the keyword searched. 

<br>

- [Rails Backend Repo](https://github.com/menu-ify/menu-ify-rails-be) - this repo holds our database and CRUD functionality<br>
- [Frontend Repo](https://github.com/menu-ify/menu-ify-fe)
- [Deployed App](https://menu-ify.vercel.app/)


# Learning Goals

[Project Specs](https://mod4.turing.edu/projects/capstone/index.html)

- Utilize Agile methodologies, Service Oriented Architecture, and Microservices to ensure deployment of a RESTful API with MVP

- Develop quality communication between Frontend and Backend teams, including daily stand-ups, project retros, a project board, and a JSON contract

- Gain experience using Continuous Integration tools to build and automate the deployment of features 

- Create API microservices to support application features for our end users

- Learn new technologies and tools (Python with FastApi Framework) 



# Developer Setup
  1. Make sure to have [Python](https://www.python.org/downloads/) Locally.
  2. Clone the repository 
  3. ```cd``` into the root directory 
  4. Create virtual environment ```python3 -m venv env```  
  5. Activate virtual environment ```source ./env/bin/activate```
  6. Sign up for the free Unsplash photo API https://unsplash.com/developers add Menu-ify under [Your apps](https://unsplash.com/oauth/applications). Scroll down to find your Access key 
  7. Create a new file called ```.env``` in root directory and add your secret key as an api_key i.e. ```api_key=123445566```
  8. To install requirements run: ```pip3 install -r requirements.txt ```
  9. To view endpoints locally run: ```uvicorn main:app --reload``` and navigate to url listed in terminal i.e. ```http://127.0.0.1:8000```
  10. You can view the interactive docs by adding ```/docs``` to the url in step 5 


# Testing 
  To run the tests using Pytest, run the following commands. Results will show in the terminal. 

  ``` 
    coverage run -m pytest
    coverage report -m 
  ```
  To see a coverage report within your browser then run.

  ```
    coverage html 
    open htmlcov/index.html
  ```
    



<br>

# Tech and Tools
- [Python 3.11.1](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/) 
- [Heroku](https://www.heroku.com/what)
- [CircleCI](https://circleci.com/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)





<br>

# Endpoint

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/24609974-41a1d2d6-5aa8-49d2-b086-76627d6839d3?action=collection%2Ffork&collection-url=entityId%3D24609974-41a1d2d6-5aa8-49d2-b086-76627d6839d3%26entityType%3Dcollection%26workspaceId%3D2902cec5-b68c-4ae7-a836-ede59d44bd2d#?env%5Bturing%20postman%5D=W3sia2V5IjoiZWNob1VSTCIsInZhbHVlIjoiaHR0cHM6Ly9wb3N0bWFuLWVjaG8uY29tIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6InNwb3RpZnlVUkwiLCJ2YWx1ZSI6Imh0dHBzOi8vcG9zdG1hbi1zcG90aWZ5LWdyYXBocWwuaGVyb2t1YXBwLmNvbSIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In1d)

- Interactive docs can be found here: https://menu-ify-fastapi.herokuapp.com/docs

- Deployed Backend Server: https://menu-ify-fastapi.herokuapp.com

- Local Backend Server: http://127.0.0.1:8000

- Example: Returns an array with 10 links for cheese photos. https://menu-ify-fastapi.herokuapp.com/photos/cheese

Request: <br>
```
 GET /photos/{food_search_term}
```
JSON Response Example:
```
 {
    "results":
    [
      "photo_url",
      "photo_url",
      "photo_url",
      "...",
      "..."
    ]
 }
```


    


# Contributors

## Project Team

<table>
  <tr>
    <td><img src="https://avatars.githubusercontent.com/u/57226658?v=4" width=110px height=auto></td>
    <td><img src="https://avatars.githubusercontent.com/u/108249540?v=4"width=110px height=auto></td>
    <td><img src="https://avatars.githubusercontent.com/u/108035840?v=4" width=110px height=auto></td>
  </tr>
  <tr>
    <td><div align="center"><strong>Emily Port</strong></div></td>
    <td><div align="center"><strong>Gabe Nunez</strong></div></td>
    <td><div align="center"><strong>Yuji Kosakowski</strong></td>

  </tr>
  <tr>
    <td>
      <div align="center">
        <a href="https://github.com/eport01">GitHub</a><br>
        <a href="https://www.linkedin.com/in/emily-port-3ab6389b/">LinkedIn</a>
      <div>
    </td>
    <td>
      <div align="center">
        <a href="https://github.com/MisterJackpots">GitHub</a><br>
        <a href="https://www.linkedin.com/in/gabriel-c-nunez/">LinkedIn</a>
      </div>
    </td>
    <td>
      <div align="center">
        <a href="https://github.com/Yuji3000">GitHub</a><br>
        <a href="https://www.linkedin.com/in/yujikosa/">LinkedIn</a>
      </div>
    </td>
  </tr>
</table>

## Project Manager

<table>
  <tr>
    <td><img src="https://avatars.githubusercontent.com/u/48163945?v=4" width=110px height=auto></td>
  </tr>
  <tr>
    <td><div align="center"><strong>Heather Faerber</strong></div></td>
  </tr>
  <tr>
    <td>
      <div align="center"><a href="https://github.com/hfaerber">GitHub</a><br>
      <a href="https://www.linkedin.com/in/heather-faerber/">LinkedIn</a></div>
    </td>
  </tr>
</table>

## Advisor

<table>
  <tr>
    <td><img src="https://avatars.githubusercontent.com/u/71724135?v=4" width=110px height=auto></td>
  </tr>
  <tr>
    <td><div align="center"><strong>Dara Rockwell</strong></div></td>
  </tr>
  <tr>
    <td>
      <div align="center"><a href="https://github.com/dara-rockwell">GitHub</a><br>
      <a href="https://www.linkedin.com/in/dcrockwell/">LinkedIn</a></div>
    </td>
  </tr>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>


