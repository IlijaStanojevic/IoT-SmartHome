import React, {useEffect, useState} from "react";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from "@mui/material";
import io from "socket.io-client";

const Home = () => {
    const [receivedMessage, setReceivedMessage] = useState('');
    const [receivedData, setReceivedData] = useState([]);
    const socket = io('http://localhost:5000', {
        reconnection: true,
        reconnectionDelay: 1000,
        reconnectionDelayMax: 5000,
        reconnectionAttempts: Infinity,
    });
    const groupByRunsOn = () => {
        const groupedData = {};
        receivedData.forEach((row) => {
            const key = row.runs_on;
            if (!groupedData[key]) {
                groupedData[key] = [];
            }
            groupedData[key].push(row);
        });
        return groupedData;
    };
    const fetchCurrentState = () => {
        fetch(`http://localhost:5000/simple_query`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                setReceivedData(data.data)
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    };
    useEffect(() => {
        socket.on('message_from_server', (data) => {
            console.log(data)
            setReceivedMessage(data);
        });
        document.title = 'Smart-Home';
        fetchCurrentState();
    }, []);
    return (
        <div>
            {Object.entries(groupByRunsOn()).map(([runsOn, rows], index) => (
                <div key={index}>
                    <h2>{runsOn}</h2>
                    <TableContainer component={Paper}>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <TableCell>Code</TableCell>
                                    <TableCell>State</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rows.map((row, rowIndex) => (
                                    <TableRow key={rowIndex}>
                                        <TableCell>{row.name}</TableCell>
                                        <TableCell>{typeof row._value === 'boolean' ? row._value.toString() : row._value}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </div>
            ))}
        </div>

    );
};

export default Home;
