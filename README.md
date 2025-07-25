# AI Test Automation Script Generator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-GPT_3.5-green)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent script generator that converts natural language test scenarios into executable test scripts across multiple frameworks using AI, with automatic file saving.

![Demo Animation](https://via.placeholder.com/800x400.png?text=AI+Test+Script+Generator+Demo+GIF)

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Frameworks](#supported-frameworks)
- [File Output](#file-output)
- [How It Works](#how-it-works)
- [Customization](#customization)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Roadmap](#roadmap)

## 🚀 Features

- **Multi-framework code generation** for 5+ test automation tools
- **Automatic file saving** with proper extensions (.py/.js)
- **Smart file naming** with timestamps to prevent conflicts
- **Natural language processing** - describe tests in plain English
- **Production-ready scripts** with proper structure and comments
- **Framework-specific best practices** included

## 🛠️ Prerequisites

Before you begin, ensure you have:

- Python 3.8+ ([download](https://www.python.org/downloads/))
- Git ([install guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- OpenAI API key ([get here](https://platform.openai.com/account/api-keys))
- Terminal (PowerShell, Bash, or ZSH)
- `dotenv` Python package (for loading `.env` variables)

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-test-automation.git
   cd ai-test-automation
   ```

2. **Set up virtual environment**  
   **Windows**  
   ```bash
   py -m venv venv
   .\venv\Scripts\activate
   ```
   **macOS/Linux**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure API key**  
   Create a `.env` file with:  
   ```ini
   OPENAI_API_KEY=sk-your-key-here
   ```

## 🏃‍♂️ Usage

Run the generator:

```bash
python script_generator.py
```

1. **Select framework** from the menu (1-5)  
2. **Describe your test scenario** in natural language  
3. **View** the generated script in the terminal  
4. The script is **automatically saved** to `generated_scripts/` with:
   - Framework-appropriate extension
   - Descriptive filename
   - Timestamp for uniqueness

Example saved file:
```
generated_scripts/test_login_invalid_creds_20240215_142310.py
```

## 🛠️ Supported Frameworks

| Option | Framework                     | Language   | Extension | Key Features                           |
| ------ | ----------------------------- | ---------- | --------- | -------------------------------------- |
| 1      | Selenium (Python)             | Python     | .py       | Page Object Model, WebDriverWaits      |
| 2      | Cypress (JavaScript)          | JavaScript | .js       | Time-travel debugging, automatic waits |
| 3      | Playwright (Python)           | Python     | .py       | Cross-browser support, auto-wait       |
| 4      | Playwright (JavaScript)       | JavaScript | .js       | Modern async/await syntax              |
| 5      | API Testing (Python - requests)| Python    | .py       | Requests library, pytest assertions    |

## 💾 File Output

Generated scripts are saved with this naming convention:  
```
generated_scripts/test_[scenario]_[YYYYMMDD_HHMMSS][extension]
```

Example structure:
```
generated_scripts/
├── test_login_invalid_creds_20240215_142310.py
├── test_checkout_flow_20240215_142415.js
└── test_api_auth_20240215_142521.py
```

## 🧠 How It Works

1. **User selects** target framework  
2. **System constructs** an optimized prompt for GPT  
3. **AI generates** complete test script with:
   - Framework-specific syntax
   - Proper imports
   - Best practices
   - Clear comments
4. **Outputs** to terminal and **saves** to file

## 🧩 Customization

- **Modify file saving**:  
  Edit the `save_to_file()` function to change the output directory, adjust filename format, or add new extensions.

- **Add new frameworks**:  
  - Update `get_framework_details()`  
  - Add a new prompt in `get_framework_prompt()`

## 📂 Project Structure

```
ai-test-automation/
├── generated_scripts/     # Auto-created output folder
├── venv/                  # Virtual environment
├── .env                   # API key configuration
├── script_generator.py    # Main application
├── requirements.txt       # Dependencies
├── README.md              # This document
└── LICENSE                # MIT License
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ❤️ Acknowledgments

- OpenAI for the GPT API  
- Selenium, Cypress, and Playwright teams  
- Python community for amazing testing tools

## 📈 Roadmap

- Add syntax validation  
- Create a web interface  
- Add CI/CD integration examples  
- Implement test data generation  
- Support additional frameworks (Appium, Robot Framework)
