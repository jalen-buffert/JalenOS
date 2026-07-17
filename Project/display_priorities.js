import {career_priorities, learning_priorities, project_priorities } from "./priority_list.js";

function convert_to_JSON(priorities) {
    return JSON.stringify(priorities)
}


function display(priorities) {
    
    //for(i = 0 ; i < priorities.length; i ++){
    //    console.log(priorities.forEach(priorities =>console.log(priorities)));
    //}
    return priorities
    
}
const json_s = convert_to_JSON(career_priorities);
// console.log(json_s)
console.log(career_priorities)
export {json_s};

//console.log(display([career_priorities, learning_priorities, project_priorities]));

// Objects 
// Modules
// File system
// HTTP Server 