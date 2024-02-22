import React from "react";
import TopBar from "./components/top-bar";
import SideBar from "./components/side-bar";

export default function Home() {
  return (
    <div className="page">
      <TopBar links={["Home", "About", "Contact"]} />
      <div className="flex gap-3">
        <SideBar links={["Home", "About", "Contact"]} />
        <div className="main-content mt-3">
          <h1>Nutrition</h1>
          <p>Let's find some nutritious foods.</p>
        </div>
      </div>
    </div>
  );
}
