import React, { Component } from 'react';
import { render } from 'react-dom';
import HomePage from './HomePage';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <HomePage />
            </div>

        );
        // return <h1>Testing React</h1>;
        // return <h1>Testing React Code: {this.props.name}</h1>;
    }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);
// render(<App name="this is a prop" />, appDiv);
