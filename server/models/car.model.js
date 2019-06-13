const uuid = require('uuid/v1');

class Car {
    constructor(owner, state, price, manufacturer, model, body_type){
        this.id = uuid(),
        this.owner = owner; // user id
        this.created_on = Date.now();
        this.state = state; // new,used
        this.status = 'available'; // sold, available - default is available
        this.price = price;
        this.manufacturer = manufacturer;
        this.model = model;
        this.body_type = body_type;
    }
}

let cars = [];

module.exports.Car = Car;
module.exports.cars = cars;