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
        <div className="min-h-screen bg-gradient-to-br from-stone-950 via-stone-900 to-stone-800 flex items-center justify-center px-4">
            <div className="w-full max-w-md">
                <form
                    onSubmit={handleLogin}
                    className="bg-stone-900/80 backdrop-blur-md border border-stone-700 shadow-2xl rounded-2xl p-8 flex flex-col gap-5"
                >
                    <div className="text-center">
                        <h1 className="text-3xl font-bold text-green-400">Welcome back</h1>
                        <p className="text-stone-400 mt-2 text-sm">
                            Login to access your dashboard
                        </p>
                    </div>

                    <div className="flex flex-col gap-2">
                        <label htmlFor="email" className="text-sm font-medium text-stone-300">
                            Email
                        </label>
                        <input
                            id="email"
                            type="email"
                            placeholder="email@example.com"
                            onChange={(e) => setEmail(e.target.value)}
                            value={email}
                            className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30"
                        />
                    </div>

                    <div className="flex flex-col gap-2">
                        <label htmlFor="password" className="text-sm font-medium text-stone-300">
                            Password
                        </label>
                        <input
                            id="password"
                            type="password"
                            placeholder="••••••••"
                            onChange={(e) => setPassword(e.target.value)}
                            value={password}
                            className="w-full rounded-xl border border-stone-700 bg-stone-800 px-4 py-3 text-white placeholder:text-stone-500 outline-none transition focus:border-green-400 focus:ring-2 focus:ring-green-400/30"
                        />
                    </div>

                    <button
                        type="submit"
                        className="mt-2 w-full rounded-xl bg-green-400 px-4 py-3 font-semibold text-stone-950 transition hover:bg-green-300 active:scale-[0.99]"
                    >
                        Login
                    </button>

                    <button
                        type="button"
                        onClick={() => navigate("/register")}
                        className="w-full rounded-xl border border-stone-600 bg-transparent px-4 py-3 font-semibold text-stone-200 transition hover:bg-stone-800"
                    >
                        Create an account
                    </button>
                </form>
            </div>
        </div>
    );
}