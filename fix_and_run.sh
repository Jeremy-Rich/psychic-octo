#!/bin/bash

# Fix invalid package name
sed -i '' 's/"_globals":/"globals":/' package.json

# Fix TypeScript Errors
cat <<EOF > src/components/Layout.tsx
import React from 'react';

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <div>{children}</div>;
};

export default Layout;
EOF

# Replace `Switch` with `Routes` in App.tsx
sed -i '' 's/Switch/Routes/' src/App.tsx
sed -i '' 's/component=/element=/' src/App.tsx

# Ensure file case consistency
mv src/pages/HomePage.tsx src/pages/Homepage.tsx

# Install and build
npm install
npm run build
npm run dev
