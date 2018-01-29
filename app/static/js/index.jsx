import React from "react";
import ReactDOM from "react-dom";
//import App from "./LoginForm";
//ReactDOM.render(<App />, document.getElementById("content"));

import { render } from 'react-dom'
import { Router, Route, hashHistory } from 'react-router'
import App from './App'
import LoginForm from './LoginForm'


var element = <Router history={hashHistory}>
    <Route path='/' component={App}>
      <Route path='/LoginForm' component={LoginForm}/>
    </Route>
  </Router>;


render((
	element
), document.getElementById("content"))
