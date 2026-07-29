from server.models.priority import Priority

real_priorities = [
    #Career, Education, Projects, Investments
    Priority(
        priority_id = 1,
        title = 'Update Resume', 
        category = 'Career',
        action = 'Reach out to XXX, and edit version XXX',
        status = 'Last spoke to XXX and did XXX',
        importance = 'High',
        link = 'NA'
        ),
    Priority(
        priority_id = 2,
        title = 'Apply to 5 jobs', 
        category = 'Career',
        action = 'Research XXX companies',
        status = 'Last spoke to XXX',
        importance = 'High',
        link = 'NA'
        ),
    
    Priority(
        priority_id = 3,
        title = 'Read XXX', 
        category = 'Education',
        action = 'SEt 30 minutes out of the day to read',
        status = 'Currently on Page XXX',
        importance = 'High',
        link = 'NA'
        ),
    Priority(
        priority_id = 4,
        title = 'AWS Certification', 
        category = 'Education',
        action = 'Continue Udemy course',
        status = 'Last learned about XXX',
        importance = 'High',
        link = 'NA'
        ),
    
    Priority(
        priority_id = 5,
        title = 'JalenOS', 
        category = 'Projects',
        action = 'Continue building project out',
        status = 'Last worked on changing data into pydantic classes',
        importance = 'High',
        link = 'NA'
        ),
    Priority(
        priority_id = 6,
        title = 'Revamp Efficient Frontier', 
        category = 'Projects',
        action = 'See any pitfalls and commentary from Devs',
        status = 'Last Published on web and didn\'t touch',
        importance = 'Medium',
        link = 'NA'
        ),
    
    Priority(
        priority_id = 7,
        title = 'Rebalance Portfolio', 
        category = 'Investments',
        action = 'Research XXX companies for insights into next investment',
        status = 'Last looked into XXX',
        importance = 'Medium',
        link = 'NA'
        ),
    Priority(
        priority_id = 8,
        title = 'Build Models for forecasting', 
        category = 'Investments',
        action = 'Look into previous models built',
        status = 'Last worked on were Black litterman, Mean-Variance',
        importance = 'Low',
        link = 'NA'
        )
]
