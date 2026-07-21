import express from 'express';
import { getAllPriorities } from '../controllers/prioritycontroller';
const router = express.Router();
const port = 3000;


router.get('/', getAllPriorities);

router.post('/', (req,res) => {
    res.send('POST request for JalenOS');
});

router.get('/:id', (req, res) => {
    res.send('Get a specific priority');
});

router.patch('/:id', (req,res) => {
    res.send('Update a priority');
});

router.delete('/:id', (req,res) => {
    res.send('Delete a priority');
});

export {router};