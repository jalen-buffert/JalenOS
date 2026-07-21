// Well no, a class
class Priority{
    constructor(title, category, action, latest_Status, level_Of_Importance, quick_Link) {
    this.title = title;
    this.category = category;
    this.action = action; 
    this.status = latest_Status;
    this.importance = level_Of_Importance;
    this.link = quick_Link;
    }
}


// Career Priorities 
const pc1 = new Priority('Company Research', 'Career','Apply to XXX', 'Connected with XXX', 'High', 'Quick Link');
                    
const pc2 = new Priority('Stay Connected', 'Career','Reach out to XXX', 'Recently spoke with XXX', 'Medium', 'Quick Link');         

//Learning 
const pl1 = new Priority('New Book', 'Learning','Go through XXX', 'Currently Reading XXX', 'Low', 'Quick Link');

const pl2 = new Priority('Learn Node','Learning','Start the lectures on Async','Implemented Objects into JalenOS','High','Quick_Link');

// Project 
const pp1 = new Priority('JalenOS','Projects','Continue to build out project','Added Objects','High', 'Quick_Link');


const pp2 = new Priority('Research Engine','Projects','Create the Repo','Have only ideated','High','Quick_Link');


const career_priorities = [pc1,pc2];
const learning_priorities = [pl1,pl2];
const project_priorities = [pp1,pp2];

function convert_to_JSON(priorities) {
    return JSON.stringify(priorities)
}

const data = convert_to_JSON([career_priorities,learning_priorities,project_priorities]);

console.log(data);

export {data};
