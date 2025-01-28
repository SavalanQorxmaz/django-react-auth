import Image from "next/image";
import Login from "./components/Login";
import Register from "./components/RegisterOTP";

export default function Home() {
  return (
    <div className="w-full h-screen flex justify-center items-center">
      <div className="w-80 border-2 p-2 bg-blue-50">
      <Register/>
      </div>

    </div>
  );
}
