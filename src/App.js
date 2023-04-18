import React from 'react'
import './index.css';
import './App.css';


const Home = (props) => {
  return (
    <div className="home-container">

      <div className="home-container1">
        <h1 className="home-heading">CARDTRADE.IO</h1>
        <button name="LOGIN" type="submit" className="home-button button">
          login
        </button>
        <button name="LOGIN" type="submit" className="home-button1 button">
          view collection
        </button>
        <img
          alt="Card Preview"
          src="/playground_assets/card.io-1000w.png"
          className="home-image"
        />
      </div>
    </div>
  )
}

export default Home
