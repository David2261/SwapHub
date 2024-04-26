import React from "react";

// function Header(props) {

//   const handleClickAvatar = () => {
//     props.onClickAvatar()
//   }

//   return (
//     <header className="Header">
//       <h1 className="Swap">
//         Swap<span className="Hub">Hub</span>
//       </h1>
//       <img src="http://localhost:80/media/user.png" alt="avatar" onClick={handleClickAvatar} />
//     </header>
//   );
// }

const Header = (props) => {
	return <>
		<div className="header-global-block">
			<div className="header-location-block">
					<p>Местоположение: {props.location}</p>
			</div>
			<div className="header-links-block">
				<div className="header-block">
					<div className="header-block-icon">
						<img src={props.icon} alt="logo" />
					</div>
				</div>
				<div className="header-block">
					<div className="header-block-catalog">
						<button>Каталог</button>
					</div>
				</div>
				<div className="header-block">
					<div className="header-block-search">
						<input type="text" />
					</div>
				</div>
				<div className="header-block">
					<div className="header-block-user-widgets">
						<button>Разместить объявление</button>
						<button>Войти</button>
					</div>
				</div>
			</div>
		</div>
	</>
}

export default Header;
