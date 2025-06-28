# ⚡️ Electrical Load Power Calculator – Web Application and Application

## Project Overview

The ***Electrical Load Power Calculator*** is a *web-based tool* built using *Python Flask* that allows users to compute essential electrical power values:

- Real Power (P)
- Apparent Power (S)
- Reactive Power (Q)

<em>It supports ***single-phase*** and ***three-phase*** systems. The app includes user registration, login, personalized history tracking, visual power triangle generation, and CSV export functionality.</em>

## Objectives

- Build an intuitive and interactive interface for calculating electrical load power.
- Provide real-time feedback and visual representation (power triangle).
- Store each user’s input and result for future reference.
- Allow easy data export and user authentication for personalized experience.

## Features

|           Feature             |           Description               |
|-------------------------------|-------------------------------------|
|   🔐 User Registration/Login  |Secure authentication for each user |
|   📥 Input Fields             |   BTS7960 / L298N / VESC           |
|   📊 Output Results           |   250W/500W BLDC Motor             |
|   📐 Power Triangle Plot      |   Hall Effect Based Throttle       |
|   🗂️ Calculation History      |   Hall Effect + Magnet             |
|   📤 CSV Export               |   24V / 36V Lithium Ion            |

## Technologies Used

|           Layer       |           Technology                  |
|-----------------------|---------------------------------------|
|   Backend             |   Python Flask, SQLAlchemy, SQLite    |
|   Frontend            |   HTML, CSS, Jinja2 (Flask templating)|
|   Data Visualization  |   Matplotlib                          |
|   Authentication      |   Werkzeug password hashing           |
|   File Export         |   CSV                                 |

## Theoretical Background

- Real Power (P):
P=VIcos(θ)

- Reactive Power (Q):
Q=VIsin(θ)

- Apparent Power (S):
S=VI

- Three-Phase Correction:
Multiply all formulas by √3 for 3-phase systems.

## System Architecture

System_Architecture.pgsql
```
User Browser ──▶ Flask Web Server
                  │
                  ├── Templates (HTML/Jinja2)
                  ├── Database (SQLite via SQLAlchemy)
                  └── Power Calculator Logic + Plotting
```
## Key Modules & Code Summary

1. *models.py* – Database Models
Defines: <br>
***User:*** Stores usernames and hashed passwords <br>
***Calculation:*** Stores all power calculations tied to a user <br>

2. *app.py* – Main Application
Handles user login, form submissions, calculation logic <br>
Stores results in SQLite and generates graphs with *matplotlib* <br>

3. Templates
***index.html***: Form and result display <br>
***login.html*** & ***register.html***: Authentication pages <br>
***history.html***: Displays user-specific past calculations <br>

## Screenshots
Homepage with Calculator Form <br>
Login/Register Page <br>
Output Power Triangle Plot <br>
History Page with *Data Table* <br>
Exported *CSV File* Example <br>












```


```


```

```

```

```

```

```

```

```

```
