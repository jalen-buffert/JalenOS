import data from '../priority_list.js';

export const getAllPriorities = (req,res) => {
    res.send(data);
};

export const createPriority =  (req, res) => {
    res.send("..");
};

export const getPriorityByID = (req,res,next)=> {
    res.send("...");
};

export const updatePriority = (req,res) => {
    res.send("...");
};

export const deletePriority = (req,res) => {
    res.send("..");
};