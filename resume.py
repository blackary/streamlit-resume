import streamlit as st

st.balloons()

"""
*[blackary.com](https://blackary.com) · [LinkedIn](https://www.linkedin.com/in/blackary/) · [StackOverflow](https://stackoverflow.com/story/blackary) · [Github](https://www.github.com/blackary/)* · *[printable](https://resume.blackary.com/zachary-blackwood-resume.pdf)*
"""

"""
# Zachary Blackwood
> Machine Learning Engineer and Python Developer
"""

with st.expander("EXPERIENCE"):
    """
    ## [DTN](https://www.dtn.com/), West Lafayette, IN
    #### Machine Learning Engineer, April 2018-Present
    * Creating and maintaining scalable computing and data storage/access for data science team with AWS EC2, S3, EFS, Batch & Lambda
    * Deploying and maintaining infrastructure for the data science team on AWS, including scalable computing, and data access/storage
    * Training developers in Python development and best practices through code feedback, mentorship conversations and python training seminars
    * Building and maintaining a distributed ML training pipeline for multiple production models that provide electric utility outage prediction
    * Creating and maintaining a data catalog tool which enables Data Scientists across the company to create new and access new data sets for modeling and analysis
    """
    """
    ## [Spensa](https://www.dtn.com/dtn-acquires-spensa-technologies/), West Lafayette, IN
    #### Full Stack Web Developer, July 2015-April 2018
    * Developing end-to-end features to conform to both detailed and limited specifications derived through conversations with product management
    * Managing and scaling web servers and PostgreSQL servers with a growing customer base and seasonal demand spikes
    * Integrating with several third-party APIs to allow users to asynchronously move terrabytes of data to and from these other services
    * Technical management for multi-million dollar long-term contract, including prioritizing tasks, training and assistance for a team of developers and facilitating customer and product management relationships
    * Monitoring and maintaining system to address outages and various other customer issues
    """
    """
    ## [Lewis Cass](http://www.lewiscass.net/), Walton, IN
    #### High School Teacher, September 2010-July 2015
    * Teaching courses including Physics, Computer Science & Principles of Engineering
    * Introducing multiple new courses to the school, including beta-teaching PLTW Computer Science
    * Researching, developing, delivering and revising effective lessons based on student success and student and mentor feedback
    * Creating and mentoring the Iron Kings, a FIRST Robotics team, who were able to advance to the World Championship in our rookie season
    * Mentoring the team members in fundraising, software development, electrical wiring, etc. in the process of creating our robot
    """


def two_cols(label: str, content: str):
    c1, c2 = st.columns((1, 3))

    with c1:
        f"**{label}**"

    with c2:
        content


with st.expander("TECHNICAL EXPERIENCE"):
    two_cols(
        "Open Source",
        """
        Contributed to python libraries, including

        [intake](https://github.com/intake/intake/commits?author=blackary) • [intake-geopandas](https://github.com/intake/intake_geopandas/commits?author=blackary) • [apache arrow](https://github.com/apache/arrow/commits?author=blackary)

        Co-developer and maintainer of a custom plugin for Intake which allows for the automatic population of a data catalog with data files matching a certain pattern
        """,
    )
    two_cols(
        "Programming Languages",
        """
        **high proficiency**: Python

        **medium proficiency**: JavaScrip
        """,
    )
    two_cols(
        "Technical Tools",
        """
        **ci/cd tools:** Bitbucket pipelines, GitLab, Bamboo

        **data science packages:** Pandas, Intake, Scikit-learn, Lightgbm

        **cloud architecture:** Amazon Web Services (Batch, Fargate, Lambda, EC2, S3, RDS, CloudFormation, CloudWatch, IAM)

        **web development:** Django, backbone.js, Postgresql, Postgis, Django Rest Framework, HTML, CSS
        """,
    )
    two_cols(
        "Side Projects",
        """
        Web development, design & hosting for various non-profit sites such as:

        [Gentle Reformation](https://gentlereformation.com) • [Women’s Retreat](https://rpcwomensretreat.com/) • [How Shall We Then Vote](https://howshallwethenvote.com/)
        """,
    )

with st.expander("EDUCATION"):
    two_cols(
        "2009-2011",
        """
        **M.S.Ed, Mathematics and Physics Education**; Purdue University (West Lafayette, IN)
        """,
    )
    two_cols(
        "2005-2009",
        """
        **B.S., Math & Physics**; Purdue University (West Lafayette, IN)

        *Minor: Computer Science*
        """,
    )
