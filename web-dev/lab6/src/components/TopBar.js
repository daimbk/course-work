import React from "react";
import "./TopBar.css";

const TopBar = () => {
  return (
    <div className="top-bar">
      <nav>
        <div className="logo-title-container">
          <img src="assets/globe.png" alt="Logo" className="logo" />
          <h1 className="title">Travel Journal</h1>
        </div>
      </nav>
    </div>
  );
};

export default TopBar;
