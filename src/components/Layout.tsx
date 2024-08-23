import React from 'react';
import { Link } from 'react-router-dom';

const Layout: React.FC = ({ children }) => {
  return (
    <div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/stories">Stories</Link></li>
          <li><Link to="/submit-story">Submit Your Story</Link></li>
          <li><Link to="/about-us">About Us</Link></li>
          <li><Link to="/resources">Resources</Link></li>
          <li><Link to="/contact-us">Contact Us</Link></li>
        </ul>
      </nav>
      <main>{children}</main>
      <footer>
        <p>© 2024 Your Website Name. All rights reserved.</p>
      </footer>
    </div>
  );
};

