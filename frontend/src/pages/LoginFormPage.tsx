import React from "react";
import Header from "./components/header/Header.tsx";
import LoginForm from "./components/auth/LoginForm.tsx";


function LoginFormPage(props) {



    const handleClickAvatar = () => {
        alert("Avatar clicked");
    }
    const handleLogin = (formData) => {props.onLogin(formData);}

    return (
        <div className="AuthFormPage">
            <Header onClickAvatar={handleClickAvatar} />
                <LoginForm onLogin={handleLogin} /> 
        </div>
    )
}

export default LoginFormPage;
