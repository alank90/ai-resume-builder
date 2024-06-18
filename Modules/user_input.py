from Classes import resume_builder
import streamlit as st


def get():
    # Gather user input for creating the resume
    name = st.text_input("Enter your name: ", placeholder="Full name", key="1")
    st.write(name)
    current_position = st.text_input("Enter your current position: ", key="2")
    email = st.text_input("Ënter your email: ", key="3")
    mobile = st.text_input("Enter your mobile number: ",
                           placeholder="i.e. 555 233-1212", key="4")

    print("\nEducation:")
    education = []
    counter = 1000

    while True:
        # Prompt user to add education details
        edu_input = st.text_input(
            "Do you want to add education details? (yes/no)", key=counter).lower()
        counter = counter + 1
        if edu_input != 'yes':
            break

        level = st.text_input(
            "Enter education level (e.g., Graduation(UG/PG), High School): ", key="6")
        institution = st.text_input(
            f"Enter the name of the {level} institution: ", key="7")
        field = st.text_input(f"Enter the field of study at {
                              institution}: ", key="8")
        duration = st.text_input(f"Enter passing year of {
            level} at {institution}: ", key="9")
        score = st.text_input(
            f"Enter your score (e.g., GPA/Percentage) of {level} at {institution}: ", key="10")
        education.append({"level": level, "institution": institution,
                          "field": field, "duration": duration, "score": score, })
    """
    skills = st.text_input("\nEnter your skills (comma-seperated): ",  key= "11")

    print("\nExperience:")
    experience = []
    while True:
        # Prompt user to add work experience details
        job_role = st.text_input(
            "Enter your job role (or type 'done' to finish): ")
        if job_role.lower() == 'done':
            break
        exp_company_name = st.text_input("Enter the company name: ")
        exp_description = st.text_input(
            f"Enter the description for '{job_role}': ")
        experience.append(
            {"job_role": job_role, "company_name": exp_company_name,
                "description": exp_description})

    print("\nProjects:")
    projects = []
    while True:
        # Prompt user to add project details
        proj_heading = st.text_input(
            "Enter the project Title (or type 'done' to finish): ")
        if proj_heading.lower() == 'done':
            break
        proj_description = st.text_input(
            f"Enter the description for '{proj_heading}': ")
        projects.append(
            {"name": proj_heading, "description": proj_description})

    print("\nAchievements:")
    achievements = []
    while True:
        # Prompt user to add achievement details
        ach_input = st.text_input(
            "Enter an achievement detail (or type 'done' to finish): ")
        if ach_input.lower() == 'done':
            break
        achievements.append(ach_input)

    print("\nOther Activities like hobbies:") """
    # Prompt user to add other activities or hobbies
    # activities = st.text_input("Enter your other activities: ")
    # return resume_builder.Resume(name, email, mobile, current_position, education, skills, experience, projects, achievements, activities)
    return resume_builder.Resume(name, email, mobile, education)
