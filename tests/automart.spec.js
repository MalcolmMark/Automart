const app = require("../server/index")

const chai = require("chai")

const chaiHttp = require("chai-http")

const {
    expect
} = chai;

chai.use(chaiHttp)

const signupUrl = '/api/v1/auth/signup'
const regData = {
    "first_name": "Malcolm",
    "last_name": "Mark",
    "email": "malcolmmarkokabo@gmail.com",
    "password": "123456",
    "address": "Kigali",
    "is_admin": false
}
const regData2 = {
    "first_name": "Malcolm",
    "last_name": "Mark",
    "email": "malcolmmarkokabo@gmail.com",
    "password": "123456",
    "address": "Kigali",
    "is_admin": false
}
const regData_valid1 = {
    "last_name": "Mark",
    "email": "malcolmmarkokabo@gmail.com",
    "password": "123456",
    "address": "Kigali",
    "is_admin": false
}

describe('main', ()=>{
    it("should return 201 if the request was completed successfully", ()=>{
        chai.request(app).post(signupUrl).send(regData).end((err, res) =>{
            expect(res.status).to.eq(201)
        });
    })
    it("should return 404 for missing fields", ()=>{
        chai.request(app).post(signupUrl).send(regData_valid1).end((err, res) =>{
            expect(res.status).to.eq(404)
        });
    })
    it("should return 404 for missing fields", ()=>{
        chai.request(app).post(signupUrl).send(regData_valid1).end((err, res) =>{
            expect(res.status).to.eq(404)
        });
    })
    it("should return 409 for already existing email", ()=>{
        chai.request(app).post(signupUrl).send(regData)
        chai.request(app).post(signupUrl).send(regData).end((err, res) =>{
            console.log(res.body);   
        });
    })
})