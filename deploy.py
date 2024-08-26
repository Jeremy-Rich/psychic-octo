#!/bin/bash

# Navigate to the project directory
cd /Users/jbear/my-project

# Resolve merge conflicts by accepting the current changes
git add README.md eslint.config.js package-lock.json package.json

# Commit the changes
git commit -m "Resolve merge conflicts"

# Pull the latest changes
git pull origin main --rebase

# Install dependencies
npm install

# Build and run the project
npm run build
npm run dev

# Deploy the project to Vercel
vercel --prod
