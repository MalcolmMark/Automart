const express = require('express');
const myapp = express();
const todoRouter = require('./routes/todos');

myapp.use(express.json());

myapp.use('/api', todoRouter)

myapp.get('/', (req, res)=>{
    res.send({
        message: "Hello Malcolm"
    })
})
const PORT = process.env.PORT || 6000;

myapp.listen(PORT, () =>{
    console.log(`Listening ${PORT}`)
})