import React from "react";

interface TopBarProps {
    links: string[];
}
const TopBar: React.FC<TopBarProps> = ({ links }) => {
    return (
        <div className="top-0 left-0 w-full bg-gray-900 text-white p-4">
            <ul className="flex flex-row gap-2 color-black">
                {links.map((link, index) => (
                    <li key={index}>{link}</li>
                ))}
            </ul>
        </div>
    );
};

export default TopBar;
