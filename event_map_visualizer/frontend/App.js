import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import EventList from "./components/EventList";
import EventForm from "./components/EventForm";
import EventMap from "./components/EventMap";
import { AppBar, Toolbar, Button } from "@mui/material";

function App() {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Button color="inherit" component={Link} to="/map">Мапа</Button>
        </Toolbar>
      </AppBar>

      <Routes>
        <Route path="/map" element={<EventMap />} />
      </Routes>
    </Router>
  );
}

export default App;