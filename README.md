# Resume Information Extractor

## Overview

The PDF Information Extractor is a Streamlit application that extracts and formats key information from PDF resumes. It utilizes pdfminer.six for text extraction and custom functions to identify and display relevant details like contact information, experience, education, and skills.

## Features

- Upload PDF resumes.
- Extract contact details, names, social links, experience, education, and skills.
- Display extracted information in a user-friendly format.

## Requirements

- Python 3.12
- Streamlit
- pdfminer.six
- re
- tabulate
- Docker
- Pytest

## Installation

1. Install the required Python packages:

   pip install -r requirements.txt

2. Run the Streamlit app:

   streamlit run app.py

## Usage

1. Open the Streamlit app in your web browser.
2. Upload a PDF resume using the file uploader.
3. Click the "Extract Info" button to extract and display the resume information.

## Code Explanation

1. app.py

The main application file that sets up the Streamlit interface:

- Uploads a PDF file.
- Extracts text using pdfminer.high_level.extract_text.
- Calls custom functions to extract and format resume information.
- Displays the extracted information.

2. text_extraction.py

Contains functions to extract different sections of the resume:

- extract_contact_details: Extracts emails.
- extract_name: Extracts the name.
- extract_social_links: Extracts LinkedIn and GitHub links.
- extract_experience: Extracts experience details.
- extract_education: Extracts education details.
- extract_skills: Extracts skills.
- extract_resume_info: Aggregates all extracted information.

3. details.py

Contains the function to format the extracted information:

- format_resume_info: Formats the extracted information into a tabular format using the tabulate library.

## Dockerization

1. Build the Docker image:

   docker build -t resume-app .

2. Run the Docker container:

   docker run -p 8501:8501 resume-app

## Testing

Tests are written using pytest to ensure the functionality of the extraction functions. The test file includes cases for extracting contact details, names, social links, experience, education, and skills from the resume text.

1. Tests are written using pytest.

   pytest test_extraction.py

2. To run the tests and generate a coverage report:

   pip install coverage
   coverage run -m pytest
   coverage report
