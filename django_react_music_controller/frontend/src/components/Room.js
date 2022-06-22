import React, { Component } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Grid, Button, Typography } from "@material-ui/core";


// https://reactrouter.com/docs/en/v6/getting-started/tutorial#reading-url-params
const Room = (props) => {
    const intialState = {
        votesToSkip: 2,
        guestCanPause: false,
        isHost: false,
    };
    const [state, setState] = React.useState(intialState);
    let navigate = useNavigate();
    let { roomCode } = useParams();

    React.useEffect(() => {
        fetch(`/api/get-room?code=${roomCode}`)
            .then(response => {
                if (!response.ok) {
                    props.clearRoomCodeCallback(); // clears roomCode state in HomePage
                    navigate("/");
                } else {
                    return response.json();
                }
            })
            .then(data => {
                setState({
                    votesToSkip: data.votes_to_skip,
                    guestCanPause: data.guest_can_pause,
                    isHost: data.is_host,
                });
            });
    }, []);

    const leaveButtonPressed = () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        };
        fetch(`/api/leave-room`, requestOptions)
            .then(_response => {
                props.clearRoomCodeCallback(); // clears roomCode state in HomePage
                navigate("/");
            });
    }

    return (
        <Grid container spacing={1}>
            <Grid item xs={12}>
                <Typography variant="h4" component="h4">
                    Room Code: {roomCode}
                </Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="h6" component="h6">
                    Votes to Skip: {state.votesToSkip}
                </Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="h6" component="h6">
                    Guest Can Pause: {state.guestCanPause.toString()}
                </Typography>
            </Grid>
            <Grid item xs={12}>
                <Typography variant="h6" component="h6">
                    Host: {state.isHost.toString()}
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Button
                    variant="contained"
                    color="secondary"
                    onClick={leaveButtonPressed}
                >
                    Leave Room
                 </Button>
            </Grid>
        </Grid>      
    );
    // return (
    //     <div>
    //         <h3>Room: {roomCode}</h3>
    //         <p>Votes: {state.votesToSkip}</p>
    //         <p>Guest Can Pause: {state.guestCanPause.toString()}</p>
    //         <p>Is Host: {state.isHost.toString()}</p>
    //     </div>
    // );
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
