import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import { Link, useNavigate } from "react-router-dom";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

const CreateRoomPage = (props) => {
    const defaultVotes = 2;

    const intialState = {
        votesToSkip: defaultVotes,
        guestCanPause: true,
    };
    const [state, setState] = React.useState(intialState);
    let navigate = useNavigate();

    const handleVotesChange = (e) => {
        setState({
            votesToSkip: e.target.value
        });
    }

    const handleGuestCanPauseChange = (e) => {
        setState({
            guestCanPause: e.target.value === "true" ? true : false,
        });
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
        // .then(data => console.log(data));
        // .then((data) => this.props.history.push("/room/" + data.code));
    }

    return (
        <div>
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Create Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component="fieldset">
                        <FormHelperText>
                            <div align="center">Guest Control of Playback State</div>
                        </FormHelperText>
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
                            defaultValue={defaultVotes}
                            inputProps={
                                {
                                    min: "1",
                                    style: { textAlign: "center" }
                                }
                            }
                        />
                        <FormHelperText>
                            <div align="center">Votes Required to Skip Song</div>
                        </FormHelperText>
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
        </div >
    );
}

export default CreateRoomPage;