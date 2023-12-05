import React, { useState } from "react";
import AddTodo from "./AddTodo";
import RemoveTodo from "./RemoveTodo";

const TodoApp = () => {
  const [todos, setTodos] = useState([]);

  const handleAddTodo = (newTodo) => {
    setTodos([...todos, newTodo]);
  };

  const handleRemoveTodo = (index) => {
    const updatedTodos = [...todos];
    updatedTodos.splice(index, 1);
    setTodos(updatedTodos);
  };

  return (
    <div>
      <AddTodo onAddTodo={handleAddTodo} />
      <RemoveTodo todos={todos} onRemoveTodo={handleRemoveTodo} />
    </div>
  );
};

export default TodoApp;
