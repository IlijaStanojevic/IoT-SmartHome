import React from 'react';
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';
import { AppBar, Toolbar, Button } from '@mui/material';
import Graphs from './components/graphs';
import Controllers from './components/controllers';

function App() {
    return (
        <BrowserRouter>
            <div>
                <AppBar position="static">
                    <Toolbar>
                        <Button component={Link} to="/" color="inherit">
                            Home
                        </Button>
                        <Button component={Link} to="/controllers" color="inherit">
                            Controllers
                        </Button>
                        <Button component={Link} to="/graphs" color="inherit">
                            Graphs
                        </Button>
                    </Toolbar>
                </AppBar>

                <Routes>
                    <Route path="/" element={<div>Home</div>} />
                    <Route path="/graphs" element={<Graphs />} />
                    <Route path="/controllers" element={<Controllers />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
