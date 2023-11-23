import React from "react";
import ContactCard from "./components/Contact";
import "./App.css";

const App = () => {
  const contactData = [
    {
      name: "Dr. Mubashar Mushtaq",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Dr-Mubashar-Mushtaq-scaled.jpg",
      phoneNumber: " EXT | 530 ",
      email: "mubasharmushtaq@fccollege.edu.pk",
    },
    {
      name: "Dr. Aasia Khanum",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Dr.-Aasia-Khanum-scaled.jpg",
      phoneNumber: "EXT | 508 ",
      email: "aasiakhanum@fccollege.edu.pk",
    },
    {
      name: "Dr. Maria Tamoor",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Maria-Tamoor-scaled.jpg",
      phoneNumber: "EXT | ",
      email: "mariatamoor@fccollege.edu.pk",
    },
    {
      name: "Dr. Sidra Minhas",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Sidra-Minhas-scaled.jpg",
      phoneNumber: "EXT | ",
      email: "sidraminhas@fccollege.edu.pk",
    },
    {
      name: "Muhammad Rauf Butt",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Muhammad-Rauf-Butt-scaled.jpg",
      phoneNumber: "EXT | ",
      email: "raufbutt@fccollege.edu.pk",
    },
    {
      name: "Muhammad Salman Chaudhry",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Muhammad-Salman-Chaudhry-scaled.jpg",
      phoneNumber: "EXT | ",
      email: "salmanchaudhry@fccollege.edu.pk",
    },
    {
      name: "Fakhir Shaheen",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Fakhir-Shaheen-scaled.jpg",
      phoneNumber: "EXT | ",
      email: "fakhirshaheen@fccollege.edu.pk",
    },
    {
      name: "Samia Asloob Qureshi",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Samia-Asloob-Qureshi-scaled.jpg",
      phoneNumber: "EXT | 612",
      email: "samiaqureshi@fccollege.edu.pk",
    },
    {
      name: "Rabranea Bqa",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/CS-Dep-Rabranea-scaled.jpg",
      phoneNumber: "EXT | 621",
      email: "rabraneabqa@fccollege.edu.pk",
    },
    {
      name: "Sharoon Nasim",
      image:
        "https://www.fccollege.edu.pk/wp-content/uploads/Mr.-Sharoon-Nasim-scaled.jpg",
      phoneNumber: "EXT | 624",
      email: "sharoonnasim@fccollege.edu.pk",
    },
  ];

  return (
    <div className="app">
      <h1>Contact Cards</h1>
      <div className="contact-container">
        {contactData.map((contact, index) => (
          <ContactCard
            key={index}
            image={contact.image}
            name={contact.name}
            phoneNumber={contact.phoneNumber}
            email={contact.email}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
