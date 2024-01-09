import React from "react";
import "./Counter.css";

const Counter = () => {
  const [count, setCount] = React.useState(0);

  return (
    <div className="counter">
      <h1 className="counter">Count: {count}</h1>
      <button className="func" onClick={() => setCount(count + 1)}>
        Increment
      </button>
      <button className="func" onClick={() => setCount(count - 1)}>
        Decrement
      </button>
    </div>
  );
};

export default Counter;
