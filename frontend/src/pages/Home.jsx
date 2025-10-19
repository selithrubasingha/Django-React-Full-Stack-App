import { useState, useEffect } from "react";
import api from "../api";
import Note from "../components/Note"
import "../styles/Home.css"

function Home() {
    //gotta initialize them variables amr
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");

    //when the cokmponent mounts run the. get notes function
    useEffect(() => {
        getNotes();
    }, []);

    const getNotes = () => {
        api
            .get("/api/notes/") //get's all the model data in this url
            .then((res) => res.data)//model is data let's say . then we target teh actual data using res.data
            .then((data) => {
                setNotes(data); //and then get that data and display them!
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    //to delete you gotta give the funtion a primary key or anything
    const deleteNote = (id) => {
        api
            .delete(`/api/notes/delete/${id}/`) //get the data from the url /
            //then the deletion automatically happens in django 'cause of the DestroyApiView
            .then((res) => { //the res returned is just a "did I do that ? or not ? kinda info"
                if (res.status === 204) alert("Note deleted!");
                else alert("Failed to delete note.");
                getNotes(); //once it is deleted call getNotes again 'cause the ntoes are updated now 
            })
            .catch((error) => alert(error));
    };

    const createNote = (e) => {
        e.preventDefault(); //this prevents reloading the page which webbrowser does sometimes , we don't need that
        api
            .post("/api/notes/", { content, title })
            .then((res) => {
                if (res.status === 201) alert("Note created!");//201 is the standard staus for "created"!
                else alert("Failed to make note.");
                getNotes();
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                <h2>Notes</h2>
                {notes.map((note) => ( //The legendary mapping technique of the sage of Code.
                    <Note note={note} onDelete={deleteNote} key={note.id} />
                ))}
            </div>
            <h2>Create a Note</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)} //this changes the title from "" to what's types                    value={title}
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}

export default Home;