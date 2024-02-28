import React from 'react';

interface SideBarProps {
  links: string[];
}

const SideBar: React.FC<SideBarProps> = ({ links }) => {
  return (
    <div className="left-0 w-16 bg-gray-800 text-white p-4">
      <ul>
        {links.map((link, index) => (
          <li key={index}>{link}</li>
        ))}
      </ul>
    </div>
  );
};

export default SideBar;
