import React from "react";
import "./Contact.css";

const ContactCard = ({ image, name, phoneNumber, email }) => {
  return (
    <div className="contact-card">
      <img src={image} alt={`${name}'s profile`} className="contact-image" />
      <div className="contact-details">
        <h2 className="contact-name">{name}</h2>
        <div className="info">
          <img
            src="https://w7.pngwing.com/pngs/421/683/png-transparent-computer-icons-mobile-phones-telephone-email-home-business-phones-phone-icon-miscellaneous-angle-service-thumbnail.png"
            alt="Phone Logo"
            className="phone-logo"
          />
          <p className="contact-info">{phoneNumber}</p>
        </div>
        <div className="info">
          <img
            src="https://png.pngtree.com/png-vector/20201109/ourmid/pngtree-email-icon-design-png-image_2413695.jpg"
            alt="Email Logo"
            className="email-logo"
          />
          <p className="contact-info">{email}</p>
        </div>
      </div>
    </div>
  );
};

export default ContactCard;
