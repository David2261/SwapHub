import { createBrowserRouter, RouterProvider } from "react-router-dom";
import StartPage from "./pages/StartPage.tsx";
import LoginFormPage from "./pages/LoginFormPage.tsx";
import SignUpFormPage from "./pages/SignUpFormPage.tsx";


function Router(props) {
  const accessToken = props.accessToken;

  const handleLogin = (formData) => {props.onLogin(formData);}
  const handleSignUp = (formData) => {props.onSignUp(formData);}
  const handleUnauthorized = () => { props.onUnauthorized(); }
  const handleLogout = () => { props.onLogout(); }

    const router = createBrowserRouter([
      {
        path: "/",
        element: (
          <StartPage
            accessToken={accessToken}
            onUnauthorized={handleUnauthorized}
            onLogout={handleLogout}
          />
        ),
      },
      {
        path: "/login/",
        element: (
          <LoginFormPage
            onLogin={handleLogin}
          />
        ),
      },
      {
        path: "/signup/",
        element: (
          <SignUpFormPage
            onSignUp={handleSignUp}
          />
        ),
      },
    ]);

  return <RouterProvider router={router} />;
}

export default Router;
