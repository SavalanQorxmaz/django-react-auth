'use client'
import React, { useEffect, useState } from 'react'


const Login = ({...props}) => {

  const {loginOrRegister, setLoginOrRegister} = props

  const [loginData, setLoginData] = useState({
    userName:'',
    password:''
  })
  const [showPassword, setShowPassword] = useState(false)

  const currentLoginDataF = (e:any)=>{
    setLoginData(prev=>({...prev,[e.target.name]:e.target.value}))
  }

  const resetLoginDataF = ()=>{
    setLoginData({
      userName: '',
      password: ''
  })

  setShowPassword(false)
}

  const loginF = async (e:any)=>{

    e.preventDefault()
        await fetch('url',{
          method: 'post',
          body: JSON.stringify(loginData) ,
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
    <form onSubmit={loginF} className='w-full flex flex-col items-center justify-center  select-none '>

     
      <label htmlFor="user-name" className='w-full p-3 py-1 m-3 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400 cursor-pointer  '>
        <span className='w-1/3 text-right mr-3 text-xs'>User Name:</span>
      <input defaultValue='' onChange={currentLoginDataF} className='w-2/3 outline-none p-1 bg-inherit' id='user-name' type="text" name='userName' placeholder='Filankes' />
      </label>
     <p className={loginData.userName.length <1 ? 'w-full p-3 py-1 mb-3  text-center  text-red-400  text-xs ': 'hidden'}>Istifadeci adi daxil et</p>
     <label htmlFor="password" className='w-full p-3 py-1 m-3 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400 cursor-pointer  '>
      <span className='w-1/3 text-right mr-3 text-xs'>Parol:</span>
     <input defaultValue='' onChange={currentLoginDataF} className='w-2/3 outline-none p-1 bg-inherit' id='password' name='password' type={showPassword?'text': 'password'} placeholder='********' />
     {
    showPassword
    ?
    
   <button onClick={()=>setShowPassword(false)}>Hide</button>
   :
   <button onClick={()=>setShowPassword(true)}>Show</button>

   }
     </label>
     <p className={loginData.password.length<1 ? 'w-full p-3 py-1 mb-3  text-center  text-red-400  text-xs ': 'hidden'}>Parolu daxil et</p>
     <input type="submit" value="Login" className={loginData.userName.length<1 || loginData.password.length<1? 'w-full px-3 py-1 m-3 rounded-lg flex items-center justify-center shadow shadow-slate-400 cursor-not-allowed ' : 'w-full px-3 py-1 m-3 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400  hover:scale-95 hover:shadow-none cursor-pointer'} disabled={loginData.userName.length<1 || loginData.password.length<1 ? true: false}/>

     <div className='w-full p-3 py-1 m-3 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400 '>

      <input type="reset" value="Clean" className='w-1/2 text-center m-2 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400 cursor-pointer hover:scale-95 hover:shadow-none '/>
     <input onClick={()=>setLoginOrRegister('register')} type="button" value="SignUp" className='w-1/2 text-center m-2 rounded-lg flex items-center justify-center transition-all shadow shadow-slate-400 cursor-pointer hover:scale-95 hover:shadow-none '/>

     </div>

    </form>
  )
}

export default Login