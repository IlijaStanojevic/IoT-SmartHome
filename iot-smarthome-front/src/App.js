import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Graphs from "./components/graphs";
import Controllers from "./components/controllers";
function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/">

          </Route>
          <Route path="graphs" element={<Graphs/>}></Route>
          <Route path="controllers" element={<Controllers/>}></Route>
        </Routes>
      </BrowserRouter>
  );
}

export default App;
