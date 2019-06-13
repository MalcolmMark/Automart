const router = require('express').Router();
const { makeOrder, updateOrder } = require ('../controllers/order.controller');

router.post('/', makeOrder);
router.patch('/:order-id', updateOrder);

module.exports = router;