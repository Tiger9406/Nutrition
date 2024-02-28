
import React, { useState } from 'react';

interface SearchBarProps {
    onSearch: (query: string) => void;
}

const SearchBar: React.FC<SearchBarProps> = ({ onSearch }) => {
    const [query, setQuery] = useState('');

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        onSearch(query);
    };

    return (
        <div className="flex items-center justify-center">
            <form onSubmit={handleSubmit}>
                <input className="border-2 border-gray-300 p-2 rounded-full"
                    type="text"
                    value={query}
                    onChange={handleChange}
                    placeholder="Ex: Vitamin B12..."
                />
                <button className="border-2 border-gray-300 p-2 rounded-full ml-3" type="submit">Search</button>
            </form>
        </div>
    );
};

export default SearchBar;