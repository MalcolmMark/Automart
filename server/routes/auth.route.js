const router = require('express').Router();
const auth = require('../middleware/auth.middleware');
const { signIn, signUp } = require('../controllers/auth.controller');

router.post('/signin', signIn);

router.post('/signup', signUp);

module.exports = router;