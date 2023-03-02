import React,{useState} from 'react'

import './SignInUp.css'

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faUser, faSpinner, faEnvelope} from '@fortawesome/free-solid-svg-icons'
// import {faUser} from '@fortawesome/free-solid-svg-icons'
import {faGoogle, faGithub} from '@fortawesome/free-brands-svg-icons'

import SignUp from '../Resources/Sign-Up.svg'
import LogIn from '../Resources/Log-In.svg'

import { changed } from '../features/username/username'
import { useSelector, useDispatch } from 'react-redux'

import { Link } from 'react-router-dom'

function SignInUp() {

  const [signUp, setSignUp] = useState(false);
  const username = useSelector((state) => state.username.usrname)
  const dispatch = useDispatch()

  const ToggleClass = (e) => {
    setSignUp(!signUp)
  }

  return (
    <div className={signUp ? 'container sign-up-mode' : 'container'}>
      <div className='forms-container'>
        <div className='signin-signup'>
          <form action='' className='sign-in-form'>
            <h2 className='title'>Sign In</h2>
            <div className='input-field'>
              <FontAwesomeIcon icon={faUser} className='font-awesome' />
              <input type="text" placeholder='Username' onChange={(e) => dispatch(changed(e.target.value.toLowerCase()))}  value={username}/>
              {/* <FontAwesomeIcon icon={faSpinner} className='font-awesome-spin' /> */}
            </div>
            {username}
            <Link to='/audioverify'>
              <label className='btn' for='btn'>
              <span style={{fontSize:'14px'}}>LOG IN</span>
                <input type="submit" value='Login' className='btn' />
              </label>
            </Link>

            <p className='social-text'>Or Log In with social partners</p>
            <div className='social-media'>
              <a href='#' className='social-icon'>
                <FontAwesomeIcon icon={faGoogle} />
              </a>

              <a href='#' className='social-icon'>
                <FontAwesomeIcon icon={faGithub} />
              </a>

            </div>


          </form>

          <form action='' className='sign-up-form'>
            <h2 className='title'>Sign Up</h2>
            <div className='input-field'>
              <FontAwesomeIcon icon={faUser} className='font-awesome' />
              <input type="text" placeholder='Username'></input>
              {/* <FontAwesomeIcon icon={faSpinner} className='font-awesome-spin' /> */}
            </div>
            <div className='input-field'>
              <FontAwesomeIcon icon={faEnvelope} className='font-awesome' />
              <input type="email" placeholder='Email'></input>
              {/* <FontAwesomeIcon icon={faSpinner} className='font-awesome-spin' /> */}
            </div>
            <label className='btn' for='btn'>
              <span style={{fontSize:'14px'}}>Get Mail</span>
              <input type="submit" value='Login' className='btn'/>
            </label>

            <p className='social-text'>Or Sign Up with Social Platforms</p>
            <div className='social-media'>
              <a href='#' className='social-icon'>
                <FontAwesomeIcon icon={faGoogle} />
              </a>

              <a href='#' className='social-icon'>
                <FontAwesomeIcon icon={faGithub} />
              </a>

            </div>


          </form>
        </div>
      </div>

      <div className='panels-container'>
        <div className='panel left-panel'>
          <div className='content'>
            <h3>New Here?</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus impedit quidem quibusdam?
            </p>
            <button className='btn trasparent' id='sign-up-btn' onClick={ToggleClass}>Sign Up</button>
          </div>

          <img src={SignUp} className='image' alt='' ></img>
        </div>

        <div className='panel right-panel'>
          <div className='content'>
            <h3>Among Us?</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus impedit quidem quibusdam?
            </p>
            <button className='btn trasparent' id='sign-in-btn' onClick={ToggleClass}>Log In</button>
          </div>

          <img src={LogIn} className='image' alt='' />
        </div>
      </div>
    </div>
  )
}

export default SignInUp