import logo from "../logo.svg";
import {Stack} from "@mui/material";
import {useEffect} from "react";


const Home = () => {
    useEffect(() => {
        document.title = 'Smart-Home';
    }, []);
    return (
        <div className="home">
            <h1>Home</h1>
            <Stack
                spacing={2}
            >


            </Stack>


        </div>
    );
}

export default Home