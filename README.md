<div align="center">
  <h1>Menu-ify Photo API</h1>
  <div align="center"><img src="images/food_photo.jpeg" alt="Deschutes Brewery GIF" class="center" width="480" height="320"></div>
</div>

<br>

# Project Overview

Menu-ify is an application created by students of [Turing School of Software and Design](https://turing.edu/). This is one of two microservices. This micro-service utilizes external api calls to produce images that will be used on our front-end application. <br>
[Our other back-end repo containing the database](https://github.com/menu-ify/menu-ify-rails-be)<br>
[Menu-ify front end Application](https://github.com/menu-ify/menu-ify-fe)


# Learning Goals

- Utilize Agile methodologies to ensure deployment of MVP

- Develop quality communication between front-end and back-end teams, which include daily stand-ups, weekly retros and an evolving process to achieve higher communication standards

- Create micro-services including a database and external API consumption to support application features for our end users

- Learn new technologies and tools (Python with FastApi Framework). 



## Developer Setup
  1. Make sure to have [Python](https://www.python.org/downloads/) Locally.
  2. In Terminal Run ```pip3 install -r requirements.txt ```
  3. If you would like to run the tests. Results will show in the terminal.

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

## Built With
- [Python 3.11.1](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/) 
- [Heroku](https://www.heroku.com/what)





<br>

# Endpoints
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
      "photo_url"
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


