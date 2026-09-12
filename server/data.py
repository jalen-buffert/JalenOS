from server.schemas.priority import Priority

real_priorities = [
    #Career, Education, Projects, Investments
    Priority(
        priority_id = '4dcbd9b0-99d4-45b3-8eba-21e7ded3cb73',
        title = 'Update Resume', 
        category = 'Career',
        action = 'Reach out to XXX, and edit version XXX',
        status = 'Last spoke to XXX and did XXX',
        importance = 'High',
        Link = None
        ),
    Priority(
        priority_id = 'a8b661f9-b4b6-42e8-9271-954b42a9e820',
        title = 'Apply to 5 jobs', 
        category = 'Career',
        action = 'Research XXX companies',
        status = 'Last spoke to XXX',
        importance = 'High',
        link = None
        ),
    
    Priority(
        priority_id = '907c7aab-56fd-4a72-b62a-045378c782d3',
        title = 'Read XXX', 
        category = 'Education',
        action = 'SEt 30 minutes out of the day to read',
        status = 'Currently on Page XXX',
        importance = 'High',
        link = None
        ),
    Priority(
        priority_id = 'ae41b068-4d45-45e7-99a6-355cfd0f7633',
        title = 'AWS Certification', 
        category = 'Education',
        action = 'Continue Udemy course',
        status = 'Last learned about XXX',
        importance = 'High',
        link = None
        ),
    
    Priority(
        priority_id = '425bb88d-267e-4080-8c41-44f47f45e525',
        title = 'JalenOS', 
        category = 'Project',
        action = 'Continue building project out',
        status = 'Last worked on changing data into pydantic classes',
        importance = 'High',
        link = None
        ),
    Priority(
        priority_id = 'c9e2ac15-a155-4d4b-9422-46b059e0d700',
        title = 'Revamp Efficient Frontier', 
        category = 'Project',
        action = 'See any pitfalls and commentary from Devs',
        status = 'Last Published on web and didn\'t touch',
        importance = 'Medium',
        link = None
        ),
    
    Priority(
        priority_id = 'f7169ff5-27c6-411a-b240-eb76e7fec7c9',
        title = 'Rebalance Portfolio', 
        category = 'Investment',
        action = 'Research XXX companies for insights into next investment',
        status = 'Last looked into XXX',
        importance = 'Medium',
        link = None
        ),
    Priority(
        priority_id = 'e2b77d4a-376c-493f-928a-b84344185730',
        title = 'Build Models for forecasting', 
        category = 'Investment',
        action = 'Look into previous models built',
        status = 'Last worked on were Black litterman, Mean-Variance',
        importance = 'Low',
        link = None
        )
]
