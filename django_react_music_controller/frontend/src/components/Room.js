import React, { Component } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Grid, Button, Typography } from "@material-ui/core";

import CreateRoomPage from "./CreateRoomPage";


// https://reactrouter.com/docs/en/v6/getting-started/tutorial#reading-url-params
const Room = (props) => {
    const intialState = {
        guestCanPause: false,
        votesToSkip: 2,
        isHost: false,
        roomIsSettings: false
    };
    const [state, setState] = React.useState(intialState);

    let navigate = useNavigate();
    let { roomCode } = useParams();

    const triggerRoomStateUpdate = () => {
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
                    ...state,
                    guestCanPause: data.guest_can_pause,
                    votesToSkip: data.votes_to_skip,
                    isHost: data.is_host,
                    roomIsSettings: false,
                });
            });
    }
    const handleHostSpotifyAuth = () => {
        // check if token exists/is-fresh or direct to spotify sign-in
        fetch("/spotify/spotify-token-exists")
            .then((response) => response.json())
            .then((data) => {
                if (!data.status) {
                    fetch("/spotify/get-spotify-auth-url")
                        .then((response) => response.json())
                        .then((data) => {
                            // may be stuck in a redirect loop if spotify-token-exists is not working
                            window.location.replace(data.url); // goes to sign in at Spotify
                        });
                }
            });
    }

    React.useEffect(() => {
        triggerRoomStateUpdate();
        // state NOT updated yet from triggerRoomStateUpdate
    }, []);

    React.useEffect(() => {
        if (state === intialState) {
            return;
        } else if (state.isHost) {
            // state IS updated from triggerRoomStateUpdate
            handleHostSpotifyAuth();
        }
    }, [state]);


    const setRoomIsSettings = (value) => {
        setState({ ...state, roomIsSettings: value });
    }

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

    if (state.roomIsSettings) {
        return (
            // <Grid container spacing={1}>
            //     <Grid item xs={12} align="center">
            <CreateRoomPage
                mode={"Update"}
                roomCode={roomCode}
                state={{ ...state, errorMsg: "", successMsg: "" }}
                toggleRoomIsSettingsCallback={setRoomIsSettings}
                triggerRoomStateUpdateCallback={triggerRoomStateUpdate}
            />
            //     </Grid>
            // </Grid>
        );
    } else {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography variant="h5" component="h5">
                        Room Code: {roomCode}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography variant="h6" component="h6">
                        Votes to Skip: {state.votesToSkip}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography variant="h6" component="h6">
                        Guest Can Pause: {state.guestCanPause.toString()}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography variant="h6" component="h6">
                        Host: {state.isHost.toString()}
                    </Typography>
                </Grid>
                {state.isHost ? (
                    <Grid item xs={12} align="center">
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={() => setRoomIsSettings(true)}
                        >
                            Settings
                        </Button>
                    </Grid>
                ) : null
                }
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
    }
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
