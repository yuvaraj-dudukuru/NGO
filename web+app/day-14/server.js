// 1. import the express library
const express = require('express');

// 2. initialize the express application
const app = express();

// 3. define the port number 
const PORT = 3000;

//4. create a GET route for the root path (the root url)
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

//5. create a GET route (A JSON API endpoint) for the path /api/data
app.get('/api/data', (req, res) => {
    const mockUsers = [
        { id: 1, name: 'Alice', email: 'alice@example.com' },
        { id: 2, name: 'Bob', email: 'bob@example.com' }
    ];
    // send the array back as json response
    res.json(mockUsers);
});

//6. start the server and listen on the defined port
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
}   );