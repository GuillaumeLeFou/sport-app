import { Navigate } from "react-router-dom";

type PublicRouteProps = {
    children: React.ReactNode;
};

export default function PublicRoute({ children }: PublicRouteProps) {
    const token = localStorage.getItem("token");

    if (token) return <Navigate to="/dashboard" replace />;

    return children;
}