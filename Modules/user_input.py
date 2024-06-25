from Classes import resume_builder
import streamlit as st


def get():
    with st.expander("Fill out your profile"):
        # Gather user input for creating the resume
        name = st.text_input("Enter your name: ",
                             placeholder="Full name", key="1")
        name = "Name: \n" + name
        current_position = st.text_input(
            "Enter your current position: ", key="2")
        current_position = "Current Title: \n" + current_position
        email = st.text_input("Ënter your email: ", key="3")
        email = "Email: \n" + email
        mobile = st.text_input("Enter your mobile number: ",
                               placeholder="i.e. 555 233-1212", key="4")
        mobile = "Mobile: \n" + mobile
        summary = st.text_area(
            "Please give a brief summary of yourself", key="5")
        summary = "SUMMARY: \n" + summary

    with st.expander("Enter your Education details: "):
        education_array = []
        counter = 1000

        while True:
            if counter != 1000:
                counter += 1
            # Prompt user to add education details
            edu_input = st.text_input(
                "Do you want to add education details? (yes/no)", key=counter).lower()
            if edu_input != 'yes':
                break
            counter += 1

            resume_builder.Education.level = st.text_input(
                "Enter education level (e.g., Graduation(UG/PG), High School): ", key=counter)
            counter += 1

            resume_builder.Education.institution = st.text_input(
                f"Enter the name of the {resume_builder.Education.level} institution: ", key=counter)
            counter += 1

            resume_builder.Education.field = st.text_input(f"Enter the field of study at {
                resume_builder.Education.institution}: ", key=counter)
            counter += 1

            resume_builder.Education.grad_year = st.text_input(f"Enter year of graduation {
                resume_builder.Education.level} at {resume_builder.Education.institution}: ", key=counter)
            counter += 1

            resume_builder.Education.score = st.text_input(
                f"Enter your score (e.g., GPA/Percentage) of {resume_builder.Education.level} at {resume_builder.Education.institution}: ", key=counter)

            # Push answers onto education_array list
            education_array.append({"level": resume_builder.Education.level, "institution": resume_builder.Education.institution,
                                    "field": resume_builder.Education.field, "score": resume_builder.Education.score, })

        with st.expander("Enter your Work Experience details: "):
            experience = []
            counter_1 = 0

            while True:
                if counter != 0:
                    counter += 1
                # Prompt user to add Experience details
                exp_input = st.text_input(
                    "Do you want to add Experience details? (yes/no)", key=counter_1).lower()
                if exp_input != 'yes':
                    break
                counter_1 += 1

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
    return resume_builder.Resume(name, email, current_position, mobile, summary), resume_builder.Education
