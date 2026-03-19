import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { getEvents } from "../api/events";
import { Typography, Container } from "@mui/material";

export default function EventMap() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const data = await getEvents();
      setEvents(data);
    };
    fetchEvents();
  }, []);

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>Мапа</Typography>
      <MapContainer
        center={[50.45, 30.52]}
        zoom={6}
        style={{ height: "500px", width: "100%", borderRadius: "8px" }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {events.map((event) => (
          <Marker
            key={event.id}
            position={[event.latitude || 50.45, event.longitude || 30.52]}
          >
            <Popup>
              <Typography variant="subtitle1">{event.name}</Typography>
              <Typography variant="body2">{event.date}</Typography>
              <Typography variant="body2">{event.category}</Typography>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </Container>
  );
}