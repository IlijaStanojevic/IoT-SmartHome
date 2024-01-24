import React, { useState } from "react";
import { Stack } from "@mui/material";

const Controllers = () => {
    const [time, setTime] = useState("10:00");
    const [hours, setHours] = useState("10");
    const [minutes, setMinutes] = useState("00");
    const [seconds, setSeconds] = useState("00");

    const handleHourChange = (e) => {
        const newHour = e.target.value;
        if (newHour >= 0 && newHour < 24) {
            setHours(newHour);
        }
    };
    const handleMinuteChange = (e) => {
        const newMinute = e.target.value;
        if (newMinute >= 0 && newMinute < 60) {
            setMinutes(newMinute);
        }
    };
    const handleSecondsChange = (e) => {
        const newSecond = e.target.value;
        if (newSecond >= 0 && newSecond < 60) {
            setSeconds(newSecond);
        }
    };
    const changeRGBColorClick = (buttonColor) => {
        fetch(`http://localhost:5000/rgbcolor/${buttonColor}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    };
    const setTimeClick = () => {
        const requestBody = {
            alarm_time: `${hours}:${minutes}:${seconds}`,
        };
        fetch(`http://localhost:5000/set_alarm`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    };
    const cancelTimeClick = () => {
        const requestBody = {
            alarm_time: `${hours}:${minutes}:${seconds}`,
        };
        fetch(`http://localhost:5000/turnOffBlinking`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    };
    return (
        <div className="controllers-container">
            <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                spacing={15}
            >
                <h1>Controllers</h1>
                <div className="controllers">
                    <div className="rgb">
                        <h2>RGB</h2>
                        <Stack>
                            <div className="row">
                                <button onClick={() => changeRGBColorClick("OFF")}>Off</button>
                                <button onClick={() => changeRGBColorClick("WHITE")} style={{ backgroundColor: "WHITE" }}>WHITE</button>
                                <button onClick={() => changeRGBColorClick("RED")} style={{ backgroundColor: "RED" }}>RED</button>
                                <button onClick={() => changeRGBColorClick("GREEN")} style={{ backgroundColor: "GREEN" }}>GREEN</button>
                            </div>
                            <div className="row">
                                <button onClick={() => changeRGBColorClick("BLUE")} style={{ backgroundColor: "BLUE", color: "white" }}>BLUE</button>
                                <button onClick={() => changeRGBColorClick("YELLOW")} style={{ backgroundColor: "YELLOW" }}>YELLOW</button>
                                <button onClick={() => changeRGBColorClick("PURPLE")} style={{ backgroundColor: "PURPLE" }}>PURPLE</button>
                                <button onClick={() => changeRGBColorClick("LIGHT_BLUE")} style={{ backgroundColor: "lightblue" }}>
                                    LIGHT_BLUE
                                </button>
                            </div>
                        </Stack>
                    </div>
                    <div>
                        <h2>Alarm clock</h2>
                        <Stack
                        spacing={1}>
                            <label>
                                Hours:
                                <input
                                    type="number"
                                    value={hours}
                                    onChange={handleHourChange}
                                    min="0"
                                    max="23"
                                />
                            </label>
                            <label>
                                Minutes:
                                <input
                                    type="number"
                                    value={minutes}
                                    onChange={handleMinuteChange}
                                    min="0"
                                    max="59"
                                />
                            </label>
                            <label>
                                Seconds:
                                <input
                                    type="number"
                                    value={seconds}
                                    onChange={handleSecondsChange}
                                    min="0"
                                    max="59"
                                />
                            </label>
                            <p>Alarm clock Time: {`${hours.padStart(2,"0")}:${minutes.padStart(2,"0")}:${seconds.padStart(2,"0")}`}</p>
                            <button onClick={setTimeClick}>Set alarm</button>
                            <button onClick={cancelTimeClick}>Cancel alarm</button>
                        </Stack>

                    </div>
                </div>
            </Stack>
        </div>
    );
};

export default Controllers;
