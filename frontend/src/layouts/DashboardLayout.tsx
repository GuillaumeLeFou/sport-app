import Sidebar from "../components/Sidebar";

type DashboardLayoutProps = {
    children: React.ReactNode;
};

export default function DashboardLayout({
    children,
}: DashboardLayoutProps) {
    return (
        <div className="min-h-screen bg-gradient-to-br from-stone-950 via-stone-900 to-stone-800 text-white flex">
            <Sidebar />

            <main className="flex-1 p-8">
                {children}
            </main>
        </div>
    );
}