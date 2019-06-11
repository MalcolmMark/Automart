const get_all_todos = require ('../controllers/get_all_todos');
const router = require('express').Router();
const get_by_id = require ('../controllers/get_by_id')

router.get('/all', get_all_todos)
router.get('/all/:id',get_by_id)

module.exports = router;
