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
        <div className="min-h-screen bg-gradient-to-br from-stone-950 via-stone-900 to-stone-800 flex items-center justify-center px-4">
            <div className="w-full max-w-md">
                <form onSubmit={handleRegister} className="bg-stone-900/80 backdrop-blur-md border border-stone-700 shadow-2xl rounded-2xl p-8 grid grid-cols-1 md:grid-cols-2 gap-5">
                    <div className="md:col-span-2 text-center">
                        <h1 className="text-3xl font-bold text-green-400">Register</h1>
                        <p className="mt-2 text-stone-400 text-sm">
                            Create an account
                        </p>
                    </div>
                    <div className="flex flex-col gap-2 md:col-span-2">
                        <label htmlFor="username" className="text-sm font-medium text-stone-300">Username</label>
                        <input id="username" type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} value={username} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="email" className="text-sm font-medium text-stone-300">Email</label>
                        <input id="email" type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} value={email} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="password" className="text-sm font-medium text-stone-300">Password</label>
                        <input id="password" type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} value={password} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="firstName" className="text-sm font-medium text-stone-300">First Name</label>
                        <input id="firstName" type="text" placeholder="First Name" onChange={(e) => setFirstName(e.target.value)} value={firstName} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="lastName" className="text-sm font-medium text-stone-300">Last Name</label>
                        <input id="lastName" type="text" placeholder="Last Name" onChange={(e) => setLastName(e.target.value)} value={lastName} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="age" className="text-sm font-medium text-stone-300">Age</label>
                        <input id="age" type="number" placeholder="Age" onChange={(e) => setAge(e.target.value)} value={age} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="birthday" className="text-sm font-medium text-stone-300">Birthday</label>
                        <input id="birthday" type="date" placeholder="Birthday" onChange={(e) => setBirthday(e.target.value)} value={birthday} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="weight" className="text-sm font-medium text-stone-300">Weight</label>
                        <input id="weight" type="number" placeholder="Weight" onChange={(e) => setWeight(e.target.value)} value={weight} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <div className="flex flex-col gap-2">
                        <label htmlFor="height" className="text-sm font-medium text-stone-300">Height</label>
                        <input id="height" type="number" placeholder="Height" onChange={(e) => setHeight(e.target.value)} value={height} className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30" />
                    </div>
                    <button type="submit" className="md:col-span-2 mt-2 w-full rounded-xl bg-green-400 px-4 py-3 font-semibold text-stone-950 transition hover:bg-green-300 active:scale-[0.99]">Register</button>
                    <button type="button" onClick={() => navigate("/login")} className="md:col-span-2 w-full rounded-xl border border-stone-600 bg-transparent px-4 py-3 font-semibold text-stone-200 transition hover:bg-stone-800">Already have an account?</button>
                </form>
            </div>
        </div>
    );
}