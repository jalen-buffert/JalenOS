# Priorities

A priority is an actionable object that JalenOS can rank or surface to the user based on importance and context.

### priority_id
- required, automatically generated, immutable

### title
- required
- cant be blank
- max length 50 chars
- represents the main idea of the priority 

### category 
- immutable
- required to set initially
- Choice between Career, Investment, Education, Health, Projects

### action
- no current cap on length
- What needs to be done next 
- required

### status 
- required
- what have you done most recently
- max length 200 chars

### importance 
- required 
- Choice between:
    - High: Prioritize this over other things. Needs much attention now.
    - Medium: Can take a passenger seat but still need to prioritize.
    - Low: Not currently on te radar
    
### Link
- Optional
- Provide a resource to help with finishing this priority.
