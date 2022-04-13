import axios from 'axios';
import React from 'react';

function UserItem(props) {
    const deleteUserHandler = (nombre) => {
        console.log(nombre);
        axios.delete(`http://localhost:8000/api/todo/${nombre}`)
            .then(res => console.log(res.data))
    }
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.user.nombre} : </span> {props.user.correo}
                <button onClick={() => deleteUserHandler(props.user.nombre)} className="btn btn-outline-danger my-2 mx-2" style={{ 'borderRadius': '50px', }}>x</button>
                <hr></hr>
            </p>
        </div>
    )
}
export default UserItem;