import React from 'react';
import Header from "../widgets/header/Header.tsx";
import AuthForm from "../components/auth/AuthForm.tsx";


function AuthFormPage(props) {

    const handleClickAvatar = () => {
        alert("Avatar clicked");
    }
    const handleLogin = (formData) => {props.onLogin(formData);}

    return (
        <>
            <Header onClickAvatar={handleClickAvatar} />
            <AuthForm onLogin={handleLogin} />
        </>
    )
}

export default AuthFormPage;
