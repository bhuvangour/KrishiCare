---
runme:
  id: 01HQZ3WD4GGREC2RCE9AZRSZWJ
  version: v3
---
<br>
<p align="center">
    <img src="static/Images/Logo.png" alt="logo" width="500">
  </a>
</p>

<p align="center">
<b>#Better Crops, Better Life </b>
</p>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Description of Project](#description-of-project)
- [Top Features](#top-features)
- [Design](#design)
- [Tech-stack used](#techstack-used)
- [Contributors](#contributors)

## Problem Statement

**College Name: Vellore Institute of Technology**

## Description of Project

India is predominantly an agricultural country. Farming is a major occupation in India and one of the biggest challenges which comes when a huge workforce is occupied is that it becomes very difficult to provide personal attention to every farmer. To help the farmers improve in agricultural sector, we propose a web-based application "कृषि Care". Through the web-app we provide online tele-consultation services as well as offline alternatives for consultation to farmers. They can get support in various agricultural activities, by the help of consultants as well as connect with their peers through the web.

## Running the Project

Run the following commands (dev build)
You can skip creating a virtual environment if there are errors.

```sh {"id":"01HQZ4SVEKP6088210YNNXH84Y"}
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

Next

```sh {"id":"01HQZ4XKGT0HW3CHNHM6BEQ87F"}
python manage.py collectstatic 
python manage.py runserver

```
