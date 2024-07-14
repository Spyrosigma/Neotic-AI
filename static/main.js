import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.outputColorSpace = THREE.SRGBColorSpace;

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x000000, 1);
renderer.setPixelRatio(window.devicePixelRatio);

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 2000);
camera.position.set(0, 0, 10);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.enablePan = false;
controls.minDistance = 3.5;
controls.maxDistance = 25;
controls.minPolarAngle = 0.5;
controls.maxPolarAngle = 1.6;
controls.autoRotate = false;
controls.autoRotateSpeed = 10.5;
controls.target = new THREE.Vector3(0, 2.35, 0);
controls.update();

const groundGeometry = new THREE.PlaneGeometry(20, 20, 32, 32);
groundGeometry.rotateX(-Math.PI / 2);
const groundMaterial = new THREE.MeshStandardMaterial({
  color: 0x00000,
  side: THREE.DoubleSide
});

const groundMesh = new THREE.Mesh(groundGeometry, groundMaterial);
groundMesh.castShadow = false;
groundMesh.receiveShadow = true;
scene.add(groundMesh);

const spotLight = new THREE.SpotLight(0xffffff, 8000, 5000, 0.15, 1.56);
spotLight.position.set(0, 25, 20);
spotLight.castShadow = true;
spotLight.shadow.bias = -0.0001;
scene.add(spotLight);


const spotLight2 = new THREE.SpotLight(0xffffff, 1000, 5000, 0.15, 1.56);
spotLight2.position.set(10, 15, 10);
spotLight2.castShadow = true;
spotLight2.shadow.bias = -0.0001;
scene.add(spotLight2);

const spotLight3 = new THREE.SpotLight(0xffffff, 1000, 5000, 0.15, 1.56);
spotLight3.position.set(-10, 15, 10);
spotLight3.castShadow = false;
spotLight3.shadow.bias = -0.0001;
scene.add(spotLight3);


const loader = new GLTFLoader().setPath('./static/harry_potter/');
loader.load('scene.gltf', (gltf) => {
  console.log('loading model');
  const mesh = gltf.scene;

  mesh.traverse((child) => {
    if (child.isMesh) {
      child.castShadow = true;
      child.receiveShadow = true;
    }
  });

  mesh.position.set(0, 0.4, 1.5);
  scene.add(mesh);

  document.getElementById('progress-container').style.display = 'auto' ;
}, (xhr) => {
  console.log(`loading ${xhr.loaded / xhr.total * 100}%`);
}, (error) => {
  console.error(error);
});

// window.addEventListener('resize', () => {
//   camera.aspect = window.innerWidth / window.innerHeight;
//   camera.updateProjectionMatrix();
//   renderer.setSize(window.innerWidth, window.innerHeight);
// });

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

animate();