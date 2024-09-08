import React from 'react';
import fs from 'fs';
import path from 'path';

export default function HomePage({ images }) {
  return (
    <div style={{ textAlign: 'center', marginTop: '100px' }}>
      {images.length > 0 ? (
        <div>
          <h1>Our Gallery</h1>
          <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', flexWrap: 'wrap' }}>
            {images.map((image, index) => (
              <img
                key={index}
                src={`/images/${image}`}
                alt="Gallery Image"
                style={{ width: '200px', height: 'auto', borderRadius: '10px' }}
              />
            ))}
          </div>
        </div>
      ) : (
        <div>
          <h1>Coming Soon!</h1>
          <p>Our site is currently under construction. Stay tuned for more updates!</p>
        </div>
      )}
    </div>
  );
}

// Fetching the list of images from the folder
export async function getServerSideProps() {
  const imageDirectory = path.join(process.cwd(), 'public/images');
  let images = [];

  // Check if the images directory exists
  if (fs.existsSync(imageDirectory)) {
    images = fs.readdirSync(imageDirectory).filter((file) => {
      return /\.(png|jpg|jpeg|gif)$/.test(file); // Only include image files
    });
  }

  return {
    props: {
      images,
    },
  };
}