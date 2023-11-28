import React from "react";
import "./BlogPost.css";

const BlogPost = ({ image, title, date, description }) => {
  return (
    <div className="blog-post">
      <img src={image} alt={title} className="post-image" />
      <div className="post-content">
        <h2>{title}</h2>
        <h3>{date}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
};

export default BlogPost;
