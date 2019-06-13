const uuid = require('uuid/v1');

class User {
    constructor(first_name, last_name, email, password, address, is_admin){
        this.id = uuid();
        this.first_name = first_name;
        this.last_name = last_name;
        this.email = email;
        this.password = password;
        this.address = address;
        this.is_admin = is_admin;
    }
}

let users = [];

module.exports.User = User;
module.exports.users = users;