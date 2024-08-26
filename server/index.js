import dotenv from 'dotenv';
import express from 'express';
import cors from 'cors';

// Import the MongoDB connection
import './mongodbConnection.js';  // Ensure the .js extension

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5001;

app.use(cors());
app.use(express.json());

// Basic route for testing
app.get('/', (req, res) => {
  res.send('Server is running');
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
