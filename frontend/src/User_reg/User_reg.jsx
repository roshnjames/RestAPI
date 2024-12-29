import React from 'react';
import './User_reg.css';

const User_reg = () => {



  const handleData=(e)=>{
    e.preventDefault();
    let user={
      'name':document.getElementById('name').value,
      'username':document.getElementById('username').value,
      'email':document.getElementById('email').value,
      'pswd1':document.getElementById('pswd1').value,
      'pswd2':document.getElementById('pswd2').value,
      }
    const verfication=validateData(user)
    if (verfication===true){
      //api call code
    }
  }

const validateData=(user)=>{
  if (user.pswd1!==user.pswd2){
    alert("passwords doesn't match!")
    document.getElementById('pswd1').focus()
    return false
  }else{
    return true
  }
}


  return (
    <div className='User-reg-main-div'>

        <div className='User-reg-form-header'>
            Register here!
        </div>
        <form className="User-reg-form" method='post' onSubmit={(e)=>handleData(e)} >
          <input type='text' id='name' placeholder='Enter your name' required/><br/>
          <input type='text' id='username' placeholder='Username' required/><br/>
          <input type='file' id='profile' placeholder='Upload Your Image'required/><br/>
          <input type='email' id='email' placeholder='Email id' required/><br/>
          <input type='password' id='pswd1' placeholder='Password' required/><br/>
          <input type='password' id='pswd2' placeholder='Confirm Password' required/><br/>
          <div className='buttons-div'>
          <button type='reset' className='submit-button' >Reset</button>
          <button type='submit' className='submit-button' >Register</button>
          </div>
        </form>
    </div>
  )
}

export default User_reg
