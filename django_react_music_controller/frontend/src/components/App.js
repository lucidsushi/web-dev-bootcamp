import React, { Component } from 'react';
// import { render } from 'react-dom';
import { createRoot } from 'react-dom/client';

import HomePage from './HomePage';

export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div className='center'>
                <HomePage />
            </div>

        );
        // return <h1>Testing React Code: {this.props.name}</h1>;
    }
}

const appDiv = document.getElementById('app');
const root = createRoot(appDiv);
root.render(<App />);
// https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html#updates-to-client-rendering-apis
// render(<App />, appDiv);
// render(<App name="this is a prop" />, appDiv);
