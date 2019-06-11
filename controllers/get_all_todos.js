const todo_db = require('../models/todos')

const get_all_todos = (req, res) =>{
    res.json(todo_db)
}

module.exports = get_all_todos;