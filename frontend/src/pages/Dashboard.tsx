import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {
    const [user, setUser] = useState<any>(null);

    const fetchUser = async () => {
        try {
            const response = await api.get("/users/me");
            setUser(response.data);
        } catch (error) {
            console.error("Error fetching user", error);
        }
    };

    useEffect(() => {
        fetchUser();
    }, []);

    return (
        <div>
            {user ? (
                <h1>Dashboard, {user.first_name}</h1>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}