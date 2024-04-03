import React from "react";
import Header from "./components/header/Header.tsx";
import SignUpForm from "./components/auth/SignUpForm.tsx";


function SignUpFormPage(props) {

    const handleClickAvatar = () => {
        alert("Avatar clicked");
    }
    const handleSignUp = (formData) => {props.onSignUp(formData);}

    return (
        <div className="AuthFormPage">
            <Header onClickAvatar={handleClickAvatar} />
                <SignUpForm onSignUp={handleSignUp} />
        </div>
    )
}

export default SignUpFormPage;
