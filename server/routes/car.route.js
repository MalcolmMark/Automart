const router = require('express').Router();
const auth = require('../middleware/auth.middleware');
const { createCar, getCars, getCarById, updateCarPrice, deleteCar } = require ('../controllers/car.controller');

router.post('/', auth, createCar);
router.get('/', getCars);
router.get('/:car-id', getCarById);
router.patch('/:car-id', updateCarPrice);
router.delete('/:car-id', deleteCar);

module.exports = router;