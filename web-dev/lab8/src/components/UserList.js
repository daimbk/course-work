import React, { useState, useEffect } from "react";
import "./UserList.css";

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [filter, setFilter] = useState("");

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/users"
        );
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    };

    fetchUsers();
  }, []);

  const handleFilterChange = (event) => {
    setFilter(event.target.value);
  };

  const filteredUsers = users.filter((user) =>
    user.company.name.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div className="user-list-container">
      <label htmlFor="filterInput">Filter by Company Name:</label>
      <input
        type="text"
        id="filterInput"
        value={filter}
        onChange={handleFilterChange}
        placeholder="Enter company name"
      />

      <ul>
        {filteredUsers.map((user) => (
          <li key={user.id}>
            {user.name} - {user.company.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
