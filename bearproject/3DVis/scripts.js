// script.js

// Set up scene, camera, and renderer  
const scene = new THREE.Scene();  
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);  
const renderer = new THREE.WebGLRenderer();  
renderer.setSize(window.innerWidth, window.innerHeight);  
document.body.appendChild(renderer.domElement);

// Function to create a cube (file/folder)  
function createBox(width, height, depth, color, name) {  
 const geometry = new THREE.BoxGeometry(width, height, depth);  
 const material = new THREE.MeshBasicMaterial({ color: color });  
 const box = new THREE.Mesh(geometry, material);

    // Position boxes
    scene.add(box);
    box.name = name;  // Assign a name to the box
    return box;

}

// Create some files and folders  
const folderColor = 0xadd8e6; // Light blue for folders  
const fileColor = 0xffffe0; // Light yellow for files  
const boxSize = { width: 1, height: 0.5, depth: 0.5 };

// Creating folders  
let folder1 = createBox(boxSize.width _ 2, boxSize.height _ 1, boxSize.depth, folderColor, "Folder 1");  
folder1.position.set(-2, 0, 0);

let folder2 = createBox(boxSize.width _ 2, boxSize.height _ 1, boxSize.depth, folderColor, "Folder 2");  
folder2.position.set(2, 0, 0);

// Creating files  
let file1 = createBox(boxSize.width, boxSize.height, boxSize.depth, fileColor, "File A");  
file1.position.set(-2, 1, 0);

let file2 = createBox(boxSize.width, boxSize.height, boxSize.depth, fileColor, "File B");  
file2.position.set(2, 1, 0);

let file3 = createBox(boxSize.width, boxSize.height, boxSize.depth, fileColor, "File C");  
file3.position.set(0, 1, -2);

// Add ambient light  
const light = new THREE.AmbientLight(0x404040); // soft white light  
scene.add(light);  
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);  
directionalLight.position.set(5, 5, 5).normalize();  
scene.add(directionalLight);

// Set camera position  
camera.position.z = 5;

// Animation loop  
function animate() {  
 requestAnimationFrame(animate);

    // Rotate the filing system for a dynamic effect
    scene.children.forEach(child => {
        if (child instanceof THREE.Mesh) {
            child.rotation.y += 0.01;
        }
    });

    // Render the scene
    renderer.render(scene, camera);

}

// Handle browser resizing  
window.addEventListener('resize', () => {  
 camera.aspect = window.innerWidth / window.innerHeight;  
 camera.updateProjectionMatrix();  
 renderer.setSize(window.innerWidth, window.innerHeight);  
});

// Start the animation  
animate();
