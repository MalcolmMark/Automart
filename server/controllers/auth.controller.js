const { User, users } = require('../models/user.model');
const { signInValid, signUpValid } = require('../middleware/validate.middleware');

signIn = (req, res) => {
    console.log(req.body);
    const { error } = signInValid(req.body);
    if (error) {
        return res.status(404).send({
            'status': 404,
            'message': error.details[0].message
        });
    }
    
    const user_data = {
        'email': req.body.email,
        'password' : req.body.password
    }

    if(users.find(u => u.email == user_data.email && u.password == user_data.password)){
        res.send('successfully signed in')
        return;
    }
    res.send('user with this email or password does not exist');
};


signUp = (req, res) => {
    const { error } = signUpValid(req.body);
    if (error) {
        return res.status(404).send({
            'status': 404,
            'message': error.details[0].message
        });
    }
    const user = new User(
        req.body.first_name,
        req.body.last_name,
        req.body.email,
        req.body.password,
        req.body.address,
        req.body.is_admin
    );

    users.push(user);

    res.status(201).send({
        'status':res.statusCode,
        'message': users.length > 0 ? 'User is created' : 'Failed to create user',
    });

};


module.exports.signIn = signIn;
module.exports.signUp = signUp;