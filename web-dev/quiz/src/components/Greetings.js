import React from "react";
import "./Greetings.css";

const Greetings = ({ name }) => {
  return <h1 className="greetings">Greetings {name}</h1>;
};

export default Greetings;
