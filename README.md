# LinkedIn-JobSeeker-AutomationProject-excel
# LinkedIn Job Search Automation

Automate your LinkedIn job search process with this Python script that searches for specific roles at target companies and exports the results to Excel.

## Features

- **Automated Job Search**: Searches LinkedIn based on role and company name
- **Excel Export**: Stores job details including:
  - Job URL
  - Role name
  - Location
  - Easy Apply status
- **Browser Automation**: Uses `webbrowser` and `pyautogui` to automate the search process
- **Customizable Parameters**: Easy configuration through parameter file

## Prerequisites

- Python 3.x
- Required libraries:
  - `webbrowser`
  - `pyautogui`
  - `openpyxl` or `pandas` (for Excel handling)

## Installation
```bash
pip install pyautogui openpyxl
```

## Configuration

### 1. Set Up Job Roles

Modify the `parameter.def` file to include your target roles, separated by commas:
```
Java Developer,Python Developer,Java full stack
```

### 2. Add Company Names

Add a new line in `parameter.def` with company names, separated by commas:
```
Codira,Digital Embrace,Code Runners
```

### 3. Prepare Excel File

- Place an Excel file in the working directory
- Set the Excel file name in `link-automate.py`

## Usage

Run the automation script:
```bash
python link-automate.py
```

Watch the magic happen! ✨

## Output

The script will populate your Excel file with:
- **Job URL**: Direct link to the job posting
- **Role Name**: Position title
- **Location**: Job location
- **Easy Apply**: Whether the job has Easy Apply enabled

## Notes

- Ensure you're logged into LinkedIn in your default browser
- The script uses GUI automation, so avoid interfering with the mouse/keyboard during execution
- Results are appended to the existing Excel file

## License

[Add your license here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
