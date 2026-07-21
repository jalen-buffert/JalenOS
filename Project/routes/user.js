import express from 'express';
const router = express.Router();
const port = 3000;


router.get('/', (req, res) => {
    res.send('JalenOS Home page');
});

router.post('/', (req,res) => {
    res.send('POST request for JalenOS');
});

router.put('/priority', (req, res) => {
    res.send('PUT request for JalenOS');
});


router.listen(port, () => {
    console.log('Example app listening on port ${port}');
});

router.delete('/priority', (req,res) => {
    res.send('Delete request for JalenOS');
});

export {router};

// GET priorities 
// return priorities
// POST priorities
// split into routes and controllers 
