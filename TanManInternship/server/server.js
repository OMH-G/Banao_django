const express = require('express')
const request = require('request');
const mysql=require('mysql')
let connection=mysql.createConnection({
  user:'root',
  password:'password',
  database:'tanmanfoundation',
  host:'localhost'
})
app = express();
const PORT = 3000;
resa=[]
function setValue(a){
resa=a
}
let user=''
let pass=''
let verify=false;
app.get('/check/:u/:p', function(req, res) {
  user=req.params.u ;
  pass=req.params.p;
  connection.query('SELECT * FROM details',(ex,rows)=>{
    if(ex) throw ex ;
    setValue(rows)
    dosomething();
  })
  if(verify===true){
    res.send([req.params.u,req.params.p])
    verify=false;
  }
  else{
    res.send('No')
  }
});
function dosomething(){
  for(let i=0;i<resa.length;i++){
    if(resa[i]['email']===user && resa[i]['password']===pass){
      verify=true;
    }
  }
}
app.listen(PORT, function (){ 
    console.log('Listening on Port 3000');
    connection.end();
});