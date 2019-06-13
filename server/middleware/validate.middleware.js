const Joi = require('@hapi/joi');

signInValid = (data) => {
    const schema = {
        email: Joi.string().required().email(),
        password: Joi.string().required()
    };
    return Joi.validate(data, schema);
}

signUpValid = (data) => {
    const schema = {
        first_name: Joi.string().required(),
        last_name: Joi.string().required(),
        email: Joi.string().required().email(),
        password: Joi.string().required(),
        address: Joi.string().required(),
        is_admin: Joi.boolean().required()
    };
    return Joi.validate(data, schema);
}

postCarValid = (data) => {
    const schema = {
        owner: Joi.string().required(),
        state: Joi.string().required(),
        price: Joi.number().required(),
        manufacturer: Joi.string().required(),
        model: Joi.string().required(),
        body_type: Joi.string().required()
    }
    return Joi.validate(data, schema);
}

makeOrderValid = (data) => {
    const schema = {
        car_id: Joi.string().required(),
    }
    return Joi.validate(data, schema);
}

module.exports.signInValid = signInValid;
module.exports.signUpValid = signUpValid;
module.exports.postCarValid = postCarValid;
module.exports.makeOrderValid = makeOrderValid;