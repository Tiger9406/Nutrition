import React from "react";

interface TopBarProps {
    links: string[];
}
const TopBar: React.FC<TopBarProps> = ({ links }) => {
    return (
        <div className="top-0 left-0 w-full bg-gray-900 text-white p-4 flex flex-row justify-between">
            <div>
                <h1>Logo</h1>
            </div>
            <ul className="flex flex-row gap-4 color-black">
                {links.map((link, index) => (
                    <li key={index}>{link}</li>
                ))}
            </ul>
        </div>
    );
};

export default TopBar;
