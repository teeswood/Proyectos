const mysql = require('mysql');
const { promisify } = require('util');

const { database } = require('./keys')

const pool = mysql.createPool(database);

pool.getConnection((err, connection) => {  if (err) (err.code === 'PROTOCOL_CONNECTION_LOST') 
{
    console.error('DATABASE CONNECTION WAS CLOSED');}  
    if (err.code === 'ER_CON_COUNT_ERROR') 
    {console.error('DATABASE HAS TO MANY CONNECTIONS');} 
    if (err.code === 'ECONREFUSED') 
    {console.error('DATABASE CONEXION WAS REFUSED');}
    if (connection) connection.release();console.log('DB IS CONNECTED'); return;});
//Convertir CALLBACKS EN PROMESAS
pool.query = promisify(pool.query);
module.exports = pool;