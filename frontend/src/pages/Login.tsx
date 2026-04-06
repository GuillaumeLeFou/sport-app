import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

export default function Login() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault()

        try {
            const formData = new URLSearchParams();
            formData.append("username", email);
            formData.append("password", password);

            const response = await api.post("/auth/login", formData, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            });

            const token = response.data.access_token;

            localStorage.setItem("token", token);

            navigate("/dashboard")

        } catch (error) {
            console.log("Login failed", error);
            alert("Invalid credentials")
        }
    }

    return (
        <div className="flex items-center justify-center h-screen">
            <form onSubmit={handleLogin} className="flex flex-col gap-4">
                <h1 className="text-2xl font-bold">Login</h1>
                <input
                    type="email"
                    placeholder="Email"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    className="border p-2"
                />

                <input
                    type="password"
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                    value={password}
                    className="border p-2"
                />

                <button type="submit" className="bg-blue-500 text-white rounded-md p-2">Login</button>
            </form>
        </div>
    );
}