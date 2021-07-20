var password= document.getElementById('password')
var confirmpassword= document.getElementById('confirmpassword')
var safe;

setInterval(()=>{
    if(password.value===confirmpassword.value && password.value!=''){
        
        confirmpassword.classList.remove('taken')
        
    }
    else{
        if(confirmpassword.classList.contains('taken')){

        }
        else{
            confirmpassword.classList.add('taken')
        }
    }
},1000)
