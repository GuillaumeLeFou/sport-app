import { useNavigate } from "react-router-dom";

export default function Sidebar() {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/login");
    };

    return (
        <aside className="w-64 border-r border-stone-800 bg-stone-900/70 backdrop-blur-md p-6 flex flex-col">
            <h1 className="text-2xl font-bold text-green-400 mb-10">
                Sport App
            </h1>

            <nav className="flex flex-col gap-3">
                <button className="text-left rounded-xl px-4 py-3 bg-green-400/10 text-green-400 border border-green-400/20">
                    Dashboard
                </button>

                <button className="text-left rounded-xl px-4 py-3 hover:bg-stone-800 transition">
                    Workouts
                </button>

                <button className="text-left rounded-xl px-4 py-3 hover:bg-stone-800 transition">
                    Progress
                </button>

                <button className="text-left rounded-xl px-4 py-3 hover:bg-stone-800 transition">
                    Routines
                </button>
            </nav>

            <button
                onClick={handleLogout}
                className="mt-auto rounded-xl border border-red-400/30 text-red-400 px-4 py-3 hover:bg-red-400/10 transition"
            >
                Logout
            </button>
        </aside>
    );
}