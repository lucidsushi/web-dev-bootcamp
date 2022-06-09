import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
    BrowserRouter,
} from "react-router-dom"

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path='/' element={<Page />} />
                    <Route path='/join' element={<RoomJoinPage />} />
                    <Route path='/create' element={<CreateRoomPage />} />
                </Routes>
            </Router>
        );
    }
}

function Page() {
    return <p>This is the Homepage!</p>
}