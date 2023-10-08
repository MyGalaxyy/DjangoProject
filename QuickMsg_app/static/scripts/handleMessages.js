
  const successmessage = document.getElementById('success-message')
setTimeout(()=>{

  if (successmessage){
    successmessage.remove()
  }

},2000);


const errormessage = document.getElementById('error-message')
setTimeout(()=>{
    
    if (errormessage){
        errormessage.remove()
    }
},2000);