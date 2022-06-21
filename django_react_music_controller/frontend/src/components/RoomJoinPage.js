import React, { Component } from "react";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link, useNavigate } from "react-router-dom";


const RoomJoinPage = (props) => {

    const intialState = {
        roomCode: "",
        error: ""
    };
    const [state, setState] = React.useState(intialState);
    let navigate = useNavigate();

    const handleRoomCodeChange = (e) => {
        setState({
            roomCode: e.target.value
        });
        // console.log(`room code set as ${e.target.value}`);
    };
    
    const handleJoinRoomButtonClicked = () => {
        const request = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                code: state.roomCode
            })
        };
        fetch("/api/join-room", request)
        .then(response => {
            if (response.ok) {
                navigate(`/room/${state.roomCode}`);
            } else {
                setState({
                    error: `Room ${state.roomCode} not found`
                });
            }   
        })
        .catch(error => {
            console.log(error);
        });
    };


    return (
        <>
            <Grid container spacing={1} align="center">
                <Grid item xs={12}>
                    <Typography component="h4" variant="h4">
                        Join Room
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        error={!!state.error} // TextField error is of type boolean
                        label="Code"
                        placeholder="Enter a Room Code"
                        value={state.roomCode}
                        helperText={state.error}
                        variant="outlined"
                        onChange={handleRoomCodeChange}
                    />
                </Grid>
                <Grid item xs={12}>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleJoinRoomButtonClicked}
                    >
                        Enter Room
                    </Button>
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained" color="secondary" to="/" component={Link}>
                        Back
                    </Button>
                </Grid>
            </Grid>
        </>
    );
}

export default RoomJoinPage;

// export default class RoomJoinPage extends Component {
//     constructor(props) {
//         super(props);
//     }
    
//     render() {
//         return <p>This is the room join page</p>;
//     }
// }