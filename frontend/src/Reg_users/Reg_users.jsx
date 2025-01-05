import axios from 'axios'
import { useEffect, useState } from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import Cards from '../Cards/Cards.jsx'
import './Reg_users.css'

const Reg_users=()=>{
    const path=useLocation()
    const loc=path.pathname

    const [data,setData]=useState([])

    useEffect(()=>{

        const fetchdata=async ()=> {
            try{
            const response=await axios.get("http://127.0.0.1:8000/reg_users/")
            if (response.data){
                setData(response.data)
                console.log("data fetched",data)
            }
        }catch(error){
            console.log("failed to fetch data ",error)
        }
        }

        fetchdata()
    },[])


    return(
        <div className='Reg-users-main'>
            <div className='cards-container'>

                {data.map((user,index)=>(
                    <Cards key={index} user={user} />
                ))}

            </div>

            <nav>
                {loc==='/reg_users' && <NavLink to='/' style={{color:'green'}}>Home</NavLink>}
            </nav>

        </div>
    )
}

export default Reg_users