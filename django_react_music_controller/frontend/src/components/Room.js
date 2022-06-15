import React, { Component } from "react";
import { useParams } from "react-router-dom";



// https://reactrouter.com/docs/en/v6/getting-started/tutorial#reading-url-params
const Room = (props) => {
    const intialState = {
        votesToSkip: 2,
        guestCanPause: false,
        isHost: false,
    };
    const [state, setState] = React.useState(intialState);
    let { roomCode } = useParams();

    // is this even working?
    const getRoomDetails = () => {
        // fetch(`/api/room/${roomCode}`)
        fetch(`/api/get-room/?code=${roomCode}`)
            .then(response => response.json())
            .then(data => {
                setState({
                    votesToSkip: data.votes_to_skip,
                    guestCanPause: data.guest_can_pause,
                    isHost: data.is_host,
                });
            });
    }
    getRoomDetails();

    return (
        <div>
            <h3>Room: {roomCode}</h3>
            <p>Votes: {state.votesToSkip}</p>
            <p>Guest Can Pause: {state.guestCanPause.toString()}</p>
            <p>Is Host: {state.isHost.toString()}</p>
        </div>
    );
}

export default Room;
// https://stackoverflow.com/questions/69967745/react-router-v6-access-a-url-parameter

// export default class Room extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             votesToSkip: 1,
//             guestCanPause: false,
//             isHost: false,
//         };
//         this.roomCode = this.props.match.params.roomCode; // https://v5.reactrouter.com/web/api/match
//     }

//     render() {
//         return (
//             <div>
//                 <h3>Room: {this.roomCode}</h3>
//                 <p>Votes: {this.state.votesToSkip}</p>
//                 <p>Guest Can Pause: {this.state.guestCanPause}</p>
//                 <p>Is Host: {this.state.isHost}</p>
//             </div>
//         );
//     }
// }
