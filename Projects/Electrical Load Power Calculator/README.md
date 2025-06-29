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

### Create a Python application that calculates:

1. Real Power (P)
2. Reactive Power (Q)
3. Apparent Power (S)
4. Power Factor (PF)
5. Load Current (I)
<em>based on user inputs for voltage, current, power factor, and type of load (single-phase or three-phase).</em>

## Features

|           Feature             |           Description               |
|-------------------------------|-------------------------------------|
|   User Registration/Login  |Secure authentication for each user |
|   Input Fields             |   BTS7960 / L298N / VESC           |
|   Output Results           |   250W/500W BLDC Motor             |
|   Power Triangle Plot      |   Hall Effect Based Throttle       |
|   Calculation History      |   Hall Effect + Magnet             |
|   CSV Export               |   24V / 36V Lithium Ion            |

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
- ***User:*** Stores usernames and hashed passwords <br>
- ***Calculation:*** Stores all power calculations tied to a user <br>

2. *app.py* – Main Application
- Handles user login, form submissions, calculation logic <br>
- Stores results in *SQLite* and generates graphs with *matplotlib* <br>

3. Templates
- ***index.html***: Form and result display <br>
- ***login.html*** & ***register.html***: Authentication pages <br>
- ***history.html***: Displays user-specific past calculations <br>

## Screenshots
Homepage with Calculator Form <br>
Login/Register Page <br>
Output Power Triangle Plot <br>
History Page with *Data Table* <br>
Exported *CSV File* Example <br>

## Output Example
***User inputs:***
```
Voltage  |  Current  |	Power Factor  |	Phase Type
230 |  10  |  0.8   | Single
```

***Output:***
```
Real Power (P) | Reactive Power (Q) | Apparent Power (S)
1.84 kW	       | 1.38 kVAR          | 2.30 kVA
```

## Security Features

- Passwords stored securely using hashing (Werkzeug)
- Sessions to track user logins
- Calculation history is user-specific and private

## Export Feature

Clicking "Export" generates a downloadable *CSV file* with all previous results for a user, formatted as: <br>
export.scss

```
Voltage,Current,PF,Phase,P (kW),Q (kVAR),S (kVA)
230,10,0.8,single,1.84,1.38,2.30
...

```

## Learning

- Built full-stack Python web application
- Applied core electrical engineering formulas
- Used Flask, SQLAlchemy, Matplotlib, and session handling
- Learned user authentication and secure password storage
- Gained practical experience in web development and Python backend



<em>This project is a fully functional web-based electrical power calculator that demonstrates both theoretical electrical engineering knowledge and practical Python web development skills. It is extendable, secure, and provides a useful educational tool for students, engineers, and technical audiences.</em>










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
