import logo from "../logo.svg";
import {Stack} from "@mui/material";
import {Label} from "@mui/icons-material";


const Controllers = () => {
    return (
        <div className="controllers">
            <Stack>
                <div className="rgb">
                    <h2>RGB</h2>
                    <Stack>
                        <div className="row">
                            <button>Off</button>
                            <button style={{ backgroundColor: 'WHITE' }}>WHITE</button>
                            <button style={{ backgroundColor: 'RED' }}>RED</button>
                            <button style={{ backgroundColor: 'GREEN' }}>GREEN</button>
                        </div>
                        <div className="row">
                            <button style={{ backgroundColor: 'BLUE' }}>BLUE</button>
                            <button style={{ backgroundColor: 'YELLOW' }}>YELLOW</button>
                            <button style={{ backgroundColor: 'PURPLE' }}>PURPLE</button>
                            <button style={{ backgroundColor: 'LIGHT_BLUE' }}>LIGHT_BLUE</button>
                        </div>
                    </Stack>
                </div>
                <div className="alarm-clock">

                </div>
            </Stack>


        </div>
    );
}

export default Controllers