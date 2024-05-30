from tabulate import tabulate

def format_resume_info(resume_info):
    table_data = []
    for key, value in resume_info.items():
        if key not in ["Programming Skills", "Query Languages", "Other Languages or Tools"]:
            table_data.append([key, value])

    combined_skills = ", ".join(filter(None, [resume_info.get("Programming Skills", ""), resume_info.get("Query Languages", ""), resume_info.get("Other Languages or Tools", "")]))
    table_data.append(["Skills", combined_skills])

    return tabulate(table_data, headers=["Category", "Information"], tablefmt="pipe")
