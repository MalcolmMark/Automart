
module.exports = (req, res, next) => {
    if (!req.header('token')) {
        return res.status(401).send({
            'status': 401,
            'message': 'Signin first'
        });
    }

    try {
        const ver_token = jwt.verify(req.header('token'), 'hjhuihadhuhjsdhu');
        req.user = {
            'email': ver_token.email,
            'token': ver_token
        }

        next();
    } catch (error) {
        res.status(400).send({
            'status': 400,
            'message': 'Invalid token'
        });
    }
}
