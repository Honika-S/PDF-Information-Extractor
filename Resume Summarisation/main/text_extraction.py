import re

def extract_contact_details(resume_text):
    resume_data = {"Email": ""}
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"  #"[a-zA-Z0-9_.+-]+" mathches string before @ symbol
    other_contacts = re.findall(email_regex, resume_text)
    if other_contacts:
        resume_data["Email"] += " ".join(other_contacts) + " "
        
    return resume_data

def extract_name(resume_text):
    name_line = resume_text.splitlines()[0] #splitlines() splits into line breaks
    return {"Name": name_line.strip()} #strip() to remove the whitespace

def extract_social_links(resume_text):
    resume_data = {"LinkedIn": "", "GitHub": ""}
    linkedin_regex = r"(linkedin\.com\/in\/[^\s]+)"
    github_regex = r"(github\.com\/[^\s]+)"
    for line in resume_text.splitlines():
        if "linkedin.com/in/" in line:
            resume_data["LinkedIn"] = line.strip()
        elif "github.com/" in line:
            resume_data["GitHub"] = line.strip()
    return resume_data

def extract_experience(resume_text):
    resume_data = {"Experience": ""}
    experience = re.findall(r"(\d+\+)(.*)", resume_text)
    if experience:
        years, remaining = experience[0]
        resume_data["Experience"] = f"{years} {remaining.strip()}"
    else:
        resume_data["Experience"] = "No experience"
    return resume_data

def extract_education(resume_text):
    resume_data = {"Education": ""}
    education_pattern = re.compile(r"(?i)\bEducation\b\s*(.*?)\s*(?!\d{4}-\d{4})(\bCGPA\s+\d+\.\d+\b)", re.DOTALL)
    match_education = re.search(education_pattern, resume_text)
    if match_education:
        resume_data['Education'] = match_education.group(0).strip()
    return resume_data

def extract_skills(resume_text):
    resume_data = {"Programming Skills": "", "Query Languages": "", "Other Languages or Tools": ""}
    programming_skills = re.findall(r"(Programming Languages|.*\bSkills)\s*:(.*)", resume_text, re.IGNORECASE)
    for heading, content in programming_skills:
        if content.strip():  
            resume_data["Programming Skills"] = content.strip()
    query_languages = re.findall(r"Query Languages:(.*)", resume_text, re.IGNORECASE)
    if query_languages:
        resume_data["Query Languages"] = query_languages[0].strip()
    other_languages_tools = re.findall(r"Tools:(.*)", resume_text, re.IGNORECASE)
    if other_languages_tools:
        resume_data["Other Languages or Tools"] = other_languages_tools[0].strip()
    return resume_data

def extract_resume_info(resume_text):
    resume_data = {}
    resume_data.update(extract_contact_details(resume_text))
    resume_data.update(extract_name(resume_text))
    resume_data.update(extract_social_links(resume_text))
    resume_data.update(extract_experience(resume_text))
    resume_data.update(extract_education(resume_text))
    resume_data.update(extract_skills(resume_text))
    return resume_data
