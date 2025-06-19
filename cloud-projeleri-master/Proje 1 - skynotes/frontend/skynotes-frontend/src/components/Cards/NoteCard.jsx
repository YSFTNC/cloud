import React from "react";
import { MdOutlinePushPin } from "react-icons/md";
import { MdCreate, MdDelete } from "react-icons/md";
import moment from "moment";

const NoteCard = ({
  title,
  date,
  content,
  tags,
  isPinned,
  onEdit,
  onDelete,
  onPinNote,
}) => {
  return (
    // <div className="max-w-md mx-auto border rounded p-4 bg-white hover:shadow-xl transition-all ease-in-out">
    <div className="border-gray-300 border-solid border-1 rounded-lg p-4 bg-gray-50 hover:shadow-xl transition-all ease-in-out">
      <div className="flex items-center justify-between">
        <div>
          <h6 className="text-sm font-medium break-all">{title}</h6>
          <span className="text-xs text-slate-500">
            {moment(date).format("DD MMM YYYY")}
          </span>
        </div>

        <MdOutlinePushPin
          className={`icon-btn ${isPinned ? "text-primary" : "text-slate-300"}`}
          onClick={onPinNote}
        />
      </div>

      <p className="text-xs text-slate-600 mt-2 break-words">
        {content?.slice(0, 60)}
      </p>

      <div className="flex items-center justify-between mt-2">
        <div className="text-xs text-slate-500 break-all max-w-[70%]">
          {tags.map((item, index) => (
            <span key={index} className="mr-1">
              #{item}
            </span>
          ))}
        </div>

        <div className="flex items-center gap-2">
          <MdCreate
            className="icon-btn text-slate-300 hover:text-green-600"
            onClick={onEdit}
          />
          <MdDelete
            className="icon-btn text-slate-300 hover:text-red-500"
            onClick={onDelete}
          />
        </div>
      </div>
    </div>
  );
};

export default NoteCard;
