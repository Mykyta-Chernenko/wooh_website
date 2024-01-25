// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAbGuf-qffploA92w-q8yShjwW6whQXIx0",
  authDomain: "wooh.app",
  projectId: "friending-web",
  storageBucket: "friending-web.appspot.com",
  messagingSenderId: "301794036815",
  appId: "1:301794036815:web:11092f1566d979665eae3a",
  measurementId: "G-EZ5BD036RJ",
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);

// Initialize Firebase Authentication and get a reference to the service
export const auth = getAuth(app);

export const db = getFirestore(app);
