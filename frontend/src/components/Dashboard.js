import React from "react";
import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api";

const Dashboard = () => {
  const { isLoaded } = useLoadScript({
    googleMapsApiKey: "YOUR_GOOGLE_MAPS_API_KEY",
  });

  if (!isLoaded) return <div>Loading...</div>;
  return (
    <GoogleMap zoom={10} center={{ lat: 37.7749, lng: -122.4194 }}>
      <Marker position={{ lat: 37.7749, lng: -122.4194 }} />
    </GoogleMap>
  );
};

export default Dashboard;