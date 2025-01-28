'use client'
import React, { useEffect, useState } from 'react'


const Register = ({...props}) => {

  const {loginOrRegister, setLoginOrRegister} = props

  const [data, setData] = useState({
    email:''
  })

  const currentDataF = (e:any)=>{
    setData(prev=>({...prev,[e.target.name]:e.target.value}))
  }


  const getOTP = async (e:any)=>{

    e.preventDefault()
        await fetch('http://127.0.0.1:8000/accounts/check-email',{
          method: 'post',
          body: JSON.stringify(data) ,
          headers:{
            "Content-Type": "application/json",
          }
        })
        .then(res=>res.json())
        .then(res=>{
     
          return res
        })
       
    }

 



    return (
      <form onSubmit={getOTP} className='w-full flex flex-col items-center justify-center  select-none '>
  
       
        <input className='w-full p-3 py-1 m-3 outline-none  flex items-center justify-center transition-all shadow shadow-slate-400' defaultValue='' onChange={currentDataF}  id='email' type="email" name='email' placeholder='user@mail.com' />
       <input type="submit" value="Get OTP" className={data.email.length<1? 'w-full px-3 py-1 m-3 rounded-lg flex items-center justify-center shadow shadow-slate-400 cursor-not-allowed ' : 'w-full px-3 py-1 m-3 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400  hover:scale-95 hover:shadow-none cursor-pointer'} disabled={data.email.length < 1  ? true: false}/>
  
  
      </form>
    )
  }
  
  export default Register