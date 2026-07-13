const Career = ['Research Companies', ' Submit Applications', 'Follow up with Recruiters', ' Reach out to Jermee for lunch resched'];
const Learning = ['Find new book', 'Finish node learning lesson','Read Chapter', 'Update Efficient Frontier Project'];
const Projects = ['JalenOS', 'Portfolio', 'AWS'];
const Investments = ['Review Roth', 'Review Earnings', 'Macro News', 'Review Individual Acc'];

// Career Priorities 
const priority1 = { 'Title':'Company Research',
                    'Level of Importance':'High',
                    'Category':'Career',
                    'Action':'Apply to XXXX, and research XXX until you find 10 jobs then reach out to 3 people within company.',
                    'Latest Status': 'Connected with XXXX and XXX, but also have not applied to any of the 4 positions.',
                    'Quick Link': '.....'
}

// Learning Priorities 

// Project Priorities 

// Investment Priorities 

Each Priority needs: 
 - Title 1-3 words 
 - Level of Importance
 - Category
 - 1 Sentence Action Item
 - Latest Status 
 - Quick Link to Anything that will help accomplish priority

function display(priorities) {
    for(i = 0 ; i < priorities.length; i ++){
        console.log(priorities.forEach(priorities =>console.log(priorities)));
    }
    return priorities
    
}

console.log(display([Career,Learning,Projects,Investments]));

// Objects 
// Modules
// File system
// HTTP Server 