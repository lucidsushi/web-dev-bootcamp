import React, { Component } from "react";
import { TextField, Button, Grid, Typography, Box } from "@material-ui/core";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import { Link, useNavigate } from "react-router-dom";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

const CreateRoomPage = (props) => {

    const intialState = {
        votesToSkip: 2,
        guestCanPause: true,
    };
    const [state, setState] = React.useState(intialState);
    let navigate = useNavigate();

    const handleVotesChange = (e) => {
        setState(state => ({...state, votesToSkip: e.target.value}));
        // setState({...state, votesToSkip: e.target.value}); // this is the same as the above line?

    }

    const handleGuestCanPauseChange = (e) => {
        setState(state => ({...state, guestCanPause: e.target.value === "true" ? true : false}));
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

    return (
        <>
            <Grid container spacing={1} >
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Create Room
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
                            defaultValue="true"
                            onChange={handleGuestCanPauseChange}
                        >
                            <FormControlLabel
                                value='true'
                                control={<Radio color='primary' />}
                                label="Play/Pause"
                                labelPlacement="end"
                            />
                            <FormControlLabel
                                value='false'
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
                        onClick={createRoomButtonClicked}
                    >
                        Create a Room
                    </Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="secondary" to="/" component={Link} >
                        Back
                    </Button>
                </Grid>
            </Grid>
        </>
    );
}

export default CreateRoomPage;