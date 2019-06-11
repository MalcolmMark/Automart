const todo_db = require('../models/todos')

const get_by_id = (req, res) =>{
    const got_it = todo_db.some(x => x.id === parseInt(req.params.id))
    if(got_it){
        const _data = todo_db.filter(x => x.id === parseInt(req.params.id))
        res.json(_data)

    } else {
        res.json({
            message: "not found"
        })
    }
}

module.exports = get_by_id;