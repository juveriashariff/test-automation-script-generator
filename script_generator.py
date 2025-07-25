import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_framework_details():
    """Return available frameworks and their details"""
    return {
        "1": {"name": "Selenium (Python)", "key": "selenium", "language": "python", "extension": ".py"},
        "2": {"name": "Cypress (JavaScript)", "key": "cypress", "language": "javascript", "extension": ".js"},
        "3": {"name": "Playwright (Python)", "key": "playwright-py", "language": "python", "extension": ".py"},
        "4": {"name": "Playwright (JavaScript)", "key": "playwright-js", "language": "javascript", "extension": ".js"},
        "5": {"name": "API Testing (Python - requests)", "key": "requests", "language": "python", "extension": ".py"}
    }

def get_framework_prompt(framework_key):
    """Return the appropriate system prompt for each framework"""
    prompts = {
        "selenium": "Generate modern Selenium 4 WebDriver code in Python using Page Object Model pattern. "
                   "Use WebDriverWait for explicit waits and locators using By class. "
                   "Include proper setup/teardown and clear comments.",
        "cypress": "Generate Cypress test scripts in JavaScript with best practices. "
                  "Use fixtures if needed for test data. Include clear comments and assertions.",
        "playwright-py": "Generate Playwright test scripts in Python. "
                        "Use the page object pattern and include proper assertions. "
                        "Include necessary imports and clear comments.",
        "playwright-js": "Generate Playwright test scripts in JavaScript. "
                        "Use modern async/await syntax. "
                        "Include proper setup and assertions with clear comments.",
        "requests": "Generate API test scripts in Python using requests library. "
                   "Include proper authentication if needed, status code checks, "
                   "and response validation. Use pytest style assertions."
    }
    return prompts.get(framework_key, prompts["selenium"])

def generate_test_script(requirement, framework_key):
    """Generate test automation script for the selected framework"""
    system_prompt = get_framework_prompt(framework_key)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful test automation assistant. {system_prompt}"},
            {"role": "user", "content": f"Create a complete test for: {requirement}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def save_to_file(content, framework_details, requirement):
    """Save generated script to a file with appropriate extension"""
    # Create output directory if it doesn't exist
    os.makedirs("generated_scripts", exist_ok=True)
    
    # Generate filename from requirement and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_requirement = "".join(c if c.isalnum() else "_" for c in requirement[:30])
    filename = f"generated_scripts/test_{safe_requirement}_{timestamp}{framework_details['extension']}"
    
    # Write to file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    
    return filename

def display_framework_options(frameworks):
    """Display framework options to user"""
    print("\nAvailable Test Frameworks:")
    for key, details in frameworks.items():
        print(f"{key}. {details['name']}")
    print("")

if __name__ == "__main__":
    frameworks = get_framework_details()
    
    print("AI Test Automation Script Generator")
    print("----------------------------------")
    
    # Display framework options
    display_framework_options(frameworks)
    
    # Get user input
    while True:
        choice = input("Select framework (1-5): ")
        if choice in frameworks:
            framework_key = frameworks[choice]["key"]
            framework_details = frameworks[choice]
            break
        print("Invalid choice. Please select 1-5.")
    
    requirement = input("\nDescribe the test scenario (e.g., 'login with invalid credentials'): ")
    
    print("\nGenerating test script...")
    script = generate_test_script(requirement, framework_key)
    
    print("\n=== Generated Test Script ===")
    print(script)
    
    # Save to file
    saved_path = save_to_file(script, framework_details, requirement)
    print(f"\nScript saved to: {saved_path}")
    print("Script generation complete!")