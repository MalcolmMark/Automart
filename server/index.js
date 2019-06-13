const express = require('express');

const auth_routes = require('./routes/auth.route');
const order_routes = require('./routes/order.route');
const car_routes = require('./routes/car.route');


const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.json());

app.use('/api/v1/auth', auth_routes);
app.use('/api/v1/order', order_routes);
app.use('/api/v1/car', car_routes);


app.listen(PORT, () => {
    console.log(`Server is running on PORT ${PORT}`);
});