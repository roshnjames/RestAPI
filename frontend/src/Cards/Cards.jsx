import './Cards.css'

import React from 'react'

const Cards = (props) => {
  console.log(props.user.profile)
  return (
    <div className='cards-main' key={props.index}>
      <div className="profile" style={{ backgroundImage:`url(${props.user.profile})` }}/>
      <div className="cards-text">
        <ul>
          <li><span><i>Name :</i></span><span>{props.user.name}</span></li>
          <li><span><i>Username :</i></span><span>{props.user.username}</span></li>
          <li><span><i>Email :</i></span><span>{props.user.email}</span></li>
        </ul>
      </div>
      
    </div>
  )
}

export default Cards
