import React from "react";
import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[#fdfdff] font-sans">
      <nav className="absolute top-0 w-full bg-[#2b85ff] py-4 text-white text-center">
        <h2>SkyNotes</h2>
      </nav>
      <div className="bg-white p-8 rounded-lg shadow-lg text-center">
        <h1 className="text-4xl text-[#ef863e] mb-4">404 - Page Not Found</h1>
        <p className="text-lg text-gray-600 mb-6">
          The page you are looking for does not exist.
        </p>
        <Link to="/" className="text-[#2b85ff] underline text-lg">
          Return to Home
        </Link>
      </div>
    </div>
  );
};

export default NotFound;
