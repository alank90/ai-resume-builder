# ============== Class object Resume ================================= #


class Resume:
    # pylint: disable-next=too-many-arguments
    def __init__(self, name,  email, current_position, mobile, summary):
        # Initialize the resume object with user information
        self.name = name
        self.email = email
        self.current_position = current_position
        self.mobile = mobile
        self.summary = summary
    """ def __init__(self, name,  email, mobile, education, skills,
                 experience, projects, achievements, activities):
        # Initialize the resume object with user information
        self.name = name
        self.email = email
        self.mobile = mobile
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.achievements = achievements
        self.activities = activities """

    def generate_markdown(self):
        # Generate Markdown content for the resume
        markdown_text = f"<h1 style=\"text-align:center;\">{self.name
                                                            }/h1>\n<p style=\"text-align:center;\">Email: {self.email
                                                                                                           } |  Mobile: {self.mobile} </p>\n\n"
        markdown_text += "### Education\n\n---\n\n"
        # Add education details to the Markdown content
        for edu in self.education:
            markdown_text += f"- {edu['level']}: {edu['institution']} | {
                edu['field']} | Score: {edu['score']} | {edu['duration']}." + "\n\n"

        markdown_text += "### Skills\n\n---\n\n"
        # Add skills to the Markdown content
        markdown_text += f"{self.skills} \n\n"

        markdown_text += "### Experience\n\n---\n\n"
        # Add work experience details to the Markdown content
        for exp in self.experience:
            markdown_text += f"- **{exp['job_role']
                                    }({exp['company_name']})**: {exp['description']}\n"

        markdown_text += "\n### Projects\n\n---\n\n"
        # Add project details to the Markdown content
        for proj in self.projects:
            markdown_text += f"- **{proj['name']}**: {proj['description']}\n"

        markdown_text += "\n### Achievements\n\n---\n\n"
        # Add achievement details to the Markdown content
        for ach in self.achievements:
            markdown_text += f"- {ach}\n"

        markdown_text += "\n### Other Activities\n\n---\n\n"
        # Add other activities to the Markdown content
        markdown_text += self.activities + '\n'

        return markdown_text
# ============== End of class object Resume ========================== #
