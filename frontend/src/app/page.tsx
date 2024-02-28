"use client"

import React from "react";
import TopBar from "./components/top-bar";
import SearchBar from "./components/search-bar";
import './globals.css';

export default function Home() {
  const handleSearch = (query: string) => {
    //search function
    console.log("Search query:", query);
  };
  return (
    <div className="page">
      <TopBar links={["Home", "About", "Contact", "Log In"]} />
      <div className="flex items-center justify-center w-full">
        {/* <SideBar links={["Home", "About", "Contact"]} /> */}
        <div className="bg-[url('./../../public/white.avif')] bg-cover bg-center bg-no-repeat 
                        flex flex-col items-center gap-5 h-screen w-full">
          <h1 className="text-9xl font-bold mt-16">Nutrition</h1>
          <p className="text-3xl font-light"> Let's find some nutritious foods.</p>
          <SearchBar onSearch={handleSearch} />
        </div>
      </div>
      <div className="flex flex-col items-center justify-center">
        <h2 className="text-6xl font-bold m-6">Blog Area</h2>
        <div className="flex gap-5 flex-wrap justify-around">
          <p>Blog post 1</p>
          <p>Blog post 2</p>
          <p>Blog post 3</p>
          
        </div>
      </div>
    </div>
  );
}
