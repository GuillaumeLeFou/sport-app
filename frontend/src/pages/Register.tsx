import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

export default function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [age, setAge] = useState("");
    const [birthday, setBirthday] = useState("");
    const [weight, setWeight] = useState("");
    const [height, setHeight] = useState("");
    const navigate = useNavigate();

    const handleRegister = async (e: React.FormEvent) => {
        e.preventDefault()

        try {
            const userData = {
                email,
                password,
                username,
                first_name: firstName,
                last_name: lastName,
                age: Number(age),
                birthday: new Date(birthday),
                weight: Number(weight),
                height: Number(height)
            }

            await api.post("/auth/register", userData);

            alert("Registration Successful");
            navigate("/login");
        } catch (error) {
            console.log("Registration failed", error);
            alert("Registration failed");
        }
    }
    return (
        <div className="flex items-center justify-center h-screen">
            <form onSubmit={handleRegister} className="flex flex-col gap-4">
                <h1 className="text-2xl font-bold">Register</h1>
                <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} value={email} className="border p-2" />
                <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} value={password} className="border p-2" />
                <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} value={username} className="border p-2" />
                <input type="text" placeholder="First Name" onChange={(e) => setFirstName(e.target.value)} value={firstName} className="border p-2" />
                <input type="text" placeholder="Last Name" onChange={(e) => setLastName(e.target.value)} value={lastName} className="border p-2" />
                <input type="number" placeholder="Age" onChange={(e) => setAge(e.target.value)} value={age} className="border p-2" />
                <input type="date" placeholder="Birthday" onChange={(e) => setBirthday(e.target.value)} value={birthday} className="border p-2" />
                <input type="number" placeholder="Weight" onChange={(e) => setWeight(e.target.value)} value={weight} className="border p-2" />
                <input type="number" placeholder="Height" onChange={(e) => setHeight(e.target.value)} value={height} className="border p-2" />
                <button type="submit" className="bg-blue-500 text-white rounded-md p-2">Register</button>
            </form>
        </div>
    );
}