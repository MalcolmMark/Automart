const uuid = require('uuid/v1');

class Order {
    constructor(buyer, car_id, amount, status){
        this.id = uuid();
        this.buyer = buyer; // user id
        this.car_id = car_id;
        this.amount = amount; // price offered
        this.status = status; // [pending, accepted, or rejected]
    }
}

let orders = [];

module.exports.Order = Order;
module.exports.orders = orders;