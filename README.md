# LinkedIn Applicant Ranker Landing Page

A modern landing page for the LinkedIn Applicant Ranker application, built with FastAPI and TailwindCSS.

## Features

- Modern, responsive design
- Early access signup form
- FastAPI backend
- TailwindCSS styling
- Font Awesome icons

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   python main.py
   ```
2. Open your browser and visit:
   ```
   http://localhost:8000
   ```

## Development

- The main landing page is in `index.html`
- The FastAPI server is in `main.py`
- Static files (if any) should be placed in the `public` directory

## Form Submissions

The signup form submissions are currently handled by the FastAPI backend and printed to the console. In a production environment, you would want to:

1. Add proper database integration
2. Implement email notifications
3. Add form validation
4. Set up proper error handling
5. Add CSRF protection

## License

MIT License 