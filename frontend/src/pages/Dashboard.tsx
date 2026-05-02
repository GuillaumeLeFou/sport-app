import { useEffect, useState } from "react";
import api from "../services/api";
import DashboardLayout from "../layouts/DashboardLayout";

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
        <DashboardLayout>
            <div className="mb-8">
                <h1 className="text-3xl font-bold">
                    Welcome,{" "}
                    <span className="text-green-400">
                        {user?.first_name || "Athlete"}
                    </span>
                </h1>

                <p className="text-stone-400 mt-2">
                    Track your workouts and monitor your progress.
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="rounded-2xl border border-stone-700 bg-stone-900/70 backdrop-blur-md p-6 shadow-xl">
                    <p className="text-stone-400 text-sm">
                        Current Weight
                    </p>
                    <h2 className="text-3xl font-bold mt-2">
                        {user?.weight || "--"} kg
                    </h2>
                </div>

                <div className="rounded-2xl border border-stone-700 bg-stone-900/70 backdrop-blur-md p-6 shadow-xl">
                    <p className="text-stone-400 text-sm">
                        Height
                    </p>
                    <h2 className="text-3xl font-bold mt-2">
                        {user?.height || "--"} cm
                    </h2>
                </div>

                <div className="rounded-2xl border border-stone-700 bg-stone-900/70 backdrop-blur-md p-6 shadow-xl">
                    <p className="text-stone-400 text-sm">
                        Age
                    </p>
                    <h2 className="text-3xl font-bold mt-2">
                        {user?.age || "--"}
                    </h2>
                </div>
            </div>

            <div className="mt-8 rounded-2xl border border-stone-700 bg-stone-900/70 backdrop-blur-md p-6 shadow-xl">
                <h2 className="text-xl font-semibold mb-4">
                    Weekly Activity
                </h2>

                <div className="h-64 flex items-center justify-center text-stone-500 border border-dashed border-stone-700 rounded-xl">
                    Future chart / stats here
                </div>
            </div>
        </DashboardLayout>
    );
}