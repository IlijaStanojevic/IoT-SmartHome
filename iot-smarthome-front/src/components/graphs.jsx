import logo from "../logo.svg";
import {Stack} from "@mui/material";
import {useEffect} from "react";


const Graphs = () => {
    useEffect(() => {
        document.title = 'Graphs';
    }, []);
    return (
        <div className="graphs">
                <Stack
                spacing={2}
                >
                    <iframe src="http://localhost:3000/d-solo/e4808398-51ac-4e6a-965b-cc7a99ad42f1/iot-smarthome?orgId=1&panelId=3"  height="300" frameBorder="0"></iframe>

                </Stack>


        </div>
    );
}

export default Graphs