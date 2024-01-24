import React from "react";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from "@mui/material";

const MyMaterialTable = () => {
    return (
        <div >
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>PI</TableCell>
                            <TableCell>Code</TableCell>
                            <TableCell>State</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        <TableRow>
                            <TableCell rowSpan={10}>PI 1</TableCell>
                            <TableCell>DS1</TableCell>
                            <TableCell>Row 1</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DL</TableCell>
                            <TableCell>Row 2</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DUS1</TableCell>
                            <TableCell>Row 2</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DB</TableCell>
                            <TableCell>Row 3</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DPIR1</TableCell>
                            <TableCell>Row 4</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DMS</TableCell>
                            <TableCell>Row 5</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RPIR1</TableCell>
                            <TableCell>Row 6</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RPIR2</TableCell>
                            <TableCell>Row 6</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RDHT1</TableCell>
                            <TableCell>Row 7</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RDHT2</TableCell>
                            <TableCell>Row 8</TableCell>
                        </TableRow>

                        <TableRow>
                            <TableCell rowSpan={8}>PI 2</TableCell>
                            <TableCell>DS2</TableCell>
                            <TableCell>Row 9</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DUS2</TableCell>
                            <TableCell>Row 10</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>DPIR2</TableCell>
                            <TableCell>Row 11</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>GDHT</TableCell>
                            <TableCell>Row 12</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>GLCD</TableCell>
                            <TableCell>Row 13</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>GSG</TableCell>
                            <TableCell>Row 14</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RPIR3</TableCell>
                            <TableCell>Row 15</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RDHT3</TableCell>
                            <TableCell>Row 16</TableCell>
                        </TableRow>

                        <TableRow>
                            <TableCell rowSpan={6}>PI 3</TableCell>
                            <TableCell>RPIR4</TableCell>
                            <TableCell>Row 9</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>RDHT4</TableCell>
                            <TableCell>Row 10</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>BB</TableCell>
                            <TableCell>Row 11</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>B4SD</TableCell>
                            <TableCell>Row 12</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>BIR</TableCell>
                            <TableCell>Row 13</TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell>BRGB</TableCell>
                            <TableCell>Row 14</TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </TableContainer>
        </div>

    );
};

export default MyMaterialTable;
