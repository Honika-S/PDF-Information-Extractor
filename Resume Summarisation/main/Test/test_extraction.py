import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from text_extraction import extract_contact_details, extract_name, extract_social_links, extract_experience, extract_education, extract_skills
def test_extract_contact_details():
    resume_text_no_email = ""
    expected_output_no_email = {"Email": ""}
    assert extract_contact_details(resume_text_no_email) == expected_output_no_email

    resume_text_multiple_emails = "test@example.com"
    expected_output_multiple_emails = {"Email": "test@example.com "}
    assert extract_contact_details(resume_text_multiple_emails) == expected_output_multiple_emails

def test_extract_name():
    resume_text_name="John Doe"
    expected_output_name={"Name":"John Doe"}
    assert extract_name(resume_text_name)==(expected_output_name)
    resume_text_no_name = "\nEmail: test@example.com"
    expected_output_no_name = {"Name": ""}
    assert extract_name(resume_text_no_name) == (expected_output_no_name)

def test_extract_social_links():
    resume_text = "linkedin.com/in/johndoe\n github.com/johndoe"
    expected_output = {"LinkedIn": "linkedin.com/in/johndoe", "GitHub": 'github.com/johndoe'}
    assert extract_social_links(resume_text) == expected_output
    resume_text_no = ""
    expected_output_no = {"LinkedIn": "", "GitHub": ''}
    assert extract_social_links(resume_text_no) == (expected_output_no)
    

def test_extract_experience():
    resume_text_no_experience = "No experience"
    expected_output_no_experience = {"Experience": "No experience"}
    assert extract_experience(resume_text_no_experience) == expected_output_no_experience
    resume_text_experience = "5+ years of experience in software development."
    expected_output_experience = {"Experience": "5+ years of experience in software development."}
    assert extract_experience(resume_text_experience) == (expected_output_experience)

def test_extract_education():
    resume_text = "Education: B.E in Computer Science, CGPA 8.5"
    expected_output = {"Education": "Education: B.E in Computer Science, CGPA 8.5"}
    assert extract_education(resume_text) == expected_output
    resume_text_no = ""
    expected_output_no = {"Education": ""}
    assert extract_education(resume_text_no) == (expected_output_no)

def test_extract_skills():
    resume_text = "Skills: Python, Java\nQuery Languages: SQL\nTools: Git"
    expected_output = {"Programming Skills": "Python, Java", "Query Languages": "SQL", "Other Languages or Tools": "Git"}
    assert extract_skills(resume_text) == expected_output
    resume_text_no_skills = ""
    expected_output_no_skills = {"Programming Skills": "", "Query Languages": "", "Other Languages or Tools": ""}
    assert extract_skills(resume_text_no_skills) == expected_output_no_skills

from text_extraction import (
    extract_contact_details,
    extract_name,
    extract_social_links,
    extract_experience,
    extract_education,
    extract_skills,
    extract_resume_info,
)

def test_extract_resume_info():
    # Test case with complete information
    resume_text_complete = (
        "John Doe\n"
        "Email: john.doe@example.com\n"
        "linkedin.com/in/johndoe\n"
        "github.com/johndoe\n"
        "5+ years of experience in software development.\n"
        "Education: Bachelor of Science in Computer Science, CGPA 3.8\n"
        "Programming Languages: Python, Java\n"
        "Query Languages: SQL\n"
        "Tools: Git, Docker"
    )
    expected_output_complete = {
        "Name": "John Doe",
        "Email": "john.doe@example.com ",
        "LinkedIn": "linkedin.com/in/johndoe",
        "GitHub": "github.com/johndoe",
        "Experience": "5+ years of experience in software development.",
        "Education": "Education: Bachelor of Science in Computer Science, CGPA 3.8",
        "Programming Skills": "Python, Java",
        "Query Languages": "SQL",
        "Other Languages or Tools": "Git, Docker"
    }
    assert extract_resume_info(resume_text_complete) == expected_output_complete

    # Test case with missing name
    resume_text_no_name = (
        "\n"
        "Email: john.doe@example.com\n"
        "linkedin.com/in/johndoe\n"
        "github.com/johndoe\n"
        "5+ years of experience in software development.\n"
        "Education: Bachelor of Science in Computer Science, CGPA 3.8\n"
        "Programming Languages: Python, Java\n"
        "Query Languages: SQL\n"
        "Tools: Git, Docker"
    )
    expected_output_no_name = {
        "Name": "",
        "Email": "john.doe@example.com ",
        "LinkedIn": "linkedin.com/in/johndoe",
        "GitHub": "github.com/johndoe",
        "Experience": "5+ years of experience in software development.",
        "Education": "Education: Bachelor of Science in Computer Science, CGPA 3.8",
        "Programming Skills": "Python, Java",
        "Query Languages": "SQL",
        "Other Languages or Tools": "Git, Docker"
    }
    assert extract_resume_info(resume_text_no_name) == expected_output_no_name

    # Test case with missing email
    resume_text_no_email = (
        "John Doe\n"
        "linkedin.com/in/johndoe\n"
        "github.com/johndoe\n"
        "5+ years of experience in software development.\n"
        "Education: Bachelor of Science in Computer Science, CGPA 3.8\n"
        "Programming Languages: Python, Java\n"
        "Query Languages: SQL\n"
        "Tools: Git, Docker"
    )
    expected_output_no_email = {
        "Name": "John Doe",
        "Email": "",
        "LinkedIn": "linkedin.com/in/johndoe",
        "GitHub": "github.com/johndoe",
        "Experience": "5+ years of experience in software development.",
        "Education": "Education: Bachelor of Science in Computer Science, CGPA 3.8",
        "Programming Skills": "Python, Java",
        "Query Languages": "SQL",
        "Other Languages or Tools": "Git, Docker"
    }
    assert extract_resume_info(resume_text_no_email) == expected_output_no_email

    # Test case with missing social links
    resume_text_no_social_links = (
        "John Doe\n"
        "Email: john.doe@example.com\n"
        "5+ years of experience in software development.\n"
        "Education: Bachelor of Science in Computer Science, CGPA 3.8\n"
        "Programming Languages: Python, Java\n"
        "Query Languages: SQL\n"
        "Tools: Git, Docker"
    )
    expected_output_no_social_links = {
        "Name": "John Doe",
        "Email": "john.doe@example.com ",
        "LinkedIn": "",
        "GitHub": "",
        "Experience": "5+ years of experience in software development.",
        "Education": "Education: Bachelor of Science in Computer Science, CGPA 3.8",
        "Programming Skills": "Python, Java",
        "Query Languages": "SQL",
        "Other Languages or Tools": "Git, Docker"
    }
    assert extract_resume_info(resume_text_no_social_links) == expected_output_no_social_links

    # Test case with missing experience
    resume_text_no_experience = (
        "John Doe\n"
        "Email: john.doe@example.com\n"
        "linkedin.com/in/johndoe\n"
        "github.com/johndoe\n"
        "Education: Bachelor of Science in Computer Science, CGPA 3.8\n"
        "Programming Languages: Python, Java\n"
        "Query Languages: SQL\n"
        "Tools: Git, Docker"
    )
    expected_output_no_experience = {
        "Name": "John Doe",
        "Email": "john.doe@example.com ",
        "LinkedIn": "linkedin.com/in/johndoe",
        "GitHub": "github.com/johndoe",
        "Experience": "No experience",
        "Education": "Education: Bachelor of Science in Computer Science, CGPA 3.8",
        "Programming Skills": "Python, Java",
        "Query Languages": "SQL",
        "Other Languages or Tools": "Git, Docker"
    }
    assert extract_resume_info(resume_text_no_experience) == expected_output_no_experience

    # Test case with missing education
    resume_text_no_education = (
        "John Doe\n"
        "Email: john.doe@example.com\n"
        "linkedin.com/in/johndoe\n"
        "github.com/johndoe\n"
        "5+ years of experience in software development.\n"
        "Programming Languages: Python, Java\n"
        "Query Languages: SQL\n"
        "Tools: Git, Docker"
    )
    expected_output_no_education = {
        "Name": "John Doe",
        "Email": "john.doe@example.com ",
        "LinkedIn": "linkedin.com/in/johndoe",
        "GitHub": "github.com/johndoe",
        "Experience": "5+ years of experience in software development.",
        "Education": "",
        "Programming Skills": "Python, Java",
        "Query Languages": "SQL",
        "Other Languages or Tools": "Git, Docker"
    }
    assert extract_resume_info(resume_text_no_education) == expected_output_no_education

    # Test case with missing skills
    resume_text_no_skills = (
        "John Doe\n"
        "Email: john.doe@example.com\n"
        "linkedin.com/in/johndoe\n"
        "github.com/johndoe\n"
        "5+ years of experience in software development.\n"
        "Education: Bachelor of Science in Computer Science, CGPA 3.8"
    )
    expected_output_no_skills = {
        "Name": "John Doe",
        "Email": "john.doe@example.com ",
        "LinkedIn": "linkedin.com/in/johndoe",
        "GitHub": "github.com/johndoe",
        "Experience": "5+ years of experience in software development.",
        "Education": "Education: Bachelor of Science in Computer Science, CGPA 3.8",
        "Programming Skills": "",
        "Query Languages": "",
        "Other Languages or Tools": ""
    }
    assert extract_resume_info(resume_text_no_skills) == expected_output_no_skills

    # Test case with minimal information
    resume_text_minimal = (
        "John Doe\n"
        "Email: john.doe@example.com"
    )
    expected_output_minimal = {
        "Name": "John Doe",
        "Email": "john.doe@example.com ",
        "LinkedIn": "",
        "GitHub": "",
        "Experience": "No experience",
        "Education": "",
        "Programming Skills": "",
        "Query Languages": "",
        "Other Languages or Tools": ""
    }
    assert extract_resume_info(resume_text_minimal) == expected_output_minimal
