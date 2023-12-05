import React from "react";
import "./RemoveTodo.css";

const RemoveTodo = ({ todos, onRemoveTodo }) => {
  return (
    <div className="remove-todo-container">
      <h2>Todo List</h2>
      <ul className="remove-todo-list">
        {todos.map((todo, index) => (
          <li key={index} className="remove-todo-item">
            {todo}
            <button
              onClick={() => onRemoveTodo(index)}
              className="remove-todo-button"
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RemoveTodo;
