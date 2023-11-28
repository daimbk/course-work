import React from "react";
import TopBar from "./components/TopBar";
import BlogPost from "./components/BlogPost";

function App() {
  return (
    <div className="app">
      <TopBar />

      <BlogPost
        image="assets/fuji.jpg"
        title="Mount Fuji"
        date="2 January 2022 - 18 January 2022"
        description="Mount Fuji, located in Japan, is an iconic stratovolcano and the country's highest peak. Revered for its symmetrical cone shape, it is a UNESCO World Heritage Site and a symbol of Japanese culture. Mount Fuji attracts hikers, climbers, and tourists, offering breathtaking views of its surroundings, especially during the cherry blossom season."
      />

      <BlogPost
        image="assets/aurora.jpg"
        title="Icelandic Aurora Borealis"
        date="2 April 2022 - 5 April 2022"
        description="The Icelandic Aurora Borealis, or Northern Lights, is a celestial light display that graces the night skies near the Earth's polar regions, including Iceland. This natural phenomenon occurs when charged particles from the sun interact with the Earth's magnetic field, producing vibrant hues of green, pink, and purple across the Arctic heavens. Iceland's minimal light pollution makes it an ideal destination for experiencing this captivating light show."
      />

      <BlogPost
        image="assets/pyramid.jpg"
        title="Great Pyramid of Giza"
        date="19 April 2023 - 28 May 2023"
        description="The Great Pyramid of Giza, located on the outskirts of Cairo, Egypt, is one of the Seven Wonders of the Ancient World. Built for Pharaoh Khufu, this colossal structure is the largest of the three pyramids on the Giza Plateau. Constructed around 2560 BCE, the pyramid is an architectural marvel, and its precision in design and alignment continues to intrigue scholars. The Great Pyramid stands as a testament to the engineering prowess of ancient civilizations."
      />
    </div>
  );
}

export default App;
