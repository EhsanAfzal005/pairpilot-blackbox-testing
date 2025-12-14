# PairPilot IDE – Black Box Testing using Selenium

## 📌 Project Overview

This repository contains **black box test automation** for the **PairPilot IDE** Final Year Project (FYP). The testing is performed using **Selenium WebDriver with Python**. The goal is to validate critical user-facing functionalities without inspecting internal source code.

### 🔍 Tested Modules

1. **User Registration (Sign Up)**
2. **User Authentication (Sign In)**
3. **Create Project**
4. **Join Project**

Each module is tested independently following black box testing principles.

---

## 🛠️ Technologies Used

* Python 3.x
* Selenium WebDriver
* Google Chrome (Version 143.x)
* WebDriver Manager

---

## 📁 Recommended Project Structure

```
Pair-Pilot-Testing/
│
├── selenium_scripts/
│   ├── test_signup.py
│   ├── test_signin.py
│   ├── test_create_project.py
│   └── test_join_project.py
│
├── screenshots/
│   ├── signup_before.png
│   ├── signup_after.png
│   ├── signin_before.png
│   ├── signin_after.png
│   └── ...
│
├── drivers/               # (optional – webdriver-manager auto handles this)
│
|── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python

Make sure **Python 3.9+** is installed:

```bash
python --version
```

### 2️⃣ Install Required Libraries

Run the following command in the project root:

```bash
pip install -r requirements.txt
```

### 3️⃣ Start PairPilot IDE Backend

Ensure the PairPilot IDE application is running locally:

```
http://localhost:3000
```

---

## ▶️ Running the Tests

Navigate to the `selenium_scripts` folder and run any test:

```bash
python test_signup.py
```

> ℹ️ Note: For **Create Project** and **Join Project**, the user must be **logged in** first.

---

## 📸 Screenshots Evidence

Each test script captures screenshots:

* **Before submission**
* **After submission**

These screenshots are stored in the `screenshots/` folder and serve as proof of execution for evaluation.

---

## 🧪 Testing Methodology

* **Testing Type:** Black Box Testing
* **Approach:** Functional testing based on user inputs and outputs
* **Validation:** UI behavior, form validation, navigation, and submission results

---

## 📦 requirements.txt

```txt
selenium>=4.15.0
webdriver-manager>=4.0.1
```

---

## 📤 GitHub Submission Notes

* All Selenium scripts are pushed to GitHub
* No application source code is included
* Screenshots are added as testing evidence

---

## ✅ Conclusion

This repository fulfills the requirement for **automated black box testing** of the PairPilot IDE using Selenium. The tests validate core user workflows and provide documented evidence suitable for academic submission.

---



