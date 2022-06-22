import React, { Component, useEffect } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Room from "./Room";
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
    Navigate,
    BrowserRouter,
} from "react-router-dom"

// this is more like a router?
const HomePage = () => {
    const intialState = {
        roomCode: null,
    };
    const [state, setState] = React.useState(intialState);

    // async componentDidMount() {
    //     fetch("/api/user-in-room")
    //     .then((response) => response.json())
    //     .then((data) => {
    //         setState({roomCode: data.code})
    //     });
    // }

    // check if user is already in a room (base on session)
    useEffect(() => {
        fetch("/api/user-in-room")
            .then(response => response.json())
            .then(data => {
                setState({roomCode: data.code})
            });
    }, []);

    const clearRoomCode = () => {
        setState({roomCode: null})
    }

    return (
        <Router>
            <Routes>
                {/* <Route path='/' element={<HomePageReal />} /> */}
                <Route path='/' element={state.roomCode ? (
                            <Navigate to={`/room/${state.roomCode}`} />
                        ) : <HomePageReal />
                } />
                <Route path='/join' element={<RoomJoinPage />} />
                <Route path='/create' element={<CreateRoomPage />} />
                <Route path='/room/:roomCode' element={<Room clearRoomCodeCallback={clearRoomCode} />} />
            </Routes>
        </Router>
    );
}

export default HomePage;
    
function HomePageReal() {
        // return <p>This is the Homepage!</p>
    return (
        <Grid container spacing={3}>
            <Grid item xs={12} align="center">
                <Typography variant="h3" compact="h3">
                    House Party
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <ButtonGroup disableElevation variant="contained" color="primary">
                    <Button component={Link} to="/join" color="primary">
                        Join a Room
                    </Button>
                    <Button component={Link} to="/create" color="secondary">
                        Create a Room
                    </Button>
                </ButtonGroup>
            </Grid>
        </Grid>
    );
}

// export default class HomePage extends Component {
//     constructor(props) {
//         super(props);
//     }

//     render() {
//         return (
//             <Router>
//                 <Routes>
//                     <Route path='/' element={<HomePageReal />} />
//                     <Route path='/join' element={<RoomJoinPage />} />
//                     <Route path='/create' element={<CreateRoomPage />} />
//                     <Route path='/room/:roomCode' element={<Room />} />
//                 </Routes>
//             </Router>
//         );
//     }
// }