import React from "react";
import ReactDOM from "react-dom";
//import App from "./LoginForm";
//ReactDOM.render(<App />, document.getElementById("content"));

import { render } from 'react-dom'
import { Router, Route, hashHistory } from 'react-router'
import LandingPage from './LandingPage'
import LoginForm from './LoginForm'
import RegisterForm from './RegisterForm'
import HomePage from './HomePage'
import CreateForm from './CreateForm'
import UpdateForm from './UpdateForm'
import DeleteForm from './DeleteForm'
import Display from './Display'


var element = <Router history={hashHistory}>
    <Route exact path='/' component={LandingPage}/>
    <Route exact path='/RegisterForm' component={RegisterForm}/>
    <Route exact path='/LoginForm' component={LoginForm}/>
    <Route exact path='/HomePage' component={HomePage}/>
    <Route exact path='/CreateForm' component={CreateForm}/>
    <Route exact path='/UpdateForm' component={UpdateForm}/>
    <Route exact path='/DeleteForm' component={DeleteForm}/>
    <Route exact path='/Display' component={Display}/>
  </Router>;


render((
	element
), document.getElementById("content"))
