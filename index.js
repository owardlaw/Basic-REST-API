const express = require('express');
const app = express();
const PORT = 8080;
// curl, vs code extentsin=on, insomnia, or hostman connect to API

// Saving data function
var fs = require('fs')

var logger = fs.createWriteStream('./users/user23.txt', {
    flags: 'a'

})
var writeLine = (line) => logger.write(`\n${line}`);


// convert body to json
app.use( express.json() )

// Calling the server
app.listen(

    PORT,
    () => console.log(`API is ready at http://localhost:${PORT}`)

)

// () => {} this is a call back function
app.get('/users', (req, res) => {

    // confirm request and return json data
    res.status(200).send({
        id: 1,
        uname:'admin',
        detections:'24',
        status: 'Vellus',
        date:'01/24/22'
    }) 

});

// one function any ID within group use middleware via app.use( express.json() ) POSTing here so creating a new usr and ID
app.post('/users/:id', (req, res) => {

    // data to be recieved in post
    const { id } = req.params;
    const { uname } = req.body;
    const { status } = req.body;

    // checking if username is provided
    if (!uname) {

        res.status(418).send({message: 'Need username'})
    }

    res.send({
        user1: `User ${uname}, for ID ${id}, status of ${status}`

    })

    // check if dir exists
    const path = `./users/user${id}.txt`;

    // if exists, writes to existing file
    if (fs.existsSync(path)) {
        console.log("exists:", path);
        writeLine(`Status ${status}, time ${Math.floor(+new Date() / 1000)}`)
        console.log(`post from user${id} saved at ${Math.floor(+new Date() / 1000)}`);

        } 
    
    // if does not exist writes new file with user data
    else {
        console.log("Writing new user:", path);

        fs.writeFile(`./users/user${id}.txt`, `Status ${status}, time ${Math.floor(+new Date() / 1000)}`, err => {
            if (err) {
              console.error(err);
            }
          });

        }

});

