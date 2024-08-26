<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Temp Migration Project
=======
# Psychic Octo Project
## Branches
- `main`: Core functionality and overall project management.
- `api1-integration`: Integration for API 1.
- `api2-integration`: Integration for API 2.

## Directory Structure
- `core/`: Contains the core functionalities of the project.
- `api1/`: API 1 integration scripts and documentation.
- `api2/`: API 2 integration scripts and documentation.
- `docs/`: Project documentation.
- `scripts/`: Utility scripts for various tasks.
>>>>>>> d8b6257bbd32faab45e57b73576fe24ec71b20cc
=======
# Psychic-Octo Project

## Project Structure

/psychic-octo-backend
├── keymate
│   ├── keymate_test.py
│   ├── .env
├── README.md
├── other_project_files…
## KeyMate Integration

### Setup

1. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Environment Variables:**
    - Create a `.env` file in the `keymate` directory.
    - Add the following line to `.env`:
        ```
        API_KEY=your_api_key_here
        ```

### Running the Script

1. **Navigate to the `keymate` directory:**
    ```bash
    cd /Users/bear/psychic-octo-backend/keymate
    ```

2. **Run the script:**
    ```bash
    python keymate_test.py
    ```

### Additional Information

- For any issues or further developments, refer to the project documentation and maintain proper version control.
>>>>>>> 5bb1c20 (Added KeyMate integration script and documentation)
=======
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from 'eslint-plugin-react'

export default tseslint.config({
  // Set the react version
  settings: { react: { version: '18.3' } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs['jsx-runtime'].rules,
  },
})
```
>>>>>>> 6d322ea (Initial commit)
