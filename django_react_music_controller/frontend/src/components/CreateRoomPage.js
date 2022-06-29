import React, { Component } from "react";
import {
    TextField, Button, Grid, Typography, Box,
    Collapse, FormHelperText, FormControl,
    RadioGroup, FormControlLabel, Radio, Snackbar
} from "@material-ui/core";
import Alert from "@material-ui/lab/Alert";
import { Link, useNavigate } from "react-router-dom";

const CreateRoomPage = (props) => {

    const intialState = {
        ...props.state
        // guestCanPause: true,
        // votesToSkip: 2,
    };
    const [state, setState] = React.useState(intialState);
    let navigate = useNavigate();

    const handleVotesChange = (e) => {
        setState(state => ({ ...state, votesToSkip: e.target.value }));
        // setState({...state, votesToSkip: e.target.value}); // this is the same as the above line?

    }
    const handleGuestCanPauseChange = (e) => {
        setState(state => ({ ...state, guestCanPause: e.target.value === "true" ? true : false }));
    }

    const createRoomButtonClicked = () => {
        const request = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                guest_can_pause: state.guestCanPause,
                votes_to_skip: state.votesToSkip
            })
        };
        fetch("/api/create-room", request)
            .then(response => response.json())
            .then(data => navigate(`/room/${data.code}`));
        // .then((data) => this.props.history.push("/room/" + data.code)); // old way of doing it from a class
    }

    const updateRoomButtonClicked = () => {
        const request = {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                guest_can_pause: state.guestCanPause,
                votes_to_skip: state.votesToSkip,
                code: props.roomCode
            })
        };
        fetch("/api/update-room", request)
            .then((response) => {
                if (response.ok) {
                    setState({
                        ...state,
                        successMsg: "Room updated successfully!",
                    });
                } else {
                    setState({
                        ...state,
                        errorMsg: "Error updating room...",
                    });
                }
            });
    }

    const modeEventMap = {
        "Create": {
            "primaryButton1": createRoomButtonClicked,
            "secondaryButton1": () => navigate("/")

        },
        "Update": {
            "primaryButton1": updateRoomButtonClicked,
            "secondaryButton1": () => props.toggleRoomIsSettingsCallback(false)
        }
    };

    return (
        <>
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Snackbar
                        // sx = {{
                        //     '& .MuiSnackbar-root': {
                        //         transform: 'translate(0%, -150%) !important',
                        //     },
                        // }}
                        open={state.errorMsg != "" || state.successMsg != ""}
                        autoHideDuration={500}
                        anchorOrigin={{ vertical: "top", horizontal: "center" }}
                        onClose={
                            () => {
                                // setState({...state, errorMsg: "", successMsg: ""});
                                props.triggerRoomStateUpdateCallback();
                            }
                        }
                    >
                        {state.successMsg != "" ? (
                            <Alert
                                severity="success"
                            // onClose={() => {setState({...state, successMsg: "" });}}
                            >
                                {state.successMsg}
                            </Alert>
                        ) : (
                            <Alert
                                severity="error"
                            // onClose={() => {setState({...state, errorMsg: "" });}}
                            >
                                {state.errorMsg}
                            </Alert>
                        )
                        }
                    </Snackbar>
                    <Typography sx={{ color: '#00f' }} component="h4" variant="h4">
                        {props.mode} Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component="fieldset">
                        <Box display="flex" alignItems="center" justifyContent="center">
                            <FormHelperText>
                                Guest Control of Playback State
                            </FormHelperText>
                        </Box>
                        <RadioGroup
                            row
                            value={state.guestCanPause.toString()}
                            // defaultValue="false"
                            onChange={handleGuestCanPauseChange}
                        >
                            <FormControlLabel
                                value="true"
                                control={<Radio color='primary' />}
                                label="Play/Pause"
                                labelPlacement="end"
                            />
                            <FormControlLabel
                                value="false"
                                control={<Radio color='secondary' />}
                                label="No Control"
                                labelPlacement="end"
                            />
                        </RadioGroup>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <TextField
                            required={true}
                            type="number"
                            onChange={handleVotesChange}
                            defaultValue={state.votesToSkip}
                            inputProps={
                                {
                                    min: "1",
                                    style: { textAlign: "center" }
                                }
                            }
                        />
                        <Box display="flex" alignItems="center" justifyContent="center">
                            <FormHelperText>
                                Votes Required to Skip Song
                            </FormHelperText>
                        </Box>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={modeEventMap[props.mode].primaryButton1}
                    >
                        {props.mode} Room
                    </Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="secondary"
                        onClick={modeEventMap[props.mode].secondaryButton1}
                    // to="/"
                    // component={Link} >
                    >
                        {props.secondaryButton1}
                    </Button>
                </Grid>
            </Grid>
        </>
    );
}

CreateRoomPage.defaultProps = {
    mode: "Create",
    state: {
        guestCanPause: false,
        votesToSkip: 2,
        errorMsg: "",
        successMsg: ""
    },
    secondaryButton1: "Back",
}

export default CreateRoomPage;