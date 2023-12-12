import React from "react";
import UserList from "./components/UserList";
import RandomQuote from "./components/RandomQuote";
import "./App.css";

function App() {
  return (
    <div>
      <h1>User List App</h1>
      <UserList />
      <RandomQuote />
    </div>
  );
}

export default App;
