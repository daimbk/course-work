import React, { useState, useEffect } from "react";
import "./RandomQuote.css";

const RandomQuote = () => {
  const [quote, setQuote] = useState({});

  useEffect(() => {
    const fetchRandomQuote = async () => {
      try {
        const response = await fetch("https://api.quotable.io/random");
        const data = await response.json();
        setQuote(data);
      } catch (error) {
        console.error("Error fetching random quote:", error);
      }
    };

    fetchRandomQuote();

    const intervalId = setInterval(fetchRandomQuote, 10000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <h2>Random Quote:</h2>
      <blockquote>
        <p>{quote.content}</p>
        <footer>- {quote.author}</footer>
      </blockquote>
    </div>
  );
};

export default RandomQuote;
