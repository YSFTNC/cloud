import React, { useCallback, useRef } from "react";
import { FaMagnifyingGlass } from "react-icons/fa6";
import { IoMdClose } from "react-icons/io";

const SearchBar = ({ value, onChange, handleSearch, onClearSearch }) => {
  const debounceTimeoutRef = useRef(null);

  const handleInputChange = (e) => {
    const newValue = e.target.value;

    onChange(e);

    if (newValue.trim() === "") {
      onClearSearch();
      if (debounceTimeoutRef.current) {
        clearTimeout(debounceTimeoutRef.current);
      }
      return;
    }

    if (debounceTimeoutRef.current) {
      clearTimeout(debounceTimeoutRef.current);
    }

    debounceTimeoutRef.current = setTimeout(() => {
      handleSearch();
    }, 500);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      if (debounceTimeoutRef.current) {
        clearTimeout(debounceTimeoutRef.current);
      }
      handleSearch();
    }
  };

  return (
    <div className="w-80 flex items-center px-4 bg-slate-100 rounded-full">
      <input
        type="text"
        placeholder="Search notes"
        className="w-full text-xs bg-transparent py-[11px] outline-none"
        value={value}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
      />

      {value && (
        <IoMdClose
          className="text-xl text-slate-500 cursor-pointer hover:text-black mr-3"
          onClick={onClearSearch}
        />
      )}

      <FaMagnifyingGlass
        className="text-slate-400 cursor-pointer hover:text-black"
        onClick={handleSearch}
      />
    </div>
  );
};

export default SearchBar;
